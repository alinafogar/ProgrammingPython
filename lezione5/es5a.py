class CSVfile('file_name'):
    def __init__ (self, name):
            self.name = name

    try:
        my_file=open('shampoo_sales.csv','r')
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
    
        return my_list 


my_file=CSVfile('shampo_sales.csv')
print (my_file.name)
print (my_file.get_data())