'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit H In-class assignments
'''

#                       Part 1  A Basic Class  State Data
#Create a StateData class with the following methods: __init__, __str__, displayState.
class StateData:
    #method has the parameters self, name, abbreviation, region, and population and
    # should store the name, abbreviation, region, and population as attributes.
    def __init__(self, name, abbreviation, region, population):
        self.name = name
        self.abbreviation = abbreviation
        self.region = region
        self.population = population
    # method has the parameter self and should return the state's name.
    def __str__(self):
        return  self.name
    # has the parameter self and should print formatted state data
    def displayState(self):
        print(f"{self.name} ({self.abbreviation}) is in the {self.region} region and has population of {self.population}")

#                       Part 2  Different ways of working with Attributes
#Create a StateData2 class with the following methods: __init__, setRegion, getRegion.
class StateData2:
    def __init__(self,name ):
        self.name = name
    def setRegion(self,region):
        self.region = region
    def getRegion(self):
        return self.region

#                       Part 3  Data Hiding
#Create a StateData2 class with the following method: __init__.
#Hi Professor, I believe I it should be the StateData3 class instead of StateData2
class StateData3:
    #method should have the parameter self. It should store the value "Public" in an attribute called public,
    # the value " Protected" in an attribute called _protected (use a single underscore),
    # and the value " Private" in an attribute called __private (use a double underscore).
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"


def main():
    # Create object and call methods for part 1
    s1  = StateData("California", "CA", "West", 39250000)
    print(s1.__str__())
    s1.displayState()
    print()

    # Create pbject and call methods for part 2
    s2 = StateData2("California")
    s2.setRegion("West")
    s2.pop = 39250000
    print(s2.name)
    print(s2.getRegion())
    print(s2.region)
    print(s2.pop)
    print()

    # Create object and call methods for part 3
    s3 = StateData3()
    # I use try-except to catch the Trace back error since that error show a very long message on my terminal
    try:
        print(s3.public)
        print(s3._protected)
        print(s3.__private)
    except:
        print("Traceback error")

if __name__ == '__main__':
    main()

'''
Execution result:
California
California (CA) is in the West region and has population of 39250000

California
West
West
39250000

Public
Protected
Traceback error

Process finished with exit code 0

'''