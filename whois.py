import os
import argparse
from conditions import conditions


def push_file(file):
    with open(file, 'r') as file1:
        num = 1
        for line in file1:
            domain = os.popen("whois" + " " + line)
            domain = domain.read()
            result = (domain.split('\n'))
            conditions(result, line, num)
            num += 1


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", help="add file of domain names here")
    args = vars(ap.parse_args())

    if args['file']:
        push_file(file=args["file"])

