from tkinter import Tk
import vista

######################
# CONTROLADOR


class Controller:
    def __init__(self, root):
        # PASO 2 - Creo atributos de instancia
        # la instancia de Panel
        self.root_controller = root
        # self.root = root
        self.objeto_vista = vista.Mivista(self.root_controller)


if __name__ == "__main__":
    root = Tk()
    # mi_app=vista.Panel(root)
    # Paso 1 - Instancio el controlador
    # mi_app=Controller(root)
    Controller(root)
    root.mainloop()
