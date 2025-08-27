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


def build_structured_segments(segments, idea_marks):
    highlighted = highlight_segments(segments, idea_marks)

    class IdeaHierarchy:
        def __init__(self):
            self.counters = []
            self.last_colors = []

        def get_label(self, colors):
            if not colors:
                self.last_colors = []
                return ""

            if 'red' not in colors and any(c in colors for c in ['blue', 'green']):
                colors = ['red'] + colors

            changed_level = 0
            for i, c in enumerate(colors):
                if i >= len(self.last_colors) or self.last_colors[i] != c:
                    changed_level = i
                    break
            else:
                changed_level = len(colors) - 1

            while len(self.counters) <= changed_level:
                self.counters.append(0)

            self.counters[changed_level] += 1

            for i in range(changed_level + 1, len(self.counters)):
                self.counters[i] = 0

            self.last_colors = colors[:]

            numbers = [str(n) for n in self.counters[:len(colors)]]
            return "Идея " + ".".join(numbers)


    hierarchy = IdeaHierarchy()
    structured = []

    for seg in highlighted:
        seg_copy = seg.copy()
        seg_copy['idea_label'] = hierarchy.get_label(seg_copy['idea_colors'])
        structured.append(seg_copy)

    return structured
