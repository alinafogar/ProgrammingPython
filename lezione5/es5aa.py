class CSVFile:
    def __init__ (self,name):
        self.name=name
        try:
            my_file=open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            print("Errore: Il file non esiste".format(e))

    def get_data(self):
        
        my_list = []
        my_file = open(self.name, 'r')
        
        if my_file == []: 
            return None 
        for line in my_file:
            elements = line.split (",")
            elements[-1] = elements[-1].strip()
            if elements [0] != "Date":
                my_list.append (elements)
        my_file.close()
    
        print(my_list)


my_file = CSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(my_file.name))
print('Dati contenuti nel file: #"{}"'.format(my_file.get_data()))