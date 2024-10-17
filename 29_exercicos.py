import os
os.system('cls')

print('Exercício de 1 á 7 - Calculo')
print('#####################################################')
n1 = int(input('Digite o 1º Número: '))
n2 = int(input('Digite o 2º Número: '))
# 1. Soma de dois números: Peça ao usuário dois números e mostre a soma deles.
soma = n1 + n2
# 2. Subtração de dois números: Peça ao usuário dois números e mostre a subtração do
#primeiro pelo segundo.
subtracao = n1 - n2
#3. Multiplicação de dois números: Peça ao usuário dois números e mostre o resultado
#da multiplicação entre eles.
multiplicacao = n1 * n2
#4. Divisão de dois números: Peça ao usuário dois números e mostre o resultado da
#divisão do primeiro pelo segundo.
divisao = n1 / n2
#5. Resto da divisão: Peça dois números inteiros e mostre o resto da divisão entre eles.
resto = n1 % n2
# 6. Potência de um número: Peça um número e um expoente, e mostre o resultado do
# número elevado a esse expoente.
potencia = n1 ** n2
#7. Média de três números: Peça três números e mostre a média deles.
n3 = int(input('Digite o 3º Número: '))
media = (n1 + n2 + n3) / 3
print('A SOMA dos Números n1 e n2 é:',soma)
print('A SUBSTRAÇÃO dos Números n1 e n2 é:',subtracao)
print('A MULTIPLICAÇÃO dos Números n1 e n2 é:',multiplicacao)
print('A DIVISÃO dos Números n1 e n2 é:',divisao)
print('O RESTO DA DIVISÃO dos Números n1 e n2 é:',resto)
print('POTÊNCIA dos Números n1 e expoente n2 é:',potencia)
print('A MÉDIA dos Números n1, n2 e n3 é:',media)
print('#####################################################')
print('8- Conversão de temperatura: Celsius para Fahrenheit')
############################################################
#8. Conversão de temperatura: Converta uma temperatura em graus Celsius para
#Fahrenheit usando a fórmula:
#F=95C+32F = \frac{9}{5}C + 32F=59C+32
celsius = float(input('Digite a temperatura em graus CELSIUS: '))
fahrenheit = (1.8 * celsius) + 32
print('A Temperatura Celsius para Fahrenheit é:',str(fahrenheit)+'°F')
print('#####################################################')
print('9- Conversão de REAIS para DÓLARES:')
#9. Conversão de moeda: Peça um valor em reais e mostre o valor convertido em dólares.
#Considere uma taxa de conversão fixa.
real = float(input('Digite o valor em REAIS para converter em DÓLARES: '))
dolar = 5.61
conversao = real / dolar
print(f'A Conversão de REAIS para DOLARES é US$:{conversao:.2f}')
print('#####################################################')
print('10- Área de um RETÂNGULO:')
#10. Área de um retângulo: Peça a largura e a altura de um retângulo e calcule a área.
largura = float(input("Digite a Largura do Retângulo:"))
altura = float(input("Digite a Altura do Retângulo:"))
print('A Área do RETÂNGULO é:',(largura*altura))
print('#####################################################')
print('11- Perímetro de um QUADRADO:')
# 11. Perímetro de um quadrado: Peça o lado de um quadrado e calcule o perímetro
#(soma dos lados).
lado = float(input("Digite o valor do lado de um Quadrado:"))
perimetro = lado * 4 
print('O Perímetro de um QUADRADO é:',perimetro)
print('#####################################################')
print('12- Área de um TRIÂNGULO:')
# 12. Área de um triângulo: Peça a base e a altura de um triângulo e calcule a área usando
#a fórmula:
base = float(input(" Digite o valor da Base do TRIÂNGULO: "))
altura = float(input(" Digite o valor da Altura do TRIÂNGULO:"))
area = (base * altura) / 2
print('A Área do TRIÂNGULO é:', area)
print('#####################################################')
print('13- Área de um CÍRCULO:')
# 13. Área de um círculo: Peça o raio de um círculo e calcule a área usando a fórmula:
raio = float(input(" Digite o Valor do Raio de um CÍRCULO: "))
pi = 3.14159
area = 3.14159 * raio ** raio
print(f'A Área de um CÍRCULO é: {area: .2f}')
print('#####################################################')
print('14- Conversão de METROS para CENTÍMETROS:')
# 14. Conversão de metros para centímetros: Peça um valor em metros e converta
#para centímetros.
metros = float(input(" Digite o Valor em METROS: "))
conversao = metros * 100
print(f'A Conversão de METROS para CENTÍMETROS é: {conversao:.2f}' +'cm')
print('#####################################################')
print('15- Cálculo de horas TRABALHADAS:')
#15. Cálculo de horas trabalhadas: Peça a quantidade de horas trabalhadas e o valor por
#hora, e calcule o salário total.
horas = float(input('Digite a Quantidade de Horas TRABALHADAS:'))
valor = float (input('Digite o valor por horas TRABALHADAS: '))
print('O valor do SÁLARIO TOTAL é R$:',(horas * valor))
print('#####################################################')
print('16- Preço com DESCONTO:')
# 16. Preço com desconto: Peça o preço de um produto e o percentual de desconto, e
# mostre o preço final com desconto aplicado.
preco_produto = float(input('Digite o valor do PRODUTO R$:'))
valor_percentual = float(input('Digite o valor Percentual do DESCONTO:'))
desconto = preco_produto * valor_percentual / 100
preco_final  = preco_produto - desconto
print('O Preço do PRODUTO é:', preco_produto)
print('O valor Percentual de DESCONTO é:', valor_percentual)
print('O valor do PRODUTO com DESCONTO é:', preco_final)
print('#####################################################')
print('17- Calcular a VELOCIDADE MÉDIA:')
#17. Calcular a velocidade média: Peça a distância percorrida e o tempo gasto, e calcule
#a velocidade média usando a fórmula:
distancia = float(input('Digite a DISTÂNCIA percorrida: '))
tempo = float(input('Digite o TEMPO gasto: '))
v_media = distancia / tempo
print('A VELOCIDADE MÉDIA é:', v_media)
print('#####################################################')
print('18- Converter IDADE em DIAS:')
# 18. Converter idade em dias: Peça a idade de uma pessoa em anos e converta para dias.
# Desconsidere anos bissextos.
idade = float(input('Digite a IDADE:'))
idade_dias = idade * 365
print('A IDADE em DIAS é:', idade_dias)
print('#####################################################')
print('19- Quantidade de SEGUNDOS em 1 DIA:')
# 19. Quantidade de segundos em um dia: Calcule quantos segundos existem em um
#dia (24 horas).
print('#####################################################')
print('20- Calcular o IMC (Índice de Massa Corporal):')
# 20. Calcular o IMC (Índice de Massa Corporal): Peça o peso (em kg) e a altura (em
#metros), e calcule o IMC usando a fórmula:
peso = int(input('Digite o PESO em KG:'))
altura = int(input('Digite a ALTURA:'))
altura2 = altura ** altura
imc = peso / altura2
print(f'o IMC é: {imc: .2f}')
#21. Diferença entre dois números: Peça dois números e mostre a diferença absoluta
#entre eles (sem sinal negativo).
print('#####################################################')
print('21- Diferença entre dois números::')
numero1 = float(input('Digite o PESO em KG:'))
numero2 = float(input('Digite a ALTURA:'))
if numero1 % numero2 and == 0:
    print(f'o NUMERO1 {numero1: .2f}é PAR')
else:
    print(f'o NUMERO2 {numero2: .2f}é IMPAR')
#22. Divisão inteira de dois números: Peça dois números inteiros e mostre o resultado
#da divisão inteira (sem considerar o resto).
print('#####################################################')
print('22- Divisão inteira de dois números:')
numero1 = int(input('Digite o numero1:'))
numero2 = int(input('Digite o numero2:'))
divisao = numero1 // numero2
print('Divisão inteira de dois números é:', divisao)
#23. Valor absoluto de um número: Peça um número e mostre seu valor absoluto.
print('#####################################################')
print('23- Valor absoluto de um número:')
valor_absoluto = float(input('Digite o numero1:'))
print('Valor absoluto de um número é:', abs(valor_absoluto))
#24. Converter km/h para m/s: Peça uma velocidade em km/h e converta para m/s. Use a
#fórmula: #velocidade em m/s=velocidade em km/h3.6\text{velocidade em m/s} =
#\frac{\text{velocidade em km/h}}{3.6}velocidade em m/s=3.6velocidade em km/h
print('#####################################################')
print('24- Converter km/h para m/s:')
velocidade = float(input('Digite a velocidade em KM/H:'))
conversao = velocidade / 3.6
print(f'A VELOCIDADE é {conversao} M/S')
#25. Fórmula de Bhaskara: Peça os coeficientes aaa, bbb e ccc de uma equação do
#segundo grau e calcule as raízes usando a fórmula de Bhaskara.
print('#####################################################')
print('25- Fórmula de Bhaskara:')
import math
# Coeficientes
a = int(input ("Qual o valor de a: " ))
b = int(input ("Qual o valor de b: " ))
c = int(input ("Qual o valor de c: " ))

delta = b**2 - 4*a*c
if delta == 0:
        raiz = ((-1*b) + math.sqrt(delta))/2*a
        raiz2 = ((-1*b)- math.sqrt(delta))/2*a
        print ("O valor da raiz é:" + str(raiz) )
elif delta>0:
        raiz = ((-1*b) + math.sqrt(delta))/2*a
        raiz2 = ((-1*b)- math.sqrt(delta))/2*a
        print ("O valor das raizes é: " + str(raiz) + " e " + str(raiz2) )
else:
        print ("Essa equação não possui raizes reais" )
#26. Valor total de uma compra: Peça o preço de três produtos e calcule o valor total da
#compra.
print('#####################################################')
print('26- Valor total de uma compra:')
produto1 = float (input("Digite o valor do produto 1 : "))
produto2 = float(input("Digite o valor do produto 2: "))
produto3 = float(input ("Digite o valor do produto 3: "))
total = produto1 + produto2 + produto3
print(f'Valor total da COMPRA é {total: .2f}')
#27. Converter dias para semanas e dias: Peça um valor em dias e converta para
#semanas e dias (por exemplo, 10 dias = 1 semana e 3 dias).
print('#####################################################')
print('27- Converter dias para semanas e dias:')
dias = int(input("Digite a quantidade de dias: "))
semana = 7
print(f'Quantidade de DIAS EM SEMANAS É: {total: .2f}')
#28. Desconto progressivo: Peça o valor de uma compra e aplique um desconto de 5% se
#o valor for maior que R$100,
#  e de 10% se for maior que R$500.
print('#####################################################')
print('28- Desconto progressivo:')
valor = float(input('Digite o valor de uma COMPRA: '))

if valor <= 100:
  desconto_progressivo = valor - (valor * 0.05) 
  print(f'Valor do desconto progressivo é 5% : {desconto_progressivo: .2f}')
elif valor >= 500:
  desconto_progressivo = valor - (valor * 0.10) 
  print(f'Valor do desconto progressivo é 10% : {desconto_progressivo: .2f}')
#29. Divisão com casas decimais limitadas: Peça dois números e mostre o resultado
#da divisão com apenas duas casas decimais.
print('#####################################################')
print('29- Divisão com casas decimais limitadas:')
numero1 = float(input('Digite o primeiro valor com CASAS DECIMAIS:'))
numero2 = float(input('Digite o segundo valor com CASAS DECIMAIS:'))
divisao = numero1 / numero2
print(f'Valor da DIVISÃO É: {divisao}')
print(f'Valor da DIVISÃO com 2 casas decimais É: {divisao: .2f}')