# author by claire
import random


def generate_phone_number():
    phone = '1' + random.choice(["30", "31", "32", "33", "35", "36", "37", "38", "39",
                                 "45", "47", "49",
                                 "50", "51", "52", "53", "55", "56", "57", "58", "59",
                                 "62", "66",
                                 "72", "73", "75", "76", "77", "78",
                                 "80", "81", "82", "83", "84", "85", "86", "87", "88", "89",
                                 "90", "91", "93", "95", "96", "97", "98", "99"
                                 ])
    for i in range(8):
        num = random.randint(0, 9)
        phone += str(num)
    return phone

if __name__ == '__main__':
    print(generate_phone_number())