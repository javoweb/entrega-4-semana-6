from adquisiciones.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Adquisicion(db.Model):
    __tablename__ = "adquisiciones"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    producto = db.Column(db.String, nullable=False)
    fecha = db.Column(db.String, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)