# Određivanje nepoznate transformacije

- Polaznik: Vuk Savić
- Saradnici: Milomir Stefanović

## Uvod

Date su dve slike iste scene. Potrebno je odrediti transformaciju uz
koju će druga slika što više ličiti na prvu (ili obrnuto). Jedna od
mogućih primena ovog procesa je kod spajanja više slika u panoramu, gde
je bitno poravnati slike pre spajanja.

## Postupak razvoja

1. Pronaći karakteristične tačke na slici (koristeći gotovu implementaciju)
2. Izdvojiti opise tačaka (koristeći gotovu implementaciju)
3. Upariti tačke sa obe slike (koristeći gotovu implementaciju)
4. Odrediti traženu transformaciju uz pomoć RANSAC metoda (samostalno implementirati!)
5. Prikazati transformisanu sliku preko druge (polutransparentno), da bi se videlo koliko su slične

## Dodatne mogućnosti

- Uporediti samostalno implementirani RANSAC sa implementacijom iz neke biblioteke, po tačnosti određene transformacije i po brzini izračunavanja

## Literatura

- [RANSAC](https://en.wikipedia.org/wiki/Random_sample_consensus)

## Rezultat

Očekivani rezultat je da implementirani metod može da odredi traženu
transformaciju. Nije neophodno da brzina izračunavanja bude optimalna.
