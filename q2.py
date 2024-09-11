#questão 2

string = input('Digite uma string\n')
count = string.count('a') + string.count('A')
if(count > 0):
  print("A letra 'a' existe na string")
  print(count)
else:
  print("A letra 'a' não existe na string")
