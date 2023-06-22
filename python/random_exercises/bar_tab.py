# the ninja net -> python 20 https://www.youtube.com/watch?v=h4NetyxAhv4&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=22

class Tab:

    menu = {
        'wine': 5
        'beer': 3
        'sofe_drink': 2
        'beef': 15
        'veggie': 12
        'desert': 6
    }

    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = self.total + tax + service 

    for item in self.items:
        print(f'{item} £{self.menu[item]}')

    print(f'{"Total"} £ {total:.2f}')