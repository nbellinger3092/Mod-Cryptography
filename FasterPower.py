## Fast Power w/ bit shift
## Nick Bellinger


def pow_mod(g,a,p):
    "Calculate (x ** y) % z efficiently."
    number = 1
    while a:
        if a & 1:
            number = number * g % p
        a >>= 1
        g = g * g % p
    return number