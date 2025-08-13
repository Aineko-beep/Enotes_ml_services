import whisper

def transcribe_audio(audio_path: str) -> dict:
    model = whisper.load_model("small")
    
    full_text = model.transcribe(audio_path)
    
    segments = []
    for segment in full_text["segments"]:
        segments.append({
            "start": float(segment["start"]),
            "end": float(segment["end"]),
            "text": str(segment["text"]).strip()
        })
        
    return {
        "segments": segments,
        "full_text": full_text
    }