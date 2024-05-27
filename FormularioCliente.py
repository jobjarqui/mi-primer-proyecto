import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database as database

class FormularioCliente:

    def Formulario():
        try:
            base = Tk()
            base.geometry("1200x300")
            base.title("Formulario de Clientes")

            database.connect()

            def guardar():
                nombre = textBoxNombre.get()
                apellido = textBoxApellido.get()
                sexo = seleccionSexo.get()
                database.insert(nombre, apellido, sexo)
                messagebox.showinfo("Información", "Cliente guardado exitosamente")
                actualizar_treeview()

            def modificar():
                selected_item = tree.selection()[0]
                id = tree.item(selected_item, 'values')[0]
                nombre = textBoxNombre.get()
                apellido = textBoxApellido.get()
                sexo = seleccionSexo.get()
                database.update(id, nombre, apellido, sexo)
                messagebox.showinfo("Información", "Cliente modificado exitosamente")
                actualizar_treeview()

            def eliminar():
                selected_item = tree.selection()[0]
                id = tree.item(selected_item, 'values')[0]
                database.delete(id)
                messagebox.showinfo("Información", "Cliente eliminado exitosamente")
                actualizar_treeview()

            def actualizar_treeview():
                for row in tree.get_children():
                    tree.delete(row)
                for row in database.fetch_all():
                    tree.insert("", END, values=row)

            groupBox = LabelFrame(base, text="Datos del personal", padx=5, pady=5)
            groupBox.grid(row=0, column=0, padx=10, pady=10)

            labelId = Label(groupBox, text="Id:", width=13, font=("arial", 12)).grid(row=0, column=0)
            textBoxId = Entry(groupBox)
            textBoxId.grid(row=0, column=1)

            labelNombre = Label(groupBox, text="Nombre:", width=13, font=("arial", 12)).grid(row=1, column=0)
            textBoxNombre = Entry(groupBox)
            textBoxNombre.grid(row=1, column=1)

            labelApellido = Label(groupBox, text="Apellido:", width=13, font=("Arial", 12)).grid(row=2, column=0)
            textBoxApellido = Entry(groupBox)
            textBoxApellido.grid(row=2, column=1)

            labelSexo = Label(groupBox, text="Sexo:", width=13, font=("Arial", 12)).grid(row=3, column=0)
            seleccionSexo = tk.StringVar()
            combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino"], textvariable=seleccionSexo)
            combo.grid(row=3, column=1)
            seleccionSexo.set("Masculino")

            Button(groupBox, text="Guardar", width=10, command=guardar).grid(row=4, column=0)
            Button(groupBox, text="Modificar", width=10, command=modificar).grid(row=4, column=1)
            Button(groupBox, text="Eliminar", width=10, command=eliminar).grid(row=4, column=2)

            groupBox = LabelFrame(base, text="Lista del Personal", padx=5, pady=5)
            groupBox.grid(row=0, column=1, padx=5, pady=5)

            tree = ttk.Treeview(groupBox, columns=("Id", "Nombres", "Apellidos", "Sexo"), show="headings", height=5)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="Id")

            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Nombre")

            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Apellido")

            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="Sexo")

            tree.pack()
            actualizar_treeview()

            base.mainloop()

        except ValueError as error:
            print("ERROR al mostrar el interfaz: {}".format(error))

    Formulario()
