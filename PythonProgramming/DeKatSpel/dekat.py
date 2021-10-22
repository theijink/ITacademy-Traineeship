'''Waar is de kat geweest simulatie'''

from random import choice


## 5 dozen, waarvan 1 met kat
## zoek de kat in 1 van de dozen
## kat verplaatst naar nevenliggende doos

# aantal_dozen      int
# doos_met_kat      int
# aantal_pogingen   int
# doos_te_openen    int
# kat_gevonden


def verplaats_kat(doos_met_kat):
    if doos_met_kat==0:
        doos_met_kat+=1
    elif doos_met_kat==aantal_dozen:
        doos_met_kat-=1
    else:
        doos_met_kat+=choice([-1, 1])
    return doos_met_kat

def welke_doos():
    doos_te_openen=input("Pick a box (0-{}): ".format(aantal_dozen))
    try:
        doos_te_openen=int(doos_te_openen)
    except:
        print("You're disqualified for entering invalid numbers")
        quit()
    return doos_te_openen


aantal_dozen = 5
doos_met_kat=choice(range(aantal_dozen))
kat_gevonden=False
aantal_pogingen=0

while kat_gevonden==False:
    aantal_pogingen+=1
    doos_te_openen=welke_doos()
    if doos_te_openen==doos_met_kat:
        kat_gevonden=True
    else:
        doos_met_kat=verplaats_kat(doos_met_kat)

print("You were right! The cat was in box {}".format(doos_met_kat))


