# Slika u goblen

- Polaznik: Hafiza Kahrimanović
- Saradnici: Andrej Lojdl

## Uvod

Gobleni su tapiserije koji se prave vezenjem niti od vune na platno na
specifičan način, najčešće se prave mali iksići. Suštinski ovime onaj ko
veze pravi “piksele” koji se pojavljuju kao deo slike na goblenu.

Zadatak jeste da se ulazna slika proizvoljne veličine (ali sličnih
odnosa stranica) transformiše u digitalizovane goblene, korišćenjem
palete boja koja je unapred definisana.

## Postupak razvoja

Preporuka je da se sam zadatak rešava/radi u delovima i to u sledećem
redosledu:

1. Smanjivanje veličine slike baš na veličinu izlazne slike koristeći neku od biblioteka.
2. Biranje boje goblenskog piksela, na osnovu dobijenog piksela potrebno je odabrati boju iz palete boja koja je najsličnija boji superpiksela. Za početak sam definisati 64 osnovne boje korišćenjem neke onlajn generators palete boja.
3. Svođenje ulazne slike na rezoluciju izlaznog goblena. Sami “pikseli” goblena se dobijaju od piksela ulazne slike koju utiču na dati piksel. Ovde je potrebno da sami smanjite veličinu slike.
4. Potrebno je omogućiti da se kao ulazni parametri definiše paleta boja koja je dostupna.

## Dodatne mogućnosti

- Sam zadatak se može dalje unaprediti time što se omogući biranje “pravougaonika baš takvih dimenzija” kao što je goblen sa ulazne slike.
- Moguće je aktivno unutar programa menjati paletu boja koja je dostupna.

## Literatura

- [Goblen – Wikipedija / Википедија (wikipedia.org)](https://sh.wikipedia.org/wiki/Goblen)
- [Python Image Resize With Pillow and OpenCV (cloudinary.com)](https://cloudinary.com/guides/bulk-image-resize/python-image-resize-with-pillow-and-opencv)

## Rezultat

Maksimalni krajni rezultat jeste da se može definisati ulazna slika,
definisati “veličina goblena”, odabrati dao ulazne slike koji želimo da
“goblenizujemo” i da se definiše paleta boja koja se onda koristi za
“goblenizaciju”.
