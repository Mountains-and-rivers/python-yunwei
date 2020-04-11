
from Cipher_oAES import Cipher_AES
 
key = "q435234523452345"
iv = key[::-1]
text = "changeme_123"
cipher_method = "MODE_EBC"
pad_method = "PKCS5Padding"
code_method = "base64"
cipher_text = Cipher_AES(key, iv, cipher_method, pad_method, code_method).encrypt(text)
print(cipher_text.lower())
text = Cipher_AES(key, iv, cipher_method, pad_method, code_method).decrypt(cipher_text)
print(text)