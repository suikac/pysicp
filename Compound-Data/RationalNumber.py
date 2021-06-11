from common.Pairs import *
from common.Arith import *

# a make-rat that simplify when construct
def make_rat(numer, denom):
    cons(numer / gcd(numer, denom), denom / gcd(numer, denom))