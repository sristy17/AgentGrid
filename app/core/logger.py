def log(step: str, data=None):
    print(f"[LOG] {step}")
    if data:
        print(data)