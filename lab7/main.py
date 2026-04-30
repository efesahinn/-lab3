from Car import Car
from Truck import Truck
from Motorcycle import Motorcycle


def save_fleet_to_file(vehicles, filename):

    with open(filename, "w") as file:

        for v in vehicles:

            if isinstance(v, Car):
                file.write(f"Car, {v.vid}, {v.model}, {v.year}, {v.fuel_type}, {v.doors}\n")

            elif isinstance(v, Truck):
                file.write(f"Truck, {v.vid}, {v.model}, {v.year}, {v.max_load}, {v.axles}\n")

            elif isinstance(v, Motorcycle):
                file.write(f"Motorcycle, {v.vid}, {v.model}, {v.year}, {v.engine_cc}, {v.type}\n")


def load_fleet_from_file(filename):

    vehicles = []

    with open(filename, "r") as file:

        for line in file:

            parts = line.strip().split(", ")

            if parts[0] == "Car":
                vehicle = Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))

            elif parts[0] == "Truck":
                vehicle = Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]))

            elif parts[0] == "Motorcycle":
                vehicle = Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5])

            vehicles.append(vehicle)

    return vehicles


vehicles = [

    Car("V001", "Tesla Model 3", 2023, "Electric", 4),
    Car("V002", "Toyota Corolla", 2018, "Petrol", 4),

    Truck("T101", "Volvo FH16", 2019, 25000, 6),
    Truck("T102", "Mercedes Actros", 2021, 18000, 4),

    Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
    Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
]


save_fleet_to_file(vehicles, "fleet.txt")

print("Loading fleet data from fleet.txt...")
loaded = load_fleet_from_file("fleet.txt")

print()
print("All Vehicles")

for v in loaded:
    print(v)

print()
print("Recent Vehicles (Last 4 Years)")

for v in loaded:
    if v.is_new(4):
        print(v)

print()
print("Electric Cars Only")

for v in loaded:
    if isinstance(v, Car) and v.fuel_type == "Electric":
        print(v)