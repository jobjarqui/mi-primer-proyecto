import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import basedate

class RecetasCocina:

    def Recetas():
        try:
            base = Tk()
            base.geometry("1200x600")
            base.title("Recetas de cocina")
            basedate.connect()

            def guardar():
                nombre = textBoxNombre.get()
                ingredientes = textBoxIngredientes.get()
                instrucciones = textBoxInstrucciones.get()
                tiempo = textBoxTiempo.get()
                basedate.insert(nombre, ingredientes, instrucciones, tiempo)
                messagebox.showinfo("Receta guardada", "La receta se ha guardado correctamente")
                actualizar_treeview()

            def editar():
                try:
                    selected_item = tree.selection()[0]
                    id = tree.item(selected_item, 'values')[0]
                    nombre = textBoxNombre.get()
                    ingredientes = textBoxIngredientes.get()
                    instrucciones = textBoxInstrucciones.get()
                    tiempo = textBoxTiempo.get()
                    basedate.update(id, nombre, ingredientes, instrucciones, tiempo)
                    messagebox.showinfo("Receta editada", "La receta se ha editado correctamente")
                    actualizar_treeview()
                except IndexError:
                    messagebox.showwarning("Seleccionar receta", "Por favor selecciona una receta para editar.")

            def eliminar():
                try:
                    selected_item = tree.selection()[0]
                    id = tree.item(selected_item, 'values')[0]
                    basedate.delete(id)
                    messagebox.showinfo("Receta eliminada", "La receta se ha eliminado correctamente")
                    actualizar_treeview()
                except IndexError:
                    messagebox.showwarning("Seleccionar receta", "Por favor selecciona una receta para eliminar.")

            def actualizar_treeview():
                for row in tree.get_children():
                    tree.delete(row)
                for row in basedate.fetch_all():
                    tree.insert("", END, values=row)

            groupbox = LabelFrame(base, text="Recetas de cocina", padx=10, pady=10)
            groupbox.grid(row=0, column=0, padx=25, pady=25)

            Label(groupbox, text="Id:", width=15, font=("arial", 12)).grid(row=0, column=0)
            textBoxId = Entry(groupbox)
            textBoxId.grid(row=0, column=1)

            Label(groupbox, text="Nombre", width=15, font=("arial", 12)).grid(row=1, column=0)
            textBoxNombre = Entry(groupbox)
            textBoxNombre.grid(row=1, column=1)

            Label(groupbox, text="Ingredientes:", width=15, font=("arial", 12)).grid(row=2, column=0)
            textBoxIngredientes = Entry(groupbox)
            textBoxIngredientes.grid(row=2, column=1)

            Label(groupbox, text="Instrucciones", width=15, font=("arial", 12)).grid(row=3, column=0)
            textBoxInstrucciones = Entry(groupbox)
            textBoxInstrucciones.grid(row=3, column=1)

            Label(groupbox, text="Tiempo de Preparacion", width=19, font=("arial", 12)).grid(row=4, column=0)
            textBoxTiempo = Entry(groupbox)
            textBoxTiempo.grid(row=4, column=1)

            Button(groupbox, text="Guardar", width=10, command=guardar).grid(row=5, column=0)
            Button(groupbox, text="Editar", width=10, command=editar).grid(row=5, column=1)
            Button(groupbox, text="Eliminar", width=10, command=eliminar).grid(row=5, column=2)

            groupbox2 = LabelFrame(base, text="Lista de Recetas", padx=10, pady=10)
            groupbox2.grid(row=1, column=0, columnspan=2, padx=25, pady=25)

            tree = ttk.Treeview(groupbox2, columns=("Id", "Nombre", "Ingredientes", "Instrucciones", "Tiempo de preparacion"), show="headings", height=10)
            tree.column("#1", anchor=CENTER, width=50)
            tree.heading("#1", text="Id")

            tree.column("#2", anchor=CENTER, width=200)
            tree.heading("#2", text="Nombre")

            tree.column("#3", anchor=CENTER, width=300)
            tree.heading("#3", text="Ingredientes")

            tree.column("#4", anchor=CENTER, width=300)
            tree.heading("#4", text="Instrucciones")

            tree.column("#5", anchor=CENTER, width=150)
            tree.heading("#5", text="Tiempo de Preparacion")

            tree.pack()
            actualizar_treeview()

            base.mainloop()

        except ValueError as error:
            print(f"Error al mostrar el interfaz: {error}")

    Recetas()
