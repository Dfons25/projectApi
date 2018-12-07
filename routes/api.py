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
    'meal_pict': fields.String,
    'calories': fields.Integer,
    'cat_id': fields.Integer
})

rf_id = endpoint.model('id_rf', {
    'id': fields.Integer
})

@endpoint.route('/meals')
class Meal(Resource):

    def get(self):
        meal = db.get_meals()
        return models.MealSchemaConvert().dump(meal, many=True).data, 200

    @endpoint.expect(rf_meal)
    def post(self):

        json_object = endpoint.payload

        saved_meal = db.add_meal(json_object['meal_name'],
                                 json_object['meal_desc'],
                                 json_object['meal_pict'],
                                 json_object['calories'],
                                 json_object['cat_id'],
                                 )

        if saved_meal:
            return models.MealSchemaConvert().dump(saved_meal).data, 200
        return {'message': 'Invalid operation'}, 404


@endpoint.route('/meals/<id>')
class Meal_D(Resource):

    @endpoint.doc(params={'id': 'Cat id'})
    def get(self, id):
        meal = db.get_meals_cat_id(id)
        return models.MealSchemaConvert().dump(meal, many=True).data, 200

    @endpoint.doc(params={'id': 'Meal id'})
    def delete(self, id):

        meal = db.get_meal_byId(id)
        if meal:
            db.remove_meal(id)
            return {'message': 'Meal removed'}, 201

        return {'message': 'Invalid operation'}, 404



