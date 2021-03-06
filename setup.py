#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Cléverson Sampaio <cleverson@sampaio.dev.br>

import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

with open(join(CURDIR, 'src', 'SeleniumLibraryExtends', 'version.py'), encoding="utf8") as f:
    VERSION = re.search("\nVERSION = '(.*)'", f.read()).group(1)

with open(join(CURDIR, 'README.md'), encoding="utf8") as f:
    DESCRIPTION = f.read()

with open(join(CURDIR, 'requirements.txt'), encoding="utf8") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    # Inclui todos os outros arquivos que estão dentro da pasta do seu projeto
    include_package_data = True,
    # Nome do seu pacote
    name = 'robotframework-seleniumlibraryextends',
    # Versão do projeto
    version = VERSION,
    # Descrição do seu pacote
    description = 'Selenium Library Extension for new keywords',
    # Site para seu projeto ou repositório do Github
    url = "https://github.com/dbspt/SeleniumLibraryExtends.git",
    # Nome do Criador
    author = 'Cléverson Sampaio',
    # Endereço de e-mail do criador
    author_email = 'cleverson@sampaio.dev.br',
    # Projetos que você deseja incluir em seu pacote
    packages = find_packages('src'),
    # Diretório do seu pacote
    package_dir = {'': 'src'},
    # Dependências/outros módulos necessários para o seu pacote funcionar
    install_requires = REQUIREMENTS,
    # Descrição detalhada do seu pacote
    long_description = DESCRIPTION,
    # Formato da sua descrição detalhada
    long_description_content_type = "text/markdown",
    # Classificadores permitem que seu pacote seja categorizado com base na funcionalidade
    # Pode ser encontrado em https://pypi.org/classifiers
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Framework :: Robot Framework",
        "Framework :: Robot Framework :: Library"
    ]
)