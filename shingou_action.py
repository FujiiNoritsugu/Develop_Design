from enum import Enum
import sys


class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3


def act_shingou(color):
    # 信号機の色に対応しているかチェック
    if color in (data.value for data in Shingou):
        raise Exception('信号機の色に対応していません')
    # 信号機のEnumに変換
    shingou = Shingou(color)

    # 信号機の色に対応した処理
    if shingou is Shingou.RED:
        print('とまれ')
    elif shingou is Shingou.BLUE:
        print('すすめ')
    elif shingou is Shingou.YELLOW:
        print('ちゅうい')

    return shingou


if __name__ == '__main__':
    act_shingou(int(sys.argv[1]))
