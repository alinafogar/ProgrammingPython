class ExamException(Exception):

    pass

class CSVTimeSeriesFile:

    def __init__(self, name):

        self.name = name

    def get_data(self):

        time_series = []

        try:
            my_file = open(self.name, 'r')

        except:
            raise ExamException('Error opening or reading the file')

        #Provo a leggere una riga del file, se non riesco alzo una eccezione
        if (my_file.readline() == ''):
            raise ExamException('Void file')

        for line in my_file:

            #Divido la riga in 2 parti, la data e il valore
            elements = line.strip('\n').split(',')
            #Se la prima parte è diversa da date, procedo
            if elements[0] != 'date':
                #Provo a dividere la data in anni e mesi e a convertirla ad int, se non riesco salto la riga
                try:
                    split_date = elements[0].split('-')
                    split_date[0] = int(split_date[0])
                    split_date[1] = int(split_date[1])
                except:
                    continue
                #salto la riga se l'anno non è un intero
                if not isinstance(split_date[0], int):
                    continue
                #salto la riga se il mese non è un intero o non è compreso tra 1 e 12
                if not isinstance(split_date[1], int) or split_date[1] not in range(1,13):
                    continue
                #Se ci sono date duplicate, alzo un eccezione
                if len(time_series) > 0 and elements[0] == time_series[-1][0]:
                    raise ExamException('There are two duplicate dates')
                #Se ci sono anni non in ordine, alzo un eccezione
                if len(time_series) > 0 and split_date[0] < int(time_series[-1][0].split('-')[0]):
                    raise ExamException('The years are not in order')
                #Se ci sono mesi non in ordine nello stesso anno, alzo un eccezione
                if len(time_series) > 0 and split_date[1] < int(time_series[-1][0].split('-')[1]) and split_date[0] == int(time_series[-1][0].split('-')[0]):
                    raise ExamException('The months are not in order')

                #Converto ad intero i valori dei passeggeri, se non riesco salto la riga
                try:
                    elements[1] = int(elements[1])
                except:
                    continue
                #Se il numero di passeggeri è <=0, salto la riga
                if (elements[1] <= 0):
                    continue
                #Se il valore ha passato tutti i test, posso aggiungerlo alla lista
                time_series.append(elements)

        my_file.close()
        return time_series


def detect_similar_monthly_variations(time_series,years):
    #Controllo se gli anni richiesti sono una lista di 2 elementi interi e consecutivi
    if not isinstance(years, list) or len(years)!=2:
        raise ExamException('Error with the years')

    if not isinstance(years[0], int) or not isinstance(years[1], int):
        raise ExamException('Years are not integers')

    if years[0]!=(years[1]-1) and years[0]-1 != years[1]:
        raise ExamException('Years are not consecutive')

    #Definisco le liste dei valori come None, così se un valore mensile non è presente nel csv, quella casella rimane uguale a None
    first_year=[None]*12
    second_year=[None]*12
    variation_1,variation_2,lista=[],[],[]
    #Implemento due flag per verificare che gli anni sono nel file
    flag_1,flag_2=0,0
            
    for item in time_series:
        #Converto la data in stringa e la divido in mese e anno
        item[0]=str(item[0])
        item[0]=item[0].split('-')
        #Cerco l'anno richiesto
        if(int(item[0][0])==years[0]):
            #Se l'anno corrisponde inserisco i valori nella lista utilizzando i mesi come indici
            first_year[int(item[0][1])-1]=item[1]
            #Se ho trovato l'anno, aumento la flag
            flag_1+=1
            
        elif(int(item[0][0])==years[1]):
            second_year[int(item[0][1])-1]=item[1]
            flag_2+=1

    if flag_1 == 0 or flag_2 == 0:
        raise ExamException('The years are not in the csv file')

    #Calcolo le variazioni mensili per ogni anno richiesto
    for i in range(11):
        #Provo a calcolare la variazione, se non riesco, aggiungo None
        try:
            variation_1.append(first_year[i+1]-first_year[i])
        except:
            variation_1.append(None)

    for i in range(11):
        try:
            variation_2.append(second_year[i+1]-second_year[i])
        except:
            variation_2.append(None)

    #Controllo che sono simili con una tolleranza di 2
    for i in range(11):
        try:
            #Se il valore assoluto della differenza è minore o uguale a 2, aggiungo True
            if abs(variation_1[i] - variation_2[i])<=2:
                lista.append(True)
            else:
                lista.append(False)
        #Se non riesco a calcolare la differenza, aggiungo false
        except:
            lista.append(False)
            
    return lista
        
time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
lista=detect_similar_monthly_variations(time_series,[1959,1960])
print(lista)