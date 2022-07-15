'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit E take-home assignment
'''

#---------- First Script - Decision Making ------------

#Take user's input of information of plants
name = input("Please enter the plant name: ")
type = input("Please enter the plant type: ")
height = int(input("Please enter the plant height: "))

#if-else statement to decide which gardens plants fall in
if type == "Vegetable":
    print(f"A {name} can be planted in the Vegetables Garden")
elif type == "Flower" and height <= 3:
    print(f"A {name} can be planted in the Low Garden and the High Garden")
elif type == "Flower" and height <= 6:
    print(f"A {name} can be planted in the High Garden")
else:
    print(f"A {name} does not match the criteria for any of the gardens")


'''
Execution results:

Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planted in the Low Garden and the High Garden

Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
A Bonsai does not match the criteria for any of the gardens

Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 1
A Carrots can be planted in the Vegetables Garden

Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
A Corn can be planted in the Vegetables Garden

Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can be planted in the High Garden

Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
A Sunflower does not match the criteria for any of the gardens

'''