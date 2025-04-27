from src.ai_integration import AIIntegrator
from src.tool_executor import KaliToolExecutor
from src.anomaly_detector import AnomalyDetector
from src.notifier import Notifier

def main():
    print("🚀 Yusr-Tec1: نظام أمني قائم على الذكاء الاصطناعي")
    
    # إنشاء الكائنات الأساسية
    ai_integrator = AIIntegrator()
    anomaly_detector = AnomalyDetector()
    notifier = Notifier()

    # تدريب نموذج اكتشاف الشذوذ (مثال على البيانات التاريخية)
    historical_data = [
        {'cpu': 20, 'memory': 40, 'network': {'connections': 10}},
        {'cpu': 25, 'memory': 45, 'network': {'connections': 15}},
        {'cpu': 30, 'memory': 50, 'network': {'connections': 20}}
    ]
    anomaly_detector.train(historical_data)

    # مثال على تحليل إدخال المستخدم وتوليد أمر
    user_input = "افحص الموقع example.com بحثًا عن الثغرات"
    command = ai_integrator.generate_command(user_input)
    if command:
        print(f"⚙️ الأمر المولد: {command}")
        executor = KaliToolExecutor()
        result = executor.execute({'command': command, 'tool': 'nmap'})
        if result['vulnerabilities_found']:
            notifier.send_alert(f"تم اكتشاف ثغرات في الهدف: {result['vulnerabilities']}")
        else:
            print("✅ لم يتم العثور على أي ثغرات.")

if __name__ == "__main__":
    main()