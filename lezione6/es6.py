# Modificate l’oggetto CSVFile della lezione precedente in modo che alzi un'eccezione se il nome del file non è una stringa (nell’ __init__() ). Poi, modificate la funzione get_data() di CSVFile in modo da leggere solo un’ intervallo di righe del file*, aggiungendo gli argomenti start ed end opzionali, controllandone la correttezza e sanitizzandoli se serve.

class CSVFile:
    
    def __init__(self, name):
        self.name = name
        self.can_read = True
            
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))

        if not isinstance(CSVFile.name, str):
            raise Exception('Ho avuto un errore, ecco il parametro che lo ha generato: "{}"'.format(CSVFile.name))
            
    def get_data(self, start=None, end=None):
        
        if not self.can_read:
            print('Errore, file non aperto o illeggibile')
            return None

        else:
            data = []
            my_file = open(self.name, 'r')

            for line in my_file:
                
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
                if elements[0] != 'Date':
                    data.append(elements)
            my_file.close()
            return data

my_file=CSVFile('shampoo_sales.csv')
print (my_file.name)
print (my_file.get_data())