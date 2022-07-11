#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Cléverson Sampaio <cleverson@sampaio.dev.br>

from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from SeleniumLibraryExtends.report import Report
from SeleniumLibraryExtends.highlight import Highlight

class FindElements:
    def __init__(self):
        pass
    
    @keyword("I wait for the ${locator} element to be visible")
    def waitForElementVisible(self, locator: str):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            self.driver.wait_until_element_is_visible(locator)
            Highlight.init(locator)
        except Exception as e:
            Report().fail(e)

    @keyword("I wait for the ${locator} element not to be visible")
    def waitForElementNotVisible(self, locator: str):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            self.driver.wait_until_element_is_not_visible(locator)
        except Exception as e:
            Report().fail(e)