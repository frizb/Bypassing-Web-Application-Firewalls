# Create a binary file filled with a specific binary character (0-255)
import argparse

parser = argparse.ArgumentParser(description='Create a binary file filled with a specific binary character (0-255)')
parser.add_argument('-char', metavar='N', type=int, default=65, nargs='+', help='the character number to generate')
parser.add_argument("-out", type=argparse.FileType("wb"),default="BinaryCharFuzz.bin",help='filename to write output')
args = parser.parse_args()

data = [0,1]

for i in xrange(256):
    args.out.write(chr(args.char))

