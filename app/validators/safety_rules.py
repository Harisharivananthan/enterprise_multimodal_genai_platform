FORBIDDEN_PHRASES = [
    "I don't know for sure but",
    "this might be incorrect"
]

def apply_safety_rules(text):
    text_lower = text.lower()

    for phrase in FORBIDDEN_PHRASES:
        if phrase in text_lower:
            return "Unable to provide a confident answer based on available information"
    return text
