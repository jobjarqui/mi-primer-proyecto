from tkinter import *
from tkinter import ttk


#Nuestra clase padre(ventana)
class Ventana(Frame):


    def __init__(self, master=None):
        super().__init__(master, width=680, height=260)
        self.master = master
        self.pack()
        self.create_widgets()


#Aqui creo los metodos que va llevar cada widgets, metodos miembros
    def fNuevo(self):
        pass
    def fModificar(self):
        pass
    def fEliminar(self):
        pass
    def fGuardar(self):
        pass
    def fCancelar(self):
        pass




#Aqui creamos los widgets
#Utilizamos los frame para el diseño 
#Nuestro contenedro el Frame1
#por eso lleva el self para mandarlo a llmar desde fuera
    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=93, height=259)
        
        self.btnNuevo=Button(frame1, text="Nuevo", command=self.fNuevo, bg="blue", fg="White")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)

        self.btnModificar=Button(frame1, text="Modificar", command=self.fModificar, bg="Blue", fg="White")
        self.btnModificar.place(x=5, y=90, width=80, height=30)

        self.btnEliminar=Button(frame1, text="Eliminar", command=self.fEliminar, bg="Blue", fg="White")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)


        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=95, y=0, width=150, height=259)

#Usamos label
#el label no es miembro de mi clase, esta contenido en el frame2
        lbl1 = Label(frame2, text="ISO3: ")
        lbl1.place(x=3,y=5)
        self.txtISO3=Entry(frame2)
        self.txtISO3.place(x=3,y=25,width=50, height=20)

        lbl2 = Label(frame2, text="Country Name: ")
        lbl2.place(x=3,y=55)
        self.txtName=Entry(frame2)
        self.txtName.place(x=3,y=75,width=100, height=20)

        lbl3 = Label(frame2, text="Capital: ")
        lbl3.place(x=3,y=105)
        self.txtCapital=Entry(frame2)
        self.txtCapital.place(x=3,y=125,width=100, height=20)

        lbl4 = Label(frame2, text="Currency Code: ")
        lbl4.place(x=3,y=155)
        self.txtCurrency=Entry(frame2)
        self.txtCurrency.place(x=3,y=175,width=50, height=20)


#dentro los metodos-miembros donde estan ubicados los metodos de los 
#Estan en el mismo frame2
        self.btnGuardar=Button(frame2, text="Guardar", command=self.fGuardar, bg="Green", fg="White")
        self.btnGuardar.place(x=10,y=210,width=60, height=30)
        self.btnCancelar=Button(frame2, text="Cancelar", command=self.fCancelar, bg="Red", fg="White")
        self.btnCancelar.place(x=80,y=210,width=60, height=30)

#las 4 cuatras columnas que se van a crear, un objeto que es miembro igual de la clase
        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4"))
        self.grid.column("#0", width=0, stretch=CENTER)
        self.grid.column("col1",anchor=CENTER, width=60)
        self.grid.column("col2", anchor=CENTER, width=90)
        self.grid.column("col3", anchor=CENTER, width=90)
        self.grid.column("col4", anchor=CENTER, width=90)


#Encabezados para las 5 columnas
#Ocupamos el metodo (Heading) para los encabezados
        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4"))
        self.grid.column("#0", Text="ID",stretch=CENTER)
        self.grid.column("col1",Text="ISO3",anchor=CENTER)
        self.grid.column("col2",Text="Country Name", anchor=CENTER)
        self.grid.column("col3",Text="Capital", anchor=CENTER)
        self.grid.column("col4",Text="Currency Code", anchor=CENTER)


        self.grid.place(x=247,y=0,width=420, height=259)


        