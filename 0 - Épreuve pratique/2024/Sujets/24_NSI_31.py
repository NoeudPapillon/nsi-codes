#Alexandre, sujet 31

#exercice 1
def multiplication(a, b):
    mult = 0
    for i in range(abs(a)):
        if a<0 and b<0:
            mult += abs(b)
        else:
            mult += b
    return mult





#exercice 2
def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = debut + (fin - debut) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m -1
    return False

