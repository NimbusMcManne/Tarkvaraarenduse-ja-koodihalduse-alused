Bashi eksperiment oli mõeldud õppematerjalides seletatu praktiseerimiseks. Ülesanne hõlmas üpris väikest osa kõikidest bash käskudest kuid andis siiski hea ülevaate mida käsureal on võimalik teha.

Ülesannete järjekorra põhjal pidi:

Looma uue kataloogi käsuga ```mkdir bash_eksperiment```

Looma selle *readme.md* faili käuga ```touch readme.md```


Looma skripti nimega *generate_data.py* mis genereerib 200 juhuslikku täisarvu vahemikus 1-100. Seda tegin käsuga ```nano generate_data.py``` ning muutsin faili sisu editoriga.

Looma skripti *generate_data.sh* mis käivitab *generate_data.py* ning salvestab tulemused data/ kataloogi vastavasse faili.

Leidma üle kõigi data/ kataloogi failide millised arvud korduvad ja kui mitu korda ja salvestama saadud väljund ette antud faili. Seda tegin käsuga cat ```../data/*.txt | sort | uniq -c > ../results/summary_total_unique_numbers_counted.txt```
