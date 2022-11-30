class CSVfile:
    def __init__ (self, name):
            self.name = name

    try:
        my_file=open('self.name','r')
        my_file.readline()
    except Exception as e:
        print ("Errore: Il file non esiste".format(e))

    def get_data(self):
        
        my_list = []
        if self.my_file == []: 
            return None 
        for line in self.my_file:
            elements = line.split (",")
            if elements [0] != "Date":
                my_list.append (elements)
        self.my_file.close ()
    
        print(my_list)


mio_file = CSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: #"{}"'.format(mio_file.get_data()))