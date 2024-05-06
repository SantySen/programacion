import tkinter as tk
from PIL import Image, ImageTk


ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("800x500")


frame_izquierdo = tk.Frame(ventana,bg="white")
frame_derecho = tk.Frame(ventana, bg="gray")

image = tk.PhotoImage(file="\\Users\\Biblioteca\\Desktop\\Prog IIIcorte\\logo.png")

label = tk.Label(image=image)
label.place(x="50", y= "100", width= "203")


 
frame_izquierdo.place(x=0,y=0,width= 400,height="800")
frame_derecho.place(x=400,y=0,width= 400,height="800")




titulo_label = tk.Label(frame_derecho, text="Inicio de Sesión", font=("Arial black", 18))
titulo_label.pack()


usuario_label = tk.Label(frame_derecho, text="Usuario:")
usuario_entry = tk.Entry(frame_derecho)
usuario_label.pack()
usuario_entry.pack()


clave_label = tk.Label(frame_derecho, text="Clave:")
clave_entry = tk.Entry(frame_derecho, show="*")  
clave_label.pack()
clave_entry.pack()


boton_ingresar = tk.Button(frame_derecho, text="Ingresar", command=lambda: print("Ingresando..."))
boton_ingresar.pack()


ventana.mainloop()
