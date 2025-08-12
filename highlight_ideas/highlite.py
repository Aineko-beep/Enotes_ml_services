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
        
        closest_start_segment = None
        closest_end_segment = None
        min_start_distance = float('inf')
        min_end_distance = float('inf')
        
        for segment in highlighted_segments:
            segment_start = segment['start']
            segment_end = segment['end']
            
            start_distance = abs(start_time - segment_start)
            end_distance = abs(end_time - segment_end)
            
            if start_distance < min_start_distance:
                min_start_distance = start_distance
                closest_start_segment = segment
            
            if end_distance < min_end_distance:
                min_end_distance = end_distance
                closest_end_segment = segment
        
        if closest_start_segment:
            closest_start_segment['idea_colors'].append(mark_color)
        if closest_end_segment and closest_end_segment != closest_start_segment:
            closest_end_segment['idea_colors'].append(mark_color)
    
    return highlighted_segments 