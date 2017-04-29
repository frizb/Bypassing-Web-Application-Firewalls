# Created an ascii file filled with all combinations of URL escape characters
# I have noticed that some webservers parse wierd escape combination %*3 %(* in unexpected ways
# which may allow for web application firewall bypass
import argparse

parser = argparse.ArgumentParser(description='Created an ascii file filled with all combinations of URL escape characters.')
parser.add_argument("-out", type=argparse.FileType("wb"),default="URLEscapeCharactersAllFuzz.txt",help='filename to write output')
args = parser.parse_args()

for a in xrange(256):
    for b in xrange(256):
        args.out.write("%"+chr(a)+chr(b))