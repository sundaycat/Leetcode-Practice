class Meal(object):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

def get_unique_meal_count(meals):

    if not meals or len(meals) == 0:
        return 0

    meal_count = 0
    visited = set()
    for i in range(0, len(meals)):

        # skip the current meal if it has already been visited
        if meals[i] in visited:
            continue

        # count the number of duplicates for current meal
        cur_meal = set(meals[i].ingredients)
        for j in range(i + 1, len(meals)):
            nxt_meal = set(meals[j].ingredients)
            if nxt_meal == cur_meal:
                meal_count += 1
                visited.add(meals[j])

    return len(meals) - meal_count


# test， meal1 == meal3, meal2 == meal4 == meal5
meal1 = Meal("Basic Burger", ["Lettuce", "Tomato", "Onion", "Patty"])
meal2 = Meal("Chief Cheese Burger", ["Cheese", "Tomato", "Patty", "Lettuce"])
meal3 = Meal("Jay's Burger", ["Onion", "Tomato", "Patty", "Lettuce"])
meal4 = Meal("High Water Sandwich", ["Tomato", "Patty", "Lettuce", "Cheese"])
meal5 = Meal("Chief Cheese Burger", ["Cheese", "Tomato", "Patty", "Lettuce"])

meals = [meal1, meal2, meal3, meal4, meal5]
print(get_unique_meal_count(meals))

'''
sort by ingredient
add ingredient into set
'''