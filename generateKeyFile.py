#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wangguilin
# Description:

import rsa
import base64
from urllib import request
 
 
(public_key, private_key) = rsa.newkeys(1024)
with open('public.pem', 'wb+') as f:
    f.write(public_key.save_pkcs1())
with open('private.pem', 'wb+') as f:
    f.write(private_key.save_pkcs1())