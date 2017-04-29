# Created an ascii file filled with all combinations of URL escape numbers 0-FF
import argparse

parser = argparse.ArgumentParser(description='Created an ascii file filled with all combinations of URL escape characters.')
parser.add_argument("-out", type=argparse.FileType("wb"),default="URLEscapeAllNumbersFuzz.txt",help='filename to write output')
args = parser.parse_args()

for i in xrange(256):
    args.out.write("%"+ hex(i)[2:].zfill(2))