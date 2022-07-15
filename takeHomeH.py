'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit H take-home assignment
'''

#               First Script - Variable-Length Keyword Arguments - kwargs
def overseerSystem(**message):
    for key, value in message.items():
        if key == "temperature" and value > 500:
            print(f"Warning: {key} is {value}")
        elif key == "CO2level" and value > 0.15:
            print(f"Warning: {key} is {value}")
        elif key == "miscError":
            print(f"Misc error #{value}")

#               Second Script - Operator Overloading
class BritCoins:
    __coinValues = {"pound": 240, "shilling": 12, "penny": 1} #value of each type of coin in pennies
    def __init__(self,  **kwargs):
        self.totalPennies = 0
        for key, value in kwargs.items():
            if key == 'pound':
                self.totalPennies += value*BritCoins.__coinValues.get('pound')
            elif key == 'shilling':
                self.totalPennies += value*BritCoins.__coinValues.get('shilling')
            elif key == 'penny':
                self.totalPennies += value

    def __add__(self, other):
        coins = self.totalPennies + other.totalPennies
        return BritCoins(**{'penny' : coins})

    def __sub__(self, other):
        coins = self.totalPennies - other.totalPennies
        return BritCoins(**{'penny': coins})

    def __str__(self):
        pound = int(self.totalPennies / 240)
        shilling = int((self.totalPennies - pound * 240) / 12)
        penny = (self.totalPennies - pound * 240 - shilling * 12)
        return f'{pound} pounds {shilling} shillings {penny} pennies'

def main():
    # Create objects and call functions for part 1
    Message1 = {'temperature': 550}
    Message2 = {'temperature': 475}
    Message3 = {'temperature': 450, 'miscError': 404}
    Message4 = {'CO2level': .18}
    Message5 = {'CO2level': .2, 'miscError': 418}

    overseerSystem(**Message1)
    overseerSystem(**Message2)
    overseerSystem(**Message3)
    overseerSystem(**Message4)
    overseerSystem(**Message5)
    print()

    # Create objects and call functions for part 2
    c1 = BritCoins(**{'pound': 4, 'shilling': 24, 'penny': 3})
    c2 = BritCoins(**{'pound': 3, 'shilling': 4, 'penny': 5})
    # I try the + for 2 objects and got the same values but I prefer using the function call more
    c3 = c1.__add__(c2)
    c4 = c1.__sub__(c2)
    print(c1.__str__())
    print(c2.__str__())
    print(c3.__str__())
    print(c4.__str__())


if __name__ == '__main__':
    main()

'''
Execution results:
Warning: temperature is 550
Misc error #404
Warning: CO2level is 0.18
Warning: CO2level is 0.2
Misc error #418

5 pounds 4 shillings 3 pennies
3 pounds 4 shillings 5 pennies
8 pounds 8 shillings 8 pennies
1 pounds 19 shillings 10 pennies

Process finished with exit code 0

'''

