from math import log2

#fonction pour calculer la quantite d'information
def QT(Pi):
    QT=log2(1/Pi)
    return QT

#fonction pour calculer l'entropie d'ordre 0
def ENT0(C):
    H=0
    for i, j in C.items():
        a = j * QT(j)
        H += a
    return H


#fonction pour calculer l'entropie d'ordre 1
def ENT1(dictA,dictB):
    H1=0
    for alphabet in dictA:
        for double in dictB:
            if alphabet[:-1] == double:
                H1+=dictA[alphabet]*log2(dictB[double]/dictA[alphabet])
            else:
                continue
    return H1

#fonction pour calculer l'entropie d'ordre 2
def ENT2(dictA,dictB):  
    H2=0
    for alphabet in dictA:
        for double in dictB:
            if alphabet[:-1] == double:
                H2+=dictA[alphabet]*log2(dictB[double]/dictA[alphabet])
            else:
                continue
    return H2
#fonction pour calculer l'entropie d'ordre 3
def ENT3(dictA,dictB):
    H3=0
    for alphabet in dictA:
        for double in dictB:
            if alphabet[:-1] == double:
                H3+=dictA[alphabet]*log2(dictB[double]/dictA[alphabet])
            else:
                continue
    return H3

#fonction pour calculer l'entropie d'ordre 4
def ENT4(dictA,dictB):
    H4=0
    for alphabet in dictA:
        for double in dictB:
            if alphabet[:-1] == double:
                H4+=dictA[alphabet]*log2(dictB[double]/dictA[alphabet])
            else:
                continue
    return H4

#fonction qui verifier l'entroprie
def Vrf(C):
    k1 = len(C)
    if ENT0(C) <= log2(k1) and ENT0(C) >= 0:
        print("correct")
    else:
        print("error")

#fonction pour calcul frq de rpt d'un alphabet dans le che
def FRQL(Listn):
    List1=[]
    List2=[]
    for p in range(0,len(Listn)):
        if Listn[p] not in List1:
            List1.append(Listn[p])
            M=Listn.count(Listn[p])
            List2.append(M/len(Listn))
    D=dict({})
    for i in range(0,len(List1)):
        D[List1[i]]=List2[i]
    return D

#fonction pour calcul frq de rpt d'un alphabet dans le che
def FRQt(tex):
    x=len(tex)
    tex1=[]
    tex2=[]
    for p in range(0,x):
        if tex[p] not in tex2:
            tex2.append(tex[p])
            M=tex.count(tex[p])
            tex1.append(M/len(tex))
    D=dict({})
    for i in range(0,len(tex2)):
        D[tex2[i]]=tex1[i]
    return D

#fonction qui decoupe une chaine de caractere en n symbole
def decouper(tex,ordre):
    tex=tex.replace("\n"," ")
    liste = list()
    for n in range(6):
        n +=1
        newlist = list()
        for i in range(0,len(tex),1):
            s=tex[i:i+n]
            if( len(s)== n):
                newlist.append(tex[i:i+n])
        liste.append(newlist)  

    if( ordre == 1 ):
        return (liste[0])
    elif( ordre == 2 ):
        return (liste[1])
    elif( ordre == 3 ):
        return (liste[2])
    elif( ordre == 4 ):
        return (liste[3])
    elif( ordre == 5 ):
        return (liste[4])
    

za = input("\n donner le nom de votre fichier\n")
lm = open(za)
texte=lm.read()
texte = texte.replace("\n"," ")
texte = texte.rstrip()
texte = texte.lower()


decouper(texte,4)
decouper(texte,5)
E4 = ENT4(FRQL(decouper(texte,5)),FRQL(decouper(texte,4)))
E3 = ENT3(FRQL(decouper(texte,4)),FRQL(decouper(texte,3)))

if((E4>=0,18 and E4<=0.25) and E3>0.46 and E3<=0.56):
    print("ce texte est en français")
elif((E4>=0,14 and E4<=0.21) and E3>=0.35 and E3<=0.46):
    print("ce texte est en anglais")