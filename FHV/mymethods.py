#%%
import numpy as np
def removeNa(list): #entfernt leere Elemente aus der Liste
    newList = []
    for element in list:
        if element != '':
            newList.append(element)
    return newList

def summemitfehler(data, error, coeff = None):#Berechnung der Summe mit Unsicherheit
    anzahl = np.size(data)
    if coeff == None:
        coeff = []
        for i in range(0, anzahl):
            coeff.append(1)
    if not(anzahl == np.size(error) and anzahl == np.size(coeff)):
        return "errorsum","errorsum"
    summe = 0
    fehler = 0
    for i in range(0, anzahl):
        summe = summe + coeff[i] * data[i]
        fehler = fehler + (coeff[i] * error[i])**2
    fehler = np.sqrt(fehler)
    return summe, fehler

def produktmitfehler(data, error, power = None):#Berechnung des Produktes mit Unsicherheit
    anzahl = np.size(data)
    if (power == None):
        power = []
        for i in range(0, anzahl):
            power.append(1)
    if not(anzahl == np.size(error) and anzahl == np.size(power)):
        return "errorprod","errorprod"
    produkt = 1
    fehler = 0
    for i in range(0, anzahl):
        produkt = produkt * np.float_power(data[i],power[i])
        fehler = fehler + (power[i]*error[i]/data[i])**2
    fehler = produkt * np.sqrt(fehler)
    return produkt, fehler

def gewichteterMittelwert(data, error):#Berechnung des gewichteten Mittelwerts mit Unsicherheit
    if np.size(data) != np.size(error):
        return "errorgewMtw","errorgewMtw"
    wichtung = []
    for errori in error:
        wichtung.append(1/(errori**2))
    dataresult = sum([x * y for x,y in zip(wichtung,data)])/sum(wichtung)
    errorint = np.sqrt(1/sum(wichtung))
    errorext = np.sqrt(sum([x * ((y - dataresult) ** 2) for x,y in zip(wichtung,data)])/(sum(wichtung) * (np.size(wichtung)-1)))
    errorresult = np.max([errorint,errorext])
    return dataresult, errorresult

def sqrtsumsq(list):
    sum = 0
    for element in list:
        sum = sum + element**2
    return np.sqrt(sum)

def kehrsumkehr(list):
    sum = 0
    for element in list:
        sum = sum + 1 / element
    return 1 / sum

def typA(list):
    return np.mean(list), np.std(list, ddof=1)/np.sqrt(np.size(list))