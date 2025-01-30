class Vehicle: 
    """Parent class of Automobile"""
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type: str = vehicle_type
        
    def __str__(self):
        return self.vehicle_type

class Automobile(Vehicle):
    """Child class of Vehicle"""
    def __init__(self, vehicle_type, year: int, make: str, model: str, doors: int, roof: str):
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        self.doors: int = doors # 2 or 4
        self.roof: str = roof # Solid or Sun
        
    def __str__(self):
        return (f'Vehicle Type: {super().__str__()}\n' +
                f'Make: {self.make}\n' +
                f'Model: {self.model}\n' +
                f'Number of Doors: {self.doors}\n' +
                f'Type of Roof: {self.roof}'
                )
            
