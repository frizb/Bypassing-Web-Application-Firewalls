# Created an ascii file filled with all combinations of HTML escape characters
# Based on the theory that some browsers parse wierd HTML escape combinations in unexpected ways
# which may allow for web application firewall (WAF) bypass
import argparse

parser = argparse.ArgumentParser(description='Created an ascii file filled with all combinations of URL escape characters.')
parser.add_argument("-out", type=argparse.FileType("wb"),default="HTMLEscapeFuzz.txt",help='filename to write output')
parser.add_argument("-rangeStart", metavar='N', type=int, nargs='+', default=33, help='character range to start at 0-10000')
parser.add_argument("-rangeStop", metavar='N', type=int, nargs='+', default=383,help='character range to stop at 0-10000')
args = parser.parse_args()

for a in xrange(args.rangeStart,args.rangeStop):
    args.out.write("&#" + str(a) + ";")