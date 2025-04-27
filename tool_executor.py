# tool_executor.py

import subprocess
import shlex
import re
from vulnerabilities_db import KNOWN_VULNERABILITIES

class KaliToolExecutor:
    @staticmethod
    def execute(command_info):
        """
        تنفيذ الأوامر الأمنية وتحليل النتائج.
        """
        try:
            # استخراج الأمر من بيانات الإدخال
            command = command_info['command']
            print(f"\n🛠 جاري تنفيذ: {command}")
            
            # تشغيل الأمر باستخدام subprocess
            result = subprocess.run(
                shlex.split(command),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=600  # تحديد مهلة زمنية للتنفيذ
            )
            
            # تحليل النتائج
            target = KaliToolExecutor._extract_target(command)
            domain = KaliToolExecutor._extract_domain(target)
            vulnerabilities = KaliToolExecutor._analyze_output(result.stdout, domain)
            
            return {
                'success': True,
                'tool': command_info['tool'],
                'output': result.stdout,
                'vulnerabilities': vulnerabilities,
                'vulnerabilities_found': len(vulnerabilities) > 0
            }
            
        except subprocess.TimeoutExpired:
            return {'success': False, 'error': "Timeout occurred while executing the command."}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    @staticmethod
    def _analyze_output(output, domain):
        """
        تحليل مخرجات الأداة للكشف عن الثغرات الأمنية.
        """
        vulns = []
        if re.search(r'SQL injection|SQLi', output, re.IGNORECASE):
            vulns.append("ثغرة حقن SQL (SQLi)")
        if re.search(r'XSS|Cross-Site Scripting', output, re.IGNORECASE):
            vulns.append("ثغرة XSS")
        if re.search(r'(\\bPHP/5\\.|\\bApache/2\\.4\\.(2[0-9]|3[0-9]))', output):
            vulns.append("إصدار قديم مُعرّض للثغرات")
        cve_matches = re.findall(r'CVE-\\d{4}-\\d{4,7}', output)
        vulns.extend([f"ثغرة مسجلة ({cve})" for cve in cve_matches])
        if not vulns and domain in KNOWN_VULNERABILITIES:
            vulns.extend(KNOWN_VULNERABILITIES[domain])
        return vulns

    @staticmethod
    def _extract_target(command_str):
        """
        استخراج الهدف (URL أو IP) من الأمر.
        """
        url_match = re.search(r'(https?://[^\\s/]+)', command_str)
        ip_match = re.search(r'\\b\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\b', command_str)
        return url_match.group(1) if url_match else ip_match.group(0) if ip_match else ""

    @staticmethod
    def _extract_domain(target):
        """
        استخراج اسم النطاق من الهدف.
        """
        domain_match = re.search(r'([a-zA-Z0-9.-]+\\.[a-zA-Z]{2,})', target)
        return domain_match.group(1) if domain_match else ""