# -*- encoding: utf-8 -*-
def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'a gente só vive uma vez.'
    return f'Estou comendo {comida} porque {final}'

def dormir(num_horas):
    if num_horas > 8 :
        return f'Dormi muito, estou atrasado para o trabalho.'
    else:
        return f'Continuo cansado após dormir por 4 horas. :('

def eh_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False

