from random import randint)
N=randint(1,100)
tries=0
K=int (input ("Угадайте целое число от 1 до 100:"))
while True:
Neint (inout ("Введите ваше предположение:"))
tries+=1 if K==N:
print ("Поздравляю, вы угадали число за",tries, "попыток!")
break
if K < N:
print ("Загаданное число больше вашего")
if K. > N:
print ("Загаданное число меньше вашего")
