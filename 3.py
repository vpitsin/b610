class UsersGold:
    def __init__(self, name, surname, pennies):
        self.name = name
        self.surname = surname
        self.pennies = pennies
    def get_gold_of_user(self):
        return ("Клиент «"+self.name+" "+self.surname+"». Баланс: "+str(self.pennies)+" руб.")

user1 = UsersGold("Иван", "Петров", 50)

print(user1.get_gold_of_user())