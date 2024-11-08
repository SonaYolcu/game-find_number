from random import randint
print('Добро пожаловать в числовую угадайку')
right_s = int(input())
num = randint(1, right_s)
count=1

def is_valid(n):
      return n.isdigit() and 1<int(n)<right_s
while True:
   n = input('Введите число:')
   if is_valid(n)==False:
     print('А может быть все-таки введем целое число от 1 до 100?')
     continue
   if int(n)<num:
     print('Ваше число меньше загаданного, попробуйте еще разок')
     count+=1
   elif int(n)>num:
     print('Ваше число больше загаданного, попробуйте еще разок')
     count+=1
   else:
      print('Вы угадали, поздравляем!')
      print('Вы угадали через', count, 'попыток')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
print('Играем еще раз!!!')
