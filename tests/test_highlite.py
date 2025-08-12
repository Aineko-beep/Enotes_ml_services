from pprint import pprint
from highlight_ideas.highlite import highlight_segments

segments = [
    {'start': 0.0, 'end': 10.0, 'text': 'Часть 1'},
    {'start': 10.0, 'end': 20.0, 'text': 'Часть 2'},
    {'start': 20.0, 'end': 30.0, 'text': 'Часть 3'},
    {'start': 30.0, 'end': 40.0, 'text': 'Часть 4'},
]

idea_marks = [
    {'start_time': 0.0, 'end_time': 40.0, 'color': 'red'},
    {'start_time': 10.0, 'end_time': 30.0, 'color': 'blue'}, 
    {'start_time': 15.0, 'end_time': 20.0, 'color': 'green'}
]

result = highlight_segments(segments, idea_marks)

print("Результат выделения сегментов:")
pprint(result)

def check_nested(idea_marks):
    red = next((m for m in idea_marks if m['color'] == 'red'), None)
    blue = next((m for m in idea_marks if m['color'] == 'blue'), None)
    green = next((m for m in idea_marks if m['color'] == 'green'), None)
    
    errors = []
    if not (red['start_time'] <= blue['start_time'] and blue['end_time'] <= red['end_time']):
        errors.append("Синяя не вложена в красную")
    if not (blue['start_time'] <= green['start_time'] and green['end_time'] <= blue['end_time']):
        errors.append("Зелёная не вложена в синюю")
    
    return errors

errors = check_nested(idea_marks)
if errors:
    print("Ошибки вложенности:", errors)
else:
    print("Вложенность соблюдена")
