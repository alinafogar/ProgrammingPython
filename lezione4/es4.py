#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#venga inizializzato sul nome del file csv, 
#abbia un attributo “name” che ne contenga il nome 
#abbia un metodo “get_data()” che torni i dati dal file CSV come lista di liste, ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]

class CSVFile():
    def __init__(self, name):
            self.name = name

    def get_data(self):
        
        values = []
        my_file = open(self.name, 'r')
        if my_file == []: 
            return None 
            
        for line in my_file:    
            elements = line.split(',')
            elements[-1] = elements[-1].strip() #tolgo \n
            if elements[0] != 'Date':
                values.append(elements)
        my_file.close()
        return values

#10