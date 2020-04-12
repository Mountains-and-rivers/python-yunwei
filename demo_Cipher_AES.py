#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wangguilin
# Description:
from Cipher_oAES import Cipher_AES
 
key = "abcdefgh123456783lkiklo5o5julhyl"
iv = key[::-1]
text = "Changeme_123"
cipher_method = "MODE_GCM"
pad_method = "PKCS5Padding"
code_method = "hex"
cipher_text = Cipher_AES(key, iv, cipher_method, pad_method, code_method).encrypt(text)
print(cipher_text)
text = Cipher_AES(key, iv, cipher_method, pad_method, code_method).decrypt(cipher_text)
print(text)