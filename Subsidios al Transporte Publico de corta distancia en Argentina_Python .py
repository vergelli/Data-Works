
# coding: utf-8

# # Representacion de datos de Subsidios al transporte en Argentina

# In[1]:



# Crucial
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import FuncFormatter
plt.style.use("bmh")
import re as rglr


# In[2]:


data = open("aportes_colectivoscd.csv", encoding="utf8")


# In[3]:


data = list(data)


# In[4]:


columnas = list(data[0].split(";"))


# #### Arreglando los Strings

# In[5]:


columnas[0] = columnas[0][1:]


# In[6]:


columnas[0]


# In[7]:


columnas[5] = columnas[5][:5]


# In[8]:


columnas[5]


# In[9]:


columnas


# In[10]:


columnas = ["mes", "cuit", "provincia", "municipio", "monto", "tipo"]


# In[11]:


columnas


# #### Listo

# In[12]:


data_filas = data[1:]


# In[13]:


data_filas[660][:-1]


# In[14]:


columna_mes = []
columna_cuit = []
columna_provincia = []
columna_municipio = []
columna_monto = []
columna_tipo = []


# In[15]:


U = [
    columna_mes,
    columna_cuit,
    columna_provincia,
    columna_municipio,
    columna_monto,
    columna_tipo,
]


# In[16]:



for fila in data_filas:
    valores = fila.strip("").split(";")
    columna_mes.append(valores[0])
    columna_cuit.append(valores[1])
    columna_provincia.append(valores[2])
    columna_municipio.append(valores[3])
    columna_monto.append(valores[4])
    columna_tipo.append(valores[5][:-1])


# #### Limpiando los Strings

# In[17]:


columna_provincia


# In[18]:


# Funcion "limpiar_comillas"
def limpiar_comillas(x):
    for i in range( len( x)):
        x[i] = x[i].replace('"', '')
    return x


# In[19]:


limpiar_comillas(columna_provincia)
limpiar_comillas(columna_municipio)
limpiar_comillas(columna_tipo)

for i in range( len( columna_monto)):
    columna_monto[i] = float(columna_monto[i])


# In[20]:


columna_provincia


# In[21]:


columna_municipio


# In[22]:


columna_tipo


# * Pasando a Data Frame de Pandas
# * Agregando las columnas pertinentes

# #### Mes

# In[23]:


# Primero: creo una version de "columnas_mes" en array de pandas.dataframe
columna_mes_df = pd.DataFrame(columna_mes)


# In[24]:


# Añadir el nombre de la columna pertinente
columna_mes_df = pd.DataFrame(columna_mes_df.values, columns = ["{}".format(columnas[0])])


# In[25]:


columna_mes_df


# #### CUIT

# In[26]:


columna_cuit_df = pd.DataFrame(columna_cuit)
columna_cuit_df = pd.DataFrame(columna_cuit_df.values, columns = ["{}".format(columnas[1])])


# In[27]:


columna_cuit_df


# #### provincia

# In[28]:


columna_provincia_df = pd.DataFrame(columna_provincia)
columna_provincia_df = pd.DataFrame(columna_provincia_df.values, columns = ["{}".format(columnas[2])])


# In[29]:


columna_provincia_df


# #### municipio

# In[30]:


columna_municipio_df = pd.DataFrame(columna_municipio)
columna_municipio_df = pd.DataFrame(columna_municipio_df.values, columns = ["{}".format(columnas[3])])


# In[31]:


columna_municipio_df


# #### monto

# In[32]:


columna_monto_df = pd.DataFrame(columna_monto)
columna_monto_df = pd.DataFrame(columna_monto_df.values, columns = ["{}".format(columnas[4])])


# In[33]:


columna_monto_df


# #### tipo

# In[34]:


columna_tipo_df = pd.DataFrame(columna_tipo)
columna_tipo_df = pd.DataFrame(columna_tipo_df.values, columns = ["{}".format(columnas[5])])


# In[35]:


columna_tipo_df


# #### ----------------- >> Listo

# #### Merging las columnas de tipo pandas.df en uno solo

# In[36]:


data_df_final = pd.concat([columna_mes_df, columna_cuit_df, columna_provincia_df, columna_municipio_df, columna_monto_df, columna_tipo_df], axis = 1)


# In[37]:


data_df_final


# In[38]:


data_df_final.dtypes


# In[39]:


plt.hist(data_df_final["monto"], bins = 50)
plt.show()


# In[40]:


plt.boxplot(data_df_final["monto"], sym='_', vert=1, whis=1.5)#whis es 1.5 por el rango intercuartilico
plt.grid(True)
plt.show()


# In[41]:


data_df_final["monto"].describe()


# In[42]:


descripcion_lista = list(data_df_final["monto"].describe())


# In[43]:


descripcion_lista


# In[44]:


x1, y1 = [0, 1, 2], [data_df_final["monto"].min(), data_df_final["monto"].min(), data_df_final["monto"].min()]
x2, y2 = [0, 1, 3], [data_df_final["monto"].mean(), data_df_final["monto"].mean(), data_df_final["monto"].mean()]
x3, y3 = [0, 1, 3], [315201.755, 315201.755, 315201.755]
fig1 = plt.boxplot(data_df_final["monto"], 0, "")
fig2 = plt.plot(x1, y1, "--r")
fig3 = plt.plot(x2, y2, "--g")
fig4 = plt.plot(x3, y3, "--", color = "orange")

plt.grid(True)
plt.show()


# In[45]:


plt.boxplot(data_df_final["monto"], notch=0, sym='.', vert=1, whis=1.5)
x, y = [0, 1, 3], [data_df_final["monto"].max(), data_df_final["monto"].max(), data_df_final["monto"].max()]
plt.plot(x, y, "--c")

#plt.ylabel("Numero de llamadas diarias")
#plt.title("Boxplot de las llamadas dias")
plt.xlim()
plt.ylim()
plt.grid(True)
plt.show()


# In[46]:


x11 = data_df_final["mes"]
y11 = data_df_final["monto"]
y12 = []
y13 = []

for l in range( len(x11)):
        y12.append( data_df_final["monto"].max())

for l in range( len(x11)):
        y13.append( data_df_final["monto"].mean())

def millions(x, pos):
    return '$%1.1fM' % (x*1e-6)
formatter = FuncFormatter(millions)

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)


plt.plot(x11, y11, "darkcyan")
plt.plot(x11, y12, "--r")
plt.plot(x11, y13, "--b")
plt.xticks(rotation = 'vertical')
plt.tick_params(axis='both', labelsize = 10)
plt.grid(True)
plt.show()


# #### Voy a intentar Dummybilizar los meses en columnas cuyos valores son los montos de los subsidios 

# In[47]:


dummy_provincia = pd.get_dummies(data_df_final["provincia"], prefix = "provincia")


# In[48]:


provincias_columnas = dummy_provincia.columns.get_values()


# In[49]:


provincias_columnas = list(provincias_columnas)


# In[50]:


provincias_columnas


# In[51]:


#Limpiando la chanchada
for i in range( len( provincias_columnas)):
    provincias_columnas[i] = provincias_columnas[i].replace("provincia_", "")
    


# In[52]:


provincias_columnas


# In[53]:


# Hago un diccionario con con el nombre de las provincias
provincias = {}
for provincia in provincias_columnas:
    provincias[provincia] = []


# In[54]:


data_df_monto_provincia = pd.concat([columna_provincia_df, columna_monto_df], axis = 1)


# In[55]:



for i in range( len(dummy_provincia)):
        if dummy_provincia["provincia_BUENOS AIRES"][i] == 1:
            provincias["BUENOS AIRES"].append(data_df_monto_provincia["monto"][i])

        elif dummy_provincia["provincia_C.A.B.A."][i] == 1:
            provincias["C.A.B.A."].append(data_df_monto_provincia["monto"][i])
          
        elif dummy_provincia["provincia_CATAMARCA"][i] == 1:
            provincias["CATAMARCA"].append(data_df_monto_provincia["monto"][i])
            
        elif dummy_provincia["provincia_SANTA FE"][i] == 1:
            provincias["SANTA FE"].append(data_df_monto_provincia["monto"][i])
            
        elif dummy_provincia["provincia_CHACO"][i] == 1:
            provincias["CHACO"].append(data_df_monto_provincia["monto"][i])
            
        elif dummy_provincia["provincia_CHUBUT"][i] == 1:
            provincias["CHUBUT"].append(data_df_monto_provincia["monto"][i])
            
        elif dummy_provincia["provincia_CORDOBA"][i] == 1:
            provincias['CORDOBA'].append(data_df_monto_provincia["monto"][i])

        elif dummy_provincia["provincia_CORRIENTES"][i] == 1:
            provincias['CORRIENTES'].append(data_df_monto_provincia["monto"][i])
            
        elif dummy_provincia["provincia_ENTRE RIOS"][i] == 1:
            provincias['ENTRE RIOS'].append(data_df_monto_provincia["monto"][i])

        elif dummy_provincia["provincia_FORMOSA"][i] == 1:
            provincias['FORMOSA'].append(data_df_monto_provincia["monto"][i]) 

        elif dummy_provincia["provincia_JN"][i] == 1:
            provincias['JN'].append(data_df_monto_provincia["monto"][i])  

        elif dummy_provincia["provincia_JUJUY"][i] == 1:
            provincias['JUJUY'].append(data_df_monto_provincia["monto"][i])

        elif dummy_provincia["provincia_LA PAMPA"][i] == 1:
            provincias['LA PAMPA'].append(data_df_monto_provincia["monto"][i]) 

        elif dummy_provincia["provincia_LA RIOJA"][i] == 1:
            provincias['LA RIOJA'].append(data_df_monto_provincia["monto"][i]) 

        elif dummy_provincia["provincia_MENDOZA"][i] == 1:
            provincias['MENDOZA'].append(data_df_monto_provincia["monto"][i])
            
        elif dummy_provincia["provincia_MISIONES"][i] == 1:
            provincias['MISIONES'].append(data_df_monto_provincia["monto"][i])

        elif dummy_provincia["provincia_NEUQUEN"][i] == 1:
            provincias['NEUQUEN'].append(data_df_monto_provincia["monto"][i])
            
        elif dummy_provincia["provincia_RIO NEGRO"][i] == 1:
            provincias['RIO NEGRO'].append(data_df_monto_provincia["monto"][i])

        elif dummy_provincia["provincia_SALTA"][i] == 1:
            provincias['SALTA'].append(data_df_monto_provincia["monto"][i])
            
        elif dummy_provincia["provincia_SAN JUAN"][i] == 1:
            provincias['SAN JUAN'].append(data_df_monto_provincia["monto"][i])
            
        elif dummy_provincia["provincia_SAN LUIS"][i] == 1:
            provincias['SAN LUIS'].append(data_df_monto_provincia["monto"][i])

        elif dummy_provincia["provincia_SANTA CRUZ"][i] == 1:
            provincias['SANTA CRUZ'].append(data_df_monto_provincia["monto"][i])

        elif dummy_provincia["provincia_SANTIAGO DEL ESTERO"][i] == 1:
            provincias['SANTIAGO DEL ESTERO'].append(data_df_monto_provincia["monto"][i])

        elif dummy_provincia["provincia_TIERRA DEL FUEGO"][i] == 1:
            provincias['TIERRA DEL FUEGO'].append(data_df_monto_provincia["monto"][i])

        elif dummy_provincia["provincia_TUCUMAN"][i] == 1:
            provincias['TUCUMAN'].append(data_df_monto_provincia["monto"][i])


# ### He llenado el diccionario "provincias" con  los montos de los subsidios de estos dos años [2017, 2018] para cada provincia correspondiente, lo que voy a hacer ahora es sumar los montos y representarlos

# In[56]:


provincias_columnas


# In[57]:


provincias["BUENOS AIRES"] = sum(provincias["BUENOS AIRES"])
provincias["C.A.B.A."] = sum(provincias["C.A.B.A."])
provincias["CATAMARCA"] = sum(provincias["CATAMARCA"])
provincias["CHACO"] = sum(provincias["CHACO"])
provincias["CHUBUT"] = sum(provincias["CHUBUT"])
provincias["CORDOBA"] = sum(provincias["CORDOBA"])
provincias["CORRIENTES"] = sum(provincias["CORRIENTES"])
provincias["ENTRE RIOS"] = sum(provincias["ENTRE RIOS"])
provincias["FORMOSA"] = sum(provincias["FORMOSA"])
provincias["JN"] = sum(provincias["JN"])
provincias["JUJUY"] = sum(provincias["JUJUY"])
provincias["LA PAMPA"] = sum(provincias["LA PAMPA"])
provincias["LA RIOJA"] = sum(provincias["LA RIOJA"])
provincias["MENDOZA"] = sum(provincias["MENDOZA"])
provincias["MISIONES"] = sum(provincias["MISIONES"])
provincias["NEUQUEN"] = sum(provincias["NEUQUEN"])
provincias["RIO NEGRO"] = sum(provincias["RIO NEGRO"])
provincias["SALTA"] = sum(provincias["SALTA"])
provincias["SAN JUAN"] = sum(provincias["SAN JUAN"])
provincias["SAN LUIS"] = sum(provincias["SAN LUIS"])
provincias["SANTA CRUZ"] = sum(provincias["SANTA CRUZ"])
provincias["SANTA FE"] = sum(provincias["SANTA FE"])
provincias["SANTIAGO DEL ESTERO"] = sum(provincias["SANTIAGO DEL ESTERO"])
provincias["TIERRA DEL FUEGO"] = sum(provincias["TIERRA DEL FUEGO"])
provincias["TUCUMAN"] = sum(provincias["TUCUMAN"])


# In[58]:


monto_total_provincias_df = pd.DataFrame(provincias, index = [0])


# In[59]:


monto_total_provincias_df


# In[60]:


provincias


# In[61]:


xsY = []
for i in provincias:
    xsY.append( provincias[i])
    
xsX = list(monto_total_provincias_df)

def billions(x, pos):
    return '$%2.0f Mil Millones' % (x*1e-9)
formatter2 = FuncFormatter(billions)

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter2)


plt.title("Subsidios al transporte publico de corta distancia entre los años 2017 y 2018 por provincia\n", fontsize = 17)
plt.ylabel("Monto en Pesos\n(En Mil de Millones)\n\n", fontsize=16)
plt.xlabel("\nProvincias", fontsize=16)
plt.style.use("bmh")
plt.grid(zorder=4)

plt.yticks(rotation = 'horizontal')
plt.xticks(rotation = 'vertical')
plt.tick_params(axis='both', labelsize = 10)
plt.bar(xsX, xsY, color = "darkcyan")
plt.show()


# #### Para poder representar los datos de forma mas fiable vamos a dividir el monto sobre la cantidad total de habitantes de cada provincia en el año pertinente.
# #### Los datos demograficos se actualizan cada 10 años, necesitamos datos para el año 2017 pero los mismos no existen pues el ultimo censo fue hecho en 2010. Lo que haré sera tratar de estimar un valor aproximado a la cantidad de habitantes para cada provincia en particular, voy a hacer una funcion tomando la ecuacion de la recta que une los puntos formados por las cordenadas (x, y) en donde "x" es el año en el que se tomo el censo, e "y" es el censo en cuestion. 
# #### (x - x2)/(x2 - x1) = (y - y2)/(y2 - y1)
# #### *Notacion:* Sea p_creciente_PROVINCIA(x) Nuestra funcion
# #### *Aclaracion*: El hecho de por que esta funcion es creciente, y no, decreciente o constante fue consultado de la [Central Intellifence Agency](https://www.cia.gov/library/publications/the-world-factbook/geos/ar.html), donde podemos observar que la dinamica demografica en Argentina es creciente. (En general esto es así en toda America Latina).
# #### Los datos demograficos fueron obtenidos de [Wikipedia](https://es.wikipedia.org/wiki/Censo_argentino_de_2010). Voy a usar estos datos demograficos historicos, en particular de los censos de los años 2001 - 2010 para construir la funcion. El sesgo de nuestra prediccion, solo se va poder estimar una vez el INDEC emita los datos demograficos pertinentes para poder compararlos, aún asi la precisión para nuestro caso en particular es satisfactoria, y los margenes de error que debe haber son despreciables en relacion a los resultados que vamos a obtener. 
# 
# #### Una posible forma de estimar  la diferencia entre el dato real y la estimacion. Es confiar en la precisión de los datos emitidos por la [Central Intellifence Agency](https://www.cia.gov/library/publications/the-world-factbook/geos/ar.html) . Esta misma sostiene que la cantidad de habitantes es de 44,694,198 para el año 2018.
# #### Primero establecemos las predicciones con las funciones pertinentes; Luego, sumamos las mismas. Debería darnos un valor que oscile entre los 43 y 44millones y medio aprox.. Luego calculamos la diferencia entre  44,694,198 y nuestra suma, y esta proporcion  es la que podriamos usar como un error. Aunque a fines practicos podríamos obtar por omitirlo.

# In[62]:


del(monto_total_provincias_df["JN"])


# In[63]:


def p_creciente_BA(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(15625083 - 13827203) + 13827203 #Esta es la ecuacion de la recta que une los puntos (2001, 13827203) y (2010, 15625083) 
    return (float("{}".format(float(y))))

def p_creciente_CATAMARCA(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(367828 - 334568) + 334568 
    return (float("{}".format(float(y))))

def p_creciente_CHACO(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(1055259 - 984446) + 984446 
    return (float("{}".format(float(y))))

def p_creciente_CHUBUT(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(509108 - 413234) + 413234 
    return (float("{}".format(float(y))))

def p_creciente_CABA(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(2890151 - 2776138) + 2776138 
    return (float("{}".format(float(y))))

def p_creciente_CORRIENTES(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(992595 - 930991) + 930991 
    return float(y)

def p_creciente_CORDOBA(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(3308876 - 3066801) + 3066801 
    return float(y)

def p_creciente_ERRIOS(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(1235994 - 1158147) + 1158147 
    return float(y)

def p_creciente_FORMOSA(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(530162 - 486559) + 486559 
    return float(y)

def p_creciente_JUJUY(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(673307 - 611888) + 611888 
    return float(y)

def p_creciente_LAPAMPA(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(318951 - 299294) + 299294 
    return float(y)

def p_creciente_LARIOJA(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(333642 - 289983) + 289983 
    return float(y)

def p_creciente_MENDOZA(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(1738929 - 1579651) + 1579651 
    return float(y)

def p_creciente_MISIONES(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(1101593 - 965522) + 965522 
    return float(y)

def p_creciente_NEUQUEN(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(551266 - 474155) + 474155 
    return float(y)

def p_creciente_RIONEGRO(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(638645 - 552822) + 552822 
    return float(y)

def p_creciente_SALTA(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(1214441 - 1079051) + 1079051 
    return float(y)

def p_creciente_SANJUAN(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(681055 - 620023) + 620023 
    return float(y)

def p_creciente_SANLUIS(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(432310 - 367933) + 367933
    return float(y)

def p_creciente_SANTACRUZ(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(273964 - 196958) + 196958
    return float(y)

def p_creciente_SANTAFE(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(3194537 - 3000701) + 3000701
    return float(y)

def p_creciente_SANTIAGODELESTERO(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(874006 - 804457) + 804457
    return float(y)

def p_creciente_TIERRADELFUEGO(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(127205 - 101079) + 101079
    return float(y)

def p_creciente_TUCUMAN(x):
    
    x = float(x)
    y = ((x - 2001)/(2010 - 2001))*(1448188 - 1338523) + 1338523
    return float(y)


# In[64]:


ys2017 = [
    p_creciente_BA(2017),
    p_creciente_CABA(2017),
    p_creciente_CATAMARCA(2017),
    p_creciente_CHACO(2017),
    p_creciente_CHUBUT(2017),
    p_creciente_CORDOBA(2017),
    p_creciente_CORRIENTES(2017),
    p_creciente_ERRIOS(2017),
    p_creciente_FORMOSA(2017),
    p_creciente_JUJUY(2017),
    p_creciente_LAPAMPA(2017),
    p_creciente_LARIOJA(2017),
    p_creciente_MENDOZA(2017),
    p_creciente_MISIONES(2017),
    p_creciente_NEUQUEN(2017),
    p_creciente_RIONEGRO(2017),
    p_creciente_SALTA(2017),
    p_creciente_SANJUAN(2017),
    p_creciente_SANLUIS(2017),
    p_creciente_SANTACRUZ(2017),
    p_creciente_SANTAFE(2017),
    p_creciente_SANTIAGODELESTERO(2017),
    p_creciente_TIERRADELFUEGO(2017),
    p_creciente_TUCUMAN(2017)    
]

ys2018 = [
    p_creciente_BA(2018),
    p_creciente_CABA(2018),
    p_creciente_CATAMARCA(2018),
    p_creciente_CHACO(2018),
    p_creciente_CHUBUT(2018),
    p_creciente_CORDOBA(2018),
    p_creciente_CORRIENTES(2018),
    p_creciente_ERRIOS(2018),
    p_creciente_FORMOSA(2018),
    p_creciente_JUJUY(2018),
    p_creciente_LAPAMPA(2018),
    p_creciente_LARIOJA(2018),
    p_creciente_MENDOZA(2018),
    p_creciente_MISIONES(2018),
    p_creciente_NEUQUEN(2018),
    p_creciente_RIONEGRO(2018),
    p_creciente_SALTA(2018),
    p_creciente_SANJUAN(2018),
    p_creciente_SANLUIS(2018),
    p_creciente_SANTACRUZ(2018),
    p_creciente_SANTAFE(2018),
    p_creciente_SANTIAGODELESTERO(2018),
    p_creciente_TIERRADELFUEGO(2018),
    p_creciente_TUCUMAN(2018)    
]


# In[66]:


sum_ys2018 = sum(ys2018)
error = (44694198 - sum_ys2018)/44694198
error


# In[68]:


xs = list(monto_total_provincias_df)


plt.title("Una aproximacion de la cantidad de habitantes por provincias para los años 2017 y 2018\n", fontsize = 17)
plt.ylabel("Habitantes \n\n", fontsize=16)
plt.xlabel("\nProvincias", fontsize=16)
plt.style.use("bmh")
plt.grid(zorder=4)

width = 0.35
plt.yticks(rotation = 'horizontal')
plt.xticks(rotation = 'vertical')
plt.tick_params(axis='both', labelsize = 10)
plt.bar(xs, ys2017, color = "darkcyan")
plt.bar(xs, ys2018, xerr = error, width = width, color = "darkred", ecolor= "g")
plt.legend(["Habitantes en año 2017", "Habitantes en año 2018"], bbox_to_anchor=(1.04,1), loc = "upper left")

plt.show()


# In[77]:


montos_discriminados = {}
for provincia in provincias_columnas:
    montos_discriminados[provincia] = [[],[]]


# In[78]:


# Como va a estar estructurado este diccionario:
# La lista tendra dos valores, en el primer valor la suma de un tipo de variable y en el segundo la suma del otro tipo
montos_discriminados


# #### Para cerciorarnos de que existen dos (Y SOLO DOS) clasificaciones para el monto, vamos a dummyficar la columna "tipo".
# 

# In[80]:


dummy_tipo = pd.get_dummies(data_df_final["tipo"], prefix = "tipo")
dummy_tipo.head()


# #### Como podemos ver, solo reconocemos 2 tipos de montos. Gasoil y Tarifa.

# In[81]:



for i in range( len( data_df_final)):
    x = list(data_df_final.iloc[i])
    if x[2] == "BUENOS AIRES":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["BUENOS AIRES"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["BUENOS AIRES"][1]).append(x[-2])
            
    if x[2] == "C.A.B.A.":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["C.A.B.A."][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["C.A.B.A."][1]).append(x[-2])    

    if x[2] == "CATAMARCA":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["CATAMARCA"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["CATAMARCA"][1]).append(x[-2])
            
    if x[2] == "CHACO":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["CHACO"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["CHACO"][1]).append(x[-2])
            
    if x[2] == "CHUBUT":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["CHUBUT"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["CHUBUT"][1]).append(x[-2])
            
    if x[2] == "CORDOBA":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["CORDOBA"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["CORDOBA"][1]).append(x[-2])

    if x[2] == "CORRIENTES":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["CORRIENTES"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["CORRIENTES"][1]).append(x[-2])
            
    if x[2] == "ENTRE RIOS":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["ENTRE RIOS"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["ENTRE RIOS"][1]).append(x[-2])    

    if x[2] == "FORMOSA":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["FORMOSA"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["FORMOSA"][1]).append(x[-2])
            
    if x[2] == "JUJUY":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["JUJUY"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["JUJUY"][1]).append(x[-2])
            
    if x[2] == "LA PAMPA":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["LA PAMPA"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["LA PAMPA"][1]).append(x[-2])
            
    if x[2] == "LA RIOJA":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["LA RIOJA"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["LA RIOJA"][1]).append(x[-2])
            
    if x[2] == "MENDOZA":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["MENDOZA"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["MENDOZA"][1]).append(x[-2])
            
    if x[2] == "MISIONES":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["MISIONES"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["MISIONES"][1]).append(x[-2])    

    if x[2] == "NEUQUEN":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["NEUQUEN"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["NEUQUEN"][1]).append(x[-2])
            
    if x[2] == "RIO NEGRO":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["RIO NEGRO"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["RIO NEGRO"][1]).append(x[-2])
            
    if x[2] == "SALTA":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["SALTA"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["SALTA"][1]).append(x[-2])
            
    if x[2] == "SAN JUAN":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["SAN JUAN"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["SAN JUAN"][1]).append(x[-2])
            
    if x[2] == "SAN LUIS":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["SAN LUIS"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["SAN LUIS"][1]).append(x[-2])
            
    if x[2] == "SANTA CRUZ":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["SANTA CRUZ"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["SANTA CRUZ"][1]).append(x[-2])    

    if x[2] == "SANTA FE":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["SANTA FE"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["SANTA FE"][1]).append(x[-2])
            
    if x[2] == "SANTIAGO DEL ESTERO":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["SANTIAGO DEL ESTERO"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["SANTIAGO DEL ESTERO"][1]).append(x[-2])
            
    if x[2] == "TIERRA DEL FUEGO":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["TIERRA DEL FUEGO"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["TIERRA DEL FUEGO"][1]).append(x[-2])
            
    if x[2] == "TUCUMAN":
        if x[-1] == "Comp. Tarifaria":
            (montos_discriminados["TUCUMAN"][0]).append(x[-2])
        elif x[-1] == "Comp. Gasoil":
            (montos_discriminados["TUCUMAN"][1]).append(x[-2])


# In[82]:


del(montos_discriminados["JN"])


# #### Una vez hecho esto; Vamos a crear otro diccionario con la suma de dichos montos. 
# #### Para verificarlo vamos a demostrar que la suma de los dos rubros  nos da el total.

# In[83]:


montos_discriminados_suma = {}
for provincia in provincias_columnas:
    montos_discriminados_suma[provincia] = [[],[]]

del(montos_discriminados_suma["JN"])
montos_discriminados_suma

for provincia in montos_discriminados_suma:
    montos_discriminados_suma[provincia][0] = sum(montos_discriminados[provincia][0])
    montos_discriminados_suma[provincia][1] = sum(montos_discriminados[provincia][1])


# In[84]:


montos_discriminados_suma
# En donde ["Tarifa", "Gasoil"]


# ### Demostracion:
# 

# In[85]:



def proof(x):
    
    if x == "BUENOS AIRES":
        return int(montos_discriminados_suma["BUENOS AIRES"][0] + montos_discriminados_suma["BUENOS AIRES"][1]) == int(provincias["BUENOS AIRES"])
    elif x == 'C.A.B.A.':
        return int(montos_discriminados_suma['C.A.B.A.'][0] + montos_discriminados_suma['C.A.B.A.'][1]) == int(provincias['C.A.B.A.'])
    elif x == 'CATAMARCA':
        return int(montos_discriminados_suma["CATAMARCA"][0] + montos_discriminados_suma["CATAMARCA"][1]) == int(provincias["CATAMARCA"])
    elif x == 'CHACO':
        return int(montos_discriminados_suma['CHACO'][0] + montos_discriminados_suma['CHACO'][1]) == int(provincias['CHACO'])
    elif x == 'CHUBUT':
        return int(montos_discriminados_suma['CHUBUT'][0] + montos_discriminados_suma['CHUBUT'][1]) == int(provincias['CHUBUT'])
    elif x == 'CORDOBA':
        return int(montos_discriminados_suma['CORDOBA'][0] + montos_discriminados_suma['CORDOBA'][1]) == int(provincias['CORDOBA'])
    elif x == 'CORRIENTES':
        return int(montos_discriminados_suma['CORRIENTES'][0] + montos_discriminados_suma['CORRIENTES'][1]) == int(provincias['CORRIENTES'])
    elif x == 'ENTRE RIOS':
        return int(montos_discriminados_suma['ENTRE RIOS'][0] + montos_discriminados_suma['ENTRE RIOS'][1]) == int(provincias['ENTRE RIOS'])
    elif x == 'FORMOSA':
        return int(montos_discriminados_suma['FORMOSA'][0] + montos_discriminados_suma['FORMOSA'][1]) == int(provincias['FORMOSA'])
    elif x == 'JUJUY':
        return int(montos_discriminados_suma['JUJUY'][0] + montos_discriminados_suma['JUJUY'][1]) == int(provincias['JUJUY'])
    elif x == 'LA PAMPA':
        return int(montos_discriminados_suma['LA PAMPA'][0] + montos_discriminados_suma['LA PAMPA'][1]) == int(provincias['LA PAMPA'])
    elif x == 'LA RIOJA':
        return int(montos_discriminados_suma['LA RIOJA'][0] + montos_discriminados_suma['LA RIOJA'][1]) == int(provincias['LA RIOJA'])
    elif x == 'MENDOZA':
        return int(montos_discriminados_suma['MENDOZA'][0] + montos_discriminados_suma['MENDOZA'][1]) == int(provincias['MENDOZA'])
    elif x == 'MISIONES':
        return int(montos_discriminados_suma['MISIONES'][0] + montos_discriminados_suma['MISIONES'][1]) == int(provincias['MISIONES'])
    elif x == 'NEUQUEN':
        return int(montos_discriminados_suma['NEUQUEN'][0] + montos_discriminados_suma['NEUQUEN'][1]) == int(provincias['NEUQUEN'])
    elif x == 'RIO NEGRO':
        return int(montos_discriminados_suma['RIO NEGRO'][0] + montos_discriminados_suma['RIO NEGRO'][1]) == int(provincias['RIO NEGRO'])
    elif x == 'SALTA':
        return int(montos_discriminados_suma['SALTA'][0] + montos_discriminados_suma['SALTA'][1]) == int(provincias['SALTA'])    
    elif x == 'SAN LUIS':
        return int(montos_discriminados_suma['SAN LUIS'][0] + montos_discriminados_suma['SAN LUIS'][1]) == int(provincias['SAN LUIS'])
    elif x == 'SAN JUAN':
        return int(montos_discriminados_suma['SAN JUAN'][0] + montos_discriminados_suma['SAN JUAN'][1]) == int(provincias['SAN JUAN'])
    elif x == 'SANTA CRUZ':
        return int(montos_discriminados_suma['SANTA CRUZ'][0] + montos_discriminados_suma['SANTA CRUZ'][1]) == int(provincias['SANTA CRUZ'])
    elif x == 'SANTA FE':
        return int(montos_discriminados_suma['SANTA FE'][0] + montos_discriminados_suma['SANTA FE'][1]) == int(provincias['SANTA FE'])
    elif x == 'SANTIAGO DEL ESTERO':
        return int(montos_discriminados_suma['SANTIAGO DEL ESTERO'][0] + montos_discriminados_suma['SANTIAGO DEL ESTERO'][1]) == int(provincias['SANTIAGO DEL ESTERO'])
    elif x == 'TIERRA DEL FUEGO':
        return int(montos_discriminados_suma['TIERRA DEL FUEGO'][0] + montos_discriminados_suma['TIERRA DEL FUEGO'][1]) == int(provincias['TIERRA DEL FUEGO'])
    elif x == 'TUCUMAN':
        return int(montos_discriminados_suma['TUCUMAN'][0] + montos_discriminados_suma['TUCUMAN'][1]) == int(provincias['TUCUMAN'])


# In[86]:


for i in range( len( provincias_columnas)):
    print(proof(provincias_columnas[i]))


# #### El valor de "NONE" solo es por una columna del data frame que tengo sin identificar LLAMADA "JN"
# ### Fin demostración

# In[87]:


xs3 = list(provincias_columnas)
del(xs3[9])
ys3_tarifa = []
ys3_gasoil = []
for provincia in xs3:
    
    ys3_tarifa.append(montos_discriminados_suma[provincia][0])
    ys3_gasoil.append(montos_discriminados_suma[provincia][1])
    

def billions2(x, pos):
    return '$%2.0f Mil Millones' % (x*1e-9)
formatter2 = FuncFormatter(billions2)

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter2)
    

plt.title("Monto total de subsidios acumulados por provincia en los años 2017 y 2018\n", fontsize = 17)
plt.ylabel("Monto en Miles de Millones \n\n", fontsize=16)
plt.xlabel("\nProvincias", fontsize=16)
plt.style.use("bmh")
plt.grid(zorder=4)

plt.yticks(rotation = 'horizontal')
plt.xticks(rotation = 'vertical')
plt.tick_params(axis='both', labelsize = 10)
plt.bar(xs3, ys3_tarifa, color = "darkcyan")
plt.bar(xs3, ys3_gasoil, bottom = ys3_tarifa, color = "darkred")
plt.legend(["Comp. Tarifaria", "Comp. Gasoil"], bbox_to_anchor=(1.04,1), loc = "upper left")

plt.show()


# In[88]:


xs3 = list(provincias_columnas)
del(xs3[9])
ys3_tarifa = []
ys3_gasoil = []
for provincia in xs3:
    
    ys3_tarifa.append(montos_discriminados_suma[provincia][0])
    ys3_gasoil.append(montos_discriminados_suma[provincia][1])
    

def billions2(x, pos):
    return '$%2.0f Mil Millones' % (x*1e-9)
formatter2 = FuncFormatter(billions)

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter2)
    

plt.title("Monto total de subsidios acumulados por provincia en los años 2017 y 2018\n", fontsize = 17)
plt.ylabel("Monto en en Miles de Millones \n\n", fontsize=16)
plt.xlabel("\nProvincias", fontsize=16)
plt.style.use("bmh")
plt.grid(zorder=4)

plt.yticks(rotation = 'horizontal')
plt.xticks(rotation = 'vertical')
plt.tick_params(axis='both', labelsize = 10)
plt.bar(xs3, ys3_tarifa, color = "darkcyan")
plt.bar(xs3, ys3_gasoil, bottom = ys3_tarifa, color = "darkred")
plt.legend(["Comp. Tarifaria", "Comp. Gasoil"], bbox_to_anchor=(1.04,1), loc = "upper left")
plt.ylim(-1, 3558600864.340008)


plt.show()


# In[89]:


xs3 = list(provincias_columnas)
del(xs3[9])
ys3_tarifa = []
ys3_gasoil = []
for provincia in xs3:
    
    ys3_tarifa.append(montos_discriminados_suma[provincia][0])
    ys3_gasoil.append(montos_discriminados_suma[provincia][1])
    

def billions2(x, pos):
    return '$%2.0f Mil Millones' % (x*1e-9)
formatter2 = FuncFormatter(billions)

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter2)
    

plt.title("Monto total de subsidios acumulados por provincia en los años 2017 y 2018\n", fontsize = 17)
plt.ylabel("Monto en en Miles de Millones \n\n", fontsize=16)
plt.xlabel("\nProvincias", fontsize=16)
plt.style.use("bmh")
plt.grid(zorder=4)

plt.yticks(rotation = 'horizontal')
plt.xticks(rotation = 'vertical')
plt.tick_params(axis='both', labelsize = 10)
plt.bar(xs3, ys3_tarifa, color = "darkcyan")
plt.bar(xs3, ys3_gasoil, bottom = ys3_tarifa, color = "darkred")
plt.legend(["Comp. Tarifaria", "Comp. Gasoil"], bbox_to_anchor=(1.04,1), loc = "upper left")
plt.ylim(-1, 2558600864.340008)
#plt.xlim('C.A.B.A.', "TUCUMAN")

plt.show()


# #### Voy a plotear los subsidios acumulados en los años 2017 y 2018 sobre la cantidad de habitantes

# In[90]:


ys2017 = [
    p_creciente_BA(2017),
    p_creciente_CABA(2017),
    p_creciente_CATAMARCA(2017),
    p_creciente_CHACO(2017),
    p_creciente_CHUBUT(2017),
    p_creciente_CORDOBA(2017),
    p_creciente_CORRIENTES(2017),
    p_creciente_ERRIOS(2017),
    p_creciente_FORMOSA(2017),
    p_creciente_JUJUY(2017),
    p_creciente_LAPAMPA(2017),
    p_creciente_LARIOJA(2017),
    p_creciente_MENDOZA(2017),
    p_creciente_MISIONES(2017),
    p_creciente_NEUQUEN(2017),
    p_creciente_RIONEGRO(2017),
    p_creciente_SALTA(2017),
    p_creciente_SANJUAN(2017),
    p_creciente_SANLUIS(2017),
    p_creciente_SANTACRUZ(2017),
    p_creciente_SANTAFE(2017),
    p_creciente_SANTIAGODELESTERO(2017),
    p_creciente_TIERRADELFUEGO(2017),
    p_creciente_TUCUMAN(2017)    
]


# In[91]:


list(provincias_columnas)


# In[92]:


xs4 = list(provincias_columnas)
del(xs4[9])

ys4_2017 = [(provincias["BUENOS AIRES"]/p_creciente_BA(2017)),
            (provincias["C.A.B.A."]/p_creciente_CABA(2017)),
            (provincias["CATAMARCA"]/p_creciente_CATAMARCA(2017)),
            (provincias["CHACO"]/p_creciente_CHACO(2017)),
            (provincias["CHUBUT"]/p_creciente_CHUBUT(2017)),
            (provincias["CORDOBA"]/p_creciente_CORDOBA(2017)),
            (provincias["CORRIENTES"]/p_creciente_CORRIENTES(2017)),
            (provincias["ENTRE RIOS"]/p_creciente_ERRIOS(2017)),
            (provincias["FORMOSA"]/p_creciente_FORMOSA(2017)),
            (provincias["JUJUY"]/p_creciente_JUJUY(2017)),
            (provincias["LA PAMPA"]/p_creciente_LAPAMPA(2017)),
            (provincias["LA RIOJA"]/p_creciente_LARIOJA(2017)),
            (provincias["MENDOZA"]/p_creciente_MENDOZA(2017)),
            (provincias["MISIONES"]/p_creciente_MISIONES(2017)),
            (provincias["NEUQUEN"]/p_creciente_NEUQUEN(2017)),
            (provincias["RIO NEGRO"]/p_creciente_RIONEGRO(2017)),
            (provincias["SALTA"]/p_creciente_SALTA(2017)),
            (provincias["SAN JUAN"]/p_creciente_SANJUAN(2017)),
            (provincias["SAN LUIS"]/p_creciente_SANLUIS(2017)),
            (provincias["SANTA CRUZ"]/p_creciente_SANTACRUZ(2017)),
            (provincias["SANTA FE"]/p_creciente_SANTAFE(2017)),
            (provincias["SANTIAGO DEL ESTERO"]/p_creciente_SANTIAGODELESTERO(2017)),
            (provincias["TIERRA DEL FUEGO"]/p_creciente_TIERRADELFUEGO(2017)),
            (provincias["TUCUMAN"]/p_creciente_TUCUMAN(2017)),
           ]

ys4_2018 = [(provincias["BUENOS AIRES"]/p_creciente_BA(2018)),
            (provincias["C.A.B.A."]/p_creciente_CABA(2018)),
            (provincias["CATAMARCA"]/p_creciente_CATAMARCA(2018)),
            (provincias["CHACO"]/p_creciente_CHACO(2018)),
            (provincias["CHUBUT"]/p_creciente_CHUBUT(2018)),
            (provincias["CORDOBA"]/p_creciente_CORDOBA(2018)),
            (provincias["CORRIENTES"]/p_creciente_CORRIENTES(2018)),
            (provincias["ENTRE RIOS"]/p_creciente_ERRIOS(2018)),
            (provincias["FORMOSA"]/p_creciente_FORMOSA(2018)),
            (provincias["JUJUY"]/p_creciente_JUJUY(2018)),
            (provincias["LA PAMPA"]/p_creciente_LAPAMPA(2018)),
            (provincias["LA RIOJA"]/p_creciente_LARIOJA(2018)),
            (provincias["MENDOZA"]/p_creciente_MENDOZA(2018)),
            (provincias["MISIONES"]/p_creciente_MISIONES(2018)),
            (provincias["NEUQUEN"]/p_creciente_NEUQUEN(2018)),
            (provincias["RIO NEGRO"]/p_creciente_RIONEGRO(2018)),
            (provincias["SALTA"]/p_creciente_SALTA(2018)),
            (provincias["SAN JUAN"]/p_creciente_SANJUAN(2018)),
            (provincias["SAN LUIS"]/p_creciente_SANLUIS(2018)),
            (provincias["SANTA CRUZ"]/p_creciente_SANTACRUZ(2018)),
            (provincias["SANTA FE"]/p_creciente_SANTAFE(2018)),
            (provincias["SANTIAGO DEL ESTERO"]/p_creciente_SANTIAGODELESTERO(2018)),
            (provincias["TIERRA DEL FUEGO"]/p_creciente_TIERRADELFUEGO(2018)),
            (provincias["TUCUMAN"]/p_creciente_TUCUMAN(2018)),
           ]

max_2017 = []

for i in xs4:
    max_2017.append(max(ys4_2017))
    
max_2018 = []

for i in xs4:
    max_2018.append(max(ys4_2018))
    
max_2017_num = str( max(ys4_2017))
max_2018_num = str( max(ys4_2018)) 
    
fig, (ax1, ax2) = plt.subplots(2, 1)
plt.subplots_adjust(left=1, bottom=0, right=2.6, top=1.7, wspace=None, hspace=1.2)

ax1.title.set_text("Subsidios acumulados por provincia,\n sobre cantidad total de habitantes\naño 2017\n")
ax1.set_ylabel("Monto  sobre cantidad de habitantes \n\n", fontsize = 10)
plt.style.use("bmh")
plt.grid(zorder=4)
plt.yticks(rotation = 'horizontal')
ax1.set_xticklabels(xs4, rotation=90)
ax1.tick_params(axis='both', labelsize = 10)
ax1.bar(xs4, ys4_2017, color = "darkcyan")
ax1.plot(xs4, max_2017, "r--")
ax1.legend(["$ {}".format(max_2017_num[:8])], bbox_to_anchor=(1.04,1), loc = "upper left")

           
plt.title("Subsidios acumulados por provincia,\n sobre cantidad total de habitantes\naño 2018\n")
plt.ylabel("Monto sobre cantidad de habitantes \n\n", fontsize=10)
plt.style.use("bmh")
plt.grid(zorder=4)
plt.yticks(rotation = 'horizontal')
plt.xticks(rotation = 'vertical')
plt.tick_params(axis='both', labelsize = 10)
ax2.bar(xs4, ys4_2018, color = "darkred")
ax2.plot(xs4, max_2018, "b--")
ax2.legend(["$ {}".format(max_2018_num[:8])], bbox_to_anchor=(1.04,1), loc = "upper left")

plt.show()


# ##### Federico J.V.
