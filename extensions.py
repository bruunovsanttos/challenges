#para instanciar o banco de dados de forma correta sem dar importação circular
from flask_sqlalchemy import SQLAlchemy
banco = SQLAlchemy()
