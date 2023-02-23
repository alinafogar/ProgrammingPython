class ExamException(Exception):

    pass

class MovingAverage():

    def __init__(self,length):
        self.length=length

    def compute(self,data):
        for item in data:
            if not isinstance(item, (int,float)):
                raise ExamException('Errore, non tutti i valori sono numeri')
            elif()

        if not isinstance(self.length, int):
            raise ExamException('La lunghezza non è un numero intero')

        if(self.length <= 0):
            raise ExamException('La lunghezza è un numero negativo o uguale a zero')

        

        l=len(data)
        i=0
        c=0
        values=[]
        for item in data:
            while((l-i)>=self.length):
                c=i
                co=0
                somma=0
                while(co<self.length):
                    somma+=data[c]
                    c+=1
                    co+=1
                avg=somma/self.length
                i+=1
                values.append(avg)
        return values

valori=[3,5,7,9]
media=MovingAverage(2)
#print("Valori:{}".format(media.compute(valori)))
media= media.compute(valori)

for item in media:
    print(item)


                

        

        
            
        