from flask_restplus import Resource, fields, Namespace
import routes.database.queries as db
import routes.database.structure as models

"""
Module responsible for handling the api
Will only recieve and send json 
"""

endpoint = Namespace('api', description='api related endpoints')


rf_meal = endpoint.model('meal_rf', {
    'meal_name': fields.String,
    'meal_desc': fields.String,
    'calories': fields.Integer
})

@endpoint.route('/')
class RegisterUser(Resource):

    def get(self):

        meal = db.get_meal()
        return models.MealSchemaConvert().dump(meal, many=True).data, 200

    @endpoint.expect(rf_meal)
    def post(self):

        json_object = endpoint.payload

        meal = models.MealSchemaValidate().load(json_object)

        if not meal.errors:
            saved_meal = db.add_meal()

            if saved_meal:
                return models.MealSchemaConvert().dump(saved_meal).data, 200
            return {'message': 'Invalid operation'}, 404

        return meal.errors, 400

