from datetime import datetime


class Person:
    def __init__(self, firstName, lastName, country, birthDate):
        self.firstName = firstName
        self.lastName = lastName
        self.country = country
        try:
            self.birthDate = datetime.strptime(birthDate, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Birthdate should be like: YYYY-MM-DD") from e

    def calcAge(self):
        if datetime.now().month <= self.birthDate.month and datetime.now().day < self.birthDate.day:
            return datetime.now().year - self.birthDate.year
        return datetime.now().year - self.birthDate.year - 1

    def __str__(self):
        return f"{self.firstName} {self.lastName} from {self.country} born at {self.birthDate.strftime('%Y-%m-%d')}"

    def __repr__(self):
        return f"Person('{self.firstName}', '{self.lastName}', '{self.country}', '{self.birthDate.strftime('%Y-%m-%d')}')"


def __main__():
    p1 = Person("Sam", "Smith", "India", "2002-01-01")
    print(p1)
    print(p1.calcAge())
    # p2 = eval("Person({xxx}, {xxx}, {xxx}, {2000-01-01})")

    people = []
    while True:
        try:
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            country = input("Country: ")
            birthdate = input("Birthdate (YYYY-MM-DD): ")
            person = Person(firstName, lastName, country, birthdate)
            people.append(person)
        except ValueError as e:
            print(e)

        var = input("Do you want to add another person? (y/n): ").lower()
        if var == "n":
            break

    print("\nPeople:")
    for person in people:
        print(person)

    minAge = int(input("\nEnter min age: "))
    maxAge = int(input("Enter max age: "))

    print(f"\nPeople in age between {minAge}-{maxAge}:")
    for person in people:
        age = person.calcAge()
        if minAge <= age <= maxAge:
            print(repr(person))


if __name__ == "__main__":
    __main__()
