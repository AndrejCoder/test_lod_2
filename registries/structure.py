# coding: utf-8
from eve_sqlalchemy.decorators import registerSchema
from sqlalchemy import Integer, Column
from sqlalchemy.dialects.postgresql.json import JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@registerSchema('registry')
class RegistrySchema(Base):
    __tablename__ = 'registries_registry'
    id = Column(Integer, primary_key=True, autoincrement=True)
    json_data = Column(JSON)

