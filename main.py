"""
Un code pour tester si des nombres sont premier
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Retourne un booléen indiquant si le nombre passé en paramètre est premier.
    """
    if p<= 1:
        return False
    n = int(sqrt(p))
    for i in range(2, n+1):
        if p%i == 0:
            return False
    return True

#### Fonction principale


def main():
    """
    Tests de fonction isprime()
    """
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()
