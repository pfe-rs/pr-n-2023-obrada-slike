# Where's Waldo?

- Polaznik: Lana Lejić
- Saradnici: Luka Simić

## Uvod

[*Where’s Waldo*](https://en.wikipedia.org/wiki/Where%27s_Wally%3F) je igra u
kojoj je potrebno pronaći *Waldo*, čoveka sa majicom na crveno-bele
pruge, crveno-belom kapicom i naočarama, na velikoj slici sa različitim
dešavanjima. U ovom domaćem zadatku potrebno je pronaći Waldo metodima
digitalne obrade slike, ili barem pronaći kandidate koji su dovoljno
blizu.

## Postupak razvoja

1. Izdeliti sliku na 64×64 (ili 128×128, ili 256×256) blokove, kako bi se za svaki od tih blokova određivalo da li na njemu ima ili nema *Waldo*. Implementirati detekciju crveno-belo-crveno šare na majici i za svaki od kvadrata izvršiti detekciju. Ispisati rezultate u vidu [matrice konfuzije](https://en.wikipedia.org/wiki/Confusion_matrix). (Glavnina ovog koraka jeste implementacija detekcije, ostalo se implementira radi poređenja sa datim skupom podataka.)
    - Skup podataka sadrži referentne slike (folder original-images) imenovane brojevima od 1 do 19, nad kojima se vrši podela na kvadrate, kao i 64×64 kvadrate (folder 64) podeljene po tome da li sadrže ili ne sadrže *Waldo* (folderi waldo i notwaldo) i imenovane u formatu `[indeks originalne slike]-[x]-[y].jpg`, gde je indeks originalne slike od 1 do 19 (ignorisati indekse veće od 19), a `x` i `y` označavaju koordinate tog kvadrata na slici. Testiranje klasifikatora nad skupom podataka je moguće vršiti samo na osnovu naziva fajlova sa kvadratima i toga da li se nalaze u waldo ili notwaldo folderu.
    - Matrica konfuzije, ukratko, ima četiri polja: True Positive (klasifikovali ste kvadrat kao da ima *Waldo*, i on ga zaista ima), False Positive (klasifikovali ste kvadrat kao da ima *Waldo*, ali ga on zapravo nema), True Negative (klasifikovali ste kvadrat kao da nema *Waldo*, i on ga zaista nema) i False Negative (klasifikovali ste kvadrat kao da nema *Waldo*, ali ga on zapravo ima).
2. Implementirati detekcije ostalih karakteristika *Waldo* (na primer, detekcija naočara, detekcija kapice, itd.) Zabeležiti kolika poboljšanja oni daju.

## Literatura

- [Skup podataka na Kaggle](https://www.kaggle.com/datasets/residentmario/wheres-waldo)

## Rezultat

Krajnji rezultat razvoja jeste matrica konfuzije sa numeričkim
karakteristikama koje se iz nje mogu izvući ([*precision* i *recall*](https://en.wikipedia.org/wiki/Precision_and_recall)).
Nisu definisane tačne granice u kojima ove vrednosti moraju da budu, ali
se od polaznika očekuje da isproba nekoliko načina za njihovo
poboljšanje.
