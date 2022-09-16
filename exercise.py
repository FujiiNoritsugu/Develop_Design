from enum import Enum
import sys


class ArgNumber(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    STOP = 999
    OTHER = -1


def param_check(check_fn, param):
    try:
        return check_fn(param)
    except Exception:
        return ArgNumber.OTHER


def make_fn():
    """内部にクロージャでデータを蓄えておく関数

    Returns:
        _type_: 入力用の関数と出力用の関数
    """
    # 内部のデータはリストで保持する
    data_list = []

    def add_value(value):
        data_list.append(value)

    def print_data():
        # 出力時にセットに変換して重複を失くす
        result_list = set(data_list)
        print("コマンドライン引数には999までに以下の数字が含まれていました。")
        for result in result_list:
            print(f"{result}")

    return add_value, print_data


def main(argv):

    # param_checの最初の引数をArgNumberに変換するラムダ式で渡す
    def check(x):
        return param_check(lambda x: ArgNumber(int(x)), x)

    # 内部にクロージャでデータを蓄えておく関数を作成する
    add_value, print_data = make_fn()

    # 引数をジェネレータでチェックして値を格納する
    for arg in (data for data in argv):
        arg = check(arg)
        if arg is ArgNumber.STOP:
            # 終わりの数字が含まれていればそこでストップ
            break
        elif arg is ArgNumber.OTHER:
            add_value("1～5の数値以外")
        else:
            add_value(arg.name)

    # 結果を出力する
    print_data()


if __name__ == '__main__':
    # コマンドラインのプログラムの引数として与えられた数値を引数にする
    main(sys.argv[1:])
