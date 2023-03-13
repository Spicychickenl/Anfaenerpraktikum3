#%%
import pandas as pds
import numpy as np
def removeNa(list): #entfernt leere Elemente aus der Liste
    newList = []
    for element in list:
        if element != '':
            newList.append(element)
    return newList
#%%
file = pds.read_excel(r'/home/lize/Physics/Anfängerpraktikum3/OPA.xlsx')
file = file.fillna("")
A2_BK = np.array(removeNa(file['2bk']))-10.0
A2_BL = np.array(removeNa(file['2bl']))-10.0
A2_GK = np.array(removeNa(file['2gk']))-10.0
A2_GL = np.array(removeNa(file['2gl']))-10.0
A3_bl = np.array(removeNa(file['3bl']))
A3_br = np.array(removeNa(file['3br']))
A3_gl = np.array(removeNa(file['3gl']))
A3_gr = np.array(removeNa(file['3gr']))

