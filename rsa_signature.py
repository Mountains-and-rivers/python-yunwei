#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64


def signature(message, rsa_path):
    '''使用私钥签名'''
    # with open(rsa_path) as f:
    #     key = f.read()
    rsakey = RSA.importKey(rsa_path)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA.new()
    digest.update(message.encode())
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)

    return signature

def verify_signature(message, signature, pub_rsa_path):
    '''验证签名'''
    # with open(pub_rsa_path) as f:
    #     key = f.read()
    rsakey = RSA.importKey(pub_rsa_path)
    verifier = PKCS1_v1_5.new(rsakey)
    digest = SHA.new()
    # Assumes the data is base64 encoded to begin with
    digest.update(message.encode())
    is_verify = verifier.verify(digest, base64.b64decode(signature))
    return is_verify


if __name__ == "__main__":
    plain = 'message'
    rsa_path = '-----BEGIN RSA PRIVATE KEY-----\nMIIBPAIBAAJBALjSF4uWNMDsPzsjYJwtpRFan8/LTK+5CL5BtcXhNlA9dFaHHvt0\n72iQj9066B7iXLv3ny+KVeir6vGUzOuDjl8CAwEAAQJAVprsOZa7RaPuxVGAle61\nqPokZQTI/JbiR/UWrpEnoPLmJxVVL50GQxIiGLPVvyOKjwzKu8awhuHzYgpUSBBB\nQQIjAP7Gm0gE0/2If+n9jD+Zn2hDYZOCtG5HIJLaV8HDp+HyYu8CHwC5tW9xLgW3\nCGTHW/6vCfD18bPUYuuYxVpqpFeay5ECIlEL/Pm8D3PnqElXTvYseHlCdhfmzF8I\nYWRV8PTCuPU3liECHwCJlbws0/Xz9soDUUrND8Zv0FR045y8oGouW/dzfaECIktX\n2rwFc5utcsXjIn3tDbsAIyeoMrtNj/HR8x4uiZ1NMkg=\n-----END RSA PRIVATE KEY-----\n'

    pub_rsa_path = '-----BEGIN RSA PUBLIC KEY-----\nMEgCQQC40heLljTA7D87I2CcLaURWp/Py0yvuQi+QbXF4TZQPXRWhx77dO9okI/d\nOuge4ly7958vilXoq+rxlMzrg45fAgMBAAE=\n-----END RSA PUBLIC KEY-----\n'
    

    sign = signature(plain, rsa_path)
    print('签名：', sign)
    flag = verify_signature(plain, sign, pub_rsa_path)
    print('验证结果：', flag)