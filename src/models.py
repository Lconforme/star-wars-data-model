import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    first_name = Column(String(250))
    last_name =Column(String(250))
    email = Column(String(250))
    password = Column(String(50))


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=True)
    genders = Column(String(250), nullable=True)
    hair_color = Column(String(250), nullable=True)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=True)
    home_world_id = Column(Integer, ForeignKey('planet.id'))
    home_world = relationship('Planet')


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diameter = Column(String(250))
    rotational_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    starship_class = Column(String(250))
    manufactuer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    hyperdrive_rating = Column(String(250))
    MGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column (Integer, primary_key=True)
    user_id = Column(ForeignKey('user.id'))
    favorite_name = Column(String(250))
    favorite_planet_id = Column(Integer, ForeignKey('planet.id'))
    favorite_character_id = Column(Integer, ForeignKey('character.id'))
    favorite_starship_id = Column(Integer, ForeignKey('starship.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')