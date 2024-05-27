import tkinter as tk
import json
from tkinter import messagebox,ttk
import util.generic as utl
class PVentas(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        super().__init__()
        self.title("Panel Ventas")
        self.resizable(False, False)
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = self.winfo_screenwidth() #método para obtener Ancho
        self.alto_pantalla = self.winfo_screenheight() #método para obtener Alto

        # Establecer el tamaño completo de la ventana
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)  

        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Confirmar Venta", command=self.form)  
        menuclientes.add_command(label="Listar Ventas", command=self.listar)  
        menubar.add_cascade(label="Ventas", menu=menuclientes)
        self.config(menu=menubar)

        # frame user info

        self.frame_user_info = tk.Frame(self, bd=0,relief=tk.SOLID, width=200)
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5,fill="y")
        texto=tk.Label(self.frame_user_info, text="PANEL VENTAS", font=('Times', 20))
        texto.pack(padx=20,pady=4)
        self.usrimg = utl.leer_imagen(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\imagenes\userinfo.png", (128, 128))
        self.imgusr=tk.Label(self.frame_user_info, image=self.usrimg)
        self.imgusr.pack(padx=30,pady=4)
        texto1=tk.Label(self.frame_user_info, text=self.name, font=('Times', 14))
        texto1.pack(padx=40,pady=4)
        texto1=tk.Label(self.frame_user_info, text=self.email, font=('Times', 14))
        texto1.pack(padx=50,pady=4)
        
        #frame_data
        
        self.frame_data = tk.Frame(self, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        textobienvenida=tk.Label(self.frame_data, text="BIENVENIDO AL SISTEMA", font=('Times', 20))
        textobienvenida.pack(padx=20,pady=4)

        #frame_dinamyc
        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}",background="honeydew3")
        self.frame_dinamyc.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

    def form(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="REGISTRO DE VENTAS", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=70)
        
        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre del Animal:", font=('Times',14))
        labelnombre.place(x=70, y=130)

        with open(r'C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_animales.json', 'r') as jf:
                animal = json.load(jf)
        
        nombreanimal = [nombre["nombre"] for nombre in animal["animales"]]

        self.animal = ttk.Combobox(self.frame_dinamyc,
            values= nombreanimal
        )
        self.animal.place(x= 240, y=130)
        self.animal.bind("<<ComboboxSelected>>", self.cliente_animal)
        
        label = tk.Label(self.frame_dinamyc,text="Servicio:", font=('Times',14))
        label.place(x=70, y=160)

        with open(r'C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_atenciones.json', 'r') as jf:
            servicio = json.load(jf)

        servicio_ = [serv["atencion"] for serv in servicio["atencion"]]

        self.servicio_animal = ttk.Combobox(self.frame_dinamyc,
            values= servicio_
        )
        self.servicio_animal.place(x= 220, y=160)
        self.servicio_animal.bind("<<ComboboxSelected>>", self.servicio_an)

        labeltipo = tk.Label(self.frame_dinamyc,text="Tipo de Animal:", font=('Times',14))
        labeltipo.place(x=70, y=190)

        with open(r'C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_tipos.json', 'r') as jf:
            tipo = json.load(jf)

        tipo_ = [tip["tipo"] for tip in tipo["tipos"]]

        self.tipo_animal = ttk.Combobox(self.frame_dinamyc,
            values= tipo_
        )
        self.tipo_animal.place(x= 220, y=190)
        self.tipo_animal.bind("<<ComboboxSelected>>", self.servicio_tipo)

        labelprcio = tk.Label(self.frame_dinamyc,text="precio:", font=('Times',14))
        labelprcio.place(x=70, y=220)

        self.prcio = tk.Entry(self.frame_dinamyc, font=('Times',14))
        self.prcio.place(x= 220, y=220)

        btnventa = tk.Button(self.frame_dinamyc, text="GUARDAR VENTA", font=('Times',14), command=self.venta)
        btnventa.place(x=70, y=350)

    def cliente_animal(self, event):
        global animall
        animall = self.animal.get()

    def servicio_an(self, event):
        global serr
        serr = self.servicio_animal.get()

    def servicio_tipo(self, event):
        global tipooo
        tipooo = self.tipo_animal.get()


    def listar(self):
            self.limpiar_panel(self.frame_dinamyc)
            labelform = tk.Label(self.frame_dinamyc,text="VENTAS TOTALES", font=('Times',16),fg="#9fa8da")
            labelform.place(x=70, y=70)
            self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("atencion","tipo","precio"))
            self.tablausuarios.heading("#0", text="animal")
            self.tablausuarios.heading("atencion", text="atencion")
            self.tablausuarios.heading("tipo", text="tipo")
            self.tablausuarios.heading("precio", text="precio")
            
            with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_ventas.json", "r", encoding='utf-8') as file:
                    ventas_totales = json.load(file)
                    for venta in ventas_totales["ventas"]:
                        self.tablausuarios.insert("", "end", text=f'{venta["animal"]}',values=(f'{venta["atencion"]}',f'{venta["tipo"]}',f'{venta["precio"]}'))
            self.tablausuarios.place(x=70, y=100)
    
    def venta(self):

        
                
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_ventas.json", "r", encoding='utf-8') as file:
                venta_total = json.load(file)

                venta_total["ventas"].append({
                        "animal": animall,
                        "atencion": serr,
                        "tipo": tipooo,
                        "precio": self.prcio.get()
                
                    })
                with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_ventas.json", 'w') as jf: 
                    json.dump(venta_total, jf, indent=4, ensure_ascii=True)
                    messagebox.showinfo('Info',"Venta registrada con exito",parent=self)
                
                    
    
    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()