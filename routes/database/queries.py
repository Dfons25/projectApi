from .structure import Meal, db

def get_meals():
    return Meal.query.all()


def add_meal(meal_name, meal_desc, meal_pict, calories):
    meal = Meal(meal_name=meal_name, meal_desc=meal_desc, meal_pict=meal_pict, calories=calories)
    db.session.add(meal)
    db.session.commit()
    return meal


def get_meal_byId(id):
    return Meal.query.filter_by(id=int(id)).first()


def remove_meal(id):
    meal = Meal.query.filter_by(id=int(id)).first()
    db.session.delete(meal)
    db.session.commit()

