"""
Sean Killian
Thursday @ 2pm
"""

def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = base_wash
   
    #type your code here 
    selected_services = []

    for service_choice in [service_choice1, service_choice2]:
        if service_choice != '-':
            service_cost = services[service_choice]
            selected_services.append(f'{service_choice} - ${service_cost}')
            total += service_cost

    print("ZyCar Wash")
    print(f'Base car wash - ${base_wash}')

    for service in selected_services:
        print(service)

    print('-----')

    print(f'Total price: ${total}')

if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
