def hypotenuse(a, o):
    h = round((a ** 2 + o ** 2) ** (1/2))
    assert a + o > h, "This triangle does not satisfy the mathematic property"
    return h

def pythago(a=0, o=0, h=0):
    assert a == 0 and o == 0 and h == 0, "Positve number require"
    if not a:
        o = round((h ** 2 - o ** 2) ** (1/2))
        return o
    if not o:
        a = round((h ** 2 - a ** 2) ** (1/2))
        return a
    return hypotenuse(a, o)

if __name__ == "__main__":
    print(pythago(a=3, o=4))
    print(pythago(h=5, o=4))
    print(pythago(a=3, h=5))
