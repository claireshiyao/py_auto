import random
import string

# 随机产生一串字符，包含大小写字母、数字、特殊字符+_-.@
def generate_random_string_all(num):
    H = string.ascii_letters+string.digits+"+_-.@"
    randstr = ''
    for i in range(num):
        randstr += random.choice(H)
    return randstr

# 随机产生一串字符，包含大小写字母和数字
def generate_random_string(num):
    H = string.ascii_letters + string.digits
    randstr = ''
    for i in range(num):
        randstr += random.choice(H)
    return randstr

if __name__ == '__main__':
    print(generate_random_string_all(6))
    print(generate_random_string(6))
