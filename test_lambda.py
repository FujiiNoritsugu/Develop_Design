def main():
    execute_fn(1, lambda a: a + 1)
    execute_fn(3, lambda a: a * 3)
    pre_a = 9
    def new_fn(b, c, d, e): return complex_input(pre_a, b, c, d, e)


def execute_fn(param, param_fn):
    print(param_fn(param))


def complex_input(a, b, c, d, e):
    return a + b + c + d + e


if __name__ = '__main__':
    main()
