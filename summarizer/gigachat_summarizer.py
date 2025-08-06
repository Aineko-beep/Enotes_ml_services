import os
import json
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
        
        giga = GigaChat(
            credentials=auth_key,
            model=MODEL,
            verify_ssl_certs=False
        )
        
        # Очень жёсткий промпт с множественными ограничениями
        prompt = f"""Сократи текст до МАКСИМУМ {MAX_LENGTH} символов. НЕ ПРЕВЫШАТЬ ЛИМИТ НИ В КОЕМ СЛУЧАЕ!

Требования:
- Строго не более {MAX_LENGTH} символов
- Сохрани главную мысль
- Пиши кратко и по делу
- Заверши мысль полностью

Текст: {text}"""
        
        response = giga.chat(prompt)
        summary = response.choices[0].message.content.strip()
        
        # Двойная проверка и принудительная обрезка
        if len(summary) > MAX_LENGTH:
            # Сначала ищем завершённые предложения
            truncated = summary[:MAX_LENGTH]
            
            # Ищем последнюю точку, восклицательный или вопросительный знак
            for punct in ['.', '!', '?']:
                last_punct = truncated.rfind(punct)
                if last_punct > MAX_LENGTH * 0.6:  # Если знак в последних 40%
                    summary = truncated[:last_punct + 1]
                    break
            else:
                # Ищем последнее полное слово
                last_space = truncated.rfind(' ')
                if last_space > MAX_LENGTH * 0.5:  # Если пробел в последних 50%
                    summary = truncated[:last_space] + '.'
                else:
                    # Крайний случай - обрезаем и добавляем многоточие
                    summary = truncated[:MAX_LENGTH-3] + '...'
        
        # Финальная проверка - если всё ещё превышает, обрезаем жёстко
        if len(summary) > MAX_LENGTH:
            summary = summary[:MAX_LENGTH-3] + '...'
        
        # Исправляем запятую в конце на точку
        if summary.endswith(','):
            summary = summary[:-1] + '.'
        
        return {"summary": summary}
        
    except Exception as e:
        return {"error": str(e)}
