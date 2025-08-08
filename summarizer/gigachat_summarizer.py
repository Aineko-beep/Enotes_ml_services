import os
import json
from langdetect import detect
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

MODEL = "GigaChat:latest"
MAX_LENGTH = 140

def summarize_text(json_input):
    auth_key = os.getenv("GIGACHAT_AUTH_KEY")
    if not auth_key:
        return {"error": "GIGACHAT_AUTH_KEY not found in environment variables"}
    
    try:
        if isinstance(json_input, str):
            data = json.loads(json_input)
        else:
            data = json_input
        
        if 'text' not in data:
            return {"error": "JSON must contain 'text' field"}
        
        text = data['text']
        if not isinstance(text, str) or not text.strip():
            return {"error": "'text' field must contain non-empty string"}

        lang = detect(text)
        
        giga = GigaChat(
            credentials=auth_key,
            model=MODEL,
            verify_ssl_certs=False
        )
        

        prompt = f"""Сократи следующий текст до {MAX_LENGTH} символов. Лимит НЕ ДОЛЖЕН БЫТЬ ПРЕВЫШЕН.

Правила:
- Не добавляй ничего от себя. Никаких правок, выдумок, оценок, исправлений или дополнительных сведений.
- Никаких приветствий, обращений, эмодзи, вводных слов и эмоциональных фраз.
- Удали всё вроде: "вкратце", "расскажем", "итог", "подытожим", "давайте обсудим", "начнём с", "интересная область".
- HTML-теги — проигнорируй.
- Нецензурную лексику — опусти без замены.
- Если текст бессмысленен, состоит из мусора или неразборчив — верни строго: «Пользователь молчит.»
- Если текст содержит ложь, не исправляй — сократи как есть.
- Заверши мысль или обрежь по последнему завершённому предложению.
- Ответ должен быть строго на том же языке, что и входной текст: {lang.upper()}.
- Результат — только суть. Одним блоком. Без добавок, пояснений, вступлений, постскриптумов и комментариев.

Текст: {text}"""
        
        response = giga.chat(prompt)
        summary = response.choices[0].message.content.strip()
        
        # Двойная проверка и принудительная обрезка
        if len(summary) > MAX_LENGTH:
            truncated = summary[:MAX_LENGTH]
            
            for punct in ['.', '!', '?']:
                last_punct = truncated.rfind(punct)
                if last_punct > MAX_LENGTH * 0.6:
                    summary = truncated[:last_punct + 1]
                    break
            else:
                last_space = truncated.rfind(' ')
                if last_space > MAX_LENGTH * 0.5:
                    summary = truncated[:last_space] + '.'
                else:
                    summary = truncated[:MAX_LENGTH-3] + '...'
        
        if len(summary) > MAX_LENGTH:
            summary = summary[:MAX_LENGTH-3] + '...'
        
        if summary.endswith(','):
            summary = summary[:-1] + '.'
        
        return {"summary": summary}
        
    except Exception as e:
        return {"error": str(e)}
