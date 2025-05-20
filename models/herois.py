#herois precisam das seguintes funções
#nome
#rank (Class S, A, B, C)
#localização (latitude, longitude)
#status (disponivel, em missão, Inativo)
from extensions import banco
from sqlalchemy import Enum


class Herois(banco.Model):
    __tablename__ = "herois"

    id_hero = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(60))
    rank = banco.Column(banco.String(10))
    latitude = banco.Column(banco.float)#utilizar assim para consistencia de dados
    longitude = banco.Column(banco.float)#utilizar assim para consistencia de dados
    status = banco.Column(banco.Enum('Disponível', 'Em missão', 'Inativo', name='status_enum')) #garante que somente os 3 status sejam aceitos pelo banco e pelo python

    


    def __init__(self, id_hero, nome, rank,status, latitude, longitude):
        self.id_hero = id_hero,
        self.nome = nome,
        self.rank = rank,
        self.status = status,
        self.latitude = latitude,
        self.longitude = longitude

    def json(self):
        return {
            'id_hero': self.id_hero,
            'nome': self.nome,
            'rank': self.rank,
            'status': self.status,
            'localizacao': {self.latitude,
                            self.longitude
                            },
        }

    def save_hero(self):
        banco.session.add(self)
        banco.session.commit()

    def update_hero(self, nome, rank, localizacao, status):
        self.nome = nome
        self.rank = rank
        self.localizacao = localizacao
        self.status = status

    @classmethod
    def delete_hero(cls, id_hero):
        hero = cls.find_hero(id_hero)
        if hero:
            banco.session.delete(hero)
            banco.session.commit()

    @classmethod
    def find_hero(cls, id_hero):
        hero = cls.query.filter_by(id_hero=id_hero).first()#chamando o primeiro heroi com o id
        if hero:
            return hero
        return None

    @classmethod
    def buscar_por_rank(cls, rank):
        return cls.query.filter_by(rank=rank).all()#busca herois opr rank para chamar no combate

