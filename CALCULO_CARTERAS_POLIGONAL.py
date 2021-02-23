#CREANDO LOGIN CON PYTHON Y TKINTER.

#IMPORTAMOS LIBRERIAS NECESARIAS.
from tkinter import *
import os

#CREAMOS VENTANA PRINCIPAL
def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Programa de Calculo Carteras")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack()
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack()
    Label(text="").pack()
    ventana_principal.mainloop()
    

# CREAMOS VENTANA PARA REGISTRO
def registro () :
    global ventana_registro
    ventana_registro = Toplevel (ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")

    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar()
    clave = StringVar()

    Label(ventana_registro, text="Introduzca datos", bg="lightGreen").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label (ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario)
    entrada_nombre.pack()
    etiqueta_clave = Label (ventana_registro, text="Contrasena * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*')
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="lightGreen", command = registro_usuario).pack()

#REGISTRO USUARIO

def registro_usuario () :
    usuario_info = nombre_usuario.get ()
    clave_info = clave.get ()

    file = open (usuario_info, "w")
    file.write (usuario_info + "\n")
    file.write (clave_info)
    file.close ()

    entrada_nombre.delete (0, END)
    entrada_clave.delete (0, END)

    Label (ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()


def login () :
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()

    global verifica_usuario
    global verifica_clave

    verifica_usuario = StringVar()
    verifica_clave = StringVar()

    global entrada_login_usuario
    global entrada_login_clave

    Label (ventana_login, text="Nombre usuario * ") .pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label (ventana_login, text="") .pack()
    Label (ventana_login, text="Contraseña * ") .pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= "*")
    entrada_login_clave.pack()
    Label (ventana_login, text="") .pack()
    Button (ventana_login, text="Acceder", width=10, height=1, command = ventana_login) .pack()

def ventana_login ():
    usuariol = verifica_usuario.get ()
    clavel = verifica_clave.get ()
    entrada_login_usuario.delete (0, END)
    entrada_login_clave.delete (0, END)

    lista_archivos = os.listdir()#
    if usuariol in lista_archivos:
        archivol = open(usuariol, "r")
        verifica = archivol.read().splitlines()
        if clavel in verifica:
            exito_login()

        else:
            no_clave ()

    else:
        no_usuario ()

def no_usuario ():
    global ventana_no_usuario
    ventana_no_usuario =Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack()

def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito") .pack ()
    Button(ventana_exito, text="OK", command=borrar_exito_login) .pack ()

def no_clave() :
        global ventana_no_clave
        ventana_no_clave = Toplevel (ventana_login)
        ventana_no_clave.title("ERROR")
        ventana_no_clave.geometry("150x100")
        Label(ventana_no_clave, text="Contraseña incorrecta ") .pack ()
        Button(ventana_no_clave, text="OK", command=borrar_no_clave) .pack ()

def borrar_exito_login () :
    ventana_exito.destroy ()

def borrar_no_clave () :
    ventana_no_clave.destroy ()

def borrar_no_usuario () :
    ventana_no_usuario.destroy ()

ventana_inicio ()