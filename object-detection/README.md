# Detekcija objekta

- Polaznik: Filip Repman
- Saradnici: Milomir Stefanović

## Uvod

Detekcija objekata u digitalnoj obradi slike se bavi detekcijom zadatog
objekta u slici korišćenjem različitih metoda. Iako se danas dosta
koriste neuronske mreže za detekciju, ipak postoji i par metoda koji ne
uključuju mašinsko učenje kao što su Viola-Jones, Scale Invariant
Feature Transform, Histogram of Oriented Gradients. Potrebno je odraditi
detekciju hrama sa orginalne slike na ostalim slikama.

## Postupak razvoja

1. Potrebno je koristiti Feature Descriptor koji je već implementiran u nekoj od biblioteka (OpenCV ili SciKit) i dobiti karakteristične tačke sa slike.
2. Obradom karakterističnih tačaka potrebno je izvući najbolje karakteristične tačke, tako da se sklone one koje imaju veću verovatnoću detekcije na drugim slikama.
3. Potrebno je naći objekat na drugim slikama koristeći već implementirani uparivač obeležja. Obratiti pažnju kako su grupisani dobro spojeni parovi.

## Dodatne mogućnosti

- Upoređivanje različitih uparivača obeležja.
- Moguća je implementacija samog SIFT-a ako baš ima vremena.

## Literatura

- [Object detection - Wikipedia](https://en.wikipedia.org/wiki/Object_detection)
- [Scale-invariant feature transform - Wikipedia](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform)
- [Introduction to SIFT( Scale Invariant Feature Transform) \| by Deepanshu Tyagi \| Data Breach \| Medium](https://medium.com/data-breach/introduction-to-sift-scale-invariant-feature-transform-65d7f3a72d40)
- [SIFT Detector \| SIFT Detector - YouTube](https://www.youtube.com/watch?v=ram-jbLJjFg)

## Rezultat

Za date ulazne slike potrebno je detektovati hram na slikama
`hram[1-5]` gde je orginalna slika nazvana kao `hram_template`.
Potrebno je prikazati konturu detektovanog hrama na slikama.
