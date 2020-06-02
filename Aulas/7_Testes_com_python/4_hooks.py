# -*- encoding: utf-8 -*-

"""

Unittest - Antes e apos hooks

----------------------------------------------------------------
Hooks - são os proprios testes. Ou seja a execucao dos testes.
----------------------------------------------------------------

setup () -> é executado antes de cada método de teste. É util para criarmos
instancias de objetos e outros dados;

tearDown() -> É executado ao final de cada método de teste. É util para exlcuir
dados ou fechar conexões com bancos de dados.

"""

import unittest

class ModuloTest(unittest, TestCase):

    def setUp(self):
        #configuracao do setup()
        pass

    def test_primeiro(self):
        #setUp vai rodar antes do teste
        #tearDown() vai rodar após o teste.
        pass

    def tearDown(self):
        #Configurações do tearDown()
        pass