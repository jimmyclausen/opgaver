# -*- coding: utf-8 -*-
'''
Created on 23/11/2012

@author: jimju
'''


#!/usr/bin/env python
import platform

profile = [
platform.architecture(),#windows version
platform.dist(),
platform.libc_ver(),
platform.mac_ver(),#om computeren kører 32bit eller 64 bit
platform.machine(),# navn på maskinen
platform.node(),
platform.platform(),
platform.processor(),
platform.python_build(),
platform.python_compiler(),
platform.python_version(),
platform.system(),
platform.uname(),
platform.version(),
]

for item in profile:
    print (item)


if __name__ == '__main__':
    pass