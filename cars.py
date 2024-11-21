class Car:
    def __init__(s, make, model, year, mileage, fuel_tank_capacity=0, battery_capacity=None, battery_status=None):
        s.make = make
        s.model = model
        s.year = year
        s.mileage = mileage
        s.fuel_tank_capacity = fuel_tank_capacity
        s.total_miles = 0
        s.total_gallons_used = 0
        s.maintenance_tasks = []
        s.battery_capacity = battery_capacity
        s.battery_status = battery_status

    def add_mileage_and_fuel(s, miles_driven, fuel_used):
        s.total_miles += miles_driven
        s.total_gallons_used += fuel_used

    def calculate_fuel_efficiency(s):
        if s.total_gallons_used > 0:
            return round(s.total_miles / s.total_gallons_used, 2)
        return "Invalid input, no gallons used."

    def add_maintenance_task(s, task):
        s.maintenance_tasks.append(task)

    def display_maintenance_tasks(s):
        print("\nMaintenance Tasks:")
        if s.maintenance_tasks:
            for task in s.maintenance_tasks:
                print(f"- {task}")
        else:
            print("No maintenance tasks recorded.")

    def display_car_details(s):
        print("\nCar Details:")
        print(f"Make: {s.make}")
        print(f"Model: {s.model}")
        print(f"Year: {s.year}")
        print(f"Mileage: {s.mileage} miles")
        if s.total_gallons_used > 0:
            print(f"Fuel Efficiency: {s.calculate_fuel_efficiency()} miles per gallon")
        if s.battery_capacity is not None:
            s.display_electric_car_details()

    def add_electric_car_details(s, battery_capacity, battery_status):
        s.battery_capacity = battery_capacity
        s.battery_status = battery_status

    def calculate_electric_range(s):
        if s.battery_capacity is not None:
            return s.battery_capacity * 5  #just Assuming 5 miles per kWh
        return "Battery capacity not set."

    def display_electric_car_details(s):
        print("\nElectric Car Details:")
        print(f"Battery Capacity: {s.battery_capacity} kWh")
        print(f"Battery Status: {s.battery_status}%")
        print(f"Electric Range: {s.calculate_electric_range()} miles")


def main():
    make = input("Enter the car make: ")
    model = input("Enter the car model: ")
    year = int(input("Enter the car year: "))
    mileage = int(input("Enter the car mileage: "))

    car = Car(make, model, year, mileage)

    miles_driven = float(input("\nEnter the miles driven: "))
    gallons_used = float(input("Enter the gallons of fuel used: "))
    car.add_mileage_and_fuel(miles_driven, gallons_used)

    while True:
        task = input("Enter maintenance task (type 'finish' to save): ")
        if task.lower() == "finish":
            break
        car.add_maintenance_task(task)

    if input("\nIs this an electric car? (yes/no): ").lower() == "yes":
        battery_capacity = int(input("Enter the battery capacity (in kWh): "))
        battery_status = int(input("Enter the battery status (in %): "))
        car.add_electric_car_details(battery_capacity, battery_status)

    car.display_car_details()
    car.display_maintenance_tasks()


main()
