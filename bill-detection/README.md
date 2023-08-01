# Prepoznavanje novčanica

- Polaznik: Iva Stojanović
- Saradnici: Marija Nedeljković

## Uvod

Ideja projekta je da se vrši automatsko prepoznavanje novčanica. Pored
ovakve primene, algoritam se može koristiti i za detekciju ostalih
četvrtastih predmeta različitih boja. To može biti korisno u pomaganju
ljudima sa slabijim vidom. Novčanice su rapoređene na stolu i
proizvoljno su orjentisane. Potrebno je prebrojati novčanice, pa zatim
odrediti njihovu vrednost na osnovu boje.

## Postupak razvoja

1. **Zamućivanje slike:** slike zamućujemo kako bi se fokusirali na boju novčanica, ispitati kako različitii tipovi blurova pomažu u daljoj obradi 
2.  **Smanjenje opsega boja:** Smanjiti opseg boja kako bi lakše prepoznali element. Pravimo paletu boja za koje znamo da se mogu pojaviti na novčanicama i svaku od boja na slici dodelimo jednoj od izdvojenih grupa (npr roze, zelena, zuta, ostalo).
3.  **Prebrojavanje novčanica:** Koliko ukupno novčanica je prisutno na slici (nezavisno od boje)
4.  **Detektovanje vrednosti novčanica:** Na osnovu boje novčanice odrediti njenu vrednost i na kraju ispisati zbir vrednosti svih novčanica na slici

## Dodatne mogućnosti

- Naći za koje parametre filtra se najtačnije nalaze elementi sa slike
- Varirati sve parametre i ispitati dobijene performanse/tačnost prebrojavanja
- Naći način da osvetljenje što manje utiče na tačnost nalaženja

## Literatura

- [Open CV dokumentacija](https://pypi.org/project/opencv-python/)
- [Median blur](https://en.wikipedia.org/wiki/Median_filter)
- [Gaussian blur](https://en.wikipedia.org/wiki/Gaussian_blur)

## Rezultat

Po završetku projekta bi trebalo da postoji program koji može da uoči
različite vrste novčanica i da nađe zbir njihovih vrednosti.
