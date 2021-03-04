from tkinter import *						
#import tkinter as tk	
from PIL import ImageTk,Image			#para manipular imagenes
from tkinter import messagebox as mb	#Nos permite abrir ventanas de mensajes
import sqlite3							#Nos permite conectarnos a una base de datos (sqlite3)

def borrar_ventana() :
    ventana.destroy()
    
ventana=Tk()
ventana.title("Programa de Calculo Carteras")	#Titulo de la ventana principal
ventana.geometry("350x250+300+250")	#Tamaño de nuestra ventana Principal
	
color='#c5e2f6'			#Codigo HEX del color de fondo usado
ventana['bg']=color		#Definimos nuestra ventana 'bg' con el valor 'color'

Label(ventana,bg=color,text="Login",font=("Arial Black",16)).pack()	#Mostramos texto 'Login'

#Cajas de nuestra ventana Principal
Label(ventana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Usuario:'
caja1=Entry(ventana,font=("Arial",10))										#Creamos una caja de texto 'caja1'
caja1.pack()																#Posicion de la 'caja1'
Label(ventana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Contraseña:'
caja2=Entry(ventana,show="*")												#Creamos la 'caja2' (contraseña)
caja2.pack()																#Posicion de 'caja2'

db=sqlite3.connect('login.db')		#Nos conectamos a nuestra base de datos 'login.db'
c=db.cursor()						#Establecemos un cursor

def login():				#Funcion login ... Nos permitira comprobar 'usuario' y 'contraseña' con la base de datos
	usuario=caja1.get()		#Obtenemos el valor de la 'caja1' (usuario)
	contr=caja2.get()		#Obtenemos el valor de la 'caja2' (contraseña)
	c.execute('SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?',(usuario,contr))	#Seleccionamos datos '(usuario,contr)'
	if c.fetchall():
		mb.showinfo(title="Login Correcto",message="Usuario y contraseña correctos")		#Mostramos 'Login Correcto'
        
	else:
		mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")	#Mostramos 'Login incorrecto'
	#c.close()

def nuevaVentana():							#Funcion nuevaVentana ... Nos permitira el registro de nuevos usuarios
	newVentana=tk.Toplevel(ventana)			#Definimos 'newVentana'
	newVentana.title("Registro de Usuario")	#Le damos el titulo 'Registro de Usuario'
	newVentana.geometry("300x290+800+250")	#Tamaño de la ventana
	newVentana['bg']=color					#Definimos newVentana 'bg' con el valor de 'color'
	
	labelExample=tk.Label(newVentana,text="Registro : ",bg=color,font=("Arial Black",12)).pack(side="top")	#Texto 'Registro'
	#panel_reg=tk.Label(newVentana,image=photo_reg).pack(side="left")	#Mostramos la imagen en la posicion 'left' (Izquierda)

	Label(newVentana,text="Nombre : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Nombre:'
	caja3=Entry(newVentana)															#Creamos 'caja3' (Nombre)
	caja3.pack()
	Label(newVentana,text="Apellidos : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Apellidos'
	caja4=Entry(newVentana)															#Creamos 'caja4' (Apellidos)
	caja4.pack()
	Label(newVentana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Usuario'
	caja5=Entry(newVentana)															#Creamos 'caja5' (Usuario)
	caja5.pack()
	Label(newVentana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Contraseña'
	caja6=Entry(newVentana,show="*")												#Creamos 'caja6' (Contraseña)
	caja6.pack()	
	Label(newVentana,text="Repita la Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Repita la Contraseña'
	caja7=Entry(newVentana,show="*")															#Creamos 'caja7' 
	caja7.pack()
	def registro():				#Funcion registro ... Nos permitira escribir los datos a nuestra base de datos
		Nombre=caja3.get()		#Obtenemos el valor de 'caja3'
		Apellido=caja4.get()	#Obtenemos el valor de 'caja4'
		Usr_reg=caja5.get()		#Obtenemos el valor de 'caja5'
		Contra_reg=caja6.get()	#Obtenemos el valor de 'caja6'
		Contra_reg_2=caja7.get() #Obtenemos el valor de 'caja7'
		if(Contra_reg==Contra_reg_2):		#Esta condicion nos permite saber si las contraseñas coinciden
			#El siguiente comando es el encargado de insertar los datos obtenidos en el registro
			c.execute("INSERT INTO usuarios values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
			db.commit()			#Confirmamos los datos
			mb.showinfo(title="Registro Correcto",message="Hola "+Nombre+" "+Apellido+" ¡¡ \nSu registro fue exitoso.")
			newVentana.destroy()		#Cerramos la ventana de registro
		else:	#Se ejecutara si las contraseñas no coinciden
			mb.showerror(title="Contraseña Incorrecta",message="Error¡¡¡ \nLas contraseñas no coinciden.")	#Mostramos un mensaje
		#c.close()		#Nos permite cerrar el cursor ...
		#db.close()
	#El siguiente comando (boton) nos permite llamar ala funcion registro
	buttons=tk.Button(newVentana,text="Registrar ¡",command=registro,bg=color,font=("Arial Rounded MT Bold",10)).pack(side="bottom")
	
Label(ventana,text=" ",bg=color,font=("Arial",10)).pack()		#Solo es una linea vacia ... (lo use para separar el boton) 
Button(text=" ENTRAR ",command=login,bg='#a6d4f2',font=("Arial Rounded MT Bold",10)).pack()		#Boton ==> funcion 'login'
Label(ventana,text=" ",bg=color,font=("Arial Black",10)).pack()
Label(ventana,text="No tienes una cuenta ? : ",bg=color,font=("Arial Black",10)).pack()		#Simple texto
#La siguiente linea (boton) nos llama ala funcion 'nuevaVentana' ==> ( ventana de registro)
boton1=Button(ventana,text="REGISTRO",bg='#a6d4f2',command=nuevaVentana,font=("Arial Rounded MT Bold",10)).pack()

ventana.mainloop()

# Imprimimos el menú en pantalla
print("""Seleccione una de las siguientes opciones
    1) Nivelación       2) Poligonal
    """)
# Leemos lo que ingresa el usuario
eligio=input("-que deseas calcular :")

# Según lo que ingresó, código diferenteif eligio=="1":
    #print ("Listamos otras herramientas")
if  eligio == "1":
    print("Eligio Nivelación")
    print("""Seleccione uno de los siguientes ajustes
    a) Calculo por distancias       b) Calculo por número de cambios
    """)
    CalNiv=input("¿por cual método desea calcular?")
    if CalNiv == "a":
        print("Eligio calculo por distancias")
        #nivelacion simple ajuste por distancias
        import math
        print()
        print('='*173)
        print()
        print('{:^173}'.format('A J U S T E  D E  N I V E L A C I Ó N   P O R  D I S T A N C I A S'))
        print()
        print('='*173)
        print()
        BMS = int(input('Digite el número de BMS de la nivelación: '))
        precisión = int(input('¿precisión del equipo [1 = 1mm] [0 = 2mm]: '))

        #[AL DEFINIR PRECISIÓN CALCULA ERROR TEORICO PERMISIBLE DE LA NIVELACIÓN]
        if precisión == 1:
            error_permitido = (BMS * 1)
        else:
            error_permitido = (BMS * 2)
        #[IMPRIME EL ERROR PERMITIDO DE ACUERDO CON LA PRECISIÓN DEL EQUIPO]
        print(f'el error permitido de acuerdo con precisión del equipo es: {error_permitido}mm')
        #[SOLICITA LA COTA DEL BM DE PARTIDA]
        BM = float(input('Digite la cota del BM de inicio: '))
        #VMAS_inicio = float(input('Digite la vista mas: '))
            
        #[IMPRIME LA HI DE REFERENCIA]
        #hi_ref = (BM + VMAS_inicio)
        #print('\n', f'La ALTURA INSTRUMENTAL calculada es: {hi_ref}')
        #[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
        datos_medidos = []
        j = 0
        sumVMAS = 0.0
        sumVMENOS = 0.0
        sumdist_menos = 0.0
        sumdist_mas = 0.0

        #[SOLICITA LOS DATOS DE CADA BM, NOMBRE, VISTA +, VISTA - Y DISTANCIA]
        # CON NUMERO DE BM´S Y DIST OBSERVADOS REALIZA LA SUMA DE ANGULOS
        # CALCULA EL ERROR EN COTA Y LA CORRECCION 
        # IMPRIME EL ERROR EN COTA
        # IMPRIME LA CORRECCION EN COTA
            
        for i in (range(BMS)):
            print('='*80)
            i=i+1
            punto = input(f'Digite el nombre del punto {i}: ')
            vistaMas = float(input(f'Digite la vista más observada {i}: '))
            distancia_mas = float(input(f'Digite la distancia más observada {i}: '))
            vistaMenos = float(input(f'Digite la vista menos observada {i}: '))
            distancia_menos = float(input(f'Digite la distacia menos observada {i}: '))
        

            print('='*80)

            datos_linea = [punto, vistaMas, distancia_mas, vistaMenos, distancia_menos]
            datos_medidos.append(datos_linea.copy())
            sumVMAS = sumVMAS + vistaMas
            sumVMENOS = sumVMENOS + vistaMenos
            sumdist_menos = sumdist_menos + distancia_menos
            sumdist_mas = sumdist_mas + distancia_mas
        '''
        datos_linea = ['BM1', 1.50, 15, 2, 10 ]
        datos_medidos.append(datos_linea.copy())
        datos_linea = ['BM2', 1.99, 15, 1.50, 10 ]
        datos_medidos.append(datos_linea.copy())
        sumVMAS=3.49
        sumVMENOS=3.50
        sumdist_mas=30
        sumdist_menos=20
        '''
        error = round(sumVMAS -  sumVMENOS,8)

        print(f'Error de cierre es: {error}')
        sumatoria_total_distancia = sumdist_menos + sumdist_mas
        print(f'Distancia Total es: {sumatoria_total_distancia}')
        correccion = round(error / sumatoria_total_distancia,6)
        print(f'Corrección es: {correccion}')

        contador = 0
        ##calculamos ajuste vista +
        for dato in  datos_medidos:
            calculado = correccion * dato[2]
            datos_medidos[contador].append(calculado)
            contador=contador+1;
        contador = 0
        ##calculamos ajuste vista -
        for dato in  datos_medidos:
            calculado = correccion * dato[4]
            datos_medidos[contador].append(calculado)
            contador=contador+1;

        contador = 0
        ##calculamos v+ corregida
        for dato in  datos_medidos:
            calculado = dato[1] - dato[5]
            datos_medidos[contador].append(calculado)
            contador=contador+1;
        contador = 0
        ##calculamos v- corregida
        for dato in  datos_medidos:
            calculado = dato[3] + dato[6]
            datos_medidos[contador].append(calculado)
            contador=contador+1;


        calculado = BM + datos_medidos[0][7]
        datos_medidos[0].append(calculado)
        datos_medidos[0].append(BM)
        contador = 1
        ##calculamos altura instrumental
        for dato in  datos_medidos:
            if contador == BMS:
                continue
            cota_temporal = calculado - datos_medidos[contador-1][8]
            hi_temporal     = cota_temporal + datos_medidos[contador][7]
            
            datos_medidos[contador].append(hi_temporal)
            datos_medidos[contador].append(cota_temporal)
            contador=contador+1;
            
        ##Comprobación del cierre
        comprobacion =math.ceil((datos_medidos[BMS-1][10] +  datos_medidos[BMS-1][7] ) - datos_medidos[BMS-1][8]) 
        
        if comprobacion == BM:
            print(f'La comprobación  esta correcta por que: {comprobacion} es igual {BM}')

        contador = 0
        ##imprimir 

        print('='*173)
        print('{:^10}'.format('PUNTO'), '{:^8}'.format('Vista+'), '{:^8}'.format('Distancia+'), '{:^10}'.format('Vista-'), '{:^10}'.format('Distancia-'), '{:^10}'.format('AjusteVista+'), '{:^10}'.format('AjusteVista-'), '{:^10}'.format('Vista+Corregida'), '{:^10}'.format('Vista-Corregida'), '{:^11}'.format('AlturaInstrumental'), '{:^11}'.format('Cota'), sep='\t')

        for dato in datos_medidos:

                print('{:^10}'.format(dato[0]),'{:8.4f}'.format(dato[1]), '{:8.4f}'.format(dato[2]),'{:10}'.format(dato[3]), '{:10}'.format(dato[4]), '{:10}'.format(dato[5]), '{:+010.3f}'.format(dato[6]), '{:+010.3f}'.format(dato[7]), '{:+010.3f}'.format(dato[8]), '{:+010.3f}'.format(dato[9]), '{:11.3f}'.format(dato[10]), sep='\t')


        print('='*173)
   
    elif CalNiv == "b":
        print("Eligio calculo por número de cambios")
        #nivelacion simple ajuste por número de cambios
        import math
        print()
        print('='*173)
        print()
        print('{:^173}'.format('A J U S T E  D E  N I V E L A C I Ó N   P O R  C A M B I O S'))
        print()
        print('='*173)
        print()
        BMS = int(input('Digite el número de BMS de la nivelación: '))
        precisión = int(input('¿precisión del equipo [1 = 1mm] [0 = 2mm]: '))

        #[AL DEFINIR PRECISIÓN CALCULA ERROR TEORICO PERMISIBLE DE LA NIVELACIÓN]
        if precisión == 1:
            error_permitido = (BMS * 1)
        else:
            error_permitido = (BMS * 2)
        #[IMPRIME EL ERROR PERMITIDO DE ACUERDO CON LA PRECISIÓN DEL EQUIPO]
        print(f'el error permitido de acuerdo con precisión del equipo es: {error_permitido}mm')
        #[SOLICITA LA COTA DEL BM DE PARTIDA]
        BM = float(input('Digite la cota del BM de inicio: '))
        #VMAS_inicio = float(input('Digite la vista mas: '))
            
        #[IMPRIME LA HI DE REFERENCIA]
        #hi_ref = (BM + VMAS_inicio)
        #print('\n', f'La ALTURA INSTRUMENTAL calculada es: {hi_ref}')
        #[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
        datos_medidos = []
        j = 0
        sumVMAS = 0.0
        sumVMENOS = 0.0
        sumdist_menos = 0.0
        sumdist_mas = 0.0

        #[SOLICITA LOS DATOS DE CADA BM, NOMBRE, VISTA +, VISTA - Y DISTANCIA]
        # CON NUMERO DE BM´S Y DIST OBSERVADOS REALIZA LA SUMA DE ANGULOS
        # CALCULA EL ERROR EN COTA Y LA CORRECCION 
        # IMPRIME EL ERROR EN COTA
        # IMPRIME LA CORRECCION EN COTA
            
        for i in (range(BMS)):
            print('='*80)
            i=i+1
            punto = input(f'Digite el nombre del punto {i}: ')
            vistaMas = float(input(f'Digite la vista más observada {i}: '))
            
            vistaMenos = float(input(f'Digite la vista menos observada {i}: '))
            
        

            print('='*80)

            datos_linea = [punto, vistaMas, vistaMenos]
            datos_medidos.append(datos_linea.copy()) 
            sumVMAS = sumVMAS + vistaMas
            sumVMENOS = sumVMENOS + vistaMenos
            
        '''
        datos_linea = ['BM1', 1.50, 15, 2, 10 ]
        datos_medidos.append(datos_linea.copy())
        datos_linea = ['BM2', 1.99, 15, 1.50, 10 ]
        datos_medidos.append(datos_linea.copy())
        sumVMAS=3.49
        sumVMENOS=3.50
        sumdist_mas=30
        sumdist_menos=20
        '''
        error = round(sumVMAS -  sumVMENOS,3)

        print(f'Error de cierre es: {error}')


        correccion = round(error / BMS,3)
        print(f'Corrección es: {correccion}')

        contador = 0
        ##calculamos ajuste vista +
        for dato in  datos_medidos:
            calculado = correccion * dato[1]
            datos_medidos[contador].append(calculado)
            contador=contador+1;
        contador = 0
        ##calculamos ajuste vista -
        for dato in  datos_medidos:
            calculado = correccion * dato[2]
            datos_medidos[contador].append(calculado)
            contador=contador+1;

        contador = 0
        ##calculamos v+ corregida
        for dato in  datos_medidos:
            calculado = dato[1] - dato[3]
            datos_medidos[contador].append(calculado)
            contador=contador+1;
        contador = 0
        ##calculamos v- corregida
        for dato in  datos_medidos:
            calculado = dato[2] + dato[4]
            datos_medidos[contador].append(calculado)
            contador=contador+1;


        calculado = BM + datos_medidos[0][5]
        datos_medidos[0].append(calculado)
        datos_medidos[0].append(BM)
        contador = 1
        ##calculamos altura instrumental
        for dato in  datos_medidos:
            if contador == BMS:
                continue
            cota_temporal = calculado - datos_medidos[contador-1][6]
            hi_temporal     = cota_temporal + datos_medidos[contador][5]
            
            datos_medidos[contador].append(hi_temporal)
            datos_medidos[contador].append(cota_temporal)
            contador=contador+1;
            
        ##Comprobación del cierre
        #comprobacion =math.ceil((datos_medidos[BMS-1][10] +  datos_medidos[BMS-1][5] ) - datos_medidos[BMS-1][6]) 
        
        #if comprobacion == BM:
        #    print(f'La comprobación  esta correcta por que: {comprobacion} es igual {BM}')

        contador = 0
        ##imprimir 

        print('='*173)
        print('{:^10}'.format('PUNTO'), '{:^8}'.format('Vista+'), '{:^8}'.format('Vista-'), '{:^10}'.format('AjusteVista+'), '{:^10}'.format('AjusteVista-'), '{:^10}'.format('Vista+Corregida'), '{:^10}'.format('Vista-Corregida'), '{:^10}'.format('AlturaInstrumental'), '{:^10}'.format('Cota'), sep='\t')

        for dato in datos_medidos:

                print('{:^10}'.format(dato[0]),'{:8.4f}'.format(dato[1]), '{:8.4f}'.format(dato[2]),'{:10}'.format(dato[3]), '{:10}'.format(dato[4]), '{:10}'.format(dato[5]), '{:+010.3f}'.format(dato[6]), '{:+010.3f}'.format(dato[7]), '{:+010.3f}'.format(dato[8]), sep='\t')


        print('='*173)
    else:
        print("Opción no válida")
elif eligio == "2":
    print("Eligio poligonal")
    print("""Indique si la poligonal es Abierta o cerrada
    1) Abierta       2) Cerrada
    """)
    poligonal=input()
    if poligonal == "1":
        print("Eligio poligonal abierta")
        print("""se le sugiere calcular por el método Crandall""") 
        print("""Indique por cual método desea calcular
    1) Crandall     2) Brújula      3) Tránsito
    """)
        poligonal=input()
        if poligonal == "1":
            print("Eligio ajuste por método Crandall")
            #[A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  C R A N D A L L]
            import math
            import time as t
            import datetime
            #import numpy as np
            #file='coor.txt'
            #data=np.loadtxt(file,delimiter='\t',skiprows=0,usecols=[0,1])
            #print(data)

            tiempo_local = t.asctime(t.localtime(t.time()))
            print("Fecha y hora de creacion del archivo: ",tiempo_local)

            def gms2dec(angulo):
                grados = int(angulo)
                auxiliar = (angulo - grados) * 100
                minutos = int(auxiliar)
                segundos = (auxiliar - minutos)*100

                angulo_dec = grados + minutos / 60 + segundos / 3600

                return angulo_dec

            #[ESTE BLOQUE CALCULA EL ACIMUT INICIAL y FINAL]

            def acimut_linea(x1, y1, x2, y2):
                dx = x2 - x1
                dy = y2 - y1

                if dy != 0:
                    rumbo = math.degrees(math.atan(dx/dy))

                    if dx > 0 and dy > 0:
                        acimut = rumbo
                    elif dx > 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy > 0:
                        acimut = 360 + rumbo
                    elif dx == 0 and dy > 0:
                        acimut = 0
                    elif dx == 0 and dy > 0:
                        acimut = 180
                else:
                    if dx > 0:
                        acimut = 90
                    elif dx < 0:
                        acimut = 270
                    else:
                        acimut = -1
                
                return acimut

            #[ESTE BLOQUE CONVIERTE EL ANGULO INGRESADO DE GRADOS DECIMALES A GGMMSS]
            def dec2gms(angulo_dec):
                grados = int(angulo_dec)
                auxiliar = (angulo_dec - grados)*60
                minutos = int(auxiliar)
                segundos = round((auxiliar - minutos)*60,0)

                angulo_gms = '{:03d}'.format(grados) + '° ' + '{:02d}'.format(minutos) + "' " + '{:04.1f}'.format(segundos) + '"'

                return angulo_gms

            #[CALCULA EL CONTRA ACIMUT Y RUMBO]
            def acimut_poligonal(acimut_anterior, angulo_observ):
                if acimut_anterior >= 180:
                    contra_acimut = acimut_anterior - 180
                else:
                    contra_acimut = acimut_anterior + 180
                
                acimut = contra_acimut + angulo_observ

                if acimut >= 360:
                    acimut = acimut - 360
                
                return acimut

            #[CALCULA LAS PROYECCIONES]
            def proyecciones(acimut, distancia):
                
                acimut = math.radians(acimut)

                valor_proyecciones = []
                valor_proyecciones.append(math.sin(acimut)*distancia)
                valor_proyecciones.append(math.cos(acimut)*distancia)

                return valor_proyecciones

            #[SOLICTA NUMERO DE DELTAS Y QUE SE INDIQUE SI LOS ANGULOS SON INTERNOS Y EXTERNOS]
            def main():

                print()
                print('='*150)
                print()
                print('{:^150}'.format('A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  C R A N D A L L'))
                print()
                print('='*150)
                print()
                print('{:^150}'.format("INGENIERÍA DE SOFTWARE\n"))
                print('{:^150}'.format("PROFESOR: Evelio Luis Madera Arteaga\n"))
                print('{:^150}'.format("Wilmer Franco Hernandez         COD: 20201732014\n"))
                print('{:^150}'.format("Juliana Manuela Pachón Florián  COD: 20192732006\n"))
                print('{:^150}'.format("Jean Pierre Riaño Melo          COD: 20192732030\n"))
                print('{:^150}'.format("Julian Camilo Lopez Alcala      COD: 20192732024\n"))
                print()

                deltas = int(input('Digite el numero de deltas en la poligonal: '))
                '''ang_externos = int(input('¿Angulos externos [1 = SI] [0 = NO]: '))

                #[AL DEFINIR ANGULOS INTERNOS Y EXTERNOS CALCULA SUMATORIA TEORICA DE ANGULO]
                if ang_externos == 1:
                    suma_teorica_ang = (deltas + 2) *180
                else:
                    suma_teorica_ang = (deltas - 2) *180'''

                #[SOLICITA LAS COORDENADAS DEL PUNTO DE ARMADA Y DEL PUNTO DE REFERENCIA INICIAL]
                x_inicio = float(input('Digite la coordenada X (E) del punto de inicio: '))
                y_inicio = float(input('Digite la coordenada Y (N) del punto de inicio: '))
                x_referencia = float(input('Digite la coordena X (E) del punto de referencia: '))
                y_referencia = float(input('Digite la coordena Y (N) del punto de referencia: ') + "\n")

                
                #[SOLICITA LAS COORDENADAS DEL PUNTO DE ARMADA Y DEL PUNTO DE REFERENCIA FINAL]
                x_final = float(input('Digite la coordenada X (E) del punto de final: '))
                y_final = float(input('Digite la coordenada Y (N) del punto de final: '))
                x_reffinal = float(input('Digite la coordena X (E) del punto de reffinal: '))
                y_reffinal = float(input('Digite la coordena Y (N) del punto de reffinal: ') + "\n")

                #[IMPRIME EL ACIMUT DE REFERENCIA INICIAL]
                acimut_refini = acimut_linea(x_inicio, y_inicio, x_referencia, y_referencia)
                print('\n', f'El acimut calculado inicial es: {dec2gms(acimut_refini)}' + "\n")
                #[IMPRIME EL ACIMUT DE REFERENCIA FINAL]
                acimut_reffin = acimut_linea(x_final, y_final, x_reffinal, y_reffinal)
                print('\n', f'El acimut téorico de llegada es: {dec2gms(acimut_reffin)}' + "\n")
                
                #[IMPRIME LA SUMATORIA TEORICA DE ANGULOS]
                '''print(f'La sumatoria teórica de ángulos es: {suma_teorica_ang}°')'''

                #[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
                datos_medidos = []
                datos_medidos.append (['DELTA','AZIMUTH', 'DIST', 'AZIMUTH DEC', 'AZIMUTH CORREG', 'PRY X', 'PRY Y', 'PRY X COREG', 'PRY Y COREG', 'COORD X', 'COORD Y'])

                j = 0
                sumang = 0.0
                sumdist = 0.0

                #[SOLICITA LOS DATOS DE CADA DELTA, NOMBRE, ANGULO Y DISTANCIA]
                # CON NUMERO DE DELTAS Y ANGULOS OBSERVADOS REALIZA LA SUMA DE ANGULOS
                # CALCULA EL ERROR ANGULAR Y LA CORRECCION ANGULAR
                # IMPRIME EL ERROR ANGULAR
                # IMPRIME LA CORRECCION ANGULAR
                
                for delta in (range(deltas)):
                    print('='*160)

                    nombre_delta = input(f'Digite el nombre del delta {delta+1}: ')
                    az_observado = float(input(f'Digite el azimuth observado {delta+1}: '))
                    distancia = float(input(f'Digite la distancia de la linea {delta+1}: '))

                    print('='*160)

                    datos_linea = [nombre_delta, az_observado, distancia, gms2dec(az_observado)]
                    datos_medidos.append(datos_linea.copy())

                    if j != -1:
                        sumdist = sumdist + distancia
                        azlinfin = datos_linea[3]
                        j += 1
                    else:
                        j += 1

                    print('sumatoria de distancias')
                    print(sumdist)
                
                error_angular = acimut_reffin - azlinfin
                correccion_angular = error_angular / deltas

                print('correccion angular')
                print()
                
                print('El error angular es:', dec2gms(error_angular))
                print('La corrección angular es:', dec2gms(correccion_angular))

                datos_medidos[1].append(datos_medidos[1][3])
                datos_medidos[1].append(acimut_refini + datos_medidos[1][3])

                print(datos_medidos)

                #[VARIABLES DE SUMA DE PROYECCIONES]
                i = 0
                suma_px = 0.0
                suma_py = 0.0
                proyec_punto = []

                
                
                #[CALCULA CORRECCIONES A ANGULO, ACIMUT Y PROYECCIONES ]
                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue
                    
                    datos_medidos[i].append(datos_medidos[i][3] + correccion_angular)
                    print ('datos_medidos')
                    print(datos_medidos)

                    if datos_medidos[i-1][4] >= 180:
                        acimut_deltas = datos_medidos[i-1][4] #- 180 + datos_medidos[i][4]'''
                    else:
                        acimut_deltas = datos_medidos[i-1][4] #+ 180 + datos_medidos[i][4]'''
                    
                    if acimut_deltas >= 360:
                        acimut_deltas -= 360

                    datos_medidos[i].append(acimut_deltas)

                    proyec_punto = proyecciones(acimut_deltas, datos_medidos[i][2])

                    datos_medidos[i].append(proyec_punto[0])
                    datos_medidos[i].append(proyec_punto[1])

                    suma_px += datos_medidos[i][5]
                    suma_py += datos_medidos[i][6]

                    i += 1

                print()

                datos_medidos [1][:] += [0, 0, 0, 0, x_inicio, y_inicio]

                #[ALMACENA LAS PROYECCIONES CORREGIDAS EN LA LISTA]
                i = 0

                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue

                    #[CALCULA EL ERROR DE LAS PROYECCIONES]
                    datos_medidos[i].append(datos_medidos[i][5] - (suma_px / sumdist)*datos_medidos[i][2])
                    datos_medidos[i].append(datos_medidos[i][6] - (suma_py / sumdist)*datos_medidos[i][2])

                    #[CALCULA COORDENADAS]
                    datos_medidos[i].append(datos_medidos[i-1][9] + datos_medidos[i][7])
                    datos_medidos[i].append(datos_medidos[i-1][10] + datos_medidos[i][8])

                    i += 1

                #[IMPRIME DATOS CALCULADOS]
                print()
                print('{:^150}'.format("DATOS FINALES\n"))
                print('='*160)
                print('{:^6}'.format('DELTA'),'{:^8}'.format('AZIMUTH'),'{:^8}'.format('DISTANC'),'{:^10}'.format('AZIMUTH'),'{:^10}'.format('PROYECC'),'{:^10}'.format('PROYECC'),'{:^10}'.format('PROYECC'),'{:^10}'.format('PROYECC'),'{:^11}'.format('COORDEN'),'{:^11}'.format('COORDEN'), sep='\t')

                print('{:^6}'.format(''),'{:^8}'.format('OBSERV'),'{:^8}'.format('(m)'),'{:^10}'.format('CORREGIDO'),'{:^10}'.format('X'),'{:^10}'.format('Y'),'{:^10}'.format('CORR X'),'{:^10}'.format('CORR Y'),'{:^11}'.format('X'),'{:^11}'.format('Y'), sep='\t')
                print('='*160)

                i = 0

                for dato in datos_medidos:
                    if i == 0:
                        i += 1
                        continue

                    print('{:^6}'.format(dato[0]),'{:8.4f}'.format(dato[1]),'{:8.4f}'.format(dato[2]),'{:10}'.format(dec2gms(dato[4])),'{:+010.3f}'.format(dato[6]),'{:+010.3f}'.format(dato[7]),'{:+010.3f}'.format(dato[8]),'{:+010.3f}'.format(dato[9]),'{:11.3f}'.format(dato[10]),'{:11.3f}'.format(dato[11]), sep='\t')

                    i += 1

                print('='*160)
                

            if __name__ == '__main__':
                main()

            archivo=open("Datos_Poligonal.txt","w")
            archivo.write("**CALCULO Y AJUSTE DE UNA POLIGONAL ABIERTA POR METODO CRANDALL**\n")
            archivo.write(str("Fecha y hora de creacion del archivo: ") )
            archivo.write(str(tiempo_local) + "\n")
            archivo.write("INGENIERÍA DE SOFTWARE\n")
            archivo.write("PROFESOR: Evelio Luis Madera Arteaga\n")
            archivo.write("Wilmer Franco Hernandez         COD: 20201732014\n")
            archivo.write("Juliana Manuela Pachón Florián  COD: 20192732006\n")
            archivo.write("Jean Pierre Riaño Melo          COD: 20192732030\n")
            archivo.write("Julian Camilo Lopez Alcala      COD: 20192732024\n")
            archivo.write(" \n")
            archivo.write('{:^150}'.format("DATOS FINALES\n"))
            archivo.write(" \n")
            archivo.write('='*160)
            archivo.write(" \n")
            archivo.write('{:^6}'.format('DELTA')),archivo.write('{:^8}'.format('AZIMUTH')),archivo.write('{:^8}'.format('DISTANC')),archivo.write('{:^10}'.format('AZIMUTH')),archivo.write('{:^10}'.format('PROYECC')),archivo.write('{:^10}'.format('PROYECC')),archivo.write('{:^10}'.format('PROYECC')),archivo.write('{:^10}'.format('PROYECC')),archivo.write('{:^11}'.format('COORDEN')),archivo.write('{:^11}'.format('COORDEN'))
            archivo.write(" \n")
            archivo.write('{:^6}'.format('')),archivo.write('{:^8}'.format('OBSERV')),archivo.write('{:^8}'.format('(m)')),archivo.write('{:^10}'.format('CORREGIDO')),archivo.write('{:^10}'.format('X')),archivo.write('{:^10}'.format('Y')),archivo.write('{:^10}'.format('CORR X')),archivo.write('{:^10}'.format('CORR Y')),archivo.write('{:^11}'.format('X')),archivo.write('{:^11}'.format('Y'))
            archivo.write(" \n")
            archivo.write(" \n")
            archivo.write('='*160)
            archivo.write(" \n")
            archivo.write('='*160)
            '''archivo.write("LONG_POLIGONAL=  % s\n"%sumdist)
            archivo.write('{:^6}'.format(dato[0])),archivo.write('{:8.4f}'.format(dato[1])),archivo.write('{:8.4f}'.format(dato[2])),archivo.write('{:10}'.format(dec2gms(dato[4]))),archivo.write('{:+010.3f}'.format(dato[6])),archivo.write('{:+010.3f}'.format(dato[7])),archivo.write('{:+010.3f}'.format(dato[8])),archivo.write('{:+010.3f}'.format(dato[9])),archivo.write('{:11.3f}'.format(dato[10])),archivo.write('{:11.3f}'.format(dato[11]))
            archivo.write('{:^6}'.format('DELTA'), '{:^8}'.format('AZIMUTH'), '{:^8}'.format('DISTANC'), '{:^10}'.format('AZIMUTH'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^11}'.format('COORDEN'), '{:^11}'.format('COORDEN'), sep='\t')
            archivo.write('{:^6}'.format(''), '{:^8}'.format('OBSERV'),'{:^8}'.format('(m)'),'{:^10}'.format('CORREGIDO'),'{:^10}'.format('X'), '{:^10}'.format('Y'), '{:^10}'.format('CORR X'), '{:^10}'.format('CORR Y'), '{:^11}'.format('X'), '{:^11}'.format('Y'), sep='\t')
            archivo.write('{:^6}'.format(dato[0]), '{:8.4f}'.format(dato[1]), '{:8.4f}'.format(dato[2]), '{:10}'.format(dec2gms(dato[4])), '{:+010.3f}'.format(dato[6]), '{:+010.3f}'.format(dato[7]), '{:+010.3f}'.format(dato[8]), '{:+010.3f}'.format(dato[9]), '{:11.3f}'.format(dato[10]), '{:11.3f}'.format(dato[11]), sep='\t')
            archivo.write(" \n")
            archivo.write("ERROR_TOTAL=  % s\n"%ed )
            archivo.write(" \n")
            archivo.write("PRESICION= 1:%s\n"%prec)
            archivo.write(" \n")
            archivo.write("id,angulo,distancia,acimut,proy_N-S, proy_E-W,proy_Correg_N-S,proy_Correg_E-W,Norte, Este\n")
            archivo.write("%s"%observaciones)
            archivo.write(" \n")
            archivo.write("*****COORDENADAS FINALES*****\n")
            archivo.write("id,    Norte,    Este\n")
            archivo.write("%s\n"%coordenadas)'''
            archivo.close()
        elif poligonal == "2":
            print("Eligio ajuste por método Brújula")
			#[A J U S T E  D E  P O L I G O N A L  P O R  E L  M É T O D O  D E  L A  B R Ú J U L A]


            import math

            def gms2dec(angulo):
                grados = int(angulo)
                auxiliar = (angulo - grados) * 100
                minutos = int(auxiliar)
                segundos = (auxiliar - minutos)*100

                angulo_dec = grados + minutos / 60 + segundos / 3600

                return angulo_dec

            #[ESTE BLOQUE CALCULA EL ACIMUT INICIAL]

            def acimut_linea(x1, y1, x2, y2):
                dx = x2 - x1
                dy = y2 - y1

                if dy != 0:
                    rumbo = math.degrees(math.atan(dx/dy))

                    if dx > 0 and dy > 0:
                        acimut = rumbo
                    elif dx > 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy > 0:
                        acimut = 360 + rumbo
                    elif dx == 0 and dy > 0:
                        acimut = 0
                    elif dx == 0 and dy > 0:
                        acimut = 180
                else:
                    if dx > 0:
                        acimut = 90
                    elif dx < 0:
                        acimut = 270
                    else:
                        acimut = -1
                
                return acimut

            #[ESTE BLOQUE CONVIERTE EL ANGULO INGRESADO DE GRADOS DECIMALES A GGMMSS]
            def dec2gms(angulo_dec):
                grados = int(angulo_dec)
                auxiliar = (angulo_dec - grados)*60
                minutos = int(auxiliar)
                segundos = round((auxiliar - minutos)*60,0)

                angulo_gms = '{:03d}'.format(grados) + '° ' + '{:02d}'.format(minutos) + "' " + '{:04.1f}'.format(segundos) + '"'

                return angulo_gms

            #[CALCULA EL CONTRA ACIMUT Y RUMBO]
            def acimut_poligonal(acimut_anterior, angulo_observ):
                if acimut_anterior >= 180:
                    contra_acimut = acimut_anterior - 180
                else:
                    contra_acimut = acimut_anterior + 180
                
                acimut = contra_acimut + angulo_observ

                if acimut >= 360:
                    acimut = acimut - 360
                
                return acimut

            #[CALCULA LAS PROYECCIONES]
            def proyecciones(acimut, distancia):
                
                acimut = math.radians(acimut)

                valor_proyecciones = []
                valor_proyecciones.append(math.sin(acimut)*distancia)
                valor_proyecciones.append(math.cos(acimut)*distancia)

                return valor_proyecciones

            #[SOLICTA NUMERO DE DELTAS Y QUE SE INDIQUE SI LOS ANGULOS SON INTERNOS Y EXTERNOS]
            def main():

                print()
                print('='*173)
                print()
                print('{:^173}'.format('A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  D E  L A  B R U J U L A'))
                print()
                print('='*173)
                print()

                deltas = int(input('Digite el numero de deltas en la poligonal: '))
                ang_externos = int(input('¿Angulos externos [1 = SI] [0 = NO]: '))

                #[AL DEFINIR ANGULOS INTERNOS Y EXTERNOS CALCULA SUMATORIA TEORICA DE ANGULO]
                if ang_externos == 1:
                    suma_teorica_ang = (deltas + 2) *180
                else:
                    suma_teorica_ang = (deltas - 2) *180

                #[SOLICITA LAS COORDENADAS DEL PUNTO DE ARMADA Y DEL PUNTO DE REFERENCIA]
                x_inicio = float(input('Digite la coordenada X (E) del punto de inicio: '))
                y_inicio = float(input('DIgite la coordenada Y (N) del punto de inicio: '))
                x_referencia = float(input('Digite la coordena X (E) del punto de referencia: '))
                y_referencia = float(input('Digite la coordena Y (N) del punto de referencia: '))

                #[IMPRIME EL ACIMUT DE REFERENCIA]
                acimut_ref = acimut_linea(x_inicio, y_inicio, x_referencia, y_referencia)
                print('\n', f'El acimut calculado es: {dec2gms(acimut_ref)}')

                #[IMPRIME LA SUMATORIA TEORICA DE ANGULOS]
                print(f'La sumatoria teórica de ángulos es: {suma_teorica_ang}°')

                #[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
                datos_medidos = []
                datos_medidos.append (['DELTA','ANG OBSER', 'DIST', 'ANG OBSERV DEC', 'ANG OBSER CORREG', 'AZIMUTH', 'PRY X', 'PRY Y', 'PRY X COREG', 'PRY Y COREG', 'COORD X', 'COORD Y'])

                j = 0
                sumang = 0.0
                sumdist = 0.0

                #[SOLICITA LOS DATOS DE CADA DELTA, NOMBRE, ANGULO Y DISTANCIA]
                # CON NUMERO DE DELTAS Y ANGULOS OBSERVADOS REALIZA LA SUMA DE ANGULOS
                # CALCULA EL ERROR ANGULAR Y LA CORRECCION ANGULAR
                # IMPRIME EL ERROR ANGULAR
                # IMPRIME LA CORRECCION ANGULAR
                
                for delta in (range(deltas+1)):
                    print('='*80)

                    nombre_delta = input(f'Digite el nombre del delta {delta+1}: ')
                    ang_observado = float(input(f'Digite el angulo observado {delta+1}: '))
                    distancia = float(input(f'Digite la dista de la linea {delta+1}: '))

                    print('='*80)

                    datos_linea = [nombre_delta, ang_observado, distancia, gms2dec(ang_observado)]
                    datos_medidos.append(datos_linea.copy())

                    if j != 0:
                        sumdist = sumdist + distancia
                        sumang = sumang + datos_linea[3]
                        j += 1
                    else:
                        j += 1
                
                error_angular = suma_teorica_ang - sumang
                correccion_angular = error_angular / deltas
                
                print('El error angular es:', error_angular)
                print('La corrección angular es:', correccion_angular)

                datos_medidos[1].append(datos_medidos[1][3])
                datos_medidos[1].append(acimut_ref + datos_medidos[1][3])

                #[VARIABLES DE SUMA DE PROYECCIONES]
                i = 0
                suma_px = 0.0
                suma_py = 0.0
                proyec_punto = []

                #[CALCULA CORRECCIONES A ANGULO, ACIMUT Y PROYECCIONES ]
                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue
                    
                    datos_medidos[i].append(datos_medidos[i][3] + correccion_angular)

                    if datos_medidos[i-1][4] >= 180:
                        acimut_deltas = datos_medidos[i-1][5] - 180 + datos_medidos[i][4]
                    else:
                        acimut_deltas = datos_medidos[i-1][5] + 180 + datos_medidos[i][4]
                    
                    if acimut_deltas >= 360:
                        acimut_deltas -= 360

                    datos_medidos[i].append(acimut_deltas)

                    proyec_punto = proyecciones(acimut_deltas, datos_medidos[i][2])

                    datos_medidos[i].append(proyec_punto[0])
                    datos_medidos[i].append(proyec_punto[1])

                    suma_px += datos_medidos[i][6]
                    suma_py += datos_medidos[i][7]

                    i += 1

                print()

                datos_medidos [1][:] += [0, 0, 0, 0, x_inicio, y_inicio]

                #[ALMACENA LAS PROYECCIONES CORREGIDAS EN LA LISTA]
                i = 0

                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue

                    #[CALCULA EL ERROR DE LAS PROYECCIONES]
                    datos_medidos[i].append(datos_medidos[i][6] - (suma_px / sumdist)*datos_medidos[i][2])
                    datos_medidos[i].append(datos_medidos[i][7] - (suma_py / sumdist)*datos_medidos[i][2])

                    #[CALCULA COORDENADAS]
                    datos_medidos[i].append(datos_medidos[i-1][10] + datos_medidos[i][8])
                    datos_medidos[i].append(datos_medidos[i-1][11] + datos_medidos[i][9])

                    i += 1

                #[IMPRIME DATOS CALCULADOS]
                print()

                print('='*173)
                print('{:^10}'.format('DELTA'), '{:^8}'.format('ANGULO'), '{:^8}'.format('DISTANC'), '{:^10}'.format('ANGULO'), '{:^10}'.format('AZIMUTH'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^11}'.format('COORDEN'), '{:^11}'.format('COORDEN'), sep='\t')

                print('{:^10}'.format(''), '{:^8}'.format('OBSERV'), '{:^8}'.format('(m)'), '{:^10}'.format('CORREGIDO'), '{:^10}'.format(''), '{:^10}'.format('X'), '{:^10}'.format('Y'), '{:^10}'.format('CORR X'), '{:^10}'.format('CORR Y'), '{:^11}'.format('X'), '{:^11}'.format('Y'), sep='\t')
                print('='*173)

                i = 0

                for dato in datos_medidos:
                    if i == 0:
                        i += 1
                        continue

                    print('{:^10}'.format(dato[0]),'{:8.4f}'.format(dato[1]), '{:8.4f}'.format(dato[2]), '{:10}'.format(dec2gms(dato[4])), '{:10}'.format(dec2gms(dato[5])), '{:+010.3f}'.format(dato[6]), '{:+010.3f}'.format(dato[7]), '{:+010.3f}'.format(dato[8]), '{:+010.3f}'.format(dato[9]), '{:11.3f}'.format(dato[10]), '{:11.3f}'.format(dato[11]), sep='\t')

                    i += 1

                print('='*173)

            if __name__ == '__main__':
                main()

        elif poligonal == "3":
            print("Eligio ajuste por método Tránsito")
            
			#[A J U S T E  D E  P O L I G O N A L  P O R  E L  M É T O D O  T R A N S I T O]


            import math

            def gms2dec(angulo):
                grados = int(angulo)
                auxiliar = (angulo - grados) * 100
                minutos = int(auxiliar)
                segundos = (auxiliar - minutos)*100

                angulo_dec = grados + minutos / 60 + segundos / 3600

                return angulo_dec

            #[ESTE BLOQUE CALCULA EL ACIMUT INICIAL]

            def acimut_linea(x1, y1, x2, y2):
                dx = x2 - x1
                dy = y2 - y1

                if dy != 0:
                    rumbo = math.degrees(math.atan(dx/dy))

                    if dx > 0 and dy > 0:
                        acimut = rumbo
                    elif dx > 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy > 0:
                        acimut = 360 + rumbo
                    elif dx == 0 and dy > 0:
                        acimut = 0
                    elif dx == 0 and dy > 0:
                        acimut = 180
                else:
                    if dx > 0:
                        acimut = 90
                    elif dx < 0:
                        acimut = 270
                    else:
                        acimut = -1
                
                return acimut

            #[ESTE BLOQUE CONVIERTE EL ANGULO INGRESADO DE GRADOS DECIMALES A GGMMSS]
            def dec2gms(angulo_dec):
                grados = int(angulo_dec)
                auxiliar = (angulo_dec - grados)*60
                minutos = int(auxiliar)
                segundos = round((auxiliar - minutos)*60,0)

                angulo_gms = '{:03d}'.format(grados) + '° ' + '{:02d}'.format(minutos) + "' " + '{:04.1f}'.format(segundos) + '"'

                return angulo_gms

            #[CALCULA EL CONTRA ACIMUT Y RUMBO]
            def acimut_poligonal(acimut_anterior, angulo_observ):
                if acimut_anterior >= 180:
                    contra_acimut = acimut_anterior - 180
                else:
                    contra_acimut = acimut_anterior + 180
                
                acimut = contra_acimut + angulo_observ

                if acimut >= 360:
                    acimut = acimut - 360
                
                return acimut

            #[CALCULA LAS PROYECCIONES]
            def proyecciones(acimut, distancia):
                
                acimut = math.radians(acimut)

                valor_proyecciones = []
                valor_proyecciones.append(math.sin(acimut)*distancia)
                valor_proyecciones.append(math.cos(acimut)*distancia)

                return valor_proyecciones

            #[SOLICTA NUMERO DE DELTAS Y QUE SE INDIQUE SI LOS ANGULOS SON INTERNOS Y EXTERNOS]
            def main():

                print()
                print('='*173)
                print()
                print('{:^173}'.format('A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  T R A N S I T O'))
                print()
                print('='*173)
                print()

                deltas = int(input('Digite el numero de deltas en la poligonal: '))
                ang_externos = int(input('¿Angulos externos [1 = SI] [0 = NO]: '))

                #[AL DEFINIR ANGULOS INTERNOS Y EXTERNOS CALCULA SUMATORIA TEORICA DE ANGULO]
                if ang_externos == 1:
                    suma_teorica_ang = (deltas + 2) *180
                else:
                    suma_teorica_ang = (deltas - 2) *180

                #[SOLICITA LAS COORDENADAS DEL PUNTO DE ARMADA Y DEL PUNTO DE REFERENCIA]
                x_inicio = float(input('Digite la coordenada X (E) del punto de inicio: '))
                y_inicio = float(input('DIgite la coordenada Y (N) del punto de inicio: '))
                x_referencia = float(input('Digite la coordena X (E) del punto de referencia: '))
                y_referencia = float(input('Digite la coordena Y (N) del punto de referencia: '))

                #[IMPRIME EL ACIMUT DE REFERENCIA]
                acimut_ref = acimut_linea(x_inicio, y_inicio, x_referencia, y_referencia)
                print('\n', f'El acimut calculado es: {dec2gms(acimut_ref)}')

                #[IMPRIME LA SUMATORIA TEORICA DE ANGULOS]
                print(f'La sumatoria teórica de ángulos es: {suma_teorica_ang}°')

                #[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
                datos_medidos = []
                datos_medidos.append (['DELTA','ANG OBSER', 'DIST', 'ANG OBSERV DEC', 'ANG OBSER CORREG', 'AZIMUTH', 'PRY X', 'PRY Y', 'PRY X COREG', 'PRY Y COREG', 'COORD X', 'COORD Y'])

                j = 0
                sumang = 0.0
                sumdist = 0.0

                #[SOLICITA LOS DATOS DE CADA DELTA, NOMBRE, ANGULO Y DISTANCIA]
                # CON NUMERO DE DELTAS Y ANGULOS OBSERVADOS REALIZA LA SUMA DE ANGULOS
                # CALCULA EL ERROR ANGULAR Y LA CORRECCION ANGULAR
                # IMPRIME EL ERROR ANGULAR
                # IMPRIME LA CORRECCION ANGULAR
                
                for delta in (range(deltas+1)):
                    print('='*80)

                    nombre_delta = input(f'Digite el nombre del delta {delta+1}: ')
                    ang_observado = float(input(f'Digite el angulo observado {delta+1}: '))
                    distancia = float(input(f'Digite la dista de la linea {delta+1}: '))

                    print('='*80)

                    datos_linea = [nombre_delta, ang_observado, distancia, gms2dec(ang_observado)]
                    datos_medidos.append(datos_linea.copy())

                    if j != 0:
                        sumdist = sumdist + distancia
                        sumang = sumang + datos_linea[3]
                        j += 1
                    else:
                        j += 1
                
                error_angular = suma_teorica_ang - sumang
                correccion_angular = error_angular / deltas
                
                print('El error angular es:', error_angular)
                print('La corrección angular es:', correccion_angular)

                datos_medidos[1].append(datos_medidos[1][3])
                datos_medidos[1].append(acimut_ref + datos_medidos[1][3])

                #[VARIABLES DE SUMA DE PROYECCIONES]
                i = 0
                suma_px = 0.0
                suma_py = 0.0
                proyec_punto = []

                #[CALCULA CORRECCIONES A ANGULO, ACIMUT Y PROYECCIONES ]
                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue
                    
                    datos_medidos[i].append(datos_medidos[i][3] + correccion_angular)

                    if datos_medidos[i-1][4] >= 180:
                        acimut_deltas = datos_medidos[i-1][5] - 180 + datos_medidos[i][4]
                    else:
                        acimut_deltas = datos_medidos[i-1][5] + 180 + datos_medidos[i][4]
                    
                    if acimut_deltas >= 360:
                        acimut_deltas -= 360

                    datos_medidos[i].append(acimut_deltas)

                    proyec_punto = proyecciones(acimut_deltas, datos_medidos[i][2])

                    datos_medidos[i].append(proyec_punto[0])
                    datos_medidos[i].append(proyec_punto[1])

                    suma_px += datos_medidos[i][6]
                    suma_py += datos_medidos[i][7]

                    i += 1

                print()

                datos_medidos [1][:] += [0, 0, 0, 0, x_inicio, y_inicio]

                #[ALMACENA LAS PROYECCIONES CORREGIDAS EN LA LISTA]
                i = 0

                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue

                    #[CALCULA EL ERROR DE LAS PROYECCIONES]
                    datos_medidos[i].append(datos_medidos[i][6] - (suma_px / sumdist)*datos_medidos[i][2])
                    datos_medidos[i].append(datos_medidos[i][7] - (suma_py / sumdist)*datos_medidos[i][2])

                    #[CALCULA COORDENADAS]
                    datos_medidos[i].append(datos_medidos[i-1][10] + datos_medidos[i][8])
                    datos_medidos[i].append(datos_medidos[i-1][11] + datos_medidos[i][9])

                    i += 1

                #[IMPRIME DATOS CALCULADOS]
                print()

                print('='*173)
                print('{:^10}'.format('DELTA'), '{:^8}'.format('ANGULO'), '{:^8}'.format('DISTANC'), '{:^10}'.format('ANGULO'), '{:^10}'.format('AZIMUTH'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^11}'.format('COORDEN'), '{:^11}'.format('COORDEN'), sep='\t')

                print('{:^10}'.format(''), '{:^8}'.format('OBSERV'), '{:^8}'.format('(m)'), '{:^10}'.format('CORREGIDO'), '{:^10}'.format(''), '{:^10}'.format('X'), '{:^10}'.format('Y'), '{:^10}'.format('CORR X'), '{:^10}'.format('CORR Y'), '{:^11}'.format('X'), '{:^11}'.format('Y'), sep='\t')
                print('='*173)

                i = 0

                for dato in datos_medidos:
                    if i == 0:
                        i += 1
                        continue

                    print('{:^10}'.format(dato[0]),'{:8.4f}'.format(dato[1]), '{:8.4f}'.format(dato[2]), '{:10}'.format(dec2gms(dato[4])), '{:10}'.format(dec2gms(dato[5])), '{:+010.3f}'.format(dato[6]), '{:+010.3f}'.format(dato[7]), '{:+010.3f}'.format(dato[8]), '{:+010.3f}'.format(dato[9]), '{:11.3f}'.format(dato[10]), '{:11.3f}'.format(dato[11]), sep='\t')

                    i += 1

                print('='*173)

            if __name__ == '__main__':
                main()
        else:
            print("Opción no válida")
    elif poligonal == "2":
        print("Eligio poligonal cerrada")
        print("""se le sugiere calcular por los métodos Brújula o Tránsito""")
        print("""Indique por cual método desea calcular
    1) Crandall     2) Brújula      3) Tránsito
    """)
        poligonal=input()
        if poligonal == "1":
            print("Eligio ajuste por método Crandall")
            #[A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  C R A N D A L L]
            import math
            import time as t
            import datetime
            #import numpy as np
            #file='coor.txt'
            #data=np.loadtxt(file,delimiter='\t',skiprows=0,usecols=[0,1])
            #print(data)

            tiempo_local = t.asctime(t.localtime(t.time()))
            print("Fecha y hora de creacion del archivo: ",tiempo_local)

            def gms2dec(angulo):
                grados = int(angulo)
                auxiliar = (angulo - grados) * 100
                minutos = int(auxiliar)
                segundos = (auxiliar - minutos)*100

                angulo_dec = grados + minutos / 60 + segundos / 3600

                return angulo_dec

            #[ESTE BLOQUE CALCULA EL ACIMUT INICIAL y FINAL]

            def acimut_linea(x1, y1, x2, y2):
                dx = x2 - x1
                dy = y2 - y1

                if dy != 0:
                    rumbo = math.degrees(math.atan(dx/dy))

                    if dx > 0 and dy > 0:
                        acimut = rumbo
                    elif dx > 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy > 0:
                        acimut = 360 + rumbo
                    elif dx == 0 and dy > 0:
                        acimut = 0
                    elif dx == 0 and dy > 0:
                        acimut = 180
                else:
                    if dx > 0:
                        acimut = 90
                    elif dx < 0:
                        acimut = 270
                    else:
                        acimut = -1
                
                return acimut

            #[ESTE BLOQUE CONVIERTE EL ANGULO INGRESADO DE GRADOS DECIMALES A GGMMSS]
            def dec2gms(angulo_dec):
                grados = int(angulo_dec)
                auxiliar = (angulo_dec - grados)*60
                minutos = int(auxiliar)
                segundos = round((auxiliar - minutos)*60,0)

                angulo_gms = '{:03d}'.format(grados) + '° ' + '{:02d}'.format(minutos) + "' " + '{:04.1f}'.format(segundos) + '"'

                return angulo_gms

            #[CALCULA EL CONTRA ACIMUT Y RUMBO]
            def acimut_poligonal(acimut_anterior, angulo_observ):
                if acimut_anterior >= 180:
                    contra_acimut = acimut_anterior - 180
                else:
                    contra_acimut = acimut_anterior + 180
                
                acimut = contra_acimut + angulo_observ

                if acimut >= 360:
                    acimut = acimut - 360
                
                return acimut

            #[CALCULA LAS PROYECCIONES]
            def proyecciones(acimut, distancia):
                
                acimut = math.radians(acimut)

                valor_proyecciones = []
                valor_proyecciones.append(math.sin(acimut)*distancia)
                valor_proyecciones.append(math.cos(acimut)*distancia)

                return valor_proyecciones

            #[SOLICTA NUMERO DE DELTAS Y QUE SE INDIQUE SI LOS ANGULOS SON INTERNOS Y EXTERNOS]
            def main():

                print()
                print('='*150)
                print()
                print('{:^150}'.format('A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  C R A N D A L L'))
                print()
                print('='*150)
                print()
                print('{:^150}'.format("INGENIERÍA DE SOFTWARE\n"))
                print('{:^150}'.format("PROFESOR: Evelio Luis Madera Arteaga\n"))
                print('{:^150}'.format("Wilmer Franco Hernandez         COD: 20201732014\n"))
                print('{:^150}'.format("Juliana Manuela Pachón Florián  COD: 20192732006\n"))
                print('{:^150}'.format("Jean Pierre Riaño Melo          COD: 20192732030\n"))
                print('{:^150}'.format("Julian Camilo Lopez Alcala      COD: 20192732024\n"))
                print()

                deltas = int(input('Digite el numero de deltas en la poligonal: '))
                '''ang_externos = int(input('¿Angulos externos [1 = SI] [0 = NO]: '))

                #[AL DEFINIR ANGULOS INTERNOS Y EXTERNOS CALCULA SUMATORIA TEORICA DE ANGULO]
                if ang_externos == 1:
                    suma_teorica_ang = (deltas + 2) *180
                else:
                    suma_teorica_ang = (deltas - 2) *180'''

                #[SOLICITA LAS COORDENADAS DEL PUNTO DE ARMADA Y DEL PUNTO DE REFERENCIA INICIAL]
                x_inicio = float(input('Digite la coordenada X (E) del punto de inicio: '))
                y_inicio = float(input('Digite la coordenada Y (N) del punto de inicio: '))
                x_referencia = float(input('Digite la coordena X (E) del punto de referencia: '))
                y_referencia = float(input('Digite la coordena Y (N) del punto de referencia: ') + "\n")

                
                #[SOLICITA LAS COORDENADAS DEL PUNTO DE ARMADA Y DEL PUNTO DE REFERENCIA FINAL]
                x_final = float(input('Digite la coordenada X (E) del punto de final: '))
                y_final = float(input('Digite la coordenada Y (N) del punto de final: '))
                x_reffinal = float(input('Digite la coordena X (E) del punto de reffinal: '))
                y_reffinal = float(input('Digite la coordena Y (N) del punto de reffinal: ') + "\n")

                #[IMPRIME EL ACIMUT DE REFERENCIA INICIAL]
                acimut_refini = acimut_linea(x_inicio, y_inicio, x_referencia, y_referencia)
                print('\n', f'El acimut calculado inicial es: {dec2gms(acimut_refini)}' + "\n")
                #[IMPRIME EL ACIMUT DE REFERENCIA FINAL]
                acimut_reffin = acimut_linea(x_final, y_final, x_reffinal, y_reffinal)
                print('\n', f'El acimut téorico de llegada es: {dec2gms(acimut_reffin)}' + "\n")
                
                #[IMPRIME LA SUMATORIA TEORICA DE ANGULOS]
                '''print(f'La sumatoria teórica de ángulos es: {suma_teorica_ang}°')'''

                #[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
                datos_medidos = []
                datos_medidos.append (['DELTA','AZIMUTH', 'DIST', 'AZIMUTH DEC', 'AZIMUTH CORREG', 'PRY X', 'PRY Y', 'PRY X COREG', 'PRY Y COREG', 'COORD X', 'COORD Y'])

                j = 0
                sumang = 0.0
                sumdist = 0.0

                #[SOLICITA LOS DATOS DE CADA DELTA, NOMBRE, ANGULO Y DISTANCIA]
                # CON NUMERO DE DELTAS Y ANGULOS OBSERVADOS REALIZA LA SUMA DE ANGULOS
                # CALCULA EL ERROR ANGULAR Y LA CORRECCION ANGULAR
                # IMPRIME EL ERROR ANGULAR
                # IMPRIME LA CORRECCION ANGULAR
                
                for delta in (range(deltas)):
                    print('='*160)

                    nombre_delta = input(f'Digite el nombre del delta {delta+1}: ')
                    az_observado = float(input(f'Digite el azimuth observado {delta+1}: '))
                    distancia = float(input(f'Digite la distancia de la linea {delta+1}: '))

                    print('='*160)

                    datos_linea = [nombre_delta, az_observado, distancia, gms2dec(az_observado)]
                    datos_medidos.append(datos_linea.copy())

                    if j != -1:
                        sumdist = sumdist + distancia
                        azlinfin = datos_linea[3]
                        j += 1
                    else:
                        j += 1

                    print('sumatoria de distancias')
                    print(sumdist)
                
                error_angular = acimut_reffin - azlinfin
                correccion_angular = error_angular / deltas

                print('correccion angular')
                print()
                
                print('El error angular es:', dec2gms(error_angular))
                print('La corrección angular es:', dec2gms(correccion_angular))

                datos_medidos[1].append(datos_medidos[1][3])
                datos_medidos[1].append(acimut_refini + datos_medidos[1][3])

                print(datos_medidos)

                #[VARIABLES DE SUMA DE PROYECCIONES]
                i = 0
                suma_px = 0.0
                suma_py = 0.0
                proyec_punto = []

                
                
                #[CALCULA CORRECCIONES A ANGULO, ACIMUT Y PROYECCIONES ]
                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue
                    
                    datos_medidos[i].append(datos_medidos[i][3] + correccion_angular)
                    print ('datos_medidos')
                    print(datos_medidos)

                    if datos_medidos[i-1][4] >= 180:
                        acimut_deltas = datos_medidos[i-1][4] #- 180 + datos_medidos[i][4]'''
                    else:
                        acimut_deltas = datos_medidos[i-1][4] #+ 180 + datos_medidos[i][4]'''
                    
                    if acimut_deltas >= 360:
                        acimut_deltas -= 360

                    datos_medidos[i].append(acimut_deltas)

                    proyec_punto = proyecciones(acimut_deltas, datos_medidos[i][2])

                    datos_medidos[i].append(proyec_punto[0])
                    datos_medidos[i].append(proyec_punto[1])

                    suma_px += datos_medidos[i][5]
                    suma_py += datos_medidos[i][6]

                    i += 1

                print()

                datos_medidos [1][:] += [0, 0, 0, 0, x_inicio, y_inicio]

                #[ALMACENA LAS PROYECCIONES CORREGIDAS EN LA LISTA]
                i = 0

                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue

                    #[CALCULA EL ERROR DE LAS PROYECCIONES]
                    datos_medidos[i].append(datos_medidos[i][5] - (suma_px / sumdist)*datos_medidos[i][2])
                    datos_medidos[i].append(datos_medidos[i][6] - (suma_py / sumdist)*datos_medidos[i][2])

                    #[CALCULA COORDENADAS]
                    datos_medidos[i].append(datos_medidos[i-1][9] + datos_medidos[i][7])
                    datos_medidos[i].append(datos_medidos[i-1][10] + datos_medidos[i][8])

                    i += 1

                #[IMPRIME DATOS CALCULADOS]
                print()
                print('{:^150}'.format("DATOS FINALES\n"))
                print('='*160)
                print('{:^6}'.format('DELTA'),'{:^8}'.format('AZIMUTH'),'{:^8}'.format('DISTANC'),'{:^10}'.format('AZIMUTH'),'{:^10}'.format('PROYECC'),'{:^10}'.format('PROYECC'),'{:^10}'.format('PROYECC'),'{:^10}'.format('PROYECC'),'{:^11}'.format('COORDEN'),'{:^11}'.format('COORDEN'), sep='\t')

                print('{:^6}'.format(''),'{:^8}'.format('OBSERV'),'{:^8}'.format('(m)'),'{:^10}'.format('CORREGIDO'),'{:^10}'.format('X'),'{:^10}'.format('Y'),'{:^10}'.format('CORR X'),'{:^10}'.format('CORR Y'),'{:^11}'.format('X'),'{:^11}'.format('Y'), sep='\t')
                print('='*160)

                i = 0

                for dato in datos_medidos:
                    if i == 0:
                        i += 1
                        continue

                    print('{:^6}'.format(dato[0]),'{:8.4f}'.format(dato[1]),'{:8.4f}'.format(dato[2]),'{:10}'.format(dec2gms(dato[4])),'{:+010.3f}'.format(dato[6]),'{:+010.3f}'.format(dato[7]),'{:+010.3f}'.format(dato[8]),'{:+010.3f}'.format(dato[9]),'{:11.3f}'.format(dato[10]),'{:11.3f}'.format(dato[11]), sep='\t')

                    i += 1

                print('='*160)
                

            if __name__ == '__main__':
                main()

            archivo=open("Datos_Poligonal.txt","w")
            archivo.write("**CALCULO Y AJUSTE DE UNA POLIGONAL ABIERTA POR METODO CRANDALL**\n")
            archivo.write(str("Fecha y hora de creacion del archivo: ") )
            archivo.write(str(tiempo_local) + "\n")
            archivo.write("INGENIERÍA DE SOFTWARE\n")
            archivo.write("PROFESOR: Evelio Luis Madera Arteaga\n")
            archivo.write("Wilmer Franco Hernandez         COD: 20201732014\n")
            archivo.write("Juliana Manuela Pachón Florián  COD: 20192732006\n")
            archivo.write("Jean Pierre Riaño Melo          COD: 20192732030\n")
            archivo.write("Julian Camilo Lopez Alcala      COD: 20192732024\n")
            archivo.write(" \n")
            archivo.write('{:^150}'.format("DATOS FINALES\n"))
            archivo.write(" \n")
            archivo.write('='*160)
            archivo.write(" \n")
            archivo.write('{:^6}'.format('DELTA')),archivo.write('{:^8}'.format('AZIMUTH')),archivo.write('{:^8}'.format('DISTANC')),archivo.write('{:^10}'.format('AZIMUTH')),archivo.write('{:^10}'.format('PROYECC')),archivo.write('{:^10}'.format('PROYECC')),archivo.write('{:^10}'.format('PROYECC')),archivo.write('{:^10}'.format('PROYECC')),archivo.write('{:^11}'.format('COORDEN')),archivo.write('{:^11}'.format('COORDEN'))
            archivo.write(" \n")
            archivo.write('{:^6}'.format('')),archivo.write('{:^8}'.format('OBSERV')),archivo.write('{:^8}'.format('(m)')),archivo.write('{:^10}'.format('CORREGIDO')),archivo.write('{:^10}'.format('X')),archivo.write('{:^10}'.format('Y')),archivo.write('{:^10}'.format('CORR X')),archivo.write('{:^10}'.format('CORR Y')),archivo.write('{:^11}'.format('X')),archivo.write('{:^11}'.format('Y'))
            archivo.write(" \n")
            archivo.write(" \n")
            archivo.write('='*160)
            archivo.write(" \n")
            archivo.write('='*160)
            '''archivo.write("LONG_POLIGONAL=  % s\n"%sumdist)
            archivo.write('{:^6}'.format(dato[0])),archivo.write('{:8.4f}'.format(dato[1])),archivo.write('{:8.4f}'.format(dato[2])),archivo.write('{:10}'.format(dec2gms(dato[4]))),archivo.write('{:+010.3f}'.format(dato[6])),archivo.write('{:+010.3f}'.format(dato[7])),archivo.write('{:+010.3f}'.format(dato[8])),archivo.write('{:+010.3f}'.format(dato[9])),archivo.write('{:11.3f}'.format(dato[10])),archivo.write('{:11.3f}'.format(dato[11]))
            archivo.write('{:^6}'.format('DELTA'), '{:^8}'.format('AZIMUTH'), '{:^8}'.format('DISTANC'), '{:^10}'.format('AZIMUTH'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^11}'.format('COORDEN'), '{:^11}'.format('COORDEN'), sep='\t')
            archivo.write('{:^6}'.format(''), '{:^8}'.format('OBSERV'),'{:^8}'.format('(m)'),'{:^10}'.format('CORREGIDO'),'{:^10}'.format('X'), '{:^10}'.format('Y'), '{:^10}'.format('CORR X'), '{:^10}'.format('CORR Y'), '{:^11}'.format('X'), '{:^11}'.format('Y'), sep='\t')
            archivo.write('{:^6}'.format(dato[0]), '{:8.4f}'.format(dato[1]), '{:8.4f}'.format(dato[2]), '{:10}'.format(dec2gms(dato[4])), '{:+010.3f}'.format(dato[6]), '{:+010.3f}'.format(dato[7]), '{:+010.3f}'.format(dato[8]), '{:+010.3f}'.format(dato[9]), '{:11.3f}'.format(dato[10]), '{:11.3f}'.format(dato[11]), sep='\t')
            archivo.write(" \n")
            archivo.write("ERROR_TOTAL=  % s\n"%ed )
            archivo.write(" \n")
            archivo.write("PRESICION= 1:%s\n"%prec)
            archivo.write(" \n")
            archivo.write("id,angulo,distancia,acimut,proy_N-S, proy_E-W,proy_Correg_N-S,proy_Correg_E-W,Norte, Este\n")
            archivo.write("%s"%observaciones)
            archivo.write(" \n")
            archivo.write("*****COORDENADAS FINALES*****\n")
            archivo.write("id,    Norte,    Este\n")
            archivo.write("%s\n"%coordenadas)'''
            archivo.close()
        elif poligonal == "2":
            print("Eligio ajuste por método Brújula")
			#[A J U S T E  D E  P O L I G O N A L  P O R  E L  M É T O D O  D E  L A  B R Ú J U L A]


            import math

            def gms2dec(angulo):
                grados = int(angulo)
                auxiliar = (angulo - grados) * 100
                minutos = int(auxiliar)
                segundos = (auxiliar - minutos)*100

                angulo_dec = grados + minutos / 60 + segundos / 3600

                return angulo_dec

            #[ESTE BLOQUE CALCULA EL ACIMUT INICIAL]

            def acimut_linea(x1, y1, x2, y2):
                dx = x2 - x1
                dy = y2 - y1

                if dy != 0:
                    rumbo = math.degrees(math.atan(dx/dy))

                    if dx > 0 and dy > 0:
                        acimut = rumbo
                    elif dx > 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy > 0:
                        acimut = 360 + rumbo
                    elif dx == 0 and dy > 0:
                        acimut = 0
                    elif dx == 0 and dy > 0:
                        acimut = 180
                else:
                    if dx > 0:
                        acimut = 90
                    elif dx < 0:
                        acimut = 270
                    else:
                        acimut = -1
                
                return acimut

            #[ESTE BLOQUE CONVIERTE EL ANGULO INGRESADO DE GRADOS DECIMALES A GGMMSS]
            def dec2gms(angulo_dec):
                grados = int(angulo_dec)
                auxiliar = (angulo_dec - grados)*60
                minutos = int(auxiliar)
                segundos = round((auxiliar - minutos)*60,0)

                angulo_gms = '{:03d}'.format(grados) + '° ' + '{:02d}'.format(minutos) + "' " + '{:04.1f}'.format(segundos) + '"'

                return angulo_gms

            #[CALCULA EL CONTRA ACIMUT Y RUMBO]
            def acimut_poligonal(acimut_anterior, angulo_observ):
                if acimut_anterior >= 180:
                    contra_acimut = acimut_anterior - 180
                else:
                    contra_acimut = acimut_anterior + 180
                
                acimut = contra_acimut + angulo_observ

                if acimut >= 360:
                    acimut = acimut - 360
                
                return acimut

            #[CALCULA LAS PROYECCIONES]
            def proyecciones(acimut, distancia):
                
                acimut = math.radians(acimut)

                valor_proyecciones = []
                valor_proyecciones.append(math.sin(acimut)*distancia)
                valor_proyecciones.append(math.cos(acimut)*distancia)

                return valor_proyecciones

            #[SOLICTA NUMERO DE DELTAS Y QUE SE INDIQUE SI LOS ANGULOS SON INTERNOS Y EXTERNOS]
            def main():

                print()
                print('='*173)
                print()
                print('{:^173}'.format('A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  D E  L A  B R U J U L A'))
                print()
                print('='*173)
                print()

                deltas = int(input('Digite el numero de deltas en la poligonal: '))
                ang_externos = int(input('¿Angulos externos [1 = SI] [0 = NO]: '))

                #[AL DEFINIR ANGULOS INTERNOS Y EXTERNOS CALCULA SUMATORIA TEORICA DE ANGULO]
                if ang_externos == 1:
                    suma_teorica_ang = (deltas + 2) *180
                else:
                    suma_teorica_ang = (deltas - 2) *180

                #[SOLICITA LAS COORDENADAS DEL PUNTO DE ARMADA Y DEL PUNTO DE REFERENCIA]
                x_inicio = float(input('Digite la coordenada X (E) del punto de inicio: '))
                y_inicio = float(input('DIgite la coordenada Y (N) del punto de inicio: '))
                x_referencia = float(input('Digite la coordena X (E) del punto de referencia: '))
                y_referencia = float(input('Digite la coordena Y (N) del punto de referencia: '))

                #[IMPRIME EL ACIMUT DE REFERENCIA]
                acimut_ref = acimut_linea(x_inicio, y_inicio, x_referencia, y_referencia)
                print('\n', f'El acimut calculado es: {dec2gms(acimut_ref)}')

                #[IMPRIME LA SUMATORIA TEORICA DE ANGULOS]
                print(f'La sumatoria teórica de ángulos es: {suma_teorica_ang}°')

                #[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
                datos_medidos = []
                datos_medidos.append (['DELTA','ANG OBSER', 'DIST', 'ANG OBSERV DEC', 'ANG OBSER CORREG', 'AZIMUTH', 'PRY X', 'PRY Y', 'PRY X COREG', 'PRY Y COREG', 'COORD X', 'COORD Y'])

                j = 0
                sumang = 0.0
                sumdist = 0.0

                #[SOLICITA LOS DATOS DE CADA DELTA, NOMBRE, ANGULO Y DISTANCIA]
                # CON NUMERO DE DELTAS Y ANGULOS OBSERVADOS REALIZA LA SUMA DE ANGULOS
                # CALCULA EL ERROR ANGULAR Y LA CORRECCION ANGULAR
                # IMPRIME EL ERROR ANGULAR
                # IMPRIME LA CORRECCION ANGULAR
                
                for delta in (range(deltas+1)):
                    print('='*80)

                    nombre_delta = input(f'Digite el nombre del delta {delta+1}: ')
                    ang_observado = float(input(f'Digite el angulo observado {delta+1}: '))
                    distancia = float(input(f'Digite la dista de la linea {delta+1}: '))

                    print('='*80)

                    datos_linea = [nombre_delta, ang_observado, distancia, gms2dec(ang_observado)]
                    datos_medidos.append(datos_linea.copy())

                    if j != 0:
                        sumdist = sumdist + distancia
                        sumang = sumang + datos_linea[3]
                        j += 1
                    else:
                        j += 1
                
                error_angular = suma_teorica_ang - sumang
                correccion_angular = error_angular / deltas
                
                print('El error angular es:', error_angular)
                print('La corrección angular es:', correccion_angular)

                datos_medidos[1].append(datos_medidos[1][3])
                datos_medidos[1].append(acimut_ref + datos_medidos[1][3])

                #[VARIABLES DE SUMA DE PROYECCIONES]
                i = 0
                suma_px = 0.0
                suma_py = 0.0
                proyec_punto = []

                #[CALCULA CORRECCIONES A ANGULO, ACIMUT Y PROYECCIONES ]
                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue
                    
                    datos_medidos[i].append(datos_medidos[i][3] + correccion_angular)

                    if datos_medidos[i-1][4] >= 180:
                        acimut_deltas = datos_medidos[i-1][5] - 180 + datos_medidos[i][4]
                    else:
                        acimut_deltas = datos_medidos[i-1][5] + 180 + datos_medidos[i][4]
                    
                    if acimut_deltas >= 360:
                        acimut_deltas -= 360

                    datos_medidos[i].append(acimut_deltas)

                    proyec_punto = proyecciones(acimut_deltas, datos_medidos[i][2])

                    datos_medidos[i].append(proyec_punto[0])
                    datos_medidos[i].append(proyec_punto[1])

                    suma_px += datos_medidos[i][6]
                    suma_py += datos_medidos[i][7]

                    i += 1

                print()

                datos_medidos [1][:] += [0, 0, 0, 0, x_inicio, y_inicio]

                #[ALMACENA LAS PROYECCIONES CORREGIDAS EN LA LISTA]
                i = 0

                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue

                    #[CALCULA EL ERROR DE LAS PROYECCIONES]
                    datos_medidos[i].append(datos_medidos[i][6] - (suma_px / sumdist)*datos_medidos[i][2])
                    datos_medidos[i].append(datos_medidos[i][7] - (suma_py / sumdist)*datos_medidos[i][2])

                    #[CALCULA COORDENADAS]
                    datos_medidos[i].append(datos_medidos[i-1][10] + datos_medidos[i][8])
                    datos_medidos[i].append(datos_medidos[i-1][11] + datos_medidos[i][9])

                    i += 1

                #[IMPRIME DATOS CALCULADOS]
                print()

                print('='*173)
                print('{:^10}'.format('DELTA'), '{:^8}'.format('ANGULO'), '{:^8}'.format('DISTANC'), '{:^10}'.format('ANGULO'), '{:^10}'.format('AZIMUTH'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^11}'.format('COORDEN'), '{:^11}'.format('COORDEN'), sep='\t')

                print('{:^10}'.format(''), '{:^8}'.format('OBSERV'), '{:^8}'.format('(m)'), '{:^10}'.format('CORREGIDO'), '{:^10}'.format(''), '{:^10}'.format('X'), '{:^10}'.format('Y'), '{:^10}'.format('CORR X'), '{:^10}'.format('CORR Y'), '{:^11}'.format('X'), '{:^11}'.format('Y'), sep='\t')
                print('='*173)

                i = 0

                for dato in datos_medidos:
                    if i == 0:
                        i += 1
                        continue

                    print('{:^10}'.format(dato[0]),'{:8.4f}'.format(dato[1]), '{:8.4f}'.format(dato[2]), '{:10}'.format(dec2gms(dato[4])), '{:10}'.format(dec2gms(dato[5])), '{:+010.3f}'.format(dato[6]), '{:+010.3f}'.format(dato[7]), '{:+010.3f}'.format(dato[8]), '{:+010.3f}'.format(dato[9]), '{:11.3f}'.format(dato[10]), '{:11.3f}'.format(dato[11]), sep='\t')

                    i += 1

                print('='*173)

            if __name__ == '__main__':
                main()

        elif poligonal == "3":
            print("Eligio ajuste por método Tránsito")
            
			#[A J U S T E  D E  P O L I G O N A L  P O R  E L  M É T O D O  T R A N S I T O]


            import math

            def gms2dec(angulo):
                grados = int(angulo)
                auxiliar = (angulo - grados) * 100
                minutos = int(auxiliar)
                segundos = (auxiliar - minutos)*100

                angulo_dec = grados + minutos / 60 + segundos / 3600

                return angulo_dec

            #[ESTE BLOQUE CALCULA EL ACIMUT INICIAL]

            def acimut_linea(x1, y1, x2, y2):
                dx = x2 - x1
                dy = y2 - y1

                if dy != 0:
                    rumbo = math.degrees(math.atan(dx/dy))

                    if dx > 0 and dy > 0:
                        acimut = rumbo
                    elif dx > 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy < 0:
                        acimut = 180 + rumbo
                    elif dx < 0 and dy > 0:
                        acimut = 360 + rumbo
                    elif dx == 0 and dy > 0:
                        acimut = 0
                    elif dx == 0 and dy > 0:
                        acimut = 180
                else:
                    if dx > 0:
                        acimut = 90
                    elif dx < 0:
                        acimut = 270
                    else:
                        acimut = -1
                
                return acimut

            #[ESTE BLOQUE CONVIERTE EL ANGULO INGRESADO DE GRADOS DECIMALES A GGMMSS]
            def dec2gms(angulo_dec):
                grados = int(angulo_dec)
                auxiliar = (angulo_dec - grados)*60
                minutos = int(auxiliar)
                segundos = round((auxiliar - minutos)*60,0)

                angulo_gms = '{:03d}'.format(grados) + '° ' + '{:02d}'.format(minutos) + "' " + '{:04.1f}'.format(segundos) + '"'

                return angulo_gms

            #[CALCULA EL CONTRA ACIMUT Y RUMBO]
            def acimut_poligonal(acimut_anterior, angulo_observ):
                if acimut_anterior >= 180:
                    contra_acimut = acimut_anterior - 180
                else:
                    contra_acimut = acimut_anterior + 180
                
                acimut = contra_acimut + angulo_observ

                if acimut >= 360:
                    acimut = acimut - 360
                
                return acimut

            #[CALCULA LAS PROYECCIONES]
            def proyecciones(acimut, distancia):
                
                acimut = math.radians(acimut)

                valor_proyecciones = []
                valor_proyecciones.append(math.sin(acimut)*distancia)
                valor_proyecciones.append(math.cos(acimut)*distancia)

                return valor_proyecciones

            #[SOLICTA NUMERO DE DELTAS Y QUE SE INDIQUE SI LOS ANGULOS SON INTERNOS Y EXTERNOS]
            def main():

                print()
                print('='*173)
                print()
                print('{:^173}'.format('A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  T R A N S I T O'))
                print()
                print('='*173)
                print()

                deltas = int(input('Digite el numero de deltas en la poligonal: '))
                ang_externos = int(input('¿Angulos externos [1 = SI] [0 = NO]: '))

                #[AL DEFINIR ANGULOS INTERNOS Y EXTERNOS CALCULA SUMATORIA TEORICA DE ANGULO]
                if ang_externos == 1:
                    suma_teorica_ang = (deltas + 2) *180
                else:
                    suma_teorica_ang = (deltas - 2) *180

                #[SOLICITA LAS COORDENADAS DEL PUNTO DE ARMADA Y DEL PUNTO DE REFERENCIA]
                x_inicio = float(input('Digite la coordenada X (E) del punto de inicio: '))
                y_inicio = float(input('DIgite la coordenada Y (N) del punto de inicio: '))
                x_referencia = float(input('Digite la coordena X (E) del punto de referencia: '))
                y_referencia = float(input('Digite la coordena Y (N) del punto de referencia: '))

                #[IMPRIME EL ACIMUT DE REFERENCIA]
                acimut_ref = acimut_linea(x_inicio, y_inicio, x_referencia, y_referencia)
                print('\n', f'El acimut calculado es: {dec2gms(acimut_ref)}')

                #[IMPRIME LA SUMATORIA TEORICA DE ANGULOS]
                print(f'La sumatoria teórica de ángulos es: {suma_teorica_ang}°')

                #[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
                datos_medidos = []
                datos_medidos.append (['DELTA','ANG OBSER', 'DIST', 'ANG OBSERV DEC', 'ANG OBSER CORREG', 'AZIMUTH', 'PRY X', 'PRY Y', 'PRY X COREG', 'PRY Y COREG', 'COORD X', 'COORD Y'])

                j = 0
                sumang = 0.0
                sumdist = 0.0

                #[SOLICITA LOS DATOS DE CADA DELTA, NOMBRE, ANGULO Y DISTANCIA]
                # CON NUMERO DE DELTAS Y ANGULOS OBSERVADOS REALIZA LA SUMA DE ANGULOS
                # CALCULA EL ERROR ANGULAR Y LA CORRECCION ANGULAR
                # IMPRIME EL ERROR ANGULAR
                # IMPRIME LA CORRECCION ANGULAR
                
                for delta in (range(deltas+1)):
                    print('='*80)

                    nombre_delta = input(f'Digite el nombre del delta {delta+1}: ')
                    ang_observado = float(input(f'Digite el angulo observado {delta+1}: '))
                    distancia = float(input(f'Digite la dista de la linea {delta+1}: '))

                    print('='*80)

                    datos_linea = [nombre_delta, ang_observado, distancia, gms2dec(ang_observado)]
                    datos_medidos.append(datos_linea.copy())

                    if j != 0:
                        sumdist = sumdist + distancia
                        sumang = sumang + datos_linea[3]
                        j += 1
                    else:
                        j += 1
                
                error_angular = suma_teorica_ang - sumang
                correccion_angular = error_angular / deltas
                
                print('El error angular es:', error_angular)
                print('La corrección angular es:', correccion_angular)

                datos_medidos[1].append(datos_medidos[1][3])
                datos_medidos[1].append(acimut_ref + datos_medidos[1][3])

                #[VARIABLES DE SUMA DE PROYECCIONES]
                i = 0
                suma_px = 0.0
                suma_py = 0.0
                proyec_punto = []

                #[CALCULA CORRECCIONES A ANGULO, ACIMUT Y PROYECCIONES ]
                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue
                    
                    datos_medidos[i].append(datos_medidos[i][3] + correccion_angular)

                    if datos_medidos[i-1][4] >= 180:
                        acimut_deltas = datos_medidos[i-1][5] - 180 + datos_medidos[i][4]
                    else:
                        acimut_deltas = datos_medidos[i-1][5] + 180 + datos_medidos[i][4]
                    
                    if acimut_deltas >= 360:
                        acimut_deltas -= 360

                    datos_medidos[i].append(acimut_deltas)

                    proyec_punto = proyecciones(acimut_deltas, datos_medidos[i][2])

                    datos_medidos[i].append(proyec_punto[0])
                    datos_medidos[i].append(proyec_punto[1])

                    suma_px += datos_medidos[i][6]
                    suma_py += datos_medidos[i][7]

                    i += 1

                print()

                datos_medidos [1][:] += [0, 0, 0, 0, x_inicio, y_inicio]

                #[ALMACENA LAS PROYECCIONES CORREGIDAS EN LA LISTA]
                i = 0

                for dato in datos_medidos:

                    if i < 2:
                        i += 1
                        continue

                    #[CALCULA EL ERROR DE LAS PROYECCIONES]
                    datos_medidos[i].append(datos_medidos[i][6] - (suma_px / sumdist)*datos_medidos[i][2])
                    datos_medidos[i].append(datos_medidos[i][7] - (suma_py / sumdist)*datos_medidos[i][2])

                    #[CALCULA COORDENADAS]
                    datos_medidos[i].append(datos_medidos[i-1][10] + datos_medidos[i][8])
                    datos_medidos[i].append(datos_medidos[i-1][11] + datos_medidos[i][9])

                    i += 1

                #[IMPRIME DATOS CALCULADOS]
                print()

                print('='*173)
                print('{:^10}'.format('DELTA'), '{:^8}'.format('ANGULO'), '{:^8}'.format('DISTANC'), '{:^10}'.format('ANGULO'), '{:^10}'.format('AZIMUTH'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^10}'.format('PROYECC'), '{:^11}'.format('COORDEN'), '{:^11}'.format('COORDEN'), sep='\t')

                print('{:^10}'.format(''), '{:^8}'.format('OBSERV'), '{:^8}'.format('(m)'), '{:^10}'.format('CORREGIDO'), '{:^10}'.format(''), '{:^10}'.format('X'), '{:^10}'.format('Y'), '{:^10}'.format('CORR X'), '{:^10}'.format('CORR Y'), '{:^11}'.format('X'), '{:^11}'.format('Y'), sep='\t')
                print('='*173)

                i = 0

                for dato in datos_medidos:
                    if i == 0:
                        i += 1
                        continue

                    print('{:^10}'.format(dato[0]),'{:8.4f}'.format(dato[1]), '{:8.4f}'.format(dato[2]), '{:10}'.format(dec2gms(dato[4])), '{:10}'.format(dec2gms(dato[5])), '{:+010.3f}'.format(dato[6]), '{:+010.3f}'.format(dato[7]), '{:+010.3f}'.format(dato[8]), '{:+010.3f}'.format(dato[9]), '{:11.3f}'.format(dato[10]), '{:11.3f}'.format(dato[11]), sep='\t')

                    i += 1

                print('='*173)

            if __name__ == '__main__':
                main()    
        else:
            print("Opción no válida")
    else:
        print("Opción no válida")

else:
    print("Opción no válida")
