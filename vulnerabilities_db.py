# vulnerabilities_db.py

"""
ملف يحتوي على قاعدة بيانات بسيطة للثغرات الأمنية المعروفة.
"""

# قائمة بالثغرات الأمنية المعروفة، مصنفة حسب النطاق أو الهدف
KNOWN_VULNERABILITIES = {
    "example.com": [
        "ثغرة SQL Injection",
        "ثغرة XSS"
    ],
    "testphp.vulnweb.com": [
        "ثغرة SQL Injection في /artists.php",
        "ثغرة XSS في /search.php"
    ],
    "vulnerable-site.com": [
        "ثغرة File Inclusion في /include.php",
        "ثغرة CSRF في /form.php"
    ],
    "secure-site.net": [
        "إصدار قديم من Apache معرض للثغرات الأمنية",
        "ثغرة Path Traversal في /download"
    ],
    "demo-site.org": [
        "ثغرة Remote Code Execution (RCE)",
        "ثغرة Directory Listing في /files"
    ]
}