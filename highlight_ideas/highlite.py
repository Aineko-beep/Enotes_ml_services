def highlight_segments(segments, idea_marks):
    highlighted_segments = []
    
    for segment in segments:
        new_segment = segment.copy()
        new_segment['idea_colors'] = []
        highlighted_segments.append(new_segment)
    
    for mark in idea_marks:
        start_time = mark['start_time']
        end_time = mark['end_time']
        mark_color = mark['color']
        
        for segment in highlighted_segments:
            segment_start = segment['start']
            segment_end = segment['end']
            
            if not (segment_end <= start_time or segment_start >= end_time):
                segment['idea_colors'].append(mark_color)
    
    return highlighted_segments