#I dati: interagire con i file ed il formato CSV(Comma-separated values)

#Ogni riga è una entry, può esserci una intestazione di una o più righe. Possono essere .csv o .txt

#Interagire con i file: funzione open --> funzione built in 
my_file = open('shampoo_sales.csv', 'r') 
print(my_file.read())
my_file.close()
# Modalità di apertura del file, in questo caso “r” sta per “read” (sola lettura). Se vorrò anche scriverci, userò “rw”

#Usare lo slicing delle stringhe per stampare solo una parte del file
my_file = open('shampoo_sales.txt', 'r')
print(my_file.read()[0:50])
my_file.close()
#potrebbero andare male molte cose

# Apro il file
my_file = open('shampoo_sales.csv', 'r')
# Leggo il contenuto
my_file_contents = my_file.read()
# Stampo a schermo i primi 50 caratteri
if len(my_file_contents) > 50:
    print(my_file_contents[0:50] + '...')
else:
    print(my_file_contents)
# Chiudo il file
my_file.close()

#len è una funzione built in che mi ritorna la lunghezza dei contenuti dei file. 

#leggere riga per riga
my_file = open('shampoo_sales.csv', 'r')
print(my_file.readline())
print(my_file.readline())
my_file.close()

#leggere riga per riga tutto in una volta in modo pythonico
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:
    print(line) my_file.close()

#per leggere i dati:

# 1) Il metodo “.split” per separare le stringhe su uno specifico carattere;
mia_stringa = 'Ciao, come va?' lista_elementi = mia_stringa.split(',')

# 2) La conversione di una stringa a valore numerico (floating point);
mia_stringa = '5.5'
mio_numero = float(mia_stringa)

# 3) Sapere come aggiungere un elemento ad una lista
mia_lista = [1,2,3] mia_lista.append(4)


 