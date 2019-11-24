import sys 
import os
import androidhelper as ah
import time
from datetime import datetime
import math
import pandas as pd

droid=ah.Android()

n = 0
m = 1000
X = []
Y = []
Z = []
c_tita = []
c_phi = []


ti = datetime.now()
droid.startSensingTimed(2, 250)


for i in range(n, m+1):

    acelerometro = droid.sensorsReadAccelerometer()
    
    if (type(acelerometro[1][1]) and type(acelerometro[1][2]) and type(acelerometro[1][0]) == float or type(acelerometro[1][1]) and type(acelerometro[1][2]) and type(acelerometro[1][0]) == int) and abs(acelerometro[1][1]) < (9.81):
        
        tita = math.acos( float(acelerometro[1][1])/(9.81))
        phi = math.atan( float(acelerometro[1][0])/ float(acelerometro[1][2]))

        
    else:

        tita = 0
        phi = 0


    print("\n\n", """

    Eje x: {}[m/s^2]\n
    Eje y: {}[m/s^2]\n
    Eje z: {}[m/s^2]\n
    \nReferencia G = 9,81[m/s^2]"
    \n\nAngulo tita: {}
    \nAngulo Phi: {}

    """.format((acelerometro[1][0]), (acelerometro[1][1]), (acelerometro[1][2]), tita, phi))
    sys.stdout.flush()
   
   

    os.system('clear')
    
    c_phi.append(phi)
    c_tita.append(tita)

    (X).append(acelerometro[1][0])
    (Y).append(acelerometro[1][1])
    (Z).append(acelerometro[1][2])


    #time.sleep(.01)


tf = datetime.now()

tiempo = ti - tf 
segundos = tiempo.seconds
sss = []
sss.append(segundos)

droid.stopSensing()

datax = pd.DataFrame(X)
datay = pd.DataFrame(Y)
dataz = pd.DataFrame(Z)
datatita = pd.DataFrame(c_tita)
dataphi = pd.DataFrame(c_phi)
datasegundos = pd.DataFrame(sss)

df =  pd.concat([datax, datay, dataz, datatita, dataphi, datasegundos], axis = 1)

df.to_csv(r'\storage\emulated\0\qpython\data.csv', index = None, header=True)
print("Datos guardados en\n\storage\emulated\0\qpython")
print("Tiempo de ejecucion:", segundos)





# La inclinacion vertical con respecto al eje Z
# angulo formado por el eje "Y" y el vector G

# tita

# Si existe el angulo phi
# entonces hay una inclinacion 

# phi

# En particular, la existencia de cualquier
# angulo con respecto al vector g
# me dtermina la inperfeccion en la cual el vector
# g esta proyectado.



