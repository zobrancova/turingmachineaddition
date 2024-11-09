# Semestrálny projekt na predmet XTILO
Postup akým bol projekt zhotovený:
Z predošlej fakulty som bola oboznámená simulátorom TS, turingmachine.io. V tomto programe som si graficky vedela pekne vyhodnocovať stavy a rozmýšĺať nad riešením. 
Pre tento simulátor sa využíva kód yaml, ktorý som potom jednoducho pretvorila do programovacieho jazyka Python, v ktorom je výsledný program urobený.

## LOGIKA programu

### Stav zaciatok
Ak prečítam 1 alebo 0, choď doľava a označ si začiatok slova z. Potom choď doprava a do stavu najdikoniec.
### Stav najdikoniec
Ak prečítaš 1,0 tak choď doprava ak prečítaš symbol # tak choď do stavu mriežka koniec.
### Stav mriezkakoniec
Ak sa za tebou nachádza číslo choď do stavu nájdikoniec a choď doprava(teda nachadza sa za mriezkou cislo). V prípade, že je za mriežkou ďaľšia mriežka, je to koniec slova označ si koniec slova k a chod do stavu idem na začiatok.
### Stav idemnazaciatok
Ak prejdes symbolom 1,0 a # tak chod dolava ak najdes symbol z ides do stavu doprava a pojdes doprava.
### Stav doprava
Ak precitas symbol 1 a 0 chod doprava, ak # tak prepis na + a chod do stavu mriezka a doprava. Ak medzeru pokracuj doprava.
### Stav mriezka
Ak je 1,0 tak chod doprava, ak najdes mriezku tak chod na citaj, ak k chod do koncoveho stavu done.
### Stav citaj
Ak je tam 1 napis symbol c(oznacujem si tak cislo ktore aktualne spocitavam}, chod do stavu mam1 a dolava. Ak 0 je oznac c, chod do stavu mam0 a dolava. Ak v citaj najdem + tak idem prepisat do co je nalavo
### Stav mam1
Precitaj symboly 1,0 ak prides k + tak chod stavu pripocitaj1 a dolava.
### Stav mam0
Precitaj symboly 1,0 ak prides k + tak chod stavu pripocitaj0 a dolava.
### Stav pripocitaj1
Ak je tam 0 alebo # tak napis I v (0+1=1) a posunie do stavu vymaz 1 doprava. 
Ak je tam 1 tak zapis 0 a chod na prenasam dolava. Ak su tam symboly I A O tak len ich precita. 
### Stav pripocitaj0
Ak je tam 0 (0+0)=0, tak zapis O a chod na vymaz0, doprava. ak(0+1=1) 1 tak zapis I a chod na vymaz0 doprava. 
### Stav vymaz1
Ak su tam symboly 0,1,O,I tak chod doprava, ak precitas c tak prepis na medzeru a chod dolava a do stavu citaj.
### Stav vymaz0
Ak su tam symboly 0,1,O,I tak chod doprava, ak precitas c tak prepis na medzeru a chod dolava a do stavu citaj. 
### Stav prenasam
Ak je symbol 0 alebo z(v pripade ak prenasam cez zaciatok slova) tak napis 1 a chod na vymaz 1
### Stav prepis
I sa prepise na 1, O na 0, pri symbole z idem do stavu doprava a opakujem cely cyklus dokym nenajdem v stave mriezka k. 
### Stav done
Po prečítaní symbolu k zo stavu mriezka sa program ukonci. Tak som si označila koniec slova.

## Program
Class TuringMachine, je tam definovana paska(z inputu),co je blank, kde sa nastavi hlava(nasledne ide do funkcie find_first_number, kde vo funkcii pozrie kde sa nachadza to nase slovo), no a zaciatocny state ktory je zaciatok. 
def changestate: tu sa printuju vsetky kroky pasky a su tu definovane vsetky stavy. Funkcia write napise tam kde sa nachadza hlava dany symbol. Funkcia move je definovana na prechadzanie paskou doprava a dolava. Funkcia run prebhene cely program, 

Zdroje: 
turingmachine.io
https://www.geeksforgeeks.org/turing-machine-addition/
https://www.tutorialspoint.com//construct-turing-machine-for-addition

