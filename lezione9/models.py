"""Estendete il modello della lezione precedente IncrementModel come
FitIncrementModel, andando ad implementare il metodo fit().
Il fit deve, come appena descritto, calcolare l’incremento medio su tutto il
dataset e salvarlo da qualche parte (es: self.global_avg_increment).
Poi sovrascrivete il metodo predict() in modo che usi l’incremento
medio su tutto il dataset come descritto nelle slides precedenti.
Usate l’esempio numerico delle slides prima di provare con i dati delle vendite di shampoo!!"""

class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):

    def predict(self, data):
        prev_value = None

        somma_inc=0
        i=0
        for item in data:
            if i>0:
                somma_inc += data[i]-data[i-1]
            i+=1

        if i <= 1:
            return None

        som_med = somma_inc/(i-1)
        prediction = data[-1]+som_med
        return prediction
        
        
class FitIncrementModel(IncrementModel):

    def fit(self,data):
        c=0
        inc=0
        for item in data:
            if c>0:
                inc+= data[c]-data[c-1]
            c+=1

        if c<=1:
            return None

        self.global_avg_increment=inc/c-1

    def predict(self,data):
        
        
            
            
        

