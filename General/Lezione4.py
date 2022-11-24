#LEZIONE4: PROGRAMMAZIONE AD OGGETTI

#Oggetti: definiti con le classi. Funzioni negli oggetti: metodi. Variabili negli oggetti: attributi. 
#Dopo esser stati inizializzati diventano ISTANZE.

#Si usano per rappresentare delle gerarchie e permettono di mantenere facilmente lo stato(senza avere una struttura dati di appoggio)

#Convenzione di stile: 
#Caratteri minuscoli e underscore = VARIABILI e ISTANZE
#CamelCase = nome delle CLASSI

#doppi underscore = indicano il nome di un metodo ad uso esclusivamente interno. 
#Apici = valgono sia singoli sia doppi

#Definire oggetti
class Person():
    pass #pass non fa niente

person = Person() 
print(person)

class Person():
    def __init__(self,name,surname): 
        #Set name and surname
        self.name    = name
        self.surname = surname
        
person = Person('Mario','Rossi')
print(person) #istanza di oggetto
print(person.name) #attributo
print(person.surname) #attributo

oppure

def __str__(self): #funzione ad uso interno che vado a sovrascrivere
    return 'Person "{} {}"'.format(self.name, self.surname)

person = Person('Mario','Rossi')
print(person)

#inizializzatore prende name e surname e li salva in self
#qualsiasi funzione definita dentro a un oggetto per poter operare nell'oggetto ha bisogno della parola chiave self

#estendere gli oggetti: 
