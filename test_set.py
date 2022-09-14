import datetime
from random import randint


def main():
    a = [randint(0, 100000000) for i in range(1000000)]
    print('a start')
    checked_list = [randint(0, 100000000) for i in range(100)]
    start_a = datetime.datetime.now()
    for temp in checked_list:
        if temp in a:
            print(f'temp:{temp} in a')
    print('a end')
    a_time = datetime.datetime.now() - start_a
    print(f'a_time:{a_time}')
    b = set(a)
    print('b start')
    start_b = datetime.datetime.now()
    for temp in checked_list:
        if temp in b:
            print(f'temp:{temp} in b')
    print('b end')
    b_time = datetime.datetime.now() - start_b
    print(f'b_time:{b_time}')


if __name__ == '__main__':
    main()
