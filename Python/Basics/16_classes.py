class MyCar:
    wheels = 4
    color = 'red'

    def my_car_get_details(self):
        print("Hello, I'm your new car")

    def great_bip(self, brand):
        if brand == 'BMW':
            print('Das bip!')
        elif brand == 'Porshe':
            print('Der bip!')

    # def bip(self):
    #     print('Bip!')



my_car = MyCar()
# my_old_car = MyCar()
# my_old_car_2 = MyCar()
# my_car.my_car_details()
# print(my_car.wheels)
# print(my_car.color)
# print(my_car.my_car_get_details())
# print(my_car.bip())
# print(my_car.great_bip('Porshe'))


# class MyFirstCar(MyCar):
#     def __init__(self):
#         self.brand = "VW"
#         self.wheels = 4
#
#     def my_car_details(self):
#         print(f'Hello, {self.brand}')
#         print(f'I have, {self.wheels}')
#
# vw = MyFirstCar()
# vw.my_car_details()