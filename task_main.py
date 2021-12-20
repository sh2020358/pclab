shift = 7
encrypted_tex = "KLMLUKAOLMVYA"
plain_text = ""
for c in encrypted_tex:
    if c.isupper():
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        
        new_index = (c_index - shift) % 26
        
        new_unicode = new_index + ord("A")
        
        new_character = chr(new_unicode)
        
        plain_text = plain_text + new_character
        
    else:
        plain_text += c
        
print("Encryped text", encrypted_tex)
print("original text",plain_text)
        


shift = 7
encrypted_tex = "DEFENDTHEFORT"
plain_text = ""
for c in encrypted_tex:
    if c.isupper():
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        
        new_index = (c_index + shift) % 26
        
        new_unicode = new_index + ord("A")
        
        new_character = chr(new_unicode)
        
        plain_text = plain_text + new_character
        
    else:
        plain_text += c
        
print("Original text", encrypted_tex)
print("Encrypted text",plain_text)
        

            