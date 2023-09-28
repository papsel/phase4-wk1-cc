from flask import jsonify, request, abort
from app import app, db
from app.models import Restaurant, Pizza, RestaurantPizza
from app.validations import validate_restaurant, validate_pizza, validate_restaurant_pizza

# Define your routes here
# GET /restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [{"id": restaurant.id, "name": restaurant.name, "address": restaurant.address} for restaurant in restaurants]
    return jsonify(restaurant_list)

# GET /restaurants/:id
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404
    
    pizzas = [{"id": rp.pizza.id, "name": rp.pizza.name, "ingredients": rp.pizza.ingredients} for rp in restaurant.restaurant_pizzas]
    
    return jsonify({"id": restaurant.id, "name": restaurant.name, "address": restaurant.address, "pizzas": pizzas})

# DELETE /restaurants/:id
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({"error": "Restaurant not found"}), 404
    
    # Delete associated RestaurantPizzas
    for rp in restaurant.restaurant_pizzas:
        db.session.delete(rp)
    
    db.session.delete(restaurant)
    db.session.commit()
    
    return '', 204

# GET /pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients} for pizza in pizzas]
    return jsonify(pizza_list)

# POST /restaurant_pizzas
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    validation_errors = validate_restaurant_pizza(data)
    if validation_errors:
        return jsonify({"errors": validation_errors}), 400
    
    pizza = Pizza.query.get(data['pizza_id'])
    restaurant = Restaurant.query.get(data['restaurant_id'])
    
    if pizza is None or restaurant is None:
        return jsonify({"error": "Pizza or Restaurant not found"}), 404
    
    new_rp = RestaurantPizza(price=data['price'], pizza=pizza, restaurant=restaurant)
    db.session.add(new_rp)
    db.session.commit()
    
    return jsonify({"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients}), 201
