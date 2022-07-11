#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Cléverson Sampaio <cleverson@sampaio.dev.br>

from robot.libraries.BuiltIn import BuiltIn

class Highlight:
    def __init__(self):
        pass

    def init(self, locator: str):
        self.driver = BuiltIn().get_library_instance('SeleniumLibrary')
        element = self.driver.find_element(locator)
        if element:
            script = """
                original_style = arguments[0].getAttribute('style');
                arguments[0].setAttribute('style', original_style + ";box-shadow: inset 0 0 0 2px red;");
                setTimeout(function(){
                    arguments[0].setAttribute('style', original_style);
                }, 500);
            """
            self.driver.driver.execute_script(script, element)