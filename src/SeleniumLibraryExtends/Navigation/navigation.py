#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Cléverson Sampaio <cleverson@sampaio.dev.br>

from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from SeleniumLibraryExtends.report import Report
from SeleniumLibraryExtends.browser import Browser
from SeleniumLibraryExtends.FindElements.findElements import FindElements

class Navigation:
    def __init__(self):
        pass
    
    @keyword("I open the browser ${browser}")
    def openBrowser(self, browser: str, maximize: bool = True):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        self.driver.open_browser("about:blank", browser, None, None, None, None, None, None, Browser().path(browser))
        if maximize:
            self.driver.maximize_browser_window()

    @keyword("I am on ${url}")
    def navigateTo(self, url: str):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        self.driver.go_to(url)
        try:
            FindElements().waitForElementVisible("tag:body")
        except Exception as e:
            Report().fail(e)

    @keyword("I navigate back")
    def back(self):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        self.driver.go_back()

    @keyword("I retrieve the page title")
    def getTitle(self) -> str:
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        return self.driver.get_title()

    @keyword("I refresh page")
    def refresh(self):
        self.driver = BuiltIn().get_library_instance("SeleniumLibrary")
        self.driver.reload_page()