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
    1) Calculo por distancias       2) Calculo por número de cambios
    """)
    CalNiv=input("¿por cual método desea calcular?")
    if CalNiv == "1":
        print("Eligio calculo por distancias")
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
	    print(f'el error permitido de acuerdo con precisión del equipo es: {error_permitido}')
	#[SOLICITA LA COTA DEL BM DE PARTIDA]
	BM = float(input('Digite la cota del BM de inicio: '))
	VMAS_inicio = float(input('Digite la vista mas: '))

	#[IMPRIME LA HI DE REFERENCIA]
	hi_ref = (BM + VMAS_inicio)
	print('\n', f'La ALTURA INSTRUMENTAL calculada es: {hi_ref}')
	#[ALMACENA LOS DATOS CAPTURADOS EN LISTAS]
	datos_medidos = []
	datos_medidos.append (['BM','V+', 'V-', 'HI', 'DIST', 'COTA', 'COTA CORREG'])

	j = 0
	sumVMAS = 0.0
	sumVMENOS = 0.0
	sumdistafter = 0.0
	sumdistnext = 0.0

	#[SOLICITA LOS DATOS DE CADA BM, NOMBRE, VISTA +, VISTA - Y DISTANCIA]
	# CON NUMERO DE BM´S Y DIST OBSERVADOS REALIZA LA SUMA DE ANGULOS
	# CALCULA EL ERROR EN COTA Y LA CORRECCION 
	# IMPRIME EL ERROR EN COTA
	# IMPRIME LA CORRECCION EN COTA

	for BM in (range(BMS + 1)):
	    print('='*80)

	    nombre_BM_atras = input(f'Digite el nombre del BM {BM+1}: ')
	    vistaMas = float(input(f'Digite la vista más observada {BM+1}: '))
	    distancia_atras = float(input(f'Digite la distancia al BM atras {BM+1}: '))
	    nombre_BM_adelante = input(f'Digite el nombre del BM {BM+2}: ')
	    vistaMenos = float(input(f'Digite la vista menos observada {BM+2}: '))
	    distancia_adelante = float(input(f'Digite la distancia al BM adelante {BM+2}: '))

	    print('='*80)

	    datos_linea = [nombre_BM_atras, vistaMas, distancia_atras, nombre_BM_adelante, vistaMenos, distancia_adelante]
	    datos_medidos.append(datos_linea.copy())

	    if j != 0:
		sumVMAS = sumVMAS + datos_linea[1]
		sumdist_atras = sumdistafter + datos_linea[2]
		sumVMENOS = sumVMENOS + datos_linea[4]
		sumdist_adelante = sumdistnext + datos_linea[5]
		j += 1
	    else:
		j += 1

	dist = sumdist_atras + sumdist_adelante
	error_nivelación = sumVMAS - sumVMENOS
	corrección_nivelación = error_nivelación / dist

	print('El error de la nivelación es:', error_nivelación)
	print('La sumatoria de las vistas mas es:', sumVMAS)
	print('La sumatoria de las vistas menos es:', sumVMENOS)
	print('La distancia total es:', dist)
	print('La corrección de la nivelación es:', corrección_nivelación)
	print(datos_linea)

	datos_medidos[1].append(datos_medidos[1][3])

    elif CalNiv == "2":
        print("Eligio calculo por pesos")

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

        elif poligonal == "2":
            print("Eligio ajuste por método Brújula")
			#[A J U S T E  D E  P O L I G O N A L  P O R  E L  M E T O D O  D E  L A  B R U J U L A]


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
        elif poligonal == "2":
            print("Eligio ajuste por método Brujula")
        elif poligonal == "3":
            print("Eligio ajuste por método Tránsito")
        else:
            print("Opción no válida")
    else:
        print("Opción no válida")

else:
    print("Opción no válida")
