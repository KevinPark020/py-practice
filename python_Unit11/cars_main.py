import cars


def main():
    car1 = cars.Car("29988", "Hyundai Genesis", "G90", 2026)
    car2 = cars.Car("8829", "BMW", "X5", 2020)
    car3 = cars.Car("29988", "Audi", "R8", 2019)
    car4 = cars.Car("44925", "Rolls Royce", "Phantom", 2024)
    car5 = cars.Car("23992", "Porsche", "Panamera", 2025)

    # cars.print_cars(car1)
    # print("\n")
    # cars.print_cars(car2)

    # car1.filler_up(15)
    # car2.filler_up(13)

    # cars.print_cars(car1)
    # print("\n")
    # cars.print_cars(car2)

    print(car1)

    print(car1 == car2) # False
    print(car1 == car3) # True

    car_list = [car1, car2, car3, car4, car5]

    car_set = set()

    car_set.add(car1)
    car_set.add(car2)
    car_set.add(car3)
    car_set.add(car4)
    car_set.add(car5)
    
    # print(sorted(car_list))

    print(car_set)





if __name__ == "__main__":
    main()