import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-g','--grades', type=int, nargs='*', help="the base")
parser.add_argument('-f', type=int, nargs='*', help="the base")
args = parser.parse_args()
args.f=len(args.grades)
print(sum(args.grades) / args.f)
