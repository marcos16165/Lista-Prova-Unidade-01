#01. Desenvolva as seguintes funções

#A) A função 'soma' retorna a soma de A e B

def soma(a,b):
    soma = a + b
    return soma

#B) A função 'divide' retorna a divisão de A por B. Alternando para o caso de
#não se possível a divisão por zero, neste caso deve retornar 'None'

def divide(a,b):
    if a != 0 and b != 0:
        divide = a / b
        return divide
    else:
        return None

#C) A função 'areaTri' retorna o cálculo da área do triângulo, dado os
#valores 'base' e 'altura'

def areaTri(base,altura):
    area = (base * altura) / 2
    return area

#D) A função 'areaCirc' retorna o cálculo da área do círculo, dado o valor
#do 'raio'. Utilize a variável pi para o cálculo da área.

def areaCirc(raio):
    area = 3.1415 * (raio ** 2)
    return area

#E) A função 'seno' retorna o cálculo do seno de um ángulo, dados os
#valores do cateto oposto ao ángulo e da hipotenusa

def seno(catops,hipo):
    seno = catops / hipo
    return seno

#F) A função 'potencia' recebe dois números A e B (base e expoente
#respectivamente) e retorna A^B

def potencia(a,b):
    potencia = a ** b
    return potencia

#02.

#x=8
#if x>=8.5:
#    print('Conceito A')
#if x>=7.5:
#    print('Conceito B')
#if x>=5.5:
#    print('Conceito C')
#if x>=5:
#    print('Conceito D')

#Conceito B
#Conceito C
#Conceito D
   
#03.

#x=8
#if x>=8.5:
#    print('Conceito A')
#elif x>=7.5:
#    print('Conceito B')
#elif x>=5.5:
#    print('Conceito C')
#elif x>=5:
#    print('Conceito D')

#Conceito B

#04.

#x=8
#y=5
#z=13
#if x>=1 and x<=31:
#    if y>0 and y<13:
#        if (x+y)!= z:
#            print('A data de hoje é 8/5/2018')
#        else:
#            print('A data de hoje não é 8/5/13')

#A data de hoje não é 8/5/13

#05. Crie a 'função determinar_o_omaior_numero' que receba cinco números e
#retorne o maior valor de entre eles.

def determinar_o_maior_numero(a,b,c,d,e):
    
    maior = a
    
    if b > a and b > c and b > d and b > e:
        maior = b
        
    if c > a and c > b and c > d and c > e:
        maior = c

    if d > a and d > b and d > c and d > e:
        maior = d
        
    if e > a and e > b and e > c and e > d:
        maior = e

    return maior
    

#06. Crie uma função que permita imprimir a palavra SPAM, N vezes.
#Ultilizando o laço 'for'.

def spam_for(n):
    for i in range(n):
        print('SPAM')


#07. Crie uma função que permita imprimir a palavra SPAM, N vezes.
#Ultilizando o laço 'while'.

def spam_while(n):
    cont = 0
    while n > 1:
        print('SPAM')
        cont += 1

#08. Crie uma função que pertima mostar uma sequência de números ímpares
#de 1 até n.

def impares(n):
    for i in range(1, n+1, 2):
        print (i)

#09. Crie uma função que permita mostrar um sequência de números inteiros,
#no intervalo [x,y].Consídere x < y.
        
def intervalo(x, y):
    if x < y:
        for i in range(x, y+1, 1):
            print(i)
        
#10. Crie uma função que permita mostrar um sequência de números inteiros,
#no intervalo [x,y). Considere x < y.

def intervalo_direita(x,y):
    if x < y:
        for i in range(x, y, 1):
            print(i)
            
#11. Crie uma função que permita mostrar um sequência de números inteiros,
#no intervalo (x,y]. Considere x < y.

def intervalo_esquerda(x,y):
    if x < y:
        for i in range(x+1, y+1, 1):
            print(i)

#12 Crie uma função que permita somar a sequência de números inteiros,
#no intervalo [x,y].Consídere x < y.

def intervalo_soma(x, y):
    if x < y:
        soma = 0
        for i in range(x, y+1, 1):
            soma += i
        print(soma)

    else:
        return None

#13. Crie uma função que permita o calculo da seguinte somatória

def somatoria(n):
    soma = 0
    for i in range(1, n+1, 1):
        if i % 2 == 0:
            soma += i
        else:
            soma -= i
    print(soma)
        
#14. Crie um função em que, dado um inteiro não-negativo n, seja
#possível determinar n!

def fatorial(n):
    multi = 1
    while n > 1:
        multi *= n
        n -= 1
    print(multi)
    
#15. Dada a função da questão anterior, calcule o fatorial de 1.000.000

#inf

#16. Escreva uma função encaixa que, recebendo dois números inteiros A e
#B como parâmetros, verifique se B corresponde aos últimos digitos de A.
#Por exemplo 45 encaixa em 12345, 2026 ancaixa em 2026, 12345 não
#encaixa em 45.

#17. Crie uma função que permita imprimir a soma dos n primeiros números
#da sequência de Fibonacci. Considere n >= 2

def fibonacci(n):
    soma = 0
    a = 0
    b = 1
    while b < n:
        a = b
        b = a + b
        soma += a
    print(soma)

#18. Indique a mensagem que apresentará a execução da seguinte função.
#Considere como parâmetro de entrada a lista [1,2,4,16,32,64,-128].

def funcao1(lista):
    temp1 = lista[0] #Primeiro elemento 
    temp2 = lista[len(lista)-1] #"len" conta os elementos - 1, ou seja 64
    for elemento in lista:
        if temp1>elemento:
            tem1 = elemento
        if temp2<elemento:
            temp2 = elemento
    print (temp1, temp2)

#1 64
    
#19. Dadas uma lista numérica A, crie uma função que permita imprimir
#todos seus elementos.

def clonelista(lista):
    clone = []
    for i in lista:
        clone.append(i)
    return clone

#20. Crie uma função que permita somar todos os elementos de uma lista.

def soma_lista(lista):
    soma = 0
    clone = []
    for i in lista:
        clone.append(i)
        soma += i
    return soma

#21. Crie uma função que permita verificar se 2 listas, dadas como
#parâmetros, são iguais.

def compare_listas(lista1,lista2):
    if lista1 == lista2:
        return('As listas são íguais')
    else:
        return None

#22. dada a função 'sjakj' indique a saída para n = 10

def sjakj(n):
    if n==0:
        print ("fogo!")
    else:
        print (n)
        sjakj(n-1)
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1
#fogo!

#23. Indique a mensagem que apresentará a execução da seguinte função.
#Considerando como parãmetros: x1=2, y1=3, x2=4, y2=5,ra=112233.

def operacoes(x1, y1, x2, y2, ra):
    p = 0
    while p <(x2-x1)**2 + (y2-y1)**2:
        if x1 < x2:
            print (ra,x1)
        else:
            print(ra,y1)
        p = p+2
    
#112233 2
#112233 2
#112233 2
#112233 2
    
