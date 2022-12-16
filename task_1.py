import random 
class Dice():
    def __init__ (self, facets=6, count=1):
        self.facets=facets
        self.count=count 
    def roll(self):
        a=0
        for i in range(self.count):
            a=random.randrange(1,self.facets)
            b.append(a) #добавляем в конец списка
        print(b) #вывод списка
b=[] #создаем список
count = int (input ('Введите количество костей\n'))
facets = int(input('Введите количество граней\n'))
Dice(facets, count).roll()