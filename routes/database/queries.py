from .structure import Meal, db

def get_meals():
    return Meal.query.all()


def get_meals_cat_id(id):
    return Meal.query.filter_by(cat_id=(id)).all()


def add_meal(meal_name, meal_desc, meal_pict, calories):
    meal = Meal(meal_name=meal_name, meal_desc=meal_desc, meal_pict=meal_pict, calories=calories)
    db.session.add(meal)
    db.session.commit()
    return meal


def get_meal_byId(id):
    return_meal = Meal.query.filter_by(id=int(id)).first()
    return return_meal

def remove_meal(id):
    meal = Meal.query.filter_by(id=int(id)).first()
    db.session.delete(meal)
    db.session.commit()

def return_by_max_cal(id, cal):
    return_meal_list = []
    no_meals_left = []
    cal_sum = 0

    while cal_sum < int(cal):
        for cat_id in str(id):

            meal_to_add = Meal.query.filter_by(cat_id=int(cat_id)).order_by(Meal.calories.asc()).first()

            if not meal_to_add:
                no_meals_left.append(cat_id)

                if len(set(no_meals_left)) == len(str(id)):
                    return return_meal_list, cal_sum
                continue

            if cal_sum + meal_to_add.calories > int(cal) + int(cal) / 10:
                return return_meal_list, cal_sum

            for meal in return_meal_list:
                if meal.cat_id == int(cat_id):
                    return_meal_list.remove(meal)

            return_meal_list.append(meal_to_add)
            Meal.query.filter_by(id=int(meal_to_add.id)).delete()
            cal_sum = sum([values.calories for values in return_meal_list])

    return return_meal_list, cal_sum

def get_meals_byCal(id, cal):
    return_meal_list, cal_sum = return_by_max_cal(id, cal)
    print(cal_sum)
    return return_meal_list