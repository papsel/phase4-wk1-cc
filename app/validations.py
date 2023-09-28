def validate_restaurant(data):
    errors = []
    if 'name' not in data:
        errors.append("Name is required")
    elif len(data['name']) > 50:
        errors.append("Name must be less than 50 characters")
    return errors

def validate_pizza(data):
    errors = []
    if 'name' not in data:
        errors.append("Name is required")
    return errors

def validate_restaurant_pizza(data):
    errors = []
    if 'price' not in data:
        errors.append("Price is required")
    elif not (1 <= data['price'] <= 30):
        errors.append("Price must be between 1 and 30")
    
    if 'pizza_id' not in data:
        errors.append("Pizza ID is required")
    
    if 'restaurant_id' not in data:
        errors.append("Restaurant ID is required")
    
    return errors
