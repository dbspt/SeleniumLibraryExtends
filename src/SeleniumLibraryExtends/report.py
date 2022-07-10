#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Cléverson Sampaio <cleverson@sampaio.dev.br>

from robot.libraries.BuiltIn import BuiltIn

class Report:
    def __init__(self):
        pass

    def fail(self, exception: Exception):
        self.driver = BuiltIn().get_library_instance('SeleniumLibrary')
        self.driver.capture_page_screenshot("EMBED")
        BuiltIn().fail(exception)