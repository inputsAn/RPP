class State:
    def __init__(self, name, regime, population):
        self.regime = regime
        self.name = name
        self.population = population

    def elections(self):
     if State.regime == "monarchy":
        print("Выборов нет!")
     else:
        print("Выборы есть!")

    def state_info(self):
        print(f"Государство: {self.name}, население: {self.population}, выборы: {self.elections}")


def main():
    saudi_arabia = State("Saudi_Arabia", "monarchy", 34000000)
    israel = State("Israel", "democracy", 9500000)

    israel.state_info()
    saudi_arabia.state_info()

