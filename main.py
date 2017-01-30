#Gisselle Primera CI 24219362

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl

#1

df = pd.read_csv('student-por.csv', sep=';')  #Cargamos el archivo student-por.csv en un dataframe

#2

print(df.size)  #Retornamos numero de elementos del dataframe
 
print(df.shape) #Retornamos dimensiones del dataframe 

print(df.head(20)) #Retornamos los primeros 20 elementos del dataframe

print(df.tail(20)) #Retornamos los ultimos 20 elementos del dataframe

print(df.sample(20)) #Retornamos 20 elementos aleatorios del dataframe

print(df.info()) #Retornamos sumario del dataframe
#3

plt.hist(df.age) #Generamos un histograma con la edad de los estudiantes

plt.figure() #Observamos que la mayor cantidad de estudiantes poseen edades entre 16 y 18 años


#4 

pl.scatter(df.absences,df.G3) #Generamos un diagrama de dispersión con el numero de inasistencias y las notas finales del estudiante


#En el diagrama de dispersión podemos observar que mientras menor es el número de inasistencias mayor es la cantidad de estudiantes que poseen notas altas

#5

print(np.sum(df.age)) #Suma de todas las edades de los estudiantes
 
print(np.mean(df.health)) #Promedio de la salud de los estudiantes

print(np.max(df.absences)) #Maximo numero de inasistencias

print(np.prod(df.freetime)) #Producto del tiempo libre indicado por los estudiantes

print(np.min(df.G1)) #Nota mínima en el primer período

print(np.var(df.studytime)) #Varianza del tiempo de estudio semanal de los estudiantes



#6
	
#¿Qué edad tienen los estudiantes con la nota final más alta?

g3= df.G3

g3top=np.max(g3)

res=df[(df.G3 == g3top)]

print(res.age)

	
#Promedio de las notas finales de los estudiantes que tengan mas de 10 inasistencias


res=df.query('absences>10')

g3= res.G3

print(np.mean(g3))


#Edad mínima de los estudiantes cuyo guardián sea su madre y realicen actividades extracurriculares


res=df.query('guardian == "mother" and activities == "yes"')

age1=res.age
print(np.min(age1))



 #Mostramos las graficas

plt.show() 