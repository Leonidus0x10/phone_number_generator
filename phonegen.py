# -*- coding: utf-8 -*-
# generates phone numbers given an area code
# usage: python3 numbergen.py 602 list.txt
# written by leonidus
import sys
import itertools


def main():
    area_code = sys.argv[1]
    file = sys.argv[2]
    justnum = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    gen_num = list(itertools.permutations(justnum, 7))
    with open(file, "w") as f:
        for num in gen_num:
            iter_num = str(''.join(num))
            generated_number = area_code + iter_num
            # print(generated) uncomment this if you want to see the output
            f.write(generated_number + "\n")


if __name__ == "__main__":
    main()
