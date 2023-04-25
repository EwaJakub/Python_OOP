class Ingredient:
    def __init__(self, name: str, protein_in_100g: float, carbs_in_100g: float, fats_in_100g: float):
        self.name = name
        self.protein_in_100g = protein_in_100g
        self.carbs_in_100g = carbs_in_100g
        self.fats_in_100g = fats_in_100g

    def __str__(self):
        return f"Utwórz składnik {self.name}: " \
               f"białko = {self.protein_in_100g}, " \
               f"węglowodany = {self.carbs_in_100g}, " \
               f"tłuszcze = {self.fats_in_100g}"


class Meal:
    def __init__(self, meal_name: str):
        self.meal_name = meal_name
        self.meal_in = []

    def __str__(self):
        return f"Utwórz Posiłek {self.meal_name}"

    def meal_ingredients(self, weight, ingrid):
        self.meal_in.append([weight,
                             ingrid.name,
                             weight * ingrid.protein_in_100g/100,
                             weight * ingrid.carbs_in_100g/100,
                             weight * ingrid.fats_in_100g/100])

    def show_ingredients(self):
        print(f"Składniki {self.meal_name} to:")
        for element in self.meal_in:
            print(f"{element[0]}g {element[1]}: "
                  f"białko = {element[2]}, "
                  f"węglowodany = {element[3]}, "
                  f"tłuszcze = {element[4]}")


class DayPlan:
    def __init__(self, plan_name: str):
        self.plan_name = plan_name
        self.day_plan_meals = []

    def meals_add(self, meal):
        self.day_plan_meals.append([meal.meal_name, meal.meal_in])

    def show_meals(self):
        print(f"Plan dnia {self.plan_name} składa się z:")
        dayplan_summary = [0, 0, 0, 0]
        for element in self.day_plan_meals:
            print(f"Posiłek: {element[0]}")
            meal_summary = [0, 0, 0, 0]
            for el in element[1]:
                meal_summary[0] += el[2]
                meal_summary[1] += el[3]
                meal_summary[2] += el[4]
                meal_summary[3] += el[2]*4 + el[3]*4 + el[4]*9.4
                print(f"- {el[0]}g {el[1]} "
                      f"białko = {el[2]}, "
                      f"węglowodany = {el[3]}, "
                      f"tłuszcze = {el[4]}, "
                      f"kcal = {el[2]*4 + el[3]*4 + el[4]*9.4},")
            dayplan_summary[0] += meal_summary[0]
            dayplan_summary[1] += meal_summary[1]
            dayplan_summary[2] += meal_summary[2]
            dayplan_summary[3] += meal_summary[3]
            print(f"Razem: {meal_summary[0]}g białka, "
                  f"{meal_summary[1]} węglowodanów, "
                  f"{meal_summary[2]} tłuszczy, "
                  f"{meal_summary[3]} kcal")
        print(f"RAZEM: {dayplan_summary[0]}g białka, "
              f"{dayplan_summary[1]} węglowodanów, "
              f"{dayplan_summary[2]} tłuszczy, "
              f"{dayplan_summary[3]} kcal")


egg = Ingredient("Jajko", 13, 1.1, 11)
print(egg)
tomato = Ingredient("Pomidor", 0.9, 3.9, 0.2)
print(tomato)
bread = Ingredient("Chleb", 9, 49, 3.2)
print(bread)

scrambled_eggs = Meal("Jajecznica")
print(scrambled_eggs)

sandwich = Meal("Kanapka")
print(sandwich)

scrambled_eggs.meal_ingredients(200, egg)
scrambled_eggs.meal_ingredients(50, tomato)

sandwich.meal_ingredients(25, bread)
sandwich.meal_ingredients(50, tomato)

scrambled_eggs.show_ingredients()
sandwich.show_ingredients()

dieta_adelle = DayPlan("Dieta Adelle")
dieta_adelle.meals_add(sandwich)
dieta_adelle.meals_add(scrambled_eggs)

print(dieta_adelle.day_plan_meals)
dieta_adelle.show_meals()
