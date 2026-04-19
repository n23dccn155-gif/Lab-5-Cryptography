def validate_key_length(algorithm: str, key_hex: str) -> bool:
    ...

def print_error(message: str):
    print(f"\n❌ LỖI: {message}")

def copy_to_clipboard(text: str):
    # dùng pyperclip hoặc chỉ print hướng dẫn copy
    ...