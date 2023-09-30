class FoodItem:
    def __init__(self, name, calories_per_100_grams):
        self.name = name
        self.calories_per_100_grams = calories_per_100_grams

class CaloriesCalculator:
    def calculate(self, food_items):
        total_caloryes = 0
        for food_item in food_items:
            total_calories += food_item.calories_per_100_grams
        return total_calories

apple = FoodItem("Apple", "52")

calculator = CaloriesCalculator()
total_calories = calculator.calculate([])

print(total_calories)

# Zadanie: Znajdź błędy w tym kodzie i zasugeruj jak je naprawić