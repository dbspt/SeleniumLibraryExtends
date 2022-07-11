#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Cléverson Sampaio <cleverson@sampaio.dev.br>

from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from SeleniumLibraryExtends.FindElements.findElements import FindElements
from SeleniumLibraryExtends.report import Report

class ElementInteraction:
    def __init__(self):
        pass
    
    @keyword("I press the element ${locator}")
    def clickElement(self, locator: str):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            FindElements().waitForElementVisible(locator)
            REPEAT = "12x"
            REPEAT_INTERVAL = "5 sec"
            BuiltIn().wait_until_keyword_succeeds(REPEAT, REPEAT_INTERVAL, "Click Element", locator)
        except Exception as e:
            Report().fail(e)

    @keyword("I press the button ${locator}")
    def clickButton(self, locator: str):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            FindElements().waitForElementVisible(locator)
            REPEAT = "12x"
            REPEAT_INTERVAL = "5 sec"
            BuiltIn().wait_until_keyword_succeeds(REPEAT, REPEAT_INTERVAL, "Click Button", locator)
        except Exception as e:
            Report().fail(e)

    @keyword("I press the link ${locator}")
    def clickLink(self, locator: str):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            FindElements().waitForElementVisible(locator)
            REPEAT = "12x"
            REPEAT_INTERVAL = "5 sec"
            BuiltIn().wait_until_keyword_succeeds(REPEAT, REPEAT_INTERVAL, "Click Link", locator)
        except Exception as e:
            Report().fail(e)

    @keyword("I press the image ${locator}")
    def clickImage(self, locator: str):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            FindElements().waitForElementVisible(locator)
            REPEAT = "12x"
            REPEAT_INTERVAL = "5 sec"
            BuiltIn().wait_until_keyword_succeeds(REPEAT, REPEAT_INTERVAL, "Click Image", locator)
        except Exception as e:
            Report().fail(e)

    @keyword("I fill in the ${locator} field with ${text}")
    def sendKeys(self, locator: str, text: str):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            FindElements().waitForElementVisible(locator)
            REPEAT = "12x"
            REPEAT_INTERVAL = "5 sec"
            BuiltIn().wait_until_keyword_succeeds(REPEAT, REPEAT_INTERVAL, "Input Text", locator, text)
        except Exception as e:
            Report().fail(e)

    @keyword("I submit the form")
    def submitForm(self):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        try:
            self.driver.submit_form()
        except Exception as e:
            Report().fail(e)