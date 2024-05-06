import tkinter as tk
from tkinter import messagebox

def mostrar_informacion():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    sexo = radio_var.get()
    ciudad = listbox_ciudad.get(listbox_ciudad.curselection())

    informacion = f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nSexo: {sexo}\nCiudad: {ciudad}"
    messagebox.showinfo("Información", informacion)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Formulario")

# Crear campos de entrada
entry_nombre = tk.Entry(ventana)
entry_apellido = tk.Entry(ventana)
entry_edad = tk.Entry(ventana)
entry_direccion = tk.Entry(ventana)
entry_telefono = tk.Entry(ventana)

# Crear radio buttons para el campo sexo
radio_var = tk.StringVar()
radio_masculino = tk.Radiobutton(ventana, text="Masculino", variable=radio_var, value="Masculino")
radio_femenino = tk.Radiobutton(ventana, text="Femenino", variable=radio_var, value="Femenino")

# Crear listbox para el campo ciudad
ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"]
listbox_ciudad = tk.Listbox(ventana, selectmode=tk.SINGLE)
for ciudad in ciudades:
    listbox_ciudad.insert(tk.END, ciudad)

# Crear botón de registro
boton_registrar = tk.Button(ventana, text="Registrar", command=mostrar_informacion)

# Posicionar elementos en la ventana
entry_nombre.pack()
entry_apellido.pack()
entry_edad.pack()
entry_direccion.pack()
entry_telefono.pack()
radio_masculino.pack()
radio_femenino.pack()
listbox_ciudad.pack()
boton_registrar.pack()

ventana.mainloop()
