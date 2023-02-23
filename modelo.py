from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
import re
from tkinter import Label
from tkinter import messagebox
from peewee import *
import datetime

####################
# MODELO

# Conexion con la base de datos

db = SqliteDatabase("mi_base_datos_peewee.db")


class BaseModel(Model):
    class Meta:
        database = db


class Discografica(BaseModel):
    artista = CharField(unique=False)
    album = CharField()
    unidades = IntegerField()
    valor = DecimalField()
    # fecha_movimiento = DateTimeField(default=datetime.datetime.now)


db.connect()
db.create_tables([Discografica])


class Abmc:
    def __init__(
        self,
    ):
        pass

    def alta(self, artista, album, unidades, valor, tree):
        cadena = artista
        patron = "[a-zA-Záéíóú 0-9 \s]+"  # regex que valida campo de entrada artista tolerando varios espacios, entre caracteres alfanúmericos
        cadena2 = unidades
        if cadena2 < 0:
            messagebox.showinfo(
                title="Error",
                message="Valor no permitido, introduzca un número positivo",
            )
            raise Exception("Valor no permitido, introduzca un número positivo")
            # excepción que impide el alta si se ingresa un número negativo en el item unidades
        if re.match(patron, cadena):
            print(artista, album, unidades, valor)

            discografica = Discografica()
            discografica.artista = artista
            discografica.album = album
            discografica.unidades = unidades
            discografica.valor = valor
            discografica.save()
            self.actualizar_treeview(tree)
            print("Item dado de alta")
            messagebox.showinfo(
                title="Enhorabuena!",
                message="Item ingresado con éxito en la base de datos",
            )

            # notificacion
            # self.notificar(artista,album,unidades, valor)

        else:
            print("Error en campo Artista")
            messagebox.showinfo(
                title="Error", message="Error en campo Artista, ingrese nuevamente"
            )

    def consulta(self, tree):
        self.actualizar_treeview(tree)

    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        for fila in Discografica.select():
            mitreview.insert(
                "",
                0,
                text=fila.id,
                values=(fila.artista, fila.album, fila.unidades, fila.valor),
            )

    def baja(self, tree):
        valores = tree.selection()
        print(valores)
        item = tree.item(valores)
        print(item)
        mi_id = item["text"]
        item_seleccionado = tree.focus()
        mi_id = tree.item(item_seleccionado)
        borrar = Discografica.get(Discografica.id == mi_id["text"])
        borrar.delete_instance()

        print("Item dado de baja")
        messagebox.showinfo(title="Enhorabuena!", message="Item eliminado con éxito")
        self.actualizar_treeview(tree)
        # tree.delete(valores)

    def modificar(self, artista, album, unidades, valor, tree):
        valores = tree.selection()
        print(valores)
        item = tree.item(valores)
        print(item)
        print(item["text"])
        mi_id = item["text"]
        actualizar = Discografica.update(
            artista=artista, album=album, unidades=unidades, valor=valor
        ).where(Discografica.id == mi_id)
        actualizar.execute()

        print("Item modificado")
        messagebox.showinfo(title="Enhorabuena!", message="Item modificado con éxito")
        self.actualizar_treeview(tree)
