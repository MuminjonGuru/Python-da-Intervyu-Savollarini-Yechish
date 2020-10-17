def encrypt(text, key):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ''

  for char in text.lower():
    id = (alphabet.index(char) + key % len(alphabet))
    encrypted_text += alphabet[id]

  return encrypted_text

print(encrypt("CIsTheBest", 1))      
