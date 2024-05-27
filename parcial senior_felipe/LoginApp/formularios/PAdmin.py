import tkinter as tk
import json
from tkinter import messagebox, ttk
import util.generic as utl
class PAdmin(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        self.tipo_action ="Guardar"
        self.tipo_user = ""
        super().__init__()
        self.title("Panel Administrativo")
        self.resizable(False, False)
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = self.winfo_screenwidth() 
        self.alto_pantalla = self.winfo_screenheight() 

        # Establecer el tamaño completo de la ventana
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)  
        menuuser = tk.Menu(menubar, tearoff=0)  
        menuuser.add_command(label="Administracion de Usuarios", command=self.main_usuarios)  
        menubar.add_cascade(label="Usuarios", menu=menuuser)  

        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Administracion de Cliente", command=self.main_clientes)  
        menubar.add_cascade(label="Clientes", menu=menuclientes)

        menucategorias = tk.Menu(menubar, tearoff=0)
        menucategorias.add_command(label="Administracion de Animales", command=self.main_animales)   
        menubar.add_cascade(label="Animales", menu=menucategorias)   

        menuproducto = tk.Menu(menubar, tearoff=0)
        menuproducto.add_command(label="Administracion de TIpos", command=self.main_tipos)    
        menubar.add_cascade(label="Tipos", menu=menuproducto)

        menuventas = tk.Menu(menubar, tearoff=0)
        menuventas.add_command(label="Administracion de Atenciones", command=self.main_atenciones)
        menubar.add_cascade(label="Atenciones", menu=menuventas)

        self.config(menu=menubar)

        # frame user_info

        self.frame_user_info = tk.Frame(self, bd=0,relief=tk.SOLID, width=200)
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5,fill="y")
        texto=tk.Label(self.frame_user_info, text="PANEL ADMINISTRATIVO", font=('Times', 20))
        texto.pack(padx=20,pady=4)
        self.usrimg = utl.leer_imagen(r"C:\Users\Biblioteca\Desktop\parcial senior_felipe\LoginApp\imagenes\userinfo.png", (128, 128))

        tk.Label(self.frame_user_info,image=self.usrimg).pack(padx=30,pady=4)
        tk.Label(self.frame_user_info, text=self.name, font=('Times', 14)).pack(padx=40,pady=4)
        tk.Label(self.frame_user_info, text=self.email, font=('Times', 14)).pack(padx=50,pady=4)

        
        #frame_data
        
        self.frame_data = tk.Frame(self, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        textobienvenida=tk.Label(self.frame_data, text="BIENVENIDO AL SISTEMA", font=('Times', 20))
        textobienvenida.pack(padx=20,pady=4)

        #frame_dinamyc
        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}",background="honeydew3")
        self.frame_dinamyc.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

    def main_usuarios(self):
        self.formulario_usuario()
        self.listar_usuarios()
    
    def formulario_usuario(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="\uf0c9 REGISTRO DE USUARIOS", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=30)
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cedula:", font=('Times',14))
        labelcedula.place(x=70, y=100)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=40)
        self.ccedula.place(x=220, y=100)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre completo:", font=('Times',14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=40)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame_dinamyc,text="Username:", font=('Times',14))
        labelusuario.place(x=70,y=160)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=40)
        self.cusuario.place(x=220,y=160)

        labelclave = tk.Label(self.frame_dinamyc,text="Contraseña:", font=('Times',14))
        labelclave.place(x=500,y=100)
        self.cclave = tk.Entry(self.frame_dinamyc, width=40, show="*")
        self.cclave.place(x=600, y=100)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo:", font=('Times',14))
        labelcorreo.place(x=500,y=130)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=40)
        self.ccorreo.place(x=600, y=130)

        labeltipo = tk.Label(self.frame_dinamyc, text="Rol:", font=('Times',14))
        labeltipo.place(x=500,y=160)
        self.listatipo = tk.Listbox(self.frame_dinamyc, selectmode="Single", width=40, height=2)
        self.listatipo.place(x=600,y=160)
        self.listatipo.insert(1, "Administrador")
        self.listatipo.insert(2, "Vendedor")

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 GUARDAR", font=('Times',14), command=self.save_user,background="green")
        btnguardar.place(x=870, y=130)
    
    def listar_usuarios(self):
        tk.Label(self.frame_dinamyc,text="\uf00b LISTADO DE USUARIOS", font=('Times',16),fg="#9fa8da").place(x=70, y=200)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("NombreCompleto", "Username", "Email", "Rol"))
        self.tablausuarios.heading("#0", text="Cedula")
        self.tablausuarios.heading("NombreCompleto", text="Nombre Completo")
        self.tablausuarios.heading("Username", text="Usuario")
        self.tablausuarios.heading("Email", text="Email")
        self.tablausuarios.heading("Rol", text="Rol")
        with open(r"C:\Users\Biblioteca\Desktop\parcial senior_felipe\LoginApp\formularios\data\db_users.json", "r", encoding='utf-8') as self.file:
                self.db_users = json.load(self.file)
                for usuarios in self.db_users["users"]:
                    self.tablausuarios.insert("", "end", text=f'{usuarios["id"]}',values=(f'{usuarios["name"]}',f'{usuarios["username"]}',f'{usuarios["email"]}', f'{usuarios["role"]}'))
        self.tablausuarios.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="\uf0c7 Eliminar", font=('Times',14), command=self.delete_user,background="red")
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="\uf0c7 Actualizar", font=('Times',14), command=self.update_user,background="yellow")
        btnupdate.place(x=200, y=520)

    def save_user(self):
        for index in self.listatipo.curselection():
            self.tipo_user = self.listatipo.get(index)
        if self.ccedula.get() =="" or self.cnombre.get() == "" or self.cusuario.get() == "" or self.ccorreo.get() == "" or self.cclave.get() == "" :
            messagebox.showinfo('Info',"Debe llenar todos los campos",parent=self)
            return 
        else:
                with open(r"C:\Users\Biblioteca\Desktop\parcial senior_felipe\LoginApp\formularios\data\db_users.json", "r", encoding='utf-8') as self.file:
                        self.db_users = json.load(self.file)

                        if self.tipo_action == "Actualizar":

                            for usuarios in self.db_users["users"]:
                                if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                                    usuarios["id"] = self.ccedula.get()
                                    usuarios["name"] = self.cnombre.get()
                                    usuarios["username"] = self.cusuario.get()
                                    usuarios["password"] =  self.cclave.get()
                                    usuarios["email"] = self.ccorreo.get()
                                    usuarios["role"] = self.tipo_user
                                    with open(r"C:\Users\Biblioteca\Desktop\parcial senior_felipe\LoginApp\formularios\data\db_users.json", 'w') as jf: 
                                        json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                                        messagebox.showinfo('Info',"Usuario actualizado con exito",parent=self)
                                        #self.listar_usuarios()
                                        self.limpiar_panel(self.frame_dinamyc)
                    
                        else:
                            self.db_users["users"].append({
                                            'id': self.ccedula.get(),
                                            'name': self.cnombre.get(),
                                            'username': self.cusuario.get(),
                                            'password': self.cclave.get(),
                                            'email': self.ccorreo.get(),
                                            'role':self.tipo_user
                                            })
                            with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\db_users.json", 'w') as jf: 
                                json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                                messagebox.showinfo('Info',"Usuario registrado con exito",parent=self)
                                self.limpiar_panel(self.frame_dinamyc) 


    def delete_user(self):
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\db_users.json", "r", encoding='utf-8') as self.file:
                self.db_users = json.load(self.file)
                for usuarios in self.db_users["users"]:
                    if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.db_users["users"].remove(usuarios)
                        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\db_users.json", 'w') as jf:
                            json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                            messagebox.showinfo('Info',"Usuario eliminado con exito",parent=self)
                            self.limpiar_panel(self.frame_dinamyc)
                            break



    def update_user(self):
                with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\db_users.json", "r", encoding='utf-8') as self.file:
                    self.db_users = json.load(self.file)

                for usuarios in self.db_users["users"]:
                    if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.ccedula.delete(0, tk.END)
                        self.ccedula.insert(0, usuarios["id"])
                        self.ccedula.config(state="disabled")
                        self.cnombre.delete(0, tk.END)
                        self.cnombre.insert(0,usuarios["name"])
                        self.cusuario.delete(0, tk.END)
                        self.cusuario.insert(0,usuarios["username"])
                        self.cclave.delete(0, tk.END)
                        self.cclave.insert(0,usuarios["password"])
                        self.ccorreo.delete(0, tk.END)
                        self.ccorreo.insert(0,usuarios["email"])
                        self.tipo_action = "Actualizar"


#### frame clientes ######

    def main_clientes(self):
        self.formulario_cliente()
        self.listar_cliente()
    
    def formulario_cliente(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="\uf0c9 REGISTRO DE CLIENTES", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=30)
        
        labelcelular = tk.Label(self.frame_dinamyc,text="Telefono:", font=('Times',14))
        labelcelular.place(x=70, y=100)
        self.celular = tk.Entry(self.frame_dinamyc, width=40)
        self.celular.place(x=220, y=100)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre:", font=('Times',14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=40)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame_dinamyc,text="Username:", font=('Times',14))
        labelusuario.place(x=70,y=160)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=40)
        self.cusuario.place(x=220,y=160)

        labelclave = tk.Label(self.frame_dinamyc,text="Contraseña:", font=('Times',14))
        labelclave.place(x=500,y=100)
        self.cclave = tk.Entry(self.frame_dinamyc, width=40, show="*")
        self.cclave.place(x=600, y=100)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo:", font=('Times',14))
        labelcorreo.place(x=500,y=130)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=40)
        self.ccorreo.place(x=600, y=130)

        btnguardar = tk.Button(self.frame_dinamyc, text="REGISTRAR", font=('Times',14), command=self.save_cliente ,background="green")
        btnguardar.place(x=600, y=160)
    
    def listar_cliente(self):
        tk.Label(self.frame_dinamyc,text="\uf00b LISTADO DE CLIENTES", font=('Times',16),fg="#9fa8da").place(x=70, y=200)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("Nombre", "Username", "Email"))
        self.tablausuarios.heading("#0", text="Telefono")
        self.tablausuarios.heading("Nombre", text="Nombre")
        self.tablausuarios.heading("Username", text="Usuario")
        self.tablausuarios.heading("Email", text="Email")
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_clientes.json", "r", encoding='utf-8') as self.file:
                self.clientes = json.load(self.file)
                for clientes in self.clientes["clientes"]:
                    self.tablausuarios.insert("", "end", text=f'{clientes["telefono"]}',values=(f'{clientes["name"]}',f'{clientes["username"]}',f'{clientes["email"]}'))
        self.tablausuarios.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="\uf0c7 Eliminar", font=('Times',14), command=self.delete_cliente ,background="red")
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="\uf0c7 Actualizar", font=('Times',14), command=self.update_cliente,background="yellow")
        btnupdate.place(x=200, y=520)

    def save_cliente(self):
        if self.celular.get() =="" or self.cnombre.get() == "" or self.cusuario.get() == "" or self.ccorreo.get() == "" or self.cclave.get() == "" :
            messagebox.showinfo('Info',"Debe llenar todos los campos",parent=self)
            return 
        else:
                with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_clientes.json", "r", encoding='utf-8') as self.file:
                        self.clientes = json.load(self.file)

                        if self.tipo_action == "Actualizar":

                            for clientes in self.clientes["clientes"]:
                                if clientes["telefono"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                                    clientes["telefono"] = self.celular.get()
                                    clientes["name"] = self.cnombre.get()
                                    clientes["username"] = self.cusuario.get()
                                    clientes["password"] =  self.cclave.get()
                                    clientes["email"] = self.ccorreo.get()
                                    with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_clientes.json", 'w') as jf: 
                                        json.dump(self.clientes, jf, indent=4, ensure_ascii=True)
                                        messagebox.showinfo('Info',"Actualizacion exitosa",parent=self)
                                        #self.listar_usuarios()
                                        self.limpiar_panel(self.frame_dinamyc)
                    
                        else:
                            self.clientes["clientes"].append({
                                            'telefono': self.celular.get(),
                                            'name': self.cnombre.get(),
                                            'username': self.cusuario.get(),
                                            'password': self.cclave.get(),
                                            'email': self.ccorreo.get()
                                        
                                            })
                            with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_clientes.json", 'w') as jf: 
                                json.dump(self.clientes, jf, indent=4, ensure_ascii=True)
                                messagebox.showinfo('Info',"Registro Exitoso",parent=self)
                                self.limpiar_panel(self.frame_dinamyc) 


    def delete_cliente(self):
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_clientes.json", "r", encoding='utf-8') as self.file:
                self.clientes = json.load(self.file)
                for clientes in self.clientes["clientes"]:
                    if clientes["telefono"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.clientes["clientes"].remove(clientes)
                        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_clientes.json", 'w') as jf:
                            json.dump(self.clientes, jf, indent=4, ensure_ascii=True)
                            messagebox.showinfo('Info',"Eliminado exitosamente",parent=self)
                            self.limpiar_panel(self.frame_dinamyc)
                            break



    def update_cliente(self):
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_clientes.json", "r", encoding='utf-8') as self.file:
                self.clientes = json.load(self.file)

                for clientes in self.clientes["clientes"]:
                    if clientes["telefono"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.celular.delete(0, tk.END)
                        self.celular.insert(0, clientes["telefono"])
                        self.cnombre.delete(0, tk.END)
                        self.cnombre.insert(0,clientes["name"])
                        self.cusuario.delete(0, tk.END)
                        self.cusuario.insert(0,clientes["username"])
                        self.cclave.delete(0, tk.END)
                        self.cclave.insert(0,clientes["password"])
                        self.ccorreo.delete(0, tk.END)
                        self.ccorreo.insert(0,clientes["email"])
                        self.tipo_action = "Actualizar"


### Animales ####

    def main_animales(self):
        self.formulario_animales()
        self.listar_animales()
    
    def formulario_animales(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="REGISTRO DE ANIMALES", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=30)

        labeltamaño = tk.Label(self.frame_dinamyc,text="Tamaño:", font=('Times',14))
        labeltamaño.place(x=70, y=100)
        self.tamaño = tk.Entry(self.frame_dinamyc, width=40)
        self.tamaño.place(x=220, y=100)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre del animal:", font=('Times',14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=40)
        self.cnombre.place(x=220, y=130)

        labelgenero = tk.Label(self.frame_dinamyc,text="Genero:", font=('Times',14))
        labelgenero.place(x=70,y=160)
        self.genero = tk.Entry(self.frame_dinamyc, width=40)
        self.genero.place(x=220,y=160)

        labelraza = tk.Label(self.frame_dinamyc,text="Raza:", font=('Times',14))
        labelraza.place(x=500,y=100)
        self.raza = tk.Entry(self.frame_dinamyc, width=40)
        self.raza.place(x=600, y=100)

        btnguardar = tk.Button(self.frame_dinamyc, text="REGISTRAR", font=('Times',14), command=self.save_animales,background="green")
        btnguardar.place(x=600, y=130)
    
    def listar_animales(self):
        tk.Label(self.frame_dinamyc,text="LISTADO DE ANIMALES", font=('Times',16),fg="#9fa8da").place(x=70, y=200)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("genero", "raza", "tamaño"))
        self.tablausuarios.heading("#0", text="nombre")
        self.tablausuarios.heading("genero", text="genero")
        self.tablausuarios.heading("raza", text="raza")
        self.tablausuarios.heading("tamaño", text="tamaño")
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_animales.json", "r", encoding='utf-8') as self.file:
                self.animales = json.load(self.file)
                for animales in self.animales["animales"]:
                    self.tablausuarios.insert("", "end", text=f'{animales["nombre"]}',values=(f'{animales["genero"]}',f'{animales["raza"]}',f'{animales["tamaño"]}'))
        self.tablausuarios.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="\uf0c7 Eliminar", font=('Times',14), command=self.delete_animales,background="red")
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="\uf0c7 Actualizar", font=('Times',14), command=self.update_animales,background="yellow")
        btnupdate.place(x=200, y=520)

    def save_animales(self):
        if self.tamaño.get() == "" or self.cnombre.get() == "" or self.genero.get() == "" or self.raza.get() == "" :
            messagebox.showinfo('Info',"Debe llenar todos los campos",parent=self)
            return 
        else:
                with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_animales.json", "r", encoding='utf-8') as self.file:
                        self.animales = json.load(self.file)

                        if self.tipo_action == "Actualizar":

                            for animales in self.animales["animales"]:
                                if animales["nombre"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                                    animales["nombre"] = self.cnombre.get()
                                    animales["genero"] = self.genero.get()
                                    animales["raza"] = self.raza.get()
                                    animales["tamaño"] =  self.tamaño.get()
                                    
                                    with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_animales.json", 'w') as jf: 
                                        json.dump(self.animales, jf, indent=4, ensure_ascii=True)
                                        messagebox.showinfo('Info',"Actualizado con exito",parent=self)
                                        #self.listar_usuarios()
                                        self.limpiar_panel(self.frame_dinamyc)
                    
                        else:
                            self.animales["animales"].append({
                                            'nombre': self.cnombre.get(),
                                            'genero': self.genero.get(),
                                            'raza': self.raza.get(),
                                            'tamaño': self.tamaño.get()
                                            
                                        
                                            })
                            with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_animales.json", 'w') as jf: 
                                json.dump(self.animales, jf, indent=4, ensure_ascii=True)
                                messagebox.showinfo('Info',"Registro con exito",parent=self)
                                self.limpiar_panel(self.frame_dinamyc) 


    def delete_animales(self):
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_animales.json", "r", encoding='utf-8') as self.file:
                self.animales = json.load(self.file)
                for animales in self.animales["animales"]:
                    if animales["nombre"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.animales["animales"].remove(animales)
                        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_animales.json", 'w') as jf:
                            json.dump(self.animales, jf, indent=4, ensure_ascii=True)
                            messagebox.showinfo('Info',"Eliminado con exito",parent=self)
                            self.limpiar_panel(self.frame_dinamyc)
                            break



    def update_animales(self):
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_animales.json", "r", encoding='utf-8') as self.file:
                self.animales = json.load(self.file)


                for animales in self.animales["animales"]:
                    if animales["nombre"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.tamaño.delete(0, tk.END)
                        self.tamaño.insert(0, animales["tamaño"])
                        self.cnombre.delete(0, tk.END)
                        self.cnombre.insert(0,animales["nombre"])
                        self.genero.delete(0, tk.END)
                        self.genero.insert(0,animales["genero"])
                        self.raza.delete(0, tk.END)
                        self.raza.insert(0,animales["raza"])
                        self.tipo_action = "Actualizar"

## tipos ###

    def main_tipos(self):
        self.formulario_tipos()
        self.listar_tipos()

    
    def formulario_tipos(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="\uf0c9 REGISTRO DE TIPOS", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=30)
        
        labelproblema = tk.Label(self.frame_dinamyc,text="Problema o discapacidad:", font=('Times',12))
        labelproblema.place(x=70, y=100)
        self.problema = tk.Entry(self.frame_dinamyc, width=40)
        self.problema.place(x=270, y=100)


        labeltipo = tk.Label(self.frame_dinamyc,text="Tipo de Animal:", font=('Times',14))
        labeltipo.place(x=70, y=130)
        self.tipo = tk.Entry(self.frame_dinamyc, width=40)
        self.tipo.place(x=270, y=130)


        btnguardar = tk.Button(self.frame_dinamyc, text="REGISTRAR", font=('Times',14), command=self.save_tipos,background="green")
        btnguardar.place(x=600, y=130)
    
    def listar_tipos(self):
        tk.Label(self.frame_dinamyc,text="\uf00b LISTADO DE TIPOS", font=('Times',16),fg="#9fa8da").place(x=70, y=200)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("Tipo"))
        self.tablausuarios.heading("#0", text="Problema")
        self.tablausuarios.heading("Tipo", text="Tipo")
        
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_tipos.json", "r", encoding='utf-8') as self.file:
                self.tipos = json.load(self.file)
                for tipos in self.tipos["tipos"]:
                    self.tablausuarios.insert("", "end", text=f'{tipos["problema"]}',values=(f'{tipos["tipo"]}'))
        self.tablausuarios.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="Eliminar", font=('Times',14), command=self.delete_tipos,background="red")
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="Actualizar", font=('Times',14), command=self.update_tipos,background="yellow")
        btnupdate.place(x=200, y=520)

    def save_tipos(self):
        if self.problema.get() =="" or self.tipo == "" :
            messagebox.showinfo('Info',"Debe llenar todos los campos",parent=self)
            return 
        else:
                with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_tipos.json", "r", encoding='utf-8') as self.file:
                        self.tipos = json.load(self.file)

                        if self.tipo_action == "Actualizar":

                            for tipos in self.tipos["tipos"]:
                                if tipos["problema"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                                    tipos["problema"] = self.problema.get()
                                    tipos["tipo"] = self.tipo.get()
                                    
                                    
                                    with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_tipos.json", 'w') as jf: 
                                        json.dump(self.tipos, jf, indent=4, ensure_ascii=True)
                                        messagebox.showinfo('Info',"Actualizacion exitosa",parent=self)
                            
                                        self.limpiar_panel(self.frame_dinamyc)
                    
                        else:
                            self.tipos["tipos"].append({
                                            'problema': self.problema.get(),
                                            'tipo': self.tipo.get()
                                        
                                            })
                            with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_tipos.json", 'w') as jf: 
                                json.dump(self.tipos, jf, indent=4, ensure_ascii=True)
                                messagebox.showinfo('Info',"Registrado exitoso",parent=self)
                                self.limpiar_panel(self.frame_dinamyc) 


    def delete_tipos(self):
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_tipos.json", "r", encoding='utf-8') as self.file:
                self.tipos = json.load(self.file)
                for tipos in self.tipos["tipos"]:
                    if tipos["problema"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.tipos["tipos"].remove(tipos)
                        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_tipos.json", 'w') as jf:
                            json.dump(self.tipos, jf, indent=4, ensure_ascii=True)
                            messagebox.showinfo('Info',"Eliminado con exito",parent=self)
                            self.limpiar_panel(self.frame_dinamyc)
                            break


    def update_tipos(self):
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_tipos.json", "r", encoding='utf-8') as self.file:
                self.tipos = json.load(self.file)

                for tipos in self.tipos["tipos"]:
                    if tipos["problema"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.problema.delete(0, tk.END)
                        self.problema.insert(0, tipos["problema"])
                
                        self.tipo.delete(0, tk.END)
                        self.tipo.insert(0,tipos["tipo"])
                        
                        self.tipo_action = "Actualizar"

## Atenciones ##

    def main_atenciones(self):
        self.formulario_atenciones()
        self.listar_atenciones()

    def clientes_e(self, event):
        animal = self.cliente_e.get()
        
    
    def formulario_atenciones(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="REGISTRO DE ATENCIONES", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=30)
        
        labelatencion = tk.Label(self.frame_dinamyc,text="Atencion o Especialidad:", font=('Times',12))
        labelatencion.place(x=70, y=100)
        self.atencion = tk.Entry(self.frame_dinamyc , width=40)
        self.atencion.place(x= 270, y=100)

        labelvalor = tk.Label(self.frame_dinamyc,text="Valor:", font=('Times',14))
        labelvalor.place(x=70, y=150)
        self.valor = tk.Entry(self.frame_dinamyc , width=40)
        self.valor.place(x= 270, y=150)


        btnguardar = tk.Button(self.frame_dinamyc, text="REGISTRAR", font=('Times',14), command=self.save_atenciones,background="green")
        btnguardar.place(x= 600, y= 120 )
    
    def listar_atenciones(self):
        tk.Label(self.frame_dinamyc,text="LISTADO DE ATENCIONES", font=('Times',16),fg="#9fa8da").place(x=70, y=200)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("Precios"))
        self.tablausuarios.heading("#0", text="Atencion")
        self.tablausuarios.heading("Precios", text="Precios")
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_atenciones.json", "r", encoding='utf-8') as self.file:
                self.aten = json.load(self.file)
                for atenci in self.aten["atencion"]:
                    self.tablausuarios.insert("", "end", text=f'{atenci["atencion"]}',values=(f'{atenci["valor"]}'))
        self.tablausuarios.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="Eliminar", font=('Times',14), command=self.delete_atenciones,background="red")
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="Actualizar", font=('Times',14), command=self.update_atenciones,background="yellow")
        btnupdate.place(x=200, y=520)

    def save_atenciones(self):
        if self.atencion.get() == "" or self.valor.get() == "":
            messagebox.showinfo('Info',"Debe llenar todos los campos",parent=self)
            return 
        else:
                with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_atenciones.json", "r", encoding='utf-8') as self.file:
                        self.aten = json.load(self.file)

                        if self.tipo_action == "Actualizar":

                            for atenci in self.aten["atencion"]:
                                if atenci["atencion"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                                    atenci["atencion"] = self.atencion.get()
                                    atenci["valor"] = self.valor.get()
                                
                                    with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_atenciones.json", 'w') as jf: 
                                        json.dump(self.aten, jf, indent=4, ensure_ascii=True)
                                        messagebox.showinfo('Info',"Actualizacion exitosa",parent=self)
                            
                                        self.limpiar_panel(self.frame_dinamyc)
                    
                        else:
                            self.aten["atencion"].append({
                                            'atencion': self.atencion.get(),
                                            'valor': self.valor.get()

                                            })
                            with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_atenciones.json", 'w') as jf: 
                                json.dump(self.aten, jf, indent=4, ensure_ascii=True)
                                messagebox.showinfo('Info',"Atencion registrada con exito",parent=self)
                                self.limpiar_panel(self.frame_dinamyc) 


    def delete_atenciones(self):
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_atenciones.json", "r", encoding='utf-8') as self.file:
                self.aten = json.load(self.file)
                for atenci in self.aten["atencion"]:
                    if atenci["atencion"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.aten["atencion"].remove(atenci)
                        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_atenciones.json", 'w') as jf:
                            json.dump(self.aten, jf, indent=4, ensure_ascii=True)
                            messagebox.showinfo('Info',"Eliminada con exito",parent=self)
                            self.limpiar_panel(self.frame_dinamyc)
                            break


    def update_atenciones(self):
        with open(r"C:\Users\USUARIO\Desktop\parcial senior_felipe\LoginApp\formularios\data\data_atenciones.json", "r", encoding='utf-8') as self.file:
                self.aten = json.load(self.file)

                for atenci in self.aten["atencion"]:
                    if atenci["atencion"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.atencion.delete(0, tk.END)
                        self.atencion.insert(0, atenci["atencion"])
                        self.valor.delete(0, tk.END)
                        self.valor.insert(0,atenci["valor"])
                        
                        self.tipo_action = "Actualizar"
        

    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()
    def logout(self):
        self.destroy()