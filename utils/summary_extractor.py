def summarize_text(text):
    word_count = len(text.split())
    
    if word_count < 100:
        return text  
    
    elif word_count < 500:
        return " ".join(text.split()[:50]) + "..."
    
    else:
        return " ".join(text.split()[:100]) + "... (truncated)"
