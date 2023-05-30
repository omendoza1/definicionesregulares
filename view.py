import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

class ValidadorView(ThemedTk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.configure_theme()

        self.load_images()
        self.set_window_size()
        self.center_window()

        self.animacion_actual = None
        self.indice_animacion = 0

        self.create_widgets()

    def configure_theme(self):
        self.get_themes()
        self.set_theme("arc")
        self.title("Validador de Cadenas")

    def load_images(self):
        self.imagenes = {
            "normal": ImageTk.PhotoImage(Image.open("imagenes/normal.gif")),
            "reiniciada": ImageTk.PhotoImage(Image.open("imagenes/reiniciada.gif")),
            "abreviada": ImageTk.PhotoImage(Image.open("imagenes/abreviada.gif")),
            "par": [ImageTk.PhotoImage(Image.open(f"imagenes/par_{i}.gif")) for i in range(1, 4)],
            "impar": [ImageTk.PhotoImage(Image.open(f"imagenes/impar_{i}.gif")) for i in range(1, 4)],
            "invalid": [ImageTk.PhotoImage(Image.open(f"imagenes/invalid_{i}.gif")) for i in range(1, 4)],
        }

    def set_window_size(self):
        max_width, max_height = 0, 0

        for image_set in self.imagenes.values():
            if isinstance(image_set, list):
                for image in image_set:
                    max_width = max(max_width, image.width())
                    max_height = max(max_height, image.height())
            else:
                max_width = max(max_width, image_set.width())
                max_height = max(max_height, image_set.height())

        self.geometry(f"{max_width + 40}x{max_height + 120}")

    def center_window(self):
        self.update_idletasks()
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.geometry(f"+{x}+{y}")

    def create_widgets(self):
        self.create_content_frame()
        self.create_entry_widgets()
        self.create_animation_label()
        self.create_result_label()

    def create_content_frame(self):
        self.content = ttk.Frame(self)
        self.content.pack(fill="both", expand=True, padx=20, pady=20)

    def create_entry_widgets(self):
        self.label_entrada = ttk.Label(self.content, text="Digite una cadena:", font=("Helvetica", 20))
        self.label_entrada.grid(row=0, column=0, pady=10, sticky="ew")

        self.entrada = ttk.Entry(self.content, width=40, font=("Helvetica", 12))
        self.entrada.grid(row=0, column=1, pady=10)

        self.boton_validar = ttk.Button(self.content, text="Validar", command=self.controller.validar, style="TButton")
        self.boton_validar.grid(row=0, column=2, pady=10, padx=(20, 0))

        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_columnconfigure(1, weight=1)
        self.content.grid_columnconfigure(2, weight=1)

    def create_animation_label(self):
        self.label_animacion = ttk.Label(self.content, image=None)
        self.label_animacion.grid(row=1, column=0, columnspan=3, pady=20)

    def create_result_label(self):
        self.resultado = tk.StringVar()
        self.label_resultado = ttk.Label(self.content, textvariable=self.resultado, font=("Helvetica", 20))
        self.label_resultado.grid(row=2, column=0, columnspan=3, pady=10)

    def animar(self, repeticiones: int = 1):
        if self.animacion_actual and repeticiones > 0:
            self.label_animacion.config(image=self.imagenes[self.animacion_actual][self.indice_animacion])
            self.indice_animacion = (self.indice_animacion + 1) % len(self.imagenes[self.animacion_actual])
            
            if self.indice_animacion == 0:
                repeticiones-= 1
            
            self.after(500, self.animar, repeticiones)
        else:
            self.reset_animation()

    def reset_animation(self):
        self.animacion_actual = None

    def set_animation(self, animacion: str, repeticiones: int = 1):
        if animacion in self.imagenes:
            self.animacion_actual = animacion
            self.indice_animacion = 0
            self.animar(repeticiones)
        else:
            self.animacion_actual = None
            self.label_animacion.config(image=None)

    def set_result(self, result: str):
        self.resultado.set(result)