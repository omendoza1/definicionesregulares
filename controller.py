# controller.py
from model import validar_cadena
from view import ValidadorView

class ValidadorController:
    def __init__(self):
        self.view = ValidadorView(self)

    def validar(self):
        cadena = self.view.entrada.get()
        resultado = validar_cadena(cadena)

        self.view.resultado.set(resultado)
        self.view.label_animacion.config(image=None)

        if "hora normal" in resultado:
            self.view.label_animacion.config(image=self.view.imagenes["normal"])
        elif "hora reiniciada" in resultado:
            self.view.label_animacion.config(image=self.view.imagenes["reiniciada"])
        elif "hora abreviada" in resultado:
            self.view.label_animacion.config(image=self.view.imagenes["abreviada"])
        elif "placa par" in resultado:
            self.view.animacion_actual = "par"
            self.view.animar()
        elif "placa impar" in resultado:
            self.view.animacion_actual = "impar"
            self.view.animar()
        else:
            self.view.animacion_actual = "invalid"
            self.view.animar()

if __name__ == "__main__":
    app = ValidadorController()
    app.view.mainloop()