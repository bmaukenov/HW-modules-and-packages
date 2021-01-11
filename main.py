from Application import salary
from Application.db import people
from datetime import datetime


if __name__ == "__main__":
    salary.calculate_salary()
    people.get_employees()
    print(str(datetime.now()).split()[0])