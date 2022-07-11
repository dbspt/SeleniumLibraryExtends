#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Cléverson Sampaio <cleverson@sampaio.dev.br>

from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

class Browser:
    def __init__(self):
        pass

    def path(self, browser: str) -> str:
        if browser == "chrome":
            return ChromeDriverManager().install()
        if browser == "chromium":
            return ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        if browser == "brave":
            return ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()
        if browser == "firefox":
            return GeckoDriverManager().install()
        if browser == "ie":
            return IEDriverManager().install()
        if browser == "edge":
            return EdgeChromiumDriverManager().install()
        if browser == "opera":
            return OperaDriverManager().install()