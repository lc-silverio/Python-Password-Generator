import random

# Character Pool
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-@!?=$#%&<>|"


# Input
length = input("Insert a whole positive number: ")
length = int(float(length))

while length < 0:
    print("Valor inserido não é maior que 0")
    length = input("Insira uma valor positivo inteiro: ")
    length = int(float(length))

# Parameters
all = lower+upper+numbers+symbols
password = "".join(random.sample(all, length))
print(password)
