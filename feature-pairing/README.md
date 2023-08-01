# Uparivanje obeležja

- Polaznik: Sara Milosavljević
- Saradnici: Srđan Radović

## Uvod

Potrebno je implementirati algoritam za uparivanje izdvojenih
karakterističnih obeležja sa dve slike, i uporediti sa postojećom
bibliotečkom implentacijom (po kvalitetu uparivanja i po vremenu
izvršavanja). Ovaj proces je poslednji korak u spajanju sličnih tačaka
sa dve slike, nakon pronalaženja obeležja i njihovog opisivanja.

## Postupak razvoja

1.  Izdvojiti karakteristična obeležja i njihove opise (iskoristiti gotove implementacije)
2.  Implementirati algoritam za uparivanje obeležja (samostalno, bez korišćenja gotove implementacije!)
3.  Uporediti dobijena uparivanja sa onima koje nađe implementacija iz biblioteke

## Dodatne mogućnosti

- Isprobati i uporediti različite metrike za poređenje obeležja
- Pustiti RANSAC (uz pomoć biblioteke) nad nađenim parovima

## Literatura

- [Feature Matching](https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html)

## Rezultat

Očekivani rezultat je da su nađeni parovi obeležja slični onima koje
nađe implementacija iz biblioteke, dok vreme izvršavanja nije toliko
bitno, može biti duže nego u biblioteci.
