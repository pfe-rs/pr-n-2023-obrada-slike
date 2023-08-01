# Izdvajanje teksta

- Polaznik: Ljubica Milijanović
- Saradnici: Nikola Ristanović

## Uvod

Slike često podležu defektima koji nastaju zbog nekontrolisanih faktora
tokom njihove akvizicije. Ako se fokusiramo na osvetljenje slike,
postoje razni faktori koji mogu da utiču na smanjenje kvaliteta slike.
Ti faktori mogu biti nepogodno postavljeno unutrašnje osvetljenje,
nedovoljno osvetljenje usled oblačnosti ili ipak preeksponiranost
prilikom jakog osvetljenja. Zbog ovih nepovoljnih uslova, refleksija
slikane površine može biti smanjena ili neujednačena u svim delovima i
zbog toga nastaju razne smetnje koje dovode do lošeg kvaliteta slike.

Cilj ovog zadatka jeste poboljšanje kvaliteta slike teksta koji je
slikan pri prethodno opisanim nepovoljnim uslovima.

## Postupak razvoja

Učitati i prikazati inicijalnu sliku, a zatim utvrditi srednju
osvetljenost svih piksela na slici. Koristeći
*closure-by-reconstruction* proceniti nivo pozadinskog osvetljenja u
svim delovima slike. Iskoristiti poznavanje pozadinskog osvetljenja i
srednje osvetljenosti svih piksela kako bi se dobila konačna, čitljiva
slika teksta.

## Dodatne mogućnosti

- Pronaći dodatne primere i osposobiti algoritam da maksimalno poboljša kvalitet slike teksta za što veći broj različitih primera.

## Literatura

- Guocheng Wang et al., Morphological Background Detection and Illumination Normalization of Text Image with Poor Lighting (*DOI: 10.1371/journal.pone.0110991*)

## Rezultat

Krajnji rezultat ovog zadatka treba da bude prikaz rezultujuće slike pri
svakom primenjenom koraku kao i poređenje krajnje i početne slike
teksta.
