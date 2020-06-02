# -*- encoding: utf-8 -*-
import unittest

from atividades import comer, dormir, eh_engracada


class AtividadesTestes(unittest.TestCase):
    def teste_comer(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Dormi muito, estou atrasado para o trabalho.'
        )

    def teste_eh_engracada(self):
        #self.assertEqual(eh_engracada('Sergio Malandro'), False)
        self.assertFalse(eh_engracada('Sergio Malandro'))
        self.assertTrue('Jim Carrey'), 'Jim Carrey deveria ser engraçado.'

if __name__ == '__main__':
    unittest.main()
