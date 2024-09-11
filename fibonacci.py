#primeira questão

first = 0
second = 1
num = int(input('Digite seu número\n'))
check = True
current = 0
print('Sequência de Fibonacci até o número ou o primeiro maior que ele: \n')
print(current)
while(check):
  if(current == num):
    print('O número está na sequência')
    break
  if(current > num):
    check = False
    print('O número não está na sequência')
  else:
    current = first + second
    first = second
    second = current
    print(current)
