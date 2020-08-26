def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return f"I {instructions.replace('Simon says', '').strip()}"
    elif instructions.endswith("Simon says"):
        return f"I {instructions.replace('Simon says', '').strip()}"
    else:
        return "I won't do it!"


