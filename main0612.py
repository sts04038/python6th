# class Car:
#     wheels = 4
#
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#
#     # method
#     def drive(self):
#         return "The car is moving"
#     def stop(self):
#         return "The car has stopped."
#
# my_car = Car("Kia", "Morning", "Blue")
#
# # 속성 사용
# print(my_car.make)      # Kia
# # 메소드 호출
# print(my_car.drive())   # The car is moving
# print(my_car.stop())    # The car has stopped.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "The enging is running!"

# 자식 클래스
class Car(Vehicle):
    def start_engine(self):
        return super().start_engine() + " It's a car engine"

# 인스턴스 생성
my_car = Car("Toyota", "Corolla", 2020)

#메소드 출력
print(my_car.start_engine())