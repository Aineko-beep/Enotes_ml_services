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
    },
    {
        "name": "Короткий текст (английский)",
        "input": {"text": "Machine learning is a subset of AI that focuses on building systems that learn from data."}
    },
    {
        "name": "Русский — текст с эмодзи и вступлением",
        "input": {"text": "Привет! 👋 Сегодня я расскажу про машинное обучение. 🤖 Это очень интересно!"}
    },
    {
        "name": "Русский — текст с эмоциональной окраской",
        "input": {"text": "Машинное обучение — это безумно крутая штука! Вы не представляете, сколько оно может!"}
    },
    {
        "name": "Английский — нейтральный текст",
        "input": {"text": "Artificial intelligence is transforming industries by automating decision-making processes."}
    },
    {
        "name": "Английский — текст с эмодзи и неформальным стилем",
        "input": {"text": "Hey there! 🚀 Let’s talk about AI and how it’s changing the world 🌍!"}
    },
    {
        "name": "Испанский — формальный стиль",
        "input": {"text": "La inteligencia artificial permite automatizar procesos mediante algoritmos avanzados y redes neuronales."}
    },
    {
        "name": "Китайский — короткий технический текст",
        "input": {"text": "人工智能通过深度学习实现图像识别和语音识别。"}
    },
    {
        "name": "Китайский — текст с эмодзи",
        "input": {"text": "你好！🤖 人工智能正在改变我们的生活！📱"}
    },
    {
        "name": "Немецкий — длинное объяснение",
        "input": {"text": "Künstliche Intelligenz ist ein Bereich der Informatik, der sich mit der Entwicklung intelligenter Systeme beschäftigt, die Aufgaben ohne menschliches Eingreifen ausführen können."}
    },
    {
        "name": "Французский — научный стиль",
        "input": {"text": "L'apprentissage automatique est une branche de l'IA qui permet aux machines d'apprendre à partir de données sans être explicitement programmées."}
    },
    {
        "name": "Русский — текст < 140 символов, но с мусором",
        "input": {"text": "🌟 Вкратце: ИИ — это супер! 👍 Он умеет всё и даже больше! В этом вся суть, правда ведь?"}
    },
    {
        "name": "Русский — текст ровно 140 символов",
        "input": {"text": "ИИ позволяет автоматизировать задачи, анализировать большие данные, прогнозировать события и улучшать бизнес-процессы компаний и организаций."}
    },
    {
        "name": "Английский — текст с фразами «in summary», «to conclude»",
        "input": {"text": "In summary, machine learning is an essential component of modern AI systems. To conclude, it enables adaptive behavior."}
    },
    {
        "name": "Французский — эмоциональный отзыв",
        "input": {"text": "J'adore l'intelligence artificielle ! C’est incroyable ce qu’elle peut faire aujourd’hui 😍"}
    },
    {
        "name": "Мусорный текст на неизвестном языке",
        "input": {"text": "asfkasf!@# sakfjh3r fasdf/// fjqf 😁"}
    },
    {
        "name": "Русский — текст с матом",
        "input": {"text": "Эта чёртова система опять сломалась, какого хрена никто ничего не делает?"}
    },
    {
        "name": "Английский — HTML-теги",
        "input": {"text": "<div>Hello!</div><p>This is <strong>important</strong> text about AI.</p>"}
    },
    {
        "name": "Русский — текст с ложью",
        "input": {"text": "Илон Маск родился в России и изобрёл балалайку."}
    },
    {
        "name": "Мусорный текст — бессмысленный ввод",
        "input": {"text": "a9s8d7f98sd!@# lksdjf/// \n\n wfwfj 😵‍💫 \n\n 🤯💣 <br>"}
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