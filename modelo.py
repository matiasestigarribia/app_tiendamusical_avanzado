from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk
import re
from tkinter import Label
from tkinter import messagebox
from peewee import *


####################
# MODELO


class Abmc:
    def __init__(
        self,
    ):
        try:
            con = sqlite3.connect("mibase_intermedio.db")
            cursor = con.cursor()
            sql = """CREATE TABLE discografica
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                artista varchar(50) NOT NULL,
                album varchar(50) NOT NULL,
                unidades varchar(20) NOT NULL,
                valor varchar(20) NOT NULL
                )"""
            cursor.execute(sql)
            con.commit
            print("Bienvenido/a ingrese un item en la base de datos de música")
        except:
            print(
                "Bienvenido/a, ingrese un item o consulte en la base de datos de música"
            )
        finally:
            print("Puede consultar, modificar o eliminar")
            # excepción que comunica que la base de datos se crea al dar el alta, y en caso de estar creada da otro aviso.
            # mediante finally, en ambos casos comunica que se puede consultar, modificar o eliminar.

    def conexion(
        self,
    ):
        con = sqlite3.connect("mibase_intermedio.db")
        return con

    def crear_base(
        self,
    ):
        con = sqlite3.connect("mibase_intermedio.db")
        con.close()
        self.crear_base
        return con

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
            con = self.conexion()
            cursor = con.cursor()
            data = (artista, album, unidades, valor)
            sql = "INSERT INTO discografica(artista, album, unidades, valor) VALUES(?, ?, ?, ?)"
            cursor.execute(sql, data)
            con.commit()
            print("Item dado de alta")
            messagebox.showinfo(
                title="Enhorabuena!", message="Item ingresado con éxito"
            )
            self.actualizar_treeview(tree)

        else:
            print("Error en campo Artista")
            messagebox.showinfo(
                title="Error", message="Error en campo Artista, ingrese nuevamente"
            )

    def consulta(self, tree):
        self.actualizar_treeview(tree)

    def baja(self, tree):
        valores = tree.selection()
        print(valores)
        item = tree.item(valores)
        print(item)
        print(item["text"])
        mi_id = item["text"]

        con = self.conexion()
        cursor = con.cursor()
        data = (mi_id,)
        sql = "DELETE FROM discografica WHERE id = ?"
        cursor.execute(sql, data)
        con.commit()
        print("Item dado de baja")
        messagebox.showinfo(title="Enhorabuena!", message="Item eliminado con éxito")
        self.actualizar_treeview(tree)
        tree.delete(valores)

    def actualizar_treeview(self, mitreview):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)
        sql = "SELECT * FROM discografica ORDER BY id ASC"
        con = self.conexion()
        cursor = con.cursor()
        datos = cursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            mitreview.insert(
                "", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4])
            )

    def modificar(self, artista, album, unidades, valor, tree):
        valores = tree.selection()
        print(valores)
        item = tree.item(valores)
        print(item)
        print(item["text"])
        mi_id = item["text"]
        data = (artista, album, unidades, valor, mi_id)
        sql = "UPDATE discografica SET artista = ?, album = ?, unidades = ?, valor = ? WHERE id = ?"
        con = self.conexion()
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()
        print("Item modificado")
        messagebox.showinfo(title="Enhorabuena!", message="Item modificado con éxito")
        self.actualizar_treeview(tree)
