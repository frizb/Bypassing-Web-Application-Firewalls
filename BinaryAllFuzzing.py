# Create a binary file with all the characters from 0-255
import argparse

parser = argparse.ArgumentParser(description='Create a binary file with all the characters from 0-255.')
parser.add_argument("-out", type=argparse.FileType("wb"),default="BinaryAllFuzz.bin",help='filename to write output')
args = parser.parse_args()

data = [0,1]

for i in xrange(256):
    args.out.write(chr(i))

