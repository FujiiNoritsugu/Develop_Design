import datetime


def main():
    a = [i for i in range(100000000)]
    print('a start')
    start_a = datetime.datetime.now()
    for temp in (333, 666, 999):
        if temp in a:
            print(f'temp:{temp} in a')
    print('a end')
    a_time = datetime.datetime.now() - start_a
    print(f'a_time:{a_time}')
    b = set(a)
    print('b start')
    start_b = datetime.datetime.now()
    for temp in (333, 666, 999):
        if temp in b:
            print(f'temp:{temp} in b')
    print('b end')
    b_time = datetime.datetime.now() - start_b
    print(f'b_time:{b_time}')


if __name__ == '__main__':
    main()
