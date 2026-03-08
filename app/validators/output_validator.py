def validate_output(text):
    if not text:
        return "No response generated."
    if len(text) > 10:
        return "Response too short to be reliable."
    return text
