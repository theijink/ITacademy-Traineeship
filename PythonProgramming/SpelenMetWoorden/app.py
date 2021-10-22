'''
Spelen met woorden

In deze opdracht ga je spelen met woorden. We hebben een bestand met veel Nederlandse woorden. In deze opdracht ga je met je Python-kennis tot nu toe proberen om wat van deze woorden te maken.
Het bestand met woorden vind je hier. Alternatief kun je eens eens een blik werpen op de OpenTaal woordenlijst.
In deze opdracht probeer je antwoord te geven op enkele van de volgende vragen:

Q   Aantal woorden in dit bestand (zie voorbeeld hierna)
A   413550
Q   Het woord met de meeste letters
A   aansprakelijkheidswaardevaststellingsveranderingen
Q   Alle palindromen, zoals lepel
A   201
Q   Alle woorden die ‘omgekeerd’ ook voorkomen in de lijst
A   dat is palindromen.. (201 stuks)
Q   Of een ingevoerd woord voorkomt in de lijst, of als onderdeel van woorden
A   input statement werkt
Q   Alle woorden uit de woordenlijst die je kunt maken van de letters van een ingevoerd woord (anagrammen)
A   dit werkt tot op zekere hoogte: duplicate letters worden niet mee genomen
Q   Woorden die rijmen op een ingevoerd woord
A   dit werkt niet zo goed nog
Q   Maak een raadspel, waarbij je alle letters van het woord in alfabetische volgorde plaatst en waar de gebruiker het oorspronkelijke woord moet raden
A   die functie werkt

Het is niet nodig om elk van de vragen te beantwoorden. Maak er wat leuks van!
'''

from random import choice

# Spelen met woorden
# Wat Python code om alvast aan de slag te kunnen
# Het bestand 'woorden.txt.zip' staat op deze pagina

bestand_met_woorden = open("woorden.txt", "rt") # alleen-lezen van tekst
# lijst_met_woorden = bestand_met_woorden.readlines()
lijst_met_woorden = bestand_met_woorden.read().splitlines()
bestand_met_woorden.close()

aantal_woorden = 0
langste_woord = ''
palindromen = []
for woord in lijst_met_woorden:
    if len(woord)>len(langste_woord):
      langste_woord=woord
    if woord==woord[::-1]:
        palindromen.append(woord)
        #print(woord)
    aantal_woorden = aantal_woorden + 1

gokwoord=input('\n\tWelk woord bedoel je?\t')
if gokwoord in lijst_met_woorden:
    #print('\nJA! {} staat in de lijst'.format(gokwoord))
    gokwoord_in_lijst='wel'
else:
    #print('\nHelaas, {} staat niet in de lijst'.format(gokwoord))
    gokwoord_in_lijst='niet'

gokletters=input('\n\tMet welke letters wil je een woord maken? Typ letters aan elkaar, duplicaten worden niet meegerekend:\t')
gokletters=[i for i in gokletters]
gokletterwoorden=[]
for woord in lijst_met_woorden:
    for letter in gokletters:
        if not letter in woord:
            break
        elif letter==gokletters[-1]:
            #print('{} kan worden gemaakt van de gekozen letters {}'.format(woord, gokletters))
            gokletterwoorden.append(woord)
        else:
            pass

rijmwoord=input('\n\tVul een rijmwoord in: \t')
klanken = ['a', 'e', 'i', 'o', 'u', 'ij', 'oe', 'au', 'ou', 'aa', 'ee', 'ie', 'ei', 'oo']
rijmwoord_klanken=[]
rijmwoorden = []
for klank in klanken:
    if klank in rijmwoord:
        rijmwoord_klanken.append(klank)

i=0
for woord in lijst_met_woorden:
    i+=1
    lijstwoord_klanken=[]
    for klank in klanken:
        if klank in rijmwoord_klanken:
            lijstwoord_klanken.append(klank)
    
    if len(rijmwoord_klanken)==1 and len(lijstwoord_klanken)>=1:
        if rijmwoord_klanken[-1]==lijstwoord_klanken[-1]:
            #print('{} rijmt op {}'.format(rijmwoord, woord))
            rijmwoorden.append(woord)
    elif len(rijmwoord_klanken)>1 and len(lijstwoord_klanken)>1:
        if rijmwoord_klanken[-1]==lijstwoord_klanken[-1] and rijmwoord_klanken[-2]==lijstwoord_klanken[-2]:
            #print('{} rijmt op {}'.format(rijmwoord, woord))
            rijmwoorden.append(woord)
    if woord in rijmwoorden and False:
        print('rijmwoord', rijmwoord)
        print('rijmwoordklanken:\t', rijmwoord_klanken)
        print('lijstwoord', woord)
        print('lijstwoordklanken:\t', lijstwoord_klanken) 

keuzewoord = lijst_met_woorden[choice(range(0, len(lijst_met_woorden)))]
sorted_woord = sorted(keuzewoord)
geraden_woord = input('\n\tWelk woord denk je dat hier zou moeten staan? {}:\t'.format(sorted_woord))
if geraden_woord==keuzewoord:
    geraden_uitslag='goed'
else:
    geraden_uitslag='fout'



print('\n### statistieken van de woordenlijst ###')
print('totaal aantal woorden:\t', len(lijst_met_woorden))
print('langste woord:\t', langste_woord)
print('aantal palindromen:\t', len(palindromen))
print('het woord {} staat {} in de lijst'.format(gokwoord, gokwoord_in_lijst))
print('{} woorden uit de lijst zijn opgebouwd uit de letters {}'.format(len(gokletterwoorden), gokletters))
print('{} woorden uit de lijt rijmen op {}'.format(len(rijmwoorden), rijmwoord))
print('De letters {} zouden het woord {} moeten vormen, je dacht {} dus dat is {}'.format(sorted_woord, keuzewoord, geraden_woord, geraden_uitslag))
