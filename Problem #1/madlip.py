'''
Sean Killian
Thursday @ 2pm
'''

def food_input():
#    user_input = input()
#    tokens = user_input.split()
    #type you while  loop here

    inputs = []

    while True:
        food = input()
        tokens = food.split()

        if tokens[0] == "quit":
            break

        inputs.append((tokens[0], int(tokens[1])))

    for food, count in inputs:
        print(f"Eating {count} {food} a day keeps you happy and healthy.")
    

if __name__ == "__main__":
    food_input()
