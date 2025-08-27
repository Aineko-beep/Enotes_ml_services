import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from highlight_ideas.highlite import highlight_segments, build_structured_segments


def test_highlight_segments():
    print("=== Testing highlight_segments ===")
    segments = [
        {'start': 0.0, 'end': 5.0, 'text': 'Сегмент 1'},
        {'start': 5.0, 'end': 10.0, 'text': 'Сегмент 2'},
        {'start': 10.0, 'end': 15.0, 'text': 'Сегмент 3'},
    ]
    idea_marks = [
        {'start_time': 0.0, 'end_time': 10.0, 'color': 'red'},
        {'start_time': 2.0, 'end_time': 5.0, 'color': 'blue'},
    ]
    result = highlight_segments(segments, idea_marks)
    for seg in result:
        assert 'idea_colors' in seg
    print(json.dumps(result, indent=2, ensure_ascii=False))
    print("✓ highlight_segments works\n")

def test_build_structured_segments():
    print("=== Testing build_structured_segments ===")
    segments = [
        {'start': 0.0, 'end': 5.0, 'text': 'Сегмент 1'},
        {'start': 5.0, 'end': 10.0, 'text': 'Сегмент 2'},
        {'start': 10.0, 'end': 15.0, 'text': 'Сегмент 3'},
        {'start': 15.0, 'end': 20.0, 'text': 'Сегмент 4'},
        {'start': 20.0, 'end': 25.0, 'text': 'Сегмент 5'},
        {'start': 25.0, 'end': 30.0, 'text': 'Сегмент 6'},
    ]
    idea_marks = [
        {'start_time': 0.0, 'end_time': 10.0, 'color': 'red'},
        {'start_time': 2.0, 'end_time': 5.0, 'color': 'blue'},
        {'start_time': 6.0, 'end_time': 10.0, 'color': 'blue'},
        {'start_time': 10.0, 'end_time': 20.0, 'color': 'red'},
        {'start_time': 12.0, 'end_time': 14.0, 'color': 'blue'},
        {'start_time': 13.0, 'end_time': 14.0, 'color': 'green'},
        {'start_time': 15.0, 'end_time': 18.0, 'color': 'blue'},
        {'start_time': 20.0, 'end_time': 25.0, 'color': 'red'},
    ]
    structured = build_structured_segments(segments, idea_marks)
    for seg in structured:
        assert 'idea_colors' in seg
        assert 'idea_label' in seg
    print(json.dumps(structured, indent=2, ensure_ascii=False))
    print("✓ build_structured_segments works\n")

def test_complex_nested():
    print("=== Testing complex nested scenario ===")
    segments = [
        {'start': 0.0, 'end': 2.0, 'text': 'Начало'},
        {'start': 2.0, 'end': 4.0, 'text': 'Основная идея'},
        {'start': 4.0, 'end': 6.0, 'text': 'Под-идея'},
        {'start': 6.0, 'end': 8.0, 'text': 'Конец'},
    ]
    idea_marks = [
        {'start_time': 0.0, 'end_time': 8.0, 'color': 'red'},
        {'start_time': 2.0, 'end_time': 6.0, 'color': 'blue'},
        {'start_time': 4.0, 'end_time': 5.0, 'color': 'green'},
    ]
    structured = build_structured_segments(segments, idea_marks)
    print(json.dumps(structured, indent=2, ensure_ascii=False))
    print("✓ complex nested scenario checked\n")

if __name__ == "__main__":
    test_highlight_segments()
    test_build_structured_segments()
    test_complex_nested()
