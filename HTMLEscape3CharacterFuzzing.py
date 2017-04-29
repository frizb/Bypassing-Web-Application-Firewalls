# Created an ascii file filled with combinations of 1 HTML escape characters
# Based on the theory that web application firewalls don't filter HTML Escape characters
# and browsers can parse weird escape combinations in unexpected ways
# which may allow for web application firewall bypass / HTML render anomalies
import argparse

parser = argparse.ArgumentParser(description='Created an ascii file filled with all combinations of HTML escape characters.')
parser.add_argument("-out", type=argparse.FileType("wb"),default="HTMLEscape3CharactersFuzz.txt",help='filename to write output')
parser.add_argument("-rangeStart", metavar='N', type=int, nargs='+', default=33, help='character range to start at 0-256')
parser.add_argument("-rangeStop", metavar='N', type=int, nargs='+', default=126,help='character range to stop at 0-256')
args = parser.parse_args()

for a in xrange(args.rangeStart,args.rangeStop):
        for b in xrange(args.rangeStart, args.rangeStop):
                for c in xrange(args.rangeStart, args.rangeStop):
                        args.out.write("&#" + str(a) + str(b) + str(c) + ";")