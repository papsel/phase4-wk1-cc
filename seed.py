from app import app, db
from app.models import Restaurant, Pizza, RestaurantPizza

# Sample Restaurants
restaurants_data = [
    {"name": "Pizza Hut", "address": "Westgate Mall, Mwanzi Road, Nrb 100"},
    {"name": "Mama's Pizza", "address": "123 Main Street, Downtown"},
    {"name": "Tony's Pizzeria", "address": "456 Elm Street, Suburbia"},
    {"name": "Pizza Palace", "address": "789 Oak Street, City Center"},
    {"name": "Pizza Express", "address": "10 Elm Street, Downtown"},
    {"name": "Pizza World", "address": "123 Pine Street, Suburbia"},
    {"name": "Italian Delight", "address": "456 Oak Street, City Center"},
    {"name": "Pizza Heaven", "address": "123 Maple Street, Downtown"},
    {"name": "Pizza Land", "address": "789 Elm Street, Suburbia"},
]

# Sample Pizzas
pizzas_data = [
    {"name": "Cheese", "ingredients": "Dough, Tomato Sauce, Cheese"},
    {"name": "Pepperoni", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"},
    {"name": "Vegetarian", "ingredients": "Dough, Tomato Sauce, Cheese, Mushrooms, Peppers, Onions"},
    {"name": "Hawaiian", "ingredients": "Dough, Tomato Sauce, Cheese, Ham, Pineapple"},
    {"name": "Margherita", "ingredients": "Dough, Tomato Sauce, Cheese, Basil"},
    {"name": "Supreme", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Mushrooms, Onions, Peppers, Olives"},
    {"name": "BBQ Chicken", "ingredients": "Dough, BBQ Sauce, Cheese, Chicken, Onions"},
    {"name": "Spinach and Feta", "ingredients": "Dough, Tomato Sauce, Cheese, Spinach, Feta Cheese"},
    {"name": "Meat Lovers", "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni, Sausage, Bacon, Ham"},
    {"name": "Veggie Supreme", "ingredients": "Dough, Tomato Sauce, Cheese, Mushrooms, Onions, Peppers, Olives, Tomatoes"},
]

# Sample RestaurantPizzas (Linking pizzas to restaurants with prices)
restaurant_pizzas_data = [
    {"price": 10.99, "restaurant_id": 1, "pizza_id": 1},
    {"price": 12.99, "restaurant_id": 1, "pizza_id": 2},
    {"price": 11.99, "restaurant_id": 2, "pizza_id": 1},
    {"price": 13.99, "restaurant_id": 2, "pizza_id": 3},
    {"price": 9.99, "restaurant_id": 3, "pizza_id": 1},
    {"price": 11.99, "restaurant_id": 3, "pizza_id": 4},
    {"price": 12.99, "restaurant_id": 4, "pizza_id": 2},
    {"price": 14.99, "restaurant_id": 4, "pizza_id": 5},
    {"price": 10.99, "restaurant_id": 5, "pizza_id": 1},
    {"price": 12.99, "restaurant_id": 5, "pizza_id": 3},
    {"price": 11.99, "restaurant_id": 6, "pizza_id": 4},
    {"price": 13.99, "restaurant_id": 6, "pizza_id": 5},
    {"price": 9.99, "restaurant_id": 7, "pizza_id": 1},
    {"price": 11.99, "restaurant_id": 7, "pizza_id": 2},
    {"price": 12.99, "restaurant_id": 8, "pizza_id": 3},
    {"price": 14.99, "restaurant_id": 8, "pizza_id": 4},
    {"price": 10.99, "restaurant_id": 9, "pizza_id": 2},
    {"price": 12.99, "restaurant_id": 9, "pizza_id": 5},
    {"price": 11.99, "restaurant_id": 10, "pizza_id": 1},
    {"price": 13.99, "restaurant_id": 10, "pizza_id": 4},
]

def seed_database():
    with app.app_context():  # Push the application context
        # Add restaurants
        for restaurant_data in restaurants_data:
            restaurant = Restaurant(**restaurant_data)
            db.session.add(restaurant)

        # Add pizzas
        for pizza_data in pizzas_data:
            pizza = Pizza(**pizza_data)
            db.session.add(pizza)

        # Add restaurant pizzas
        for rp_data in restaurant_pizzas_data:
            restaurant_pizza = RestaurantPizza(**rp_data)
            db.session.add(restaurant_pizza)

        db.session.commit()

if __name__ == "__main__":
    seed_database()
