class ExamException(Exception):

    pass

class CSVTimeSeriesFile:

    def __init__(self, name):

        self.name = name

    def get_data(self):

        #creo la lista che sarà il mio output
        time_series = []

        #provo ad aprire il file
        try:
            my_file = open(self.name, 'r')

        except:
            raise ExamException('Error opening or reading the file')

        #provo a leggere una riga del file
        if (my_file.readline() == ''):
            raise ExamException('Void file')

        for line in my_file:

            #divido la riga in due parti, nella prima la data e nella seconda il numero di passeggeri
            elements = line.strip('\n').split(',')

            if elements[0] != 'date':
                #provo a dividere la data in due parti, se non riesco salto la riga
                try:
                    #divido la data in anni e mesi
                    split_date = elements[0].split('-')
                    #converto gli anni e i mesi ad int
                    split_date[0] = int(split_date[0])
                    split_date[1] = int(split_date[1])
                except:
                    continue
                #salto la riga se la data non è un intero
                if not isinstance(split_date[0], int):
                    continue
                #salto la riga se il mese non è un intero o non è compreso tra 1 e 12
                if not isinstance(split_date[1], int) or split_date[1] not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
                    continue
                #controllo se ci sono duplicati della data
                if len(time_series) > 0 and elements[0] == time_series[-1][0]:
                    raise ExamException('There are two duplicate dates')
                #controllo se le date sono tutte in ordine

                if len(time_series) > 0 and split_date[0] < int(time_series[-1][0].split('-')[0]):
                    raise ExamException('The years are not in order')
                #controllo se i mesi sono in ordine, l'anno deve essere lo stesso
                if len(time_series) > 0 and split_date[1] < int(time_series[-1][0].split('-')[1]) and split_date[0] == int(time_series[-1][0].split('-')[0]):
                    raise ExamException('The months are not in order')

                #CONTROLLO VALORI
                #converto a int, se non va salto la riga
                try:
                    elements[1] = int(elements[1])
                except:
                    continue
                #se il numero di passeggeri è <0, salto la riga, se è uguale a 0 bo
                if (elements[1] < 0):
                    continue

                #se ha passato tutti i test, posso aggiungerlo alla lista
                time_series.append(elements)

        return time_series


def detect_similar_monthly_variations(time_series,years):
    first_year, second_year, variation_1, variation_2,list = [], [], [], [],[]
    # Initialize empty lists for monthly values
    first_year = [None] * 12
    second_year = [None] * 12
    
    # Loop through time series and populate lists with monthly values
    for item in time_series:
        year, month = item[0].split('-')
        value = item[1]
        
        if year == years[0]:
            first_year[int(month)-1] = value
        elif year == years[1]:
            second_year[int(month)-1] = value

    

#SECONDA PARTE
    print(first_year)
    for i in range(11):
        try:
            variation_1.append(first_year[i+1]-first_year[i])
        except:
            variation_1.append(None)

    for i in range(11):
        try:
            variation_2.append(second_year[i+1]-second_year[i])
        except:
            variation_2.append(None)

#TERZA PARTE

    for i in range(11):
        try:
            if abs(variation_1[i] - variation_2[i])<=2:
                list.append('True')
            else:
                list.append('False')

        except:
            list.append('False')

    #print(variation_1)
    #print(variation_2)
    return list
        
#TEST
time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

#for item in time_series:
    #for it in item:
       # print(it)
   # print('')
    
lista=detect_similar_monthly_variations(time_series,['1949','1950'])
print(lista)