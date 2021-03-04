# -*- coding: utf-8 -*-
"""
#Spyder Editor

#This is a temporary script file.
"""

import pandas as pd 
import numpy as np 

cartera = pd.read_excel(r"C:\Users\PC\Desktop\Jhoan\Python\prueba.xlsx",sheet_name = "Hoja1", header = 0)
#asignamos df como dataframe de el libro Xls Cartera
df=pd.DataFrame(cartera)
#para poder visualizar todas las columnas
pd.options.display.max_columns = 100
# para que el usuario ingrese su cota de partida 
print("Buen dia ingeniero Evelio")
cota = input("Ingrese cota de inicio de su BM")



# identificar el numero de filas que tenemos con  len

a = len(df.index)
print ("el Numero maximo de columnas en este archivo son",a,sep= "  ")


# debido al inconveniente de usar el metodo .insert en el modulo de pandas
# tome la desicion de asignar valores numericos de V+ para poder darle formato tipo float

tk= df["V(+)"]




df = df.assign(hi = tk.values)

df= df.assign(CotaC= tk.values)

df= df.assign(hin= tk.values)

df= df.assign(CotaN= tk.values)

#df= df.assign(CotaN= tk.values)

df.insert(7,"  ","")

# un limpiado de variable NaN
df = df.fillna(0)

#Convirtiendo a tipo de formato float


#Asigno Un Valor Inicial de Cota
df.at[0,"CotaN"] = cota
df.at[0,"CotaC"] = cota


# continuo con el Ciclo Form par recorrer cada Valor sub i,j
for i in range(1,a):
    # inpongo condicion de modulo de 2 para inciar con los valores posicionales  no pares
    if i % 2 != 0:
       
       print(i)
       if i >=3:
           x = df.iloc[i-2,12]
           k = df.iloc[i-2,10]
       else:
           x = df.iloc[i-1,12]
           k = df.iloc[i-1,10]
       
       y =  df.iloc[i,1]
       l =  df.iloc[i,5]
       z= x+y
       m= k+l
       
       df.iloc[i,11] = z
       df.iloc[i,8] =  m
       
       
       df.iloc[i,12] =   z - df.iloc[i+1,2]
       df.iloc[i,10] =   m - df.iloc[i+1,6]
      #print(k,l,m,  df.iloc[i,10] ,sep ="--") 
      # print(x,y,z,df.iloc[i,12],sep="-----")
#print(df.dtypes)
#print(df)



df2 = df
df2.insert(13,"difn",0)
df2.insert(14,"difc",0)
df2.insert(15,"prom",0)
df2.insert(16,"Correccion",0)
df2.insert(17,"Cota_Final",0)
df2 = df2.assign(Cota_Final = tk.values)

#print("---------------------------------",df2,"-------------------------------","/n")

df3 = df2
w = len(df2.index)
print(w)
#print ("---------------------------------",a,"-------------------------------")
#print(" ")
print(df2.dtypes)
for b in  range(1,w):
    
    #print(w,end ="-")
 
       
    if b == 1:
        h = df3.iloc[b-1 , 12] 
        g = df3.iloc[b,12]
        df3.iloc[b,13] = h-g
        h1 = df3.iloc[b-1 , 10] 
        g1 = df3.iloc[b,10]
        df3.iloc[b,14] = h1-g1
        print(b)
    elif b % 2 != 0 and b != 1:
        if b == w-2:
           print(b)
           h = df2.iloc[b-2,12] 
           g = df2.iloc[b,12] 
           df2.iloc[b,13] = h-g
           h1 = df2.iloc[b-2,10] 
           g1 = df2.iloc[b,10] 
           df2.iloc[b,14] = h1-g1
           break
       
        else:
                h = df2.iloc[b-2,12] 
                g = df2.iloc[b,12] 
                df2.iloc[b,13] = h-g
                h1 = df2.iloc[b-2,10] 
                g1 = df2.iloc[b,10] 
                df3.iloc[b,14] = h1-g1
#print(df2)
#print(len(df2["cota_ajustada"].sum())
#r= len(df2.columns)
print("...............",cota)

for c in range (1,w):
    if c % 2 != 0 :
        n1 = float(df2.iloc[c,13])
        n2 = float(df2.iloc[c,14])     
        df2.iloc[c,15] = (n1+n2)/2
        
        if df2.iloc[c,12] < df2.iloc[c+1,12] and c == 1 :
            t = cota + df2.iloc[c,15]
            print(t)
            df2.iloc[c,16] = t
        
        elif df2.iloc[c,12]< df2.iloc[c+1,12] and c != 1:
            df2.iloc[c,16] = df2.iloc[c-1,16]+ df2.iloc[c,15]
        else: 
            df2.iloc[c,16] = df2.iloc[c-1,16]- df2.iloc[c,15]

for d in range (1,w):
    
    if d == 1 :
        #ini = df2.iloc[d,16] 
        df2.iloc[d,17] = float(cota) - df2.iloc[d,16]
    elif  d % 2 != 0  and d != 1:
          cont = df2.iloc[d-2,17] 
          df2.iloc[d,17] = cont - df2.iloc[d,16]
        
        
    
        

print(df2)
#print(df2)
#print(df.dtypes)
    
df2= df2 [["PUNTO","V(+)","V(-)","DISTANCIA (+)","hin","CotaN","difn","PUNTO C","V(+) C","V(-) C","DISTANCIA (-) C","CotaC","difc","prom","Correccion","Cota_Final"]]
#print(df2)

df2 = df2.fillna(" ")
df2 = df2.replace(0,"")
print(df2)


df2.to_excel(r"C:\Users\PC\Desktop\Jhoan\Python\reporte.xlsx",index=False)

