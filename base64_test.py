#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import base64
import random
#flag="flag{**some seclet**}"
#base64加密
def base64_encode(flag):
    #定义编码方式
    basecode={
          '16':lambda x:base64.b16encode(x),
          '32':lambda x:base64.b32encode(x),
          '64':lambda x:base64.b64encode(x)
          }
    #将‘str’类型转换成‘bytes’类型
    pp=flag.encode('utf-8')
    #进行循环编码
    for i in range(10):
        order=random.choice(['16','32','64'])
        pp=basecode[order](pp)
    #将‘bytes’类型转换成‘str’类型
    pp=pp.decode('utf-8')
    #写入文件中
    with open("ciphertext.txt",'w') as fp:
        fp.write(pp)
    return '###加密成功###'

#base64解密
def base64_decode(ciphertext):
    result=''
    with open(ciphertext+".txt",'r') as fp:
        ciphertext=fp.read()
    ciphertext=ciphertext.encode('utf-8')
    #定义解密方式
    basedecode={
          '16':lambda x:base64.b16decode(x),
          '32':lambda x:base64.b32decode(x),
          '64':lambda x:base64.b64decode(x)       
            }
    for j in range(10):
        try:
            ciphertext=basedecode['16'](ciphertext)
        except:
            try:
                ciphertext=basedecode['32'](ciphertext)
            except:
                ciphertext=basedecode['64'](ciphertext)
    result=ciphertext.decode('utf-8')
    print(result)
    return '###解密成功###'

def main():
    functions=input('输入A加密，输入B解密，其它关闭>>>')
    if functions=='A':
        plaintext=input('请输入加密文字明文>>>')
        print(base64_encode(plaintext))
    if functions=='B':
        ciphertext = input('请输入密文文件名>>>')
        print(base64_decode(ciphertext))

if __name__=='__main__':
    main()