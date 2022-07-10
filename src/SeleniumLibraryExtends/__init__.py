#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Cléverson Sampaio <cleverson@sampaio.dev.br>

from SeleniumLibraryExtends.version import VERSION

class SeleniumLibraryExtends():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        pass

if __name__ == '__main__':
    lib = SeleniumLibraryExtends()