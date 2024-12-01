from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    number_of_mohikan = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.
class Aso(Model):
    aso = CharField()
    class Meta:
        database = db

db.create_tables([Person, Aso])