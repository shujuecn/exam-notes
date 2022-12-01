#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-

from datetime import date
import random


def read_question():

    zhongji = []
    with open("./source/zhongji.txt", "r") as f:
        for line in f:
            zhongji.append(line.strip())

    zhongzhen = []
    with open("./source/zhongzhen.txt", "r") as f:
        for line in f:
            zhongzhen.append(line.strip())

    return zhongji, zhongzhen


def new_exam():

    zhongji, zhongzhen = read_question()

    today = date.today()

    with open("./output/{}.txt".format(today), "w") as f:

        # 终端
        print("\n【中基题目】")

        f.write("【中基题目】\n")
        for i in range(4):
            question = random.sample(zhongji, 1)[0]
            f.write("{}、{}\n".format(i + 1, question))

            # 终端
            print("{}、{}".format(i + 1, question))

        # 终端
        print("\n【中诊题目】")

        f.write("\n【中诊题目】\n")
        for i in range(4):
            question = random.sample(zhongzhen, 1)[0]
            f.write("{}、{}\n".format(i + 1, question))

            # 终端
            print("{}、{}".format(i + 1, question))


def main():

    new_exam()

    code = input("\n是否使用本套题目？(y/n): ")
    if code == "y":
        print("\n使用成功...\n")
    elif code == "n":
        print("\n正在重新生成题目...")
        main()


if __name__ == "__main__":
    main()
