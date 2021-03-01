class Person:
    def __init__(self, name):
        self.name = name
    def get_person_info(self):
        return (f'Имя клиента: {self.name}')

user1 = Person("Иван Петров")

class BigBoss(Person):
    def __init__(self, name, city, status):
        Person.__init__(self, name)
        self.city = city
        self.status = status
    def get_bigboss_info(self):
        return (self.name + ', г. ' + self.city + ', статус "' + self.status + '"')

bb1=BigBoss("Иван Петров", "Москва", "Наставник")
bb2=BigBoss("Петр Иванов", "НиНо", "Падаван")
bb3=BigBoss("Евгений Смирнов", "Екат", "Модный блогер")
bb4=BigBoss("Фёдор Фадеев", "Житомир", "Наставник")

BB = [bb1, bb2, bb3, bb4]
for p in BB:
    print(p.get_bigboss_info())