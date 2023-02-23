from tkinter import Tk
import vista
import observador

######################
# CONTROLADOR


class Controller:
    def __init__(self, root):
        # PASO 2 - Creo atributos de instancia
        # la instancia de Panel
        self.root_controller = root
        # self.root = root
        self.objeto_vista = vista.Mivista(self.root_controller)
        self.el_observador = observador.ConcreteObserverA(self.objeto_vista.obj)


if __name__ == "__main__":
    root = Tk()
    # Paso 1 - Instancio el controlador
    Controller(root)
    root.mainloop()
