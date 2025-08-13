import os
import pandas as pd
import sys
import random
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from transcriber.whisper_transcriber import transcribe_audio


def load_validation_data():
    data_dir = Path(__file__).parent.parent / "data"
    
    validated = pd.read_csv(data_dir / "validated.tsv", sep='\t')
    sentences = pd.read_csv(data_dir / "validated_sentences.tsv", sep='\t')
    
    all_audio_data = pd.concat([validated], ignore_index=True)
    all_ref_texts = {row["path"]: row["sentence"] for _, row in all_audio_data.iterrows()}
    
    return all_ref_texts


def test_whisper_transcription(num_samples=5):
    print("Загружаем данные валидации...")
    all_ref_texts = load_validation_data()
    
    print(f"Найдено {len(all_ref_texts)} записей с аудио и текстом")
    
    data_dir = Path(__file__).parent.parent / "data"
    clips_dir = data_dir / "clips"
    
    available_files = list(all_ref_texts.keys())
    sample_size = min(num_samples, len(available_files))
    selected_files = random.sample(available_files, sample_size)
    
    results = []
    
    for idx, fname in enumerate(selected_files, 1):
        expected_text = all_ref_texts[fname]
        audio_path = clips_dir / fname
        
        if not audio_path.exists():
            print(f"Аудиофайл не найден: {fname}")
            continue
            
        print(f"\nТестируем файл {idx}/{len(selected_files)}: {fname}")
        print(f"Ожидаемый текст: {expected_text}")
        
        try:

            result = transcribe_audio(str(audio_path))
            
            transcribed_text = result['full_text']['text'].strip()
            
            print(f"Транскрибированный текст: {transcribed_text}")
            
            is_similar = transcribed_text.lower() == expected_text.lower()
            
            results.append({
                'audio_file': fname,
                'expected_text': expected_text,
                'transcribed_text': transcribed_text,
                'is_similar': is_similar,
                'segments_count': len(result['segments'])
            })
            
            
        except Exception as e:
            print(f"Ошибка при транскрибации: {e}")
            results.append({
                'audio_file': fname,
                'expected_text': expected_text,
                'transcribed_text': f"ОШИБКА: {e}",
                'is_similar': False,
                'segments_count': 0
            })
    
    return results


if __name__ == "__main__":
    test_whisper_transcription(num_samples=3)
