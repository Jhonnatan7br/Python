#%%
import tkinter as tk
from tkinter import ttk

"""Aplicación base"""
class App(tk.Tk): 
    def __init__(self):
        super().__init__()

        # configurando la ventana
        self.title('Wheels GUI') #Título de la ventana
        self.geometry('750x1300') #Dimensiones
        self.resizable(False,False) #Permisos para cambiar el tamaño
        #self.attributes('-alpha',0.5) #transparencia
        #self.iconbitmap() icono
        # Entrada de datos en caja de texto
        self.caja = ttk.Entry(self)
        self.caja.pack()
        # Boton
        self.mibotonsito = ttk.Button(self, 
                                      text="Presióname", 
                                      command=self.mifuncion) # Función de recopilar texto
        self.mibotonsito.pack()
        # Etiqueta
        self.mi_variable_resultado=tk.StringVar() #Creo una variable control asociada al widget Label para guardar y actualizar la información
        self.label_resultado = ttk.Label(self, 
                                         font=("Helvetiva",40),
                                         textvariable=self.mi_variable_resultado) #Creo el Widget y asocio la variable
        self.label_resultado.pack()

        """
        # Crear un Frame para los botones
        self.frame_botones = ttk.Frame(self, bg='blue')
        self.frame_botones.pack(side='bottom', fill='x')
        
        # Botones dentro del Frame
        self.boton_1 = ttk.Button(self.frame_botones, text='Boton 1')
        self.boton_1.pack(side='left', padx=10, pady=10)
        self.boton_2 = ttk.Button(self.frame_botones, text='Boton 2')
        self.boton_2.pack(side='left', padx=10, pady=10)
        self.boton_3 = ttk.Button(self.frame_botones, text='Boton 3')
        self.boton_3.pack(side='left', padx=10, pady=10)

        # Entrada de datos en caja de texto
        self.caja = ttk.Entry(self)
        self.caja.pack()

        # Boton
        self.mibotonsito = ttk.Button(self, text="Presióname", command=self.mifuncion) # Función de recopilar texto
        self.mibotonsito.pack()

        # Etiqueta
        self.mi_variable_resultado=tk.StringVar() #Creo una variable control asociada al widget Label para guardar y actualizar la información
        self.label_resultado = ttk.Label(self, font=("Helvetiva",40), textvariable=self.mi_variable_resultado) #Creo el Widget y asocio la variable
        self.label_resultado.pack()

    def mifuncion(self):
        texto = self.caja.get()
        self.mi_variable_resultado.set(texto) """
        
    def mifuncion(self):
        #1. Guardar la información
        texto_usuario=self.caja.get() #Get es por defecto el comando para "obtener" información
        #2. Hago el cálculo que quiero
        texto_invertido = texto_usuario[::-1] #Vamos a invertir el texto
        print(texto_invertido) #por verificar el punto 2
        #3. Muestro el resultado
        self.mi_variable_resultado.set(texto_invertido) #le damos un valor a la variable control del Label
        #4. Resetear parámetros (opcional)
        self.caja.delete(0, 0)
        
    # Caja de texto con scroll
   
        
        

#Acción:
app = App()
app.mainloop()