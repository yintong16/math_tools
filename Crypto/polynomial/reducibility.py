

def EisensteinCriterion(p, n):
    """
    Eisenstein's criterion for irreducibility of a polynomial.
    """
    if p[0] % n != 0:
        return False
    for i in range(1, len(p)):
        if p[i] % n != 0:
            return False
    return True

def GaussLemma(p, n):
    """
    Gauss's lemma for irreducibility of a polynomial.
    """
    pass


def isIrreducible(polynomial, n):
    if EisensteinCriterion(polynomial, n):
        return True
    else:
        #Try Gauss's lemma
        if GaussLemma(polynomial, n):
            return True
        else:
            #TODO
            #if drg(p) == 4 do the facterization
            pass
