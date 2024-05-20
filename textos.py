import tkinter as tk
from tkinter import messagebox

def generar_texto():
    emocion = versiculo_entry.get()
    Textos = {
        "Triste": "Juan 14",
        "Miedo": "Salmo 91",
        "Enojado": "Romanos 12:17-21",
        "Ansioso": "Salmo 34",
        "Preocupado": "Mateo 6:25-34",
        "Deprimido": "Lamentaciones 3:55-57",
        "Engañado": "Jeremías 20:7-12",
        "Desanimado": "2 Corintios 4:7-17",
        "Dudo de la fe de Dios": "Hebreos 11",
        "Impaciente": "Santiago 5:7-11",
        "Inseguro": "Isaías 41:10",
        "Celoso": "Santiago 3:13-18",
        "Me siento solo": "Deuteronomio 31:8",
        "Estresado": "Mateo 11:28-30",
        "Rechazado": "Efesios 1:3-14",
        "Tentado": "Salmo 141",
        "Agotado": "Isaías 40:28-31",
        "He pecado": "Salmo 51"
    }

    if emocion in Textos:
        messagebox.showinfo("Mi estado de ánimo es: " + emocion, Textos[emocion])
    else:
        messagebox.showwarning("Emoción no encontrada", "Lo siento, no tenemos un versículo para esa emoción.")

# Configurar nuestra ventana
ventana = tk.Tk()
ventana.title("Generador de versículos bíblicos")
ventana.geometry("500x400")
ventana.resizable(0, 0)





# Crear un frame para contener los widgets y hacerlos transparentes
frame = tk.Frame(ventana, bg='white', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.6, anchor='n')

# Crear un label y los elementos de la interfaz dentro del frame
versiculo_label = tk.Label(frame, text="Estado de ánimo:", font=("Arial", 14))
versiculo_label.pack(pady=10)

versiculo_entry = tk.Entry(frame, font=("Arial", 14))
versiculo_entry.pack(pady=10)

generar_button = tk.Button(frame, text="Ver tu solución a tu estado de ánimo", command=generar_texto, font=("Arial", 14))
generar_button.pack(pady=10)

# Ejecución de nuestro bucle principal
ventana.mainloop()
