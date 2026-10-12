import tkinter as tk
from tkinter import messagebox
import re


def EnteroValido(valor):
    try:
        int(valor)
        return True
    except ValueError:
        messagebox.showerror("Error Edad", "Valor de edad equivocado")
        return False


def DecimalValido(valor):
    try:
        float(valor)
        return True
    except ValueError:
        messagebox.showerror("Error Estatura", "Valor de estatura equivocado")
        return False


def TelefonoValido(valor):
    return valor.isdigit() and len(valor) == 10


def TextoValido(valor):
    # Permite letras con acentos y la letra 'ñ' además de espacios
    return bool(re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", valor))


def borrar():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    rbSeleccionGenero.set(0)


def guardar():
    # .strip() elimina espacios vacíos accidentales al inicio o final
    nombres = tbNombre.get().strip()
    apellidos = tbApellidos.get().strip()
    edad = tbEdad.get().strip()
    tel = tbTelefono.get().strip()
    estatura = tbEstatura.get().strip()
    
    genero = ""
    if rbSeleccionGenero.get() == 1:
        genero = "Masculino"
    elif rbSeleccionGenero.get() == 2:
        genero = "Femenino"
    elif rbSeleccionGenero.get() == 3:
        genero = "No Definido"

    if (EnteroValido(edad) and DecimalValido(estatura) and
        TelefonoValido(tel) and TextoValido(nombres) and
        TextoValido(apellidos)):
        
        datos = (f"Nombre : {nombres}\n"
                 f"Apellidos : {apellidos}\n"
                 f"Edad : {edad}\n"
                 f"Telefono : {tel}\n"
                 f"Estatura : {estatura}\n"
                 f"Genero : {genero}")
        
        # encoding='utf-8' asegura que no haya problemas al guardar acentos o caracteres especiales
        with open("Datos3N_13Feb26.txt", "a", encoding="utf-8") as archivo:
            archivo.write(datos + "\n\n")
            
        messagebox.showinfo("Informacion", "Datos guardados correctamente \n\n" + datos)
    else:
        messagebox.showerror("Error", "Algunos de los campos tienen formato equivocado")


ventana = tk.Tk()
ventana.configure(bg="pink")
ventana.geometry("350x570")
ventana.title("Actividad 04 - Formulario de Registro Vr. 002")

rbSeleccionGenero = tk.IntVar()

tk.Label(ventana, text="Nombre : ", font=("Segoe UI", 12, "bold"), bg="pink").pack(padx=10, pady=4)
tbNombre = tk.Entry(ventana, width=35, justify="center")
tbNombre.pack()

tk.Label(ventana, text="Apellidos : ", font=("Segoe UI", 12, "bold"), bg="pink").pack(padx=10, pady=4)
tbApellidos = tk.Entry(ventana, width=35, justify="center")
tbApellidos.pack()

tk.Label(ventana, text="Edad : ", font=("Segoe UI", 12, "bold"), bg="pink").pack(padx=10, pady=4)
tbEdad = tk.Entry(ventana, width=15, justify="center")
tbEdad.pack()

tk.Label(ventana, text="Estatura : ", font=("Segoe UI", 12, "bold"), bg="pink").pack(padx=10, pady=4)
tbEstatura = tk.Entry(ventana, width=15, justify="center")
tbEstatura.pack()

tk.Label(ventana, text="Telefono : ", font=("Segoe UI", 12, "bold"), bg="pink").pack(padx=10, pady=4)
tbTelefono = tk.Entry(ventana, width=35, justify="center")
tbTelefono.pack()

gb = tk.LabelFrame(ventana, text="Seleccione un Genero : ", padx=10, pady=6, bg="pink")
gb.pack(padx=10, pady=6)
rbMasculino = tk.Radiobutton(gb, text="Masculino", value=1, variable=rbSeleccionGenero, bg="pink")
rbMasculino.grid(column=1, row=1, padx=4)
rbFemenino = tk.Radiobutton(gb, text="Femenino", value=2, variable=rbSeleccionGenero, bg="pink")
rbFemenino.grid(column=2, row=1, padx=4)
rbNoDefinido = tk.Radiobutton(gb, text="No Definido", value=3, variable=rbSeleccionGenero, bg="pink")
rbNoDefinido.grid(column=3, row=1, padx=4)

gb2 = tk.LabelFrame(ventana, text="", bg="pink", bd=0)
gb2.pack(padx=10, pady=6)
btnGuardar = tk.Button(gb2, text="Guardar", width=10, padx=5, pady=4, command=guardar)
btnGuardar.grid(column=1, row=1, padx=5)
btnBorrar = tk.Button(gb2, text="Borrar", width=10, padx=5, pady=4, command=borrar)
btnBorrar.grid(column=2, row=1, padx=5)

ventana.mainloop()
