from pprint import pprint
from highlight_ideas.highlite import highlight_segments

segments = [
    {'start': 0.0, 'end': 10.0, 'text': 'Часть 1'},
    {'start': 10.0, 'end': 20.0, 'text': 'Часть 2'},
    {'start': 20.0, 'end': 30.0, 'text': 'Часть 3'},
    {'start': 30.0, 'end': 40.0, 'text': 'Часть 4'},
]

idea_marks = [
    {'start_time': 0.0, 'end_time': 40.0, 'color': 'red'},   # покрывает все сегменты
    {'start_time': 10.0, 'end_time': 30.0, 'color': 'blue'}, # вложена в красную
    {'start_time': 15.0, 'end_time': 20.0, 'color': 'green'} # вложена в синюю
]

print("=== Тест 1: вложенные идеи ===")
result = highlight_segments(segments, idea_marks)
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

print("\n=== Тест 2: идея внутри сегмента ===")
idea_inside_segment = [
    {'start_time': 12.0, 'end_time': 13.0, 'color': 'yellow'}
]
res2 = highlight_segments(segments, idea_inside_segment)
pprint(res2)

print("\n=== Тест 3: идея начинается до сегмента и заканчивается внутри ===")
idea_partial_overlap = [
    {'start_time': 15.0, 'end_time': 25.0, 'color': 'purple'}
]
res3 = highlight_segments(segments, idea_partial_overlap)
pprint(res3)

print("\n=== Тест 4: идея вне диапазона сегментов ===")
idea_outside = [
    {'start_time': 50.0, 'end_time': 60.0, 'color': 'gray'}
]
res4 = highlight_segments(segments, idea_outside)
pprint(res4)
