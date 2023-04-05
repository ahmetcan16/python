def find_fact(x):
    """ faktöriyel hesabı"""
    çarpım_değeri = 1
    for i in range(x,0,-1):
        çarpım_değeri *= i
    return çarpım_değeri


def find_hypo(x,y):
    """dik üçgenin hipotenüs hesabı"""
    return (x ** 2 + y ** 2) ** 0.5

pi = 3.14

e = 2.7182

def ekok_bulma(sayı1,sayı2):
    
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i


        elif (sayı1 % i ==  0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    
    return ekok