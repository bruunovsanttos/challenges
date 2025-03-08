#herois precisam das seguintes funções
#nome
#rank (Class S, A, B, C)
#localização (latitude, longitude)
#status (disponivel, em missão, Inativo)
from extensions import banco


class Herois(banco.Model):
    __tablename__ = "herois"

    nome = banco.Column(banco.String, primary_key= True)
    rank = banco.Column(banco.String(10))
    localizacao = ()#ver qual a necessidade do banco para localização
    status = ()#criar para os tres unicos status)

    def __init__(self, nome, rank, localizacao, status):
        self.nome = nome,
        self.rank = rank,
        self.localizacao = localizacao
        self.status = status

    def json(self):
        return {
            'nome':self.nome,
            'rank':self.rank,
            'localizacao':self.localizacao,
            'status':self.status
        }