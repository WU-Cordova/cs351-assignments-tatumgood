from tests.car import Car, Color, Make, Model

def main():
    print('Hello world!')

    car = Car(vin='123456789', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
    print(car)

if __name__ == '__main__':
    main()
