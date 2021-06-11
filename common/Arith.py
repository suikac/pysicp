"""
Arithmetic computation
"""

# return the greatest common divider of a and b
def gcd(a, b):
    return b if a == 0 else a if b == 0 else gcd(b, a % b)
