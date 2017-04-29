# Created an ascii file filled with ascii character (33-126) combinations of URL escape characters
# I have noticed that some webservers parse %*3 %(* in unexpected ways which may allow for web application firewall bypass
import argparse

parser = argparse.ArgumentParser(description='Created an ascii file filled with all combinations of URL escape characters.')
parser.add_argument("-out", type=argparse.FileType("wb"),default="URLEscapeCharactersFuzz.txt",help='filename to write output')
parser.add_argument("-rangeStart", metavar='N', type=int, nargs='+', default=33, help='character range to start at 0-256')
parser.add_argument("-rangeStop", metavar='N', type=int, nargs='+', default=126,help='character range to stop at 0-256')
args = parser.parse_args()

for a in xrange(args.rangeStart,args.rangeStop):
    for b in xrange(args.rangeStart,args.rangeStop):
        args.out.write("%"+chr(a)+chr(b))