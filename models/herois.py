#herois precisam das seguintes funções
#nome
#rank (Class S, A, B, C)
#localização (latitude, longitude)
#status (disponivel, em missão, Inativo)
from extensions import banco
from sqlalchemy import Enum


from extensions import banco


class Herois(banco.Model):
    __tablename__ = "herois"

    id_hero = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(60), nullable=False)
    rank = banco.Column(banco.String(10), nullable=False)
    latitude = banco.Column(banco.Float, nullable=False)
    longitude = banco.Column(banco.Float, nullable=False)
    status = banco.Column(
        banco.Enum("Disponível", "Em missão", "Inativo", name="status_enum"),
        nullable=False,
        default="Disponível"
    )

    def __init__(self, nome, rank, status, latitude, longitude):
        self.nome = nome
        self.rank = rank
        self.status = status
        self.latitude = latitude
        self.longitude = longitude

    def json(self):
        return {
            "id_hero": self.id_hero,
            "nome": self.nome,
            "rank": self.rank,
            "status": self.status,
            "localizacao": {
                "latitude": self.latitude,
                "longitude": self.longitude
            }
        }

    def save_hero(self):
        banco.session.add(self)
        banco.session.commit()

    def update_hero(self, nome, rank, latitude, longitude, status):
        self.nome = nome
        self.rank = rank
        self.latitude = latitude
        self.longitude = longitude
        self.status = status
        banco.session.commit()

    def delete_hero(self):
        banco.session.delete(self)
        banco.session.commit()

    @classmethod
    def find_hero(cls, id_hero):
        return cls.query.filter_by(id_hero=id_hero).first()

    @classmethod
    def buscar_por_rank(cls, rank):
        return cls.query.filter_by(rank=rank).all()