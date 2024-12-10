import tkinter as tk
from tkinter import Toplevel, Label
from PIL import Image, ImageTk
import pandas as pd
import time

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Ordenamiento de Seleccion")
        self.root.geometry("1000x700")
        self.root.configure(bg="#F6E8DA") ##F6E8DA ##B2B9BF
        self.current_frame = None
        self.df = None
        self.datos = None
        
        self.create_page1()


    def cambiar_tema(self):
        # Alternar entre temas
        if self.tema_actual == "oscuro":
            self.tema_actual = "claro"
            self.root.configure(bg=self.tema_claro["bg"])
            self.boton_cambiar_tema.configure(bg=self.tema_claro["bg"], fg=self.tema_claro["fg"])
        else:
            self.tema_actual = "oscuro"
            self.root.configure(bg=self.tema_oscuro["bg"])
            self.boton_cambiar_tema.configure(bg=self.tema_oscuro["bg"], fg=self.tema_oscuro["fg"])

#PAGINA 1 Inicioo
    def create_page1(self):
        self.show_frame(self.page0)

    def page0(self, frame):
        
        tk.Label(frame, text="ORDENAMIENTO DE DATOS", font=("Comic Sans MS", 36, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=70)         


        gif_path = "load.gif"  
        self.gif = Image.open(gif_path)
        self.gif_frames = []
        try:
            while True:
                self.gif_frames.append(ImageTk.PhotoImage(self.gif.copy()))
                self.gif.seek(len(self.gif_frames))  
        except EOFError:
            pass  

        self.gif_label = tk.Label(frame, bg="#F6E8DA")
        self.gif_label.pack(pady=20)
        
        # Iniciar la animación
        self.animate_gif(0)
        
        button_frame = tk.Frame(frame, bg="#F6E8DA")
        button_frame.pack(pady=20)

        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#134B70", text="INICIAR",font=("Arial", 20, "bold"), command=self.create_page2).pack(pady=15)
    
        tk.Label(frame, text="By RomelG", font=("Comic Sans MS", 16), bg="#F6E8DA", fg="#303750").pack(side=tk.BOTTOM, anchor=tk.E, padx=10, pady=10)
        
    def animate_gif(self, frame_index):
        self.gif_label.configure(image=self.gif_frames[frame_index])
        self.root.after(100, self.animate_gif, (frame_index + 1) % len(self.gif_frames))

    def show_frame(self, frame_function):
        if self.current_frame:
            self.current_frame.destroy()
        new_frame = tk.Frame(self.root, bg="#F6E8DA")
        self.current_frame = new_frame
        frame_function(new_frame)
        new_frame.pack(fill="both", expand=True)


#PAGINA 2 MENU DEL PROGRAMA 

    def create_page2(self):
        self.show_frame(self.page2)

    def page2(self, frame):
        tk.Label(frame, text="ORDENAMIENTO POR SELECCION", font=("Comic Sans MS", 22, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=60)
        tk.Label(frame, text="Menú del Programa", font=("Comic Sans MS", 22, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=10)

        button_frame = tk.Frame(frame, bg="#F6E8DA")
        button_frame.pack(pady=20)

        # Crear el botón personalizado
        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#496A81", text="SUBIR ARCHIVO",font=("Arial", 16, "bold"), command=self.create_page3).pack(pady=15)
        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#496A81", text="ORDENAR ARCHIVO",font=("Arial", 16, "bold"), command=self.create_page4).pack(pady=15)
        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#496A81", text="VISUALIZACIÓN",font=("Arial", 16, "bold"), command=self.create_page_visualizar).pack(pady=15)
        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#496A81", text="ESTADÍSTICAS", font=("Arial", 16, "bold"), command=self.create_page_estadisticas).pack(pady=15)        
        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#496A81", text="GUARDAR ARCHIVO",font=("Arial", 16, "bold"), command=self.create_page5).pack(pady=15)       
        RoundedButton(button_frame, width=100, height=20, corner_radius=10, padding=0, color="#A5243D", text="SALIR", font=("Arial", 12, "bold"),command=self.root.quit).pack(pady=25)
        

                
#PAGINA 3 SUBIR ARCHIVO
   
    def create_page3(self):
        self.show_frame(self.page3)

    def page3(self, frame):
        tk.Label(frame, text="ORDENAMIENTO POR SELECCION", font=("Comic Sans MS", 22, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=60)
        tk.Label(frame, text="SUBIR ARCHIVO", font=("Comic Sans MS", 22, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=10)

        tk.Label(frame, text="Ingresa el nombre del archivo a subir", font=("Arial", 14, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=10)
        self.entry_filename = tk.Entry(frame, width=25, font=("Arial", 22))
        self.entry_filename.pack(pady=10)

        button_frame = tk.Frame(frame, bg="#F6E8DA")
        button_frame.pack(pady=20)
        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#AEC09A", text="SUBIR", font=("Arial", 16, "bold"),command=self.subir_archivo).pack(pady=25)
        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#496A81", text="INGRESAR DATOS", font=("Arial", 16, "bold"),command=self.create_page_manual_entry).pack(pady=15)
        RoundedButton(button_frame, width=200, height=40, corner_radius=10, padding=0, color="#2F6690", text="ACEPTAR", font=("Arial", 16, "bold"),command=self.create_page2).pack(pady=45)
        
########################

    # Nueva página para ingreso manual de datos
    def create_page_manual_entry(self):
        self.show_frame(self.page_manual_entry)

    def page_manual_entry(self, frame):
        tk.Label(frame, text="ORDENAMIENTO POR SELECCION", font=("Comic Sans MS", 22, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=20)
        tk.Label(frame, text="Ingreso Manual de Datos", font=("Comic Sans MS", 20, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=10)

        # Frame para entrada de datos
        entry_frame = tk.Frame(frame, bg="#F6E8DA")
        entry_frame.pack(pady=10)

        self.manual_entry = tk.Entry(entry_frame, width=30, font=("Arial", 16))
        self.manual_entry.pack(side=tk.LEFT, padx=5)

        add_button = RoundedButton(entry_frame, width=150, height=40, corner_radius=10, padding=0, 
                                color="#AEC09A", text="Agregar", font=("Arial", 14, "bold"),
                                command=self.add_manual_data)
        add_button.pack(side=tk.LEFT, padx=5)

        # Frame para mostrar datos
        display_frame = tk.Frame(frame, bg="#F6E8DA", width=800, height=300)
        display_frame.pack(pady=20)
        display_frame.pack_propagate(False)

        # Scrollbar para el área de texto
        scrollbar = tk.Scrollbar(display_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Área de texto para mostrar los datos ingresados
        self.manual_text = tk.Text(display_frame, wrap=tk.NONE, yscrollcommand=scrollbar.set,
                                height=15, width=70, bg="#F6E8DA", fg="#303750",
                                font=("Comic Sans MS", 16))
        self.manual_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.manual_text.yview)

        # Frame para botones de control
        control_frame = tk.Frame(frame, bg="#F6E8DA")
        control_frame.pack(pady=20)

        # Botones de control
        RoundedButton(control_frame, width=200, height=40, corner_radius=10, padding=0,
                    color="#8F2D56", text="Borrar último", font=("Arial", 14, "bold"),
                    command=self.delete_last_entry).pack(side=tk.LEFT, padx=10)
        
        RoundedButton(control_frame, width=200, height=40, corner_radius=10, padding=0,
                    color="#004643", text="Borrar todo", font=("Arial", 14, "bold"),
                    command=self.clear_all_entries).pack(side=tk.LEFT, padx=10)

        # Botón para guardar y volver
        button_frame = tk.Frame(frame, bg="#F6E8DA")
        button_frame.pack(pady=20)
        
        RoundedButton(button_frame, width=200, height=40, corner_radius=10, padding=0,
                    color="#2F6690", text="Guardar datos", font=("Arial", 14, "bold"),
                    command=self.save_manual_data).pack(pady=10)
        
        RoundedButton(button_frame, width=200, height=40, corner_radius=10, padding=0,
                    color="#2F6690", text="ACEPTAR", font=("Arial", 14, "bold"),
                    command=self.create_page3).pack(pady=10)

    def add_manual_data(self):
        """Agregar un nuevo dato a la lista"""
        new_data = self.manual_entry.get().strip()
        if new_data:
            if not hasattr(self, 'manual_data_list'):
                self.manual_data_list = []
            
            self.manual_data_list.append(new_data)
            # Actualizar visualización
            self.manual_text.delete('1.0', tk.END)
            for idx, data in enumerate(self.manual_data_list, 1):
                self.manual_text.insert(tk.END, f"[{idx}] : {data}\n")
            
            # Limpiar entrada
            self.manual_entry.delete(0, tk.END)
            
    def delete_last_entry(self):
        """Eliminar el último dato ingresado"""
        if hasattr(self, 'manual_data_list') and self.manual_data_list:
            self.manual_data_list.pop()
            # Actualizar visualización
            self.manual_text.delete('1.0', tk.END)
            for idx, data in enumerate(self.manual_data_list, 1):
                self.manual_text.insert(tk.END, f"[{idx}] : {data}\n")

    def clear_all_entries(self):
        """Limpiar todos los datos ingresados"""
        if hasattr(self, 'manual_data_list'):
            self.manual_data_list = []
        self.manual_text.delete('1.0', tk.END)

    def save_manual_data(self):
        """Guardar los datos ingresados manualmente"""
        if hasattr(self, 'manual_data_list') and self.manual_data_list:
            try:
                # Crear DataFrame con los datos manuales
                self.df = pd.DataFrame(self.manual_data_list, columns=['Datos'])
                self.datos = self.manual_data_list
                #self.mostrar_mensaje("Éxito", "Datos guardados exitosamente", tipo="info")
                self.create_page2()
            except Exception as e:
                self.mostrar_mensaje("Error", f"Error al guardar los datos: {str(e)}", tipo="error")
        else:
            self.mostrar_mensaje("Error", "No hay datos para guardar", tipo="error")

        
########################   
        
#PAGINA 4 ORDENAMIENTO

    def create_page4(self):
        self.show_frame(self.page4)

    def page4(self, frame):
        tk.Label(frame, text="ORDENAMIENTO POR SELECCION", font=("Comic Sans MS", 22, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=60)
        tk.Label(frame, text="ORDENAMIENTO DEL ARCHIVO", font=("Comic Sans MS", 22, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=10)

        tk.Label(frame, text="Como quieres ordenar los datos?", font=("Arial", 14, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=10)

        button_frame = tk.Frame(frame, bg="#F6E8DA")
        button_frame.pack(pady=20)
        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#8F2D56", text="Descendente", font=("Arial", 16, "bold"),command=lambda: self.tiempo_ord('descendente')).pack(pady=20)
        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#004643", text="Ascendente", font=("Arial", 16, "bold"),command=lambda: self.tiempo_ord('ascendente')).pack(pady=15)
        
        RoundedButton(button_frame, width=200, height=40, corner_radius=10, padding=0, color="#2F6690", text="ACEPTAR", font=("Arial", 16, "bold"),command=self.create_page2).pack(pady=55)      
        
#PAGINA 5 GAURDAR ARCHIVO
    def create_page5(self):
        self.show_frame(self.page5)

    def page5(self, frame):
        
        tk.Label(frame, text="ORDENAMIENTO POR SELECCION", font=("Comic Sans MS", 22, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=60)
        tk.Label(frame, text="GUARDAR ARCHIVO", font=("Comic Sans MS", 22, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=10)
        
        tk.Label(frame, text="Ingresa el nombre del archivo para guardar la salida", font=("Arial", 16), bg="#F6E8DA", fg="#303750").pack(pady=10)

        self.entry_guardar_archivoname = tk.Entry(frame, width=25, font=("Arial", 22))
        self.entry_guardar_archivoname.pack(pady=10)
        
        button_frame = tk.Frame(frame, bg="#F6E8DA")
        button_frame.pack(pady=20)
        RoundedButton(button_frame, width=300, height=50, corner_radius=10, padding=0, color="#AEC09A", text="GUARDAR", font=("Arial", 16, "bold"),command=self.guardar_archivo).pack(pady=25)
        RoundedButton(button_frame, width=200, height=40, corner_radius=10, padding=0, color="#2F6690", text="ACEPTAR", font=("Arial", 16, "bold"),command=self.create_page2).pack(pady=45)

#=======================================================================>
    def mostrar_mensaje(self, titulo, mensaje, tipo="info", ):
        # Crear una ventana emergente personalizada
        ventana_mensaje = Toplevel()
        ventana_mensaje.title(titulo)

        # Dimensiones de la ventana del mensaje
        ancho_ventana = 400
        alto_ventana = 180

        # Obtener las dimensiones de la pantalla
        ancho_pantalla = ventana_mensaje.winfo_screenwidth()
        alto_pantalla = ventana_mensaje.winfo_screenheight()

        # Calcular las coordenadas x e y para centrar la ventana
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        # Establecer la geometría centrada
        ventana_mensaje.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        ventana_mensaje.config(bg="#f0f0f0")

        if tipo == "error":
            ventana_mensaje.config(bg="#ff949f")  # Fondo rojo claro para error
            #etiqueta_mensaje.pack(pady=5)
            etiqueta_mensaje = Label(ventana_mensaje, text=mensaje, font=("Comic Sans MS", 14, "bold"), bg="#ff949f", fg="#000000", wraplength=350).pack(pady=20)
            
            RoundedButton(ventana_mensaje, width=200, height=40, corner_radius=10, padding=0, color="#9c2222", text="ACEPTAR", command=ventana_mensaje.destroy, font=("Arial", 16, "bold")).pack(pady=20)            
          
        elif tipo == "info":
            ventana_mensaje.config(bg="#68d48d")  # Fondo verde claro para éxito
            #etiqueta_mensaje.pack(pady=5)
            etiqueta_mensaje = Label(ventana_mensaje, text=mensaje, font=("Comic Sans MS", 14, "bold"), bg="#68d48d", fg="#000000", wraplength=350).pack(pady=20)
            
            RoundedButton(ventana_mensaje, width=200, height=40, corner_radius=10, padding=0, color="#229c43", text="ACEPTAR", command=ventana_mensaje.destroy, font=("Arial", 16, "bold")).pack(pady=20)      
                   
#=======================================================================>

#PAGINA EXTRA Visualizar datos
    def create_page_visualizar(self):
        self.show_frame(self.page_visualizar)

    def page_visualizar(self, frame):

            tk.Label(frame, text="ORDENAMIENTO POR SELECCIÓN", font=("Comic Sans MS", 24, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=20)
            tk.Label(frame, text="Visualizacion de datos", font=("Comic Sans MS", 18, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=(20, 20))

            if self.datos is not None:
                # Creamos un Frame para contener el Text y la Scrollbar
                text_frame = tk.Frame(frame, bg="#F6E8DA", width=800, height=450)  # Ajustamos tamaño del Frame
                text_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                text_frame.pack_propagate(False)
                text_frame.pack(pady=(0, 20))

                # Scrollbar
                scrollbar = tk.Scrollbar(text_frame)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                # Text widget para mostrar y editar los datos
                self.text_widget = tk.Text(text_frame, wrap=tk.NONE, yscrollcommand=scrollbar.set, height=20, width=90,
                                    bg="#F6E8DA", fg="#303750", font=("Comic Sans MS", 16))
                self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                # Configura la scrollbar para interactuar con el Text widget
                scrollbar.config(command=self.text_widget.yview)

                # Inserta los datos con índices en el Text widget
                for idx, row in enumerate(self.datos, 1):
                    self.text_widget.insert(tk.END, f"[{idx}] : {row}\n")

                # Tag para los índices
                for i in range(len(self.datos)):
                    start = f"{i+1}.0"
                    end = f"{i+1}.{self.text_widget.get(f'{i+1}.0', f'{i+1}.end').find(':')+2}"
                    self.text_widget.tag_add(f"index_{i}", start, end)
                    self.text_widget.tag_config(f"index_{i}", foreground="gray")

                # Habilita la edición del Text widget
                self.text_widget.config(state=tk.NORMAL)

                # Botones para guardar cambios y aceptar
                buttons_frame = tk.Frame(frame, bg="#F6E8DA")
                buttons_frame.pack(pady=20)

                RoundedButton(buttons_frame, width=200, height=40, corner_radius=10, padding=0, color="#2F6690", text="Guardar cambios", font=("Arial", 16, "bold"), command=self.save_data_changes).pack(side=tk.LEFT, padx=10)
                RoundedButton(buttons_frame, width=200, height=40, corner_radius=10, padding=0, color="#2F6690", text="Aceptar", font=("Arial", 16, "bold"), command=self.create_page2).pack(side=tk.LEFT, padx=10)
                
            else:            
                tk.Label(frame, text="No hay datos cargados para visualizar.", font=("Arial", 12), bg="#F6E8DA", fg="#303750").pack(pady=20)
                buttons_frame = tk.Frame(frame, bg="#F6E8DA")
                buttons_frame.pack(pady=20)
                RoundedButton(buttons_frame, width=200, height=40, corner_radius=10, padding=0, color="#2F6690", text="Aceptar", font=("Arial", 16, "bold"), command=self.create_page2).pack(side=tk.LEFT, padx=10)

    def save_data_changes(self):
        try:
            # Obtener el texto modificado del widget de texto
            modified_data = []
            for i in range(1, len(self.datos) + 1):
                line = self.text_widget.get(f"{i}.0", f"{i}.end")
                # Extraer solo el valor después de los dos puntos y espacio
                value = line.split(": ", 1)[1].strip()
                modified_data.append(value)

            # Actualizar el DataFrame con los valores limpios
            self.df[self.df.columns[0]] = modified_data
            self.datos = modified_data
            
            self.mostrar_mensaje("Éxito", "Datos actualizados exitosamente.", tipo="info")
        except Exception as e:
            self.mostrar_mensaje("Error", f"Error al actualizar los datos: {str(e)}", tipo="error")

    # Página de estadísticas de datos
    def create_page_estadisticas(self):
        self.show_frame(self.page_estadisticas)

####
    def page_estadisticas(self, frame):
        # Título principal de la página
        tk.Label(frame, text="ORDENAMIENTO POR SELECCION", font=("Comic Sans MS", 22, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=20)
        tk.Label(frame, text="Estadísticas del Archivo", font=("Comic Sans MS", 18, "bold"), bg="#F6E8DA", fg="#303750").pack(pady=(20, 10))

        if self.df is not None:
            # Separar columnas numéricas y categóricas
            columnas_numericas = self.df.select_dtypes(include="number")
            columnas_categoricas = self.df.select_dtypes(exclude="number")

            stats_text = ""
            
            if not columnas_numericas.empty:
                # Generar estadísticas para columnas numéricas
                estadisticas = columnas_numericas.describe()
                mediana = columnas_numericas.median()
                moda = columnas_numericas.mode().iloc[0]
                varianza = columnas_numericas.var()
                desviacion_estandar = columnas_numericas.std()
                rango = columnas_numericas.max() - columnas_numericas.min()
                valores_unicos = columnas_numericas.nunique()
                valores_nulos = columnas_numericas.isnull().sum()
                
                # Cálculo del coeficiente de variación
                media = columnas_numericas.mean()
                coef_variacion = (desviacion_estandar / media) * 100

                # Agrega las estadísticas adicionales para columnas numéricas
                for col in columnas_numericas.columns:
                    stats_text += f"{col}:\n"
                    stats_text += f"Mediana:               {mediana[col]:.2f}\n"
                    stats_text += f"Moda:                  {moda[col]:.2f}\n"
                    stats_text += f"Varianza:              {varianza[col]:.2f}\n"
                    stats_text += f"Desviación estándar:   {desviacion_estandar[col]:.2f}\n"
                    stats_text += f"Coef. de variación:    {coef_variacion[col]:.2f}%\n"
                    stats_text += f"Rango:                 {rango[col]:.2f}\n"
                    stats_text += f"Valores únicos:        {valores_unicos[col]}\n"
                    stats_text += f"Valores nulos:         {valores_nulos[col]}\n\n"
                
                # Filtra y muestra solo ciertas filas de estadísticas
                estadisticas_filtradas = estadisticas.loc[["min", "25%", "50%", "75%", "max"]]
                stats_text += estadisticas_filtradas.to_string(float_format="{:.2f}".format) + "\n\n"
            
            if not columnas_categoricas.empty:
                # Generar estadísticas para columnas categóricas
                for col in columnas_categoricas.columns:
                    valores_unicos = columnas_categoricas[col].nunique()
                    moda = columnas_categoricas[col].mode().iloc[0]
                    valores_nulos = columnas_categoricas[col].isnull().sum()

                    stats_text += f"\n{col}:\n"
                    stats_text += f"Valores únicos:        {valores_unicos}\n"
                    stats_text += f"Moda:                  {moda}\n"
                    stats_text += f"Valores nulos:         {valores_nulos}\n"

            text_frame = tk.Frame(frame, bg="#F6E8DA", width=400, height=475)  # Ajustamos tamaño del Frame
            text_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            text_frame.pack_propagate(False)
            text_frame.pack(pady=(0, 20))
            
            # Configura el widget de texto para mostrar las estadísticas
            text_widget = tk.Text(text_frame, wrap=tk.NONE, height=20, width=80, bg="#F6E8DA", fg="#303750", font=("Comic Sans MS", 16))
            text_widget.insert("1.0", stats_text)
            text_widget.config(state="disabled")
            text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        else:
            tk.Label(frame, text="No hay datos cargados. Por favor, sube un archivo.", font=("Arial", 14), bg="#F6E8DA", fg="red").pack(pady=20)

        # Botón para aceptar y volver a la página principal
        button_frame = tk.Frame(frame, bg="#F6E8DA")
        button_frame.pack(pady=20)
        RoundedButton(button_frame, width=200, height=40, corner_radius=10, padding=0, color="#2F6690", text="ACEPTAR", font=("Arial", 16, "bold"), command=self.create_page2).pack(pady=20)


# Funciones del archivo en plano

    def subir_archivo(self):
        filename = self.entry_filename.get()
        try:
            # Obtener la extensión del archivo
            file_extension = filename.lower().split('.')[-1]
            
            # Cargar el archivo según su extensión
            if file_extension == 'csv':
                self.df = pd.read_csv(filename)
            elif file_extension == 'txt':
                # Intenta diferentes delimitadores comunes
                try:
                    self.df = pd.read_csv(filename, sep=',')
                except:
                    try:
                        self.df = pd.read_csv(filename, sep='\t')
                    except:
                        self.df = pd.read_csv(filename, sep=';')
            elif file_extension in ['xls', 'xlsx']:
                self.df = pd.read_excel(filename)
            else:
                raise ValueError(f"Formato de archivo no soportado: {file_extension}")
            
            # Convertir la primera columna a lista
            self.datos = self.df[self.df.columns[0]].tolist()
            self.mostrar_mensaje("Éxito", f"Archivo '{filename}' cargado exitosamente.", tipo="info")
        
        except FileNotFoundError:
            self.mostrar_mensaje("Error", f"El archivo '{filename}' no fue encontrado.", tipo="error")
        except ValueError as e:
            self.mostrar_mensaje("Error", str(e), tipo="error")
        except Exception as e:
            self.mostrar_mensaje("Error", f"Error al cargar el archivo: {str(e)}", tipo="error")
            
    def guardar_archivo(self):
        filename = self.entry_guardar_archivoname.get()
        if self.df is not None:
            try:
                # Obtener la extensión del archivo
                if '.' not in filename:
                    self.mostrar_mensaje("Error", "Por favor, incluya la extensión del archivo (.csv, .txt, o .xlsx)", tipo="error")
                    return
                    
                file_extension = filename.lower().split('.')[-1]
                
                # Guardar el archivo según su extensión
                if file_extension == 'csv':
                    self.df.to_csv(filename, index=False)
                elif file_extension == 'txt':
                    # Guardar como archivo de texto con tabulación como separador
                    self.df.to_csv(filename, index=False, sep='\t')
                elif file_extension == 'xlsx':
                    # Guardar como archivo Excel
                    self.df.to_excel(filename, index=False)
                else:
                    raise ValueError(f"Formato de archivo no soportado: {file_extension}. Use .csv, .txt, o .xlsx")
                    
                self.mostrar_mensaje("Éxito", f"Archivo guardado como '{filename}'.", tipo="info")
                
            except PermissionError:
                self.mostrar_mensaje("Error", f"No se tiene permiso para guardar en '{filename}'. El archivo podría estar en uso.", tipo="error")
            except ValueError as e:
                self.mostrar_mensaje("Error", str(e), tipo="error")
            except Exception as e:
                self.mostrar_mensaje("Error", f"Error al guardar el archivo: {str(e)}", tipo="error")
        else:
            self.mostrar_mensaje("Error", "No hay datos para guardar.", tipo="error")            
            
            

    def tiempo_ord(self, orden):
        if self.df is not None and self.datos is not None:
            inicio = time.time()
            self.datos = self.ordenar(self.datos, orden)
            fin = time.time()
            self.df[self.df.columns[0]] = self.datos
            self.mostrar_mensaje("Ordenamiento", f"Datos ordenados en {orden}. Tiempo: {fin - inicio:.4f} seg.", tipo="info")
        else:
            self.mostrar_mensaje("Error", "No hay datos para ordenar.", tipo="error")

    def ordenar(self, datos, orden='descendente'):
        n = len(datos)
        for i in range(n - 1):
            for j in range(i+1, n):
                if (orden == 'descendente' and datos[i] < datos[j]) or (orden == 'ascendente' and datos[i] > datos[j]):
                    aux = datos[i]
                    datos[i] = datos[j]
                    datos[j] = aux
        return datos
 
#=======================================================================================================================>   

class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, corner_radius, padding, color, text, font, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0, 
            relief="flat", highlightthickness=0, bg=parent["bg"])
        self.command = command

        if corner_radius > 0.5*width:
            corner_radius = 0.5*width
        if corner_radius > 0.5*height:
            corner_radius = 0.5*height

        rad = 2*corner_radius
        def shape():
            self.create_polygon((padding,height-corner_radius-padding,padding,corner_radius+padding,padding+corner_radius,padding,width-padding-corner_radius,padding,width-padding,corner_radius+padding,width-padding,height-corner_radius-padding,width-padding-corner_radius,height-padding,padding+corner_radius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)

        shape()
        self.create_text(width/2, height/2, text=text, fill="white", font=font)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()
            
            
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
