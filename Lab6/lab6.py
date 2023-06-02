import string
import sqlite3
import cherrypy

from peewee import *
from datetime import date

db = SqliteDatabase('Spravki.db')


class Spravki(Model):
    number = IntegerField()
    date = DateField()
    fio = CharField()
    grant = IntegerField()
    destination = CharField()

    class Meta:
        database = db


Spravki.create_table()


class Table(object):
    @cherrypy.expose
    def index(self):
        html_code = """<html>
          <head>
                <meta charset="utf-8">
                <title>Tаблица</title>
            </head>
          <body>
          <form method="get" action="add" align="center">
              <input type="text" value="Номер" name="number" />
              <input type="text" value="Дата" name="date" />
              <input type="text" value="ФИО" name="fio" />
              <input type="text" value="Стипендия" name="grant" />
              <input type="text" value="Направление" name="destination" />
              <button type="submit">Добавить</button>
          </form>
          <table align="center">
          <style type="text/css">
          TABLE {
              margin: auto;
              max-width: 800px;
              width: 80%;
              border-collapse: separate;
              border-spacing: 20px;
              background-color: antiquewhite;
              opacity: 0.9;
          }
          TD, TH {
              padding: 3px;
              border: 1px solid black;
              background-color: burlywood
              
          }
          p {
            font-size: 50px
          }
          ya-tr-span p{
            color: black
          }
          </style>
          <p align="center">Справки из деканата</p>
          <tr>
          <td align="center">№</td>
          <td align="center">Дата</td>
          <td align="center">ФИО</td>
          <td align="center">Стипения</td>
          <td align="center">Куда выдается справка</td>
          </tr>"""
        for item in Spravki.select():
            html_code += """<tr><form method="get" action="changes">
              <td><input type="text" value=" """ + str(item.number) + """"name="number" /></td>
              <td><input type="text" value=" """ + str(item.date) + """"name="date" /></td>
              <td><input type="text" value=" """ + str(item.fio) + """"name="fio" /></td>
              <td><input type="text" value=" """ + str(item.grant) + """"name="grant" /></td>
              <td><input type="text" value=" """ + str(item.destination) + """"name="destination" /></td>
              <td><input type="hidden" value=" """ + str(item.id) + """"name="id" /></td>
              <td><button type="submit">Изменить</button></td></tr>
          </form>"""
        html_code += """</table>
        </body>
        </html>"""

        return html_code

    @cherrypy.expose
    def add(self, number="number", date="date", fio="fio", grant="grant",
            destination="destination"):
        flag = True
        for item in Spravki.select():
            if item.number == int(number):
                flag = False
                break
        if flag:
            Spravki(number=int(number), date=str(date), fio=str(fio), grant=int(grant),
                               destination=str(destination)).save()
        return Table.index(self)

    @cherrypy.expose
    def changes(self, number="number", date="date", fio="fio", grant="grant",
                destination="destination", id="id"):
        Spravki(number=int(number), date=str(date), fio=str(fio), grant=int(grant),
                           destination=str(destination)).update(number=number)
        for item in Spravki.select():
            if item.id == int(id):
                item.number = int(number)
                item.date = date.replace(' ', '')
                item.fio = fio.strip()
                item.grant = int(grant)
                item.destination = destination.strip()
                item.save()
                break
        return Table.index(self)


if __name__ == '__main__':
    cherrypy.quickstart(Table())
