class Sujeto:
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)


class Observador:
    def update(self):
        raise NotImplementedError("Delegacion de actualizacion")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observando_a = obj
        self.observando_a.agregar(self)

    def update(self, *args):
        print("actualizacion dentro de observador concretoA")
        print("Aqui estan los parametros ", args)
