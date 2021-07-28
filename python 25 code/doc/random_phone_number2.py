# author by claire
import random


def generate_phone_number():
    phone = '1' + random.choice(["3", "5", "7", "8"])
    for i in range(9):
        num = random.randint(0,9)
        phone += str(num)
    return phone

if __name__ == '__main__':
    print(generate_phone_number())