# Segmentacija pluća sa CT snimaka

- Polaznik: Emilija Pavlović
- Saradnici: Diana Sekulić

## Uvod

Cilj ovog domaćeg zadatka jeste da se upoznaju koncepti digitalne obrade
slike u medicinskom imidžingu, specifično u kompjuterizovanoj
tomografiji (CT). Potrebno je pročitati slike sa CT-a, izdvojiti oblast
na slici gde se nalaze pluća a zatim i izračunati stvarnu površinu pluća
u $mm^{2}$.

Medicinske slike osim samog zapisa slike sadrže još dodatnih podataka o
uslovima pod kojima je subjekat slikan koji su nam potrebni pri obradi i
ti podaci se zapisuju u hederu slike. Zbog ovoga, medicinske slike nisu
zapisane u standardnom formatu (jpg, png, tif,…) već u nekim drugim
formatima (DICOM, nifty,…).

## Postupak razvoja

1. Potrebno je učitati slike sa CT-a. Kako smo već napomenuli, slike nisu u standardnom formatu (date slike specifično imaju ekstenziju .nii), te je za učitavanje potrebno istražiti biblioteku ***nibabel***, učitati slike pomoću nje i prikazati ih.
2. Istražiti šta su CT brojevi, ograničiti ih u potrebnom opsegu i prikazati slike u 256 nijansi sive, a potom binarizovati sliku i prikazati taj rezultat.
3. Odlučiti se za neki algoritam za izdvajanje kontura i izdvojiti sve konture sa slike bez korišćenja bibliotečkih funkcija. Izdvojiti konturu pluća i obojiti regiju od interesa. Prikazati rezultat.
4. Iz hedera slike pročitati veličinu piksela i izračunati površinu izdvojene regije u $mm^{2}$.

## Dodatne mogućnosti

- Na sličan način (sa istih slika) moguće je izdvojiti glavne krvne sudove koji prozimaju pluća i izračunati procenat koji oni zauzimaju u plućima.

## Literatura

- [Skup podataka sa slikama](https://drive.google.com/uc?id=1qNpH_0BEy-JJE5VMNfb8kuNN2KfsFLsi)

## Rezultat

Prikazati sliku izdvojene regije i izračunatu površinu pluća za svaku
datu sliku.
