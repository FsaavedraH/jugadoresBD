from django.db import models
from mongoengine import Document, StringField, IntField

# Create your models here.
class Player(Document):
    meta = {'collection': 'players_db'}
    name = StringField(required=True)
    age = IntField(required=True)
    country = StringField()
    surname = StringField()
    team_id = StringField()

    def to_dict(self):
        return {
            'id': str(self.id),  # Convierte el ID a cadena
            'name': self.name,
            'age': self.age,
            'country': self.country,
            'surname': self.surname,
            'team_id': self.team_id,
        }
        
class Team(Document):
    meta = {'collection': 'teams_db'}
    name_team = StringField(required=True)  # Asegúrate de que este campo esté aquí
    country = StringField()

    def to_dict(self):
        return {
            'id': str(self.id),  # Asegúrate de que el ID se incluya aquí
            'name_team': self.name_team,
            'country': self.country,
        }

    


class Transfer(Document):
    player_name = StringField(required=True)
    from_team = StringField(required=True)
    to_team = StringField(required=True)
    transfer_fee = IntField()

