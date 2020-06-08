import random
Secret = "Я задумал число от 1 до 1000"
Case = random.randint(1, 1000)
print(Case)
print(Secret)
print("Угадай число: ", end="")
input=int(input())
if input < Case :
    print("Слишком маленькое!")
if input > Case :
    print("Слишком большое!")
if input == Case :
    print("Правильно!")