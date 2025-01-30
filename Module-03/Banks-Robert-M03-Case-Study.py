"""
M03 - Case Study: Lists, Functions, and Classes
Author: Robert Banks
Date Written: 1/30/2025
Banks-Robert-M03-Case-Study.py

Description: This app accepts user input for a vehicle_type, year, make, model, 
number of doors, and roof type.

VARIABLES/CLASSES:
Vehicle: class - Parent class containing vehicle_type
_vehicle_type: list - List containing parameters of acceptable vehicile types

Automobile: class - Child class containing details of vehicle_type
year: int - Variable containing the integer of the year the vehicle was made
make: str - Variable containing the string of the make of the vehicle
model: str - Variable containing the string of the model of the vehicle
doors: int - Variable containing the integer of the doors the vehicle has
roof: str - Variable containing the string of the roof type the vehicle has

valid_values: list - A mutable list that changes values based on the input needing to be validated
"""

class Vehicle: 
    """Parent class of Automobile"""
    def __init__(self, vehicle_type: str) -> None: 
        self._vehicle_type = ['car', 'truck', 'plane', 'boat', 'broomstick']
        self.vehicle_type = vehicle_type
        
    @property
    def vehicle_type(self) -> str:
        """Getter for vehicle_type"""
        return self._vehicle_type
    
    @vehicle_type.setter
    def vehicle_type(self, user_type: str) -> None:
        """Setter for vehicle_type including validation"""
        if user_type.lower() not in self._vehicle_type:
            raise ValueError(f'Invalid vehicle type. Choose from {','.join(self._vehicle_type)}.')
        self._vehicle_type = user_type.lower()
    
    def __str__(self) -> str:
        """Returns a string representation of the vehicle type"""
        return f'Vehicle Type: {self._vehicle_type}'

class Automobile(Vehicle):
    """Child class of Vehicle"""
    def __init__(self, vehicle_type, year: int, make: str, model: str, doors: int, roof: str):
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        self.doors: int = doors 
        self.roof: str = roof 
        
    def __str__(self):
        return (f'{super().__str__()}\n' +
                f'Year: {self.year}\n' +
                f'Make: {self.make}\n' +
                f'Model: {self.model}\n' +
                f'Number of Doors: {self.doors}\n' +
                f'Type of Roof: {self.roof}'
                )
            

def get_vehicle_type() -> str:
    """Gets user vehicle type and validates the input to ensure it is within the list parameters"""
    while True:
        user_type = input("Enter a vehicle type (car, truck, plane, boat, broomstick): ").lower()
        try:
            transport = Vehicle(user_type)
            return transport._vehicle_type
        except ValueError as e:
            print(e)

def get_valid_integer(prompt, valid_values = None) -> int:
    """Validates door input to ensure it is either 2 or 4"""
    while True:
        try:
            doors = int(input(prompt))
            if valid_values and doors not in valid_values:
                print(f"Invalid input. Choose from {valid_values}")
            else:
                return doors
        except ValueError:
            print("Please enter a valid number.")

def get_valid_string(prompt, valid_values = None) -> str:
    """Validates roof input to ensure it is within list parameters"""
    while True:
        roof = input(prompt).strip()
        if valid_values and roof.lower() not in valid_values:
            print(f'Invalid input. Choose from {valid_values}')
        else:
            return roof

def get_automobile_details() -> None:
    """Obtains all information of user vehicle and prints it back to them"""
    vehicle_type = get_vehicle_type()
    
    year = int(input('Enter the year of the vehicle: '))
    
    make = input('Enter the make of the vehicle: ').strip().lower()
    
    model = input('Enter the model of the vehicle: ').strip().lower()
    
    doors = get_valid_integer('Enter the number of doors (2 or 4): ', valid_values = [2, 4])
    
    roof = get_valid_string('Enter the type of roof (Solid or Sun): ', valid_values = ['solid', 'sun']).strip().lower()
    
    # Create the Automobile object with all details
    automobile = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Prints automobile details from __str__ method
    print('\nAutomobile Details:')
    print(automobile)
    
# Calls the get_automobile_details function to obtain all user inputs
get_automobile_details()