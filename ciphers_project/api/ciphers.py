
def caesar_encode(plain_text, shift):
    cipher_text = ""
    # for c in plain_text:
    #     c_encoded = ord(c) + shift
    #     c_encoded = chr(c_encoded)
    #     cipher_text += c_encoded
    for c in plain_text:
        if c.islower():
            base = ord('a')
        elif c.isupper():
            base = ord('A')
        else:
            cipher_text += c
            continue
        
        shifted = (ord(c) - base + shift) % 26 + base
        cipher_text += chr(shifted)
    
    return cipher_text
    
