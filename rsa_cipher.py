#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wangguilin
# Description:

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

#  伪随机数生成器
random_generator = Random.new().read

def encrypt(message, pub_rsa_path):
    '''使用公钥加密'''
    # with open(pub_rsa_path) as f:
    #     key = f.read()
    rsakey = RSA.importKey(pub_rsa_path)
    cipher = PKCS1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(message.encode()))
    return cipher_text

def decrypt(secret_message, rsa_path):
    '''使用私钥解密'''
    # with open(rsa_path) as f:
    #     key = f.read()
    rsakey = RSA.importKey(rsa_path)
    cipher = PKCS1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(secret_message), random_generator)
    return text


if __name__ == "__main__":
    plain = 'message'
    rsa_path = '-----BEGIN RSA PRIVATE KEY-----\nMIIBPAIBAAJBALjSF4uWNMDsPzsjYJwtpRFan8/LTK+5CL5BtcXhNlA9dFaHHvt0\n72iQj9066B7iXLv3ny+KVeir6vGUzOuDjl8CAwEAAQJAVprsOZa7RaPuxVGAle61\nqPokZQTI/JbiR/UWrpEnoPLmJxVVL50GQxIiGLPVvyOKjwzKu8awhuHzYgpUSBBB\nQQIjAP7Gm0gE0/2If+n9jD+Zn2hDYZOCtG5HIJLaV8HDp+HyYu8CHwC5tW9xLgW3\nCGTHW/6vCfD18bPUYuuYxVpqpFeay5ECIlEL/Pm8D3PnqElXTvYseHlCdhfmzF8I\nYWRV8PTCuPU3liECHwCJlbws0/Xz9soDUUrND8Zv0FR045y8oGouW/dzfaECIktX\n2rwFc5utcsXjIn3tDbsAIyeoMrtNj/HR8x4uiZ1NMkg=\n-----END RSA PRIVATE KEY-----\n'

    pub_rsa_path = '-----BEGIN RSA PUBLIC KEY-----\nMEgCQQC40heLljTA7D87I2CcLaURWp/Py0yvuQi+QbXF4TZQPXRWhx77dO9okI/d\nOuge4ly7958vilXoq+rxlMzrg45fAgMBAAE=\n-----END RSA PUBLIC KEY-----\n'
    
    print('明文：', plain)
    secret = encrypt(plain, pub_rsa_path)
    print('加密文：', secret)
    text = decrypt(secret, rsa_path)
    print('解密文：', text)