from math import *

#mon_fichier = open("chiffre3", 'r')
#print(mon_fichier)

def texte(a):
    a = a.replace('w','v')
    a = a.replace('?',"")
    a = a.replace('!',"")
    a = a.replace(',',"")
    a = a.replace('é',"e")
    a = a.replace('à',"a")
    a = a.replace('ç',"c")
    a = a.replace('è',"e")
    a = a.replace('ë',"e")
    a = a.replace('ô',"e")
    a = a.replace(" ","")
    a = a.replace('-',"")
    a = a.replace("_","")
    a = a.replace("'","")
    a = a.replace("ù","u")
    a = a.replace("<","")
    a = a.replace(">","")
    a = a.replace("(","")
    a = a.replace(")","")
    a = a.replace("/","")
    a = a.replace(".","")
    a = a.replace('œ',"oe")
    a = a.replace('’',"")
    a = a.replace("«","")
    a = a.replace("»","")
    a = a.replace(":","")
    a = a.lower()
    return(a)

def tableau():
    global h
    c = ""
    a = input("saisir chaine de caractere :")
    a = texte(a)
    b = "abcdefghijklmnopqrstuvxyz"
    e = a + b
    for f in e:
        if f in c:
            pass
        else :
            c += f
    table = c[0:5], c[5:10], c[10:15], c[15:20], c[20:25]
    h = c
    return table

def afficher_tableau(plateau):
    for ligne in plateau:
        for x in ligne:
            print(x, end=' ')
        print("\n")

def chiffrement(plateau, e):
    global v, w
    w = ""
    v = ""
    global h, k
    for g in range(0, 25):
        if h[g] == e:
            ligne = floor(g / 5)
            colonne = (g % 5)
            position_x = plateau[ligne][0]
            position_y = plateau[-1][colonne]
            w += position_x
            v += position_y
    print(w, end='')
    print(v, end='')

def clef():
    global w, v
    i = 0
    f=""
    for j in range(len(w)):
        f += w[i:i+k]
        f += v[i:i+k]
        i += k
    print(f, end='')


def chiffrement_texte(plateau):
    global k
    j = 0
    m = input("saisir texte a coder :")
    k = eval(input("saisir la clef :"))
    m = texte(m)
    m = list(m)
    while j < len(m):
        e = (m[j])
        chiffrement(plateau, e)
        j += 1
    clef()

def dechiffrement(plateau):
    global q, m, x
    n = 0
    a = ""
    b = ""
    ligne = 0
    colonne = 0
    z = q
    r = list(z)
    global h
    for g in range(0, 25):
        if h[g] == r[0]:
            ligne = floor(g / 5)
    for g in range(0, 25):
        if h[g] == r[1]:
            colonne = (g % 5)
    print(plateau[ligne][colonne], end='')
    #for j in range(len(x // 2)):
        #a += x[n:n+m]
        #b += x[n+m:n+m+m]
        #n += m * 2


def dechiffrement_texte(plateau):
    global q, m, x
    k = 0
    x = input("saisir texte a decoder :")
    #x = mon_fichier
    m = eval(input("saisir clef :"))
    l = texte(x)
    while k < len(l):
        q  = l[k]+l[k+1]
        dechiffrement(plateau)
        k += 2

def main():
    v = input("voulez vous chiffrer un texte ? (oui/non) :")
    if v == 'oui':
        plateau = tableau()
        afficher_tableau(plateau)
        chiffrement_texte(plateau)
    else :
        w = input("voulez vous dechiffrer un texte ? (oui/non) :")
        if w == 'oui':
            plateau = tableau()
            afficher_tableau(plateau)
            dechiffrement_texte(plateau)
        else :
            return False

main()