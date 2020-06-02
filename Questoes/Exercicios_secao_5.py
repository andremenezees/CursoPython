"""

Faça um programa que receba a altura e o sexo da pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes fórmulas(onde h coresponde a altura):


sexo = str(input("Digite o sexo:"))
h = float(input("Digite a altura:"))

if sexo == 'homem' or 'masculino':
    p = (72.7*h) - 58

if sexo == 'mulher' or 'feminino':
    p = (62.1*h) - 44.7

print(f'O peso ideal para a pessoa é:{p}')

"""

"""
Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo
com a tabela: menor que 18.5 -> Abaixo do peso, 18.6 - 24.9 -> Saudavel 
25.0 - 29.9 -> Execesso de peso , 30.0 - 34.9 -> Obesidade grau I, 
35.0 -39.9 ->Obesidade grau II(severa) , maior que 40 -> Obesidade grau III(morbida)



altura = float(input('Digite a sua altura:'))
peso = float(input('Digite o seu peso:'))
imc = peso/(altura*altura)

if imc < 18.5:
    print(f'Seu imc é de:{imc} portanto voce está abaixo do peso.')

if imc > 18.5 and imc < 24.9:
    print(f'Seu imc é de:{imc} portanto voce esta com peso saudavel.')

if imc > 25.0 and imc < 29.9:
    print(f'Seu imc é de:{imc} portanto voce está com execesso de peso.')

if imc > 30.0 and imc < 34.9:
    print(f'Seu imc é de:{imc} portanto voce está com obesidade grau I.')

if imc > 35.0 and imc < 39.9:
    print(f'Seu imc é de:{imc} portanto voce está com obesidade grau II(severa).')

if imc > 40.0:
    print(f'Seu imc é de:{imc} portanto voce está com obesidade grau III(morbida).')

"""

"""

Calcular o salario reajustado deste funcionario e imprima o valor do salario final reajustado,
ou uma mensagem caso o funcionario nao tenha direito a nenhum aumento.

Salario                Reajuste(%)            Tempo de Serviço          Bonus
Até 500.00                  25%                 Abaixo de 1 ano         Sem bonus
Até 1000.00                 20%                 De 1 a 3 anos           100.00
Até 1500.00                 15%                 De 4 a 6 anos           200.00
Até 2000.00                 10%                 De 7 a 10 anos          300.00
Acima de 2000.00        Sem reajuste            Mais de 10 anos         500.00

"""