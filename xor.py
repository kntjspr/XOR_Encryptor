def xor(message, key):
    encrypted_message = ""
    for char in message:
        encrypted_char = chr(ord(char) ^ key)
        encrypted_message += encrypted_char
    return encrypted_message
