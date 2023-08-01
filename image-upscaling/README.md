# Povećanje rezolucije

- Polaznik: Miloš Krneta
- Saradnici: Nikola Ristanović

## Uvod

Rezolucija slike se odnosi na broj piksela po inču koji čine sliku
(DPI), a njeno povećanje ima za cilj da učini da slika bude oštrija i
definisanija. Nemoguće je stvoriti dodatnu informaciju koje nema (setite
se samo onih magičnih uvećavanja slike u CSI serijama). Kako bi se rešio
ovaj problem koristi se interpolacija na slikama. Interpolacija
predstavlja “dodavanje” novog piksela pored već postojećih u samu sliku.
Ovo se može uraditi na više različitih načina:

- Interpolacija najbližim pikselom
- Bilinearna interpolacija
- Bikubna interpolacija
- Interpolacije višeg reda

## Postupak razvoja

Preporučeno je prvo probati uvećati sliku korišćenjem [scikit-image biblioteke](https://scikit-image.org/docs/stable/auto_examples/transform/plot_rescale.html).
Nakon toga je potrebno implementirati jednu po jednu interpolaciju i
videti kakav rezultat daju za zadate ulazne slike. Nakon što se odradi
metoda najbližeg suseda, bilinearna i bikubna interpolacija, zadatak se
potencijalno može dalje komplikovati.

## Dodatne mogućnosti

- Moguće je implementirati sofisticiranije metode uvećavanja slike.
- Istražiti metrike koje mogu da kvantifikuju kvalitet interpolacije, te svaku implementiranu metodu evaluirati odabranom metrikom/metrikama.

## Literatura

- [Image scaling - Wikipedia](https://en.wikipedia.org/wiki/Image_scaling)
- [Understanding Digital Image Interpolation (cambridgeincolour.com)](https://www.cambridgeincolour.com/tutorials/image-interpolation.htm)

## Rezultat

Očekivani rezultat su dve implementirane funkcije za uvećavanje slika u
Python-u, koje koriste makar interpolaciju najbližeg suseda i bilinearnu
interpolaciju. Nakon toga je potrebno uporediti kvalitet novih slika.
Kao što je već navedeno moguće je implementirati dodatne druge
mogućnosti za interpolaciju/uvećavanje slika.
