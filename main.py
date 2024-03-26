#Criar método que recebe 2 valores e retorna True se for divisível e False se não for
def doisValores():
  valor1 = int(input("Digite o primeiro valor: "))
  valor2 = int(input("Digite o segundo valor: "))
  if valor1 % valor2 == 0:
    print("True")
  else:
    print("False")
doisValores()

#Criar método que recebe 3 valores e retorna o maior deles
def maiorValor():
  valor1 = int(input("Digite o primeiro valor:"))
  valor2 = int(input("Digite o segundo valor:"))
  valor3 = int(input("Digite o terceiro valor:"))
  if valor1 > valor2 and valor1 > valor3:
    print("O maior valor é:", valor1)
  elif valor2 > valor1 and valor2 > valor3:
    print("O maior valor é:", valor2)
  else:
    print("O maior valor é:", valor3)
maiorValor()

#Criar método que recebe 1 valor e retorna a soma de todos os valores entre 0 e o valor
def somaValores(valor):
  soma = 0
  for i in range(valor + 1):
      soma += i
  return soma
valor = int(input("Digite um valor: "))
resultado = somaValores(valor)
print("A soma dos valores entre 0 e", valor, "é:", resultado)

#Criar método que recebe um texto e retorna a quantdade de letras
def contarLetras(texto):
  contador = 0
  for letra in texto:
    if letra.isalpha():
      contador += 1
  return contador
texto = input("Digite um texto: ")
quantidade = contarLetras(texto)
print("A quantidade de letras no texto é:", quantidade)

#Criar método para receber uma lista e retornar os elementos da lista
def retornarElementos(lista):
  for elemento in lista:
    print(elemento)
lista = input("Digite uma lista de elementos separados por espaço: ")
lista = lista.split()
retornarElementos(lista)

#Criar método que recebe uma lista e retorna a menor string da lista
def menorString(lista):
  menor = lista[0]
  for string in lista:
    if len(string) < len(menor):
      menor = string
  return menor
lista = input("Digite uma lista de strings separadas por espaço: ")
lista = lista.split()
menor = menorString(lista)
print("A menor string da lista é:", menor)

#Criar método que 1 inteiro (N) e 1 string (S) e imprime na tela N vezes a string S
def imprimir_string_n_vezes(N, S):
  for _ in range(N):
      print(S)
N = int(input("Digite o número de vezes que deseja imprimir a string: "))
S = input("Digite a string que deseja imprimir: ")
imprimir_string_n_vezes(N, S)

#Criar método que recebe 1 valor inteiro e imprime os valores de 1 até o valor recebido
def imprimir_valores(valor):
  for i in range(1, valor + 1):
    print(i)
valor = int(input("Digite um valor inteiro: "))
imprimir_valores(valor)

#Criar método que recebe 3 notas e retorna o conceito da nota
def calcular_conceito(nota1, nota2, nota3):
    if nota1 < 0 or nota2 < 0 or nota3 < 0:
        return "ERRO"
    media = (nota1 + nota2 + nota3) / 3
    if 0.0 <= media < 4.0:
        return "D"
    elif 4.0 <= media < 7.0:
        return "C"
    elif 7.0 <= media < 9.0:
        return "B"
    elif 9.0 <= media <= 10.0:
        return "A"
    else:
        return "Nota inválida"
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
conceito = calcular_conceito(nota1, nota2, nota3)
print("Conceito:", conceito)

#Criar método que recebe 1 inteiro e retorno verdadeiro se for primo ou falso se não for
def eh_primo(numero):
  if numero < 0:
      return False
  if numero < 2:
      return False
  for i in range(2, int(numero**0.5) + 1):
      if numero % i == 0:
          return False
  return True
numero = int(input("Digite um número inteiro: "))
resultado = eh_primo(numero)
print("O número", numero, "é primo?", resultado)