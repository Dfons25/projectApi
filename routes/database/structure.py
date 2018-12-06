from flask_sqlalchemy import SQLAlchemy, get_debug_queries
from flask_marshmallow import Marshmallow
import datetime


"""
Module where the database structure is handled
All tables are matched to a marshmallow ModelSchema for an automatic json convertion
All Schema can have their own validation rules
"""

db = SQLAlchemy()
ma = Marshmallow()

def _get_date():
    return datetime.datetime.utcnow()


"""
Task table
"""

class Meal(db.Model):
    __tablename__ = 'meal'
    id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(250), nullable=False)
    meal_desc = db.Column(db.String(250), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

class MealSchemaConvert(ma.ModelSchema):
    class Meta:
        model = Meal
        include_fk = True

