# Created an ascii file filled with all combinations of HTML escape characters
# Based on the theory that some browsers parse wierd HTML escape combinations in unexpected ways
# which may allow for web application firewall (WAF) bypass
import argparse

parser = argparse.ArgumentParser(description='Created an ascii file filled with all combinations of HTML escape characters.')
parser.add_argument("-out", type=argparse.FileType("wb"),default="HTMLEscapeAllFuzz.txt",help='filename to write output')
args = parser.parse_args()

for a in xrange(10000):
        args.out.write("&#"+str(a)+";")