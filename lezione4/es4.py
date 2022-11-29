#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#venga inizializzato sul nome del file csv, 
#abbia un attributo “name” che ne contenga il nome 
#abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste, ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]

class CSVfile (): #classe, cosa astratta 
    def _init_ (self, name):
            self.name = name #nome

    def get_data (self):
        
        values = []
        my_file = open ("shampo_sales.csv" , "r")
        if my_file == []: 
            return None 
        for line in my_file:
            elements = line.split (",")
            if elements [0] != "Date":
                date = elements [0]
                value = elements [1]
                values.append (float (value))