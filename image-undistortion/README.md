> *Polaznici:* *Saradnici:*
>
> Ime Prezime Pavle Pađin (priprema)

## Uvod

Data je slika koja je iskrivljena na određeni način. Potrebno je
ispraviti datu sliku. U zavisnosti od dela projekta, transformacija koja
je primenjena može, a ne mora biti poznata.

## Postupak razvoja

 1.  Slika je rotirana za poznati ugao od 30 stepeni (rotated30.png). Potrebno je ručno implementirati transformaciju koja će datu sliku ispraviti (bez korišćenja gotovih funkcija).
2.  Slika je rotirana za nepoznati ugao (rotatedUnknown.png). Potrebno je prvo nekako softverski izvršiti procenu tog ugla, te onda uraditi inverznu rotaciju poput one u prethodnom delu, samo za novi ugao.
3.  Slika je transformisana nepoznatom afinom transformacijom. Potrebno je naći parametre te afine transformacije, pa onda izvršiti inverznu afinu transformaciju radi dobijanja ispravljene slike.

## Dodatne mogućnosti

- Samostalno dodavanje različitih deformacija slici i vršenje ispravljanja

## Literatura

 - Slike su u istom folderu kao uputstvo
- [Rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix) na Vikipediji
- [What are affine transformations?](https://www.youtube.com/watch?v=E3Phj6J287o&ab_channel=LeiosLabs) na *YouTube*

## Rezultat

Rezultat rada na projektu je algoritam za ispravljanje slike.
Kompleksnost samih transformacija koje se mogu invertovati (i slika time
ispraviti) zavisi od dela projekta koji je urađen.
