def add_digit(number):  
    return sum(list(map(int, list(number))))

if __name__ == '__main__':  
    number = input()
    print(add_digit(number))
    