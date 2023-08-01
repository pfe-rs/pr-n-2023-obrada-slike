# Slika u PDF

- Polaznik: Nemanja Obradović
- Saradnici: Milomir Stefanović

## Uvod

Aplikacije za skeniranje na telefonima široko su korišćene i značajne u
digitalizaciji dokumenata. Neprecizno slikanje, prisustvo drugih
predmeta u kadru, kao i izobličenja i iskrivljenja samo su neke su od
stvari koje utiču na čitljivost, upotrebljivost i formalan izgled
skeniranog dokumenta. Potrebno je razviti algoritam koji precizno
identifikuje ivice dokumenta, ispravlja ga, obrađuje i izvršava njegovo
čuvanje u PDF fomratu.

## Postupak razvoja

1. Analizirati i odrediti tačne postupke implementacije rešenja ove problematike (skenera).
2. Primenom odabranih metoda filtriranja/transformacija, detektovati ivice dokumenta i ivične tačke (ćoškove) papira.
3. Izvršiti odgovarajući vid transformacije (rotacija/geometrijska transformacija/...), radi samostalnog izdvajanja dokumenta sa slike.
4. Čuvati obrađenu sliku u PDF formatu.

Dozvoljeno je koristiti ugrađene funkcije u svakom koraku po potrebi.

## Dodatne mogućnosti

- Pronaći (ili napraviti) dodatne primerke za analizu.
- Podesiti adaptivne parametre za sve primerke. Algoritam treba da radi za sve okolnosti.

## Rezultat

Nakon svakog koraka prikazati sliku, objasniti primenjenu transformaciju
i objasniti odabir konkretnih parametara. Finalni produkt treba da
predstavlja PDF priložene slike.
