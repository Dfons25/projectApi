from .structure import Meal, db



def get_meal():
    return Meal.query.all()

def add_meal():
    db.session.add(
        Meal(meal_name='teste', meal_desc='teste', calories=1))
    db.session.commit()

    new_meal = Meal.query.filter_by(
        meal_name='teste').first()

    return new_meal
