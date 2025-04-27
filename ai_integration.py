import subprocess

class AIIntegrator:
    def __init__(self, model="deepseek-r1:7b"):
        self.model = model
        self.system_prompt = """أنت مساعد أمني خبير يعمل على كالي لينكس. 
        مهامك:
        - تحليل الطلبات وتحديد الأداة المناسبة
        - توليد أوامر نظام آمنة
        - مراقبة النظام لاكتشاف التهديدات"""

    def generate_command(self, user_input):
        try:
            prompt = f"### System:\n{self.system_prompt}\n### User:\n{user_input}"
            result = subprocess.run(
                ['ollama', 'run', self.model],
                input=prompt.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=30  # إضافة مهلة لتجنب تعليق العملية
            )
            return self._parse_output(result.stdout.decode())
        except subprocess.TimeoutExpired:
            return "⚠️ حدثت مهلة أثناء تنفيذ العملية."
        except Exception as e:
            return f"⚠️ Error: {e}"

    def _parse_output(self, raw_output):
        if "→ التنفيذ:" in raw_output:
            return raw_output.split("→ التنفيذ:")[1].strip()
        return None