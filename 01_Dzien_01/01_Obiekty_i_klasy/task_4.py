class Employee:

    def __init__(self, id_val, first_name, last_name):
        self.id_val = id_val
        self.first_name = first_name
        self.last_name = last_name
        self._salary = 0

    def set_salary(self, salary):
        if isinstance(salary, (float, int)) and salary >= 0.0: # if salary >= 0.0 already confirms that salary is int
            self._salary = salary
            return salary
        else:
            return "Incorrect value"

    def get_salary(self):
        return self._salary


e = Employee(3, "Ewa", "Jakubowska")
print(e.set_salary(3))
print(e.set_salary(6.7))
print(e.get_salary())
