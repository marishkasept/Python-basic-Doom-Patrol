class Car:
    car_type = 'regular car'

    def __init__(self, color, brand, model, engine_type='Gasoline'):
        self.color = color
        self.brand = brand
        self.model = model
        self.engine_type = engine_type
        self.speed = 0

    def print_engine_type(self):
        print(f'I have {self.engine_type} engine.')

    def print_brand_and_model(self):
        print(f'I am {self.brand} {self.model}')

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        print(self.speed)


ford_focus = Car(color='blue', brand='Ford', model='Focus', engine_type='diesel')
toyota_prius = Car(color='green', brand='Toyota', model='Prius', engine_type='Hybrid')
bmw_3 = Car(color='red', brand='BMW', model='3')

all_car_objs = (ford_focus, toyota_prius, bmw_3)

for car in all_car_objs:
    car.print_brand_and_model()
    car.print_engine_type()
    for i in range(10):
        car.accelerate()
    car.get_speed()
    for i in range(5):
        car.brake()
    car.get_speed()


# ford_focus.print_brand_and_model()
# toyota_prius.print_brand_and_model()
# bmw_3.print_brand_and_model()
#
# ford_focus.print_engine_type()
# toyota_prius.print_engine_type()
# bmw_3.print_engine_type()
#
# def do_smth(a, b, c=None, d=None, e=None):
#     print(a, b)
#
# do_smth(5,7)
print(dir("bmw_3"))

