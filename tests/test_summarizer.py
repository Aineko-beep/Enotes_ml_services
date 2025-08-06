import os
from summarizer.gigachat_summarizer import summarize_text
from dotenv import load_dotenv

load_dotenv()

# Настройки из .env
CLIENT_ID = os.getenv("GIGACHAT_CLIENT_ID")
CLIENT_SECRET = os.getenv("GIGACHAT_CLIENT_SECRET")
SCOPE = os.getenv("GIGACHAT_SCOPE")
OAUTH_URL = os.getenv("GIGACHAT_OAUTH_URL")
API_URL = os.getenv("GIGACHAT_API_URL")
AUTH_KEY = os.getenv("GIGACHAT_AUTH_KEY")


os.environ["GIGACHAT_AUTH_KEY"] = AUTH_KEY

# Тестовые данные
test_cases = [
    {
        "name": "Короткий текст",
        "input": {"text": "Машинное обучение - это подраздел искусственного интеллекта, который фокусируется на разработке алгоритмов и статистических моделей, позволяющих компьютерам выполнять задачи без явного программирования."}
    },
    {
        "name": "Средний текст",
        "input": {"text": "Глубокое обучение представляет собой подмножество машинного обучения, основанное на искусственных нейронных сетях с множественными слоями. Эти сети способны автоматически извлекать иерархические представления из данных, что делает их особенно эффективными для задач распознавания образов, обработки естественного языка и других сложных задач."}
    },
    {
        "name": "Длинный текст",
        "input": {"text": "Машинное обучение (ML) — это область искусственного интеллекта, которая фокусируется на разработке алгоритмов и статистических моделей, позволяющих компьютерам выполнять задачи без явного программирования. Эти модели обучаются на данных, чтобы делать прогнозы или принимать решения, не требуя явного инструкций. Машинное обучение включает в себя множество подходов, таких как регрессия, классификация, кластеризация и нейронные сети. Оно широко используется в таких областях, как распознавание образов, обработка естественного языка, анализ данных и управление данными."}
    }
]

def test_summarizer():
    print("Тестирование функции суммаризации")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nТест {i}: {test_case['name']}")
        print(f"Вход: {test_case['input']['text'][:100]}...")
        
        result = summarize_text(test_case['input'])
        
        if 'error' in result:
            print(f"Ошибка: {result['error']}")
        else:
            print(f"Результат: {result['summary']}")
            print(f"Длина: {len(result['summary'])} символов")
        
        print("-" * 30)

if __name__ == "__main__":
    test_summarizer() 