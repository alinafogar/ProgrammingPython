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
            
    def get_data(self):
        
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