#!/usr/bin/env python3
"""Hello World multi-linguas

Dependendo da sua variavel de ambiente o texto é exibido em seu idioma local.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Marcos Felipe"
__license__ = "Unlicense"

import os

current_language = os.getenv('LANG', 'en_US').split('.')[0] 
message = "Hello, World!"

if current_language == "pt_BR":
    message = "Olá, Mundo!"
elif current_language == "it_IT":
    message = "Ciao, Mondo!"

print(message)
