CREANDO LOGIN CON PYTHON Y TKINTER.

#IMPORTAMOS LIBRERIAS NECESARIAS.
from tkinter import *
import os

def registro_usuario () :

    usuario_info = nombre_usuario.get ()
    clave_info = clave.get ()

    file = open (usuario_info, ¨w¨)
    file.write (usuario_info + ¨\n¨)
    file.write (clave_info)
    file.close ()
    
    entrada_nombre.delete (0, END)
    entreda_clave.delete (0, END)

    Label (ventana_registro, text=¨Registro completado con éxito¨, fg=¨green¨, font=(¨calibri¨, 11) .pack()

    def no_clave() :
        global ventana_no_clave
        ventana_no_clave = Toplevel (ventana_login)
        ventana_no_clave.title(¨ERROR¨)
        ventana_no_clave.geometry("150x100¨)
        Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
        Button(ventana_no_clave, text="OK", command=borrar_no_clave) .pack()