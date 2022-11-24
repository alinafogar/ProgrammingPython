#LEZIONE 2: INTRO SU PYTHON: TIPI DATI, COSTRUTTI, FUNZIONI, MODULI


# print usata per includere i valori delle variabili che vogliamo stampare a schermo
print('Valore 1: {}, valore 2: {}'.format(my_var_1, my_var_2))

# tipi dati: non vanno esplicitamente dichiarati e definiti

my_var = 1 # Esempio di variabile tipo intero
my_var = 1.1 # Esempio di variabile tipo floating point
my_var = 'ciao' # Esempio di variabile tipo stringa
my_var = True # Esempio di variabile tipo booleano
my_var = None # Il “niente” si rappresenta con il “None”

#slicing delle stringhe

mia_stringa[30:50]  # Dal trentesimo al cinquantesimo carattere
mia_stringa[0:-1]   # Dal primo al penultimo carattere

 #operatori
** potenza
and = &&
or = ||
not = converte il risultato, ritorna falso se il risultato è vero not(x<5 and x<10)

#liste

my_list = [1,2,3] # Lista di numeri
my_list = ['Marco', 'irene', 'paolo'] # Lista di stringhe

#operatori di appartenenza nelle liste

in = ritorna vero se quello specifico valore è presente nella lista
not in = ritorna vero se quello specifico valore NON è presente nella lista
esempio: if 'Marco' in my_list...

#dizionari

my_dict = {'Trieste': 34100, 'Padova': 35100}  # Dizionario di numeri
my_dict = {'Trieste': 'TS', 'Padova': 'PD'}    # Dizionario di stringhe

print('CAP di Trieste: {}'.format(my_dict['Trieste']) #per accedere al dizionario

#i dizionari non sono ordinati

#indentazione
      
if (my_var > your_var):
    print("My var is bigger than yours")
    if (my_var-your_var) <= 1:
        print("...but not so much")

if (my_var > your_var):
    print("My var is bigger than yours")
    if (my_var-your_var) <= 1:
        print("...but not so much")
    elif (my_var-your_var) <= 5:
        print("...quite a bit")
    else:
        print("...a lot")


#cicli

for item in mylist: #ciclo for
    print(item)

i=0
while i<10:
    print(i)
    i = i+1

for i in range(10): 
    print(i)

for i, item in enumerate(mylist): #cicla sia gli elementi della lista e il contatore i
    print("Posizione {}: {}".format(i, item))


#funzioni
 
def mia_funzione(argomento1, argomento2):
    print("Argomenti: {} e {}".format(argomento1, argomento2)) #definizione

mia_funzione("Pippo","Pluto") #chiamata della funzione

 
def eleva_al_quadrato(numero):
    return numero*numero

eleva_al_quadrato(4)

risultato = eleva_al_quadrato(4): print('Risultato: {}'.format(risultato))

#lo scope

quando scrivo una funzione posso accedere alle variabili fuori, ma non viceversa, ma è meglio di no

#moduli: va esplicitato il modulo che contiene una funzionalità

>>> import math
>>> math.sqrt(600)
24.49489742783178

>>> from math import sqrt
>>> sqrt(600)
24.49489742783178


