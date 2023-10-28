from stacja import *
from trasa import *
from kurs import *
from bilet import *
import random
import datetime
from faker import Faker

NUMBER_OF_STATIONS = 500
NUMBER_OF_ROUTES = 100

TRAIN_SPEED = 80
TRAIN_SPEED_FLUCTUATION = 10
MAX_DISTANCE = 500
MIN_DISTANCE = 5
ROUTE_NOT_USED = 0.2
MIN_COURSES_FOR_ROUTE = 50
MAX_COURSES_FOR_ROUTE = 200
NUMBER_OF_TICKETS = 1000
ONE_KILOMETER_COST = 0.1

NUMBER_OF_ROUTES_TO_CHANGE = 20
STATION_ON_ROUTE_CHANGE_CHANCE = 0.2

T0 = datetime.date(year=2023, month=1, day=1)
T1 = datetime.date(year=2023, month=3, day=1)
T2 = datetime.date(year=2023, month=4, day=1)

MethodsOfPurchase = ["Kasa", "Konduktor", "Internet"]
ClassChoice = ["I", "II", "II", "II"]
DiscountOptions = [0, 0, 0, 0, 0, 25, 33, 33, 37, 49, 50, 51, 51, 78, 80, 93, 95, 100]

fake = Faker()

def getDistance(Distances, Station1, Station2):
    for distance in Distances:
        if (distance["Stacja1"] == Station1 and distance["Stacja2"] == Station2) or (distance["Stacja1"] == Station2 and distance["Stacja2"] == Station1):
            return distance["Dystans"]
    return None

def getStationsOnRoute(StationRoute, RouteID):
    stations = []
    for sr in StationRoute:
        if sr.ID_Trasy == RouteID:
            stations.append(sr)
    return stations

Stations = []
Distances = []
Routes = []
StationRoute = []
Courses = []
Tickets = []

with open("TwojBilet1.sql", "w", encoding="utf8") as firstSnapshot:
    firstSnapshot.write("use TwojBilet\ngo\n\n")
    PossibleStations = load_stations()

    Stations = random.sample(PossibleStations, NUMBER_OF_STATIONS)

    firstSnapshot.write("-- Table: Stacja\n")
    for station in Stations:
        firstSnapshot.write(station.write())

    with open("Distances.csv", "w", encoding="utf8") as csv:
        csv.write("Stacja1, Stacja2, Dystans\n")
        for i in range(0, NUMBER_OF_STATIONS):
            for j in range(i+1, NUMBER_OF_STATIONS):
                distance = round(random.uniform(MIN_DISTANCE, MAX_DISTANCE), 2)
                csv.write(f"{Stations[i].name}, {Stations[j].name}, {distance}\n")
                Distances.append({"Stacja1": Stations[i].name, "Stacja2": Stations[j].name, "Dystans": distance})

    for i in range(NUMBER_OF_ROUTES):
        StationsOnRoute = random.sample(Stations, random.randint(4, 10))
        distance = 0
        for j in range(1, len(StationsOnRoute)):
            distance += getDistance(Distances, StationsOnRoute[j].name, StationsOnRoute[j-1].name)
        
        predkoscOdchylenie = random.randint(-TRAIN_SPEED_FLUCTUATION, TRAIN_SPEED_FLUCTUATION)
        godziny = int(distance // (TRAIN_SPEED + predkoscOdchylenie))
        minuty = int(distance % (TRAIN_SPEED + predkoscOdchylenie) * 60 / 100)
        Routes.append(Trasa(i, round(distance, 2), f"{godziny}:{0 if minuty < 10 else ''}{minuty}"))
        for idx, station in enumerate(StationsOnRoute):
            StationRoute.append(StacjaTrasa(station.name, i, idx))

    firstSnapshot.write("-- Table: Trasa\n")
    for route in Routes:
        firstSnapshot.write(route.write())

    firstSnapshot.write("-- Table: Stacja-Trasa\n")
    for sr in StationRoute:
        firstSnapshot.write(sr.write())

    index = 1
    for route in Routes:
        if random.random() > ROUTE_NOT_USED:
            CoursesForRoute = random.randint(MIN_COURSES_FOR_ROUTE, MAX_COURSES_FOR_ROUTE)
            for i in range(CoursesForRoute):
                date = fake.date_between(start_date=T0, end_date=T1)
                godzina = random.randint(0, 23)
                minuta = random.randint(0, 59)
                Courses.append(Kurs(index, route.ID, f"{0 if godzina < 10 else ''}{godzina}:{0 if minuta < 10 else ''}{minuta}", date))
                index += 1

    firstSnapshot.write("-- Table: Kurs\n")
    for course in Courses:
        firstSnapshot.write(course.write())

    for i in range(NUMBER_OF_TICKETS):
        course = random.choice(Courses)
        stations = random.sample(getStationsOnRoute(StationRoute, course.trasa), 2)
        discount = random.choice(DiscountOptions)
        price = getDistance(Distances, stations[0].Nazwa_Stacji, stations[1].Nazwa_Stacji) * ONE_KILOMETER_COST * (100 - discount) / 100
        purchaseMethod = random.choice(MethodsOfPurchase)
        choosenClass = random.choice(ClassChoice)
        date = fake.date_between(start_date=T0, end_date=T1)
        Tickets.append(Bilet(i, course.ID, stations[0].Nazwa_Stacji, stations[1].Nazwa_Stacji, round(price, 2), purchaseMethod, date, choosenClass, discount))

        print(f"Progress: {(i/NUMBER_OF_TICKETS)*100}%", end='\r', flush=True)
    
    firstSnapshot.write("-- Table: Ticket\n")
    for ticket in Tickets:
        firstSnapshot.write(ticket.write())

with open("TwojBilet2.sql", "w", encoding="utf8") as secondSnapshot:
    secondSnapshot.write("use TwojBilet\ngo\n\n")
    secondSnapshot.write("-- Update Tables: Trasa, Stacja-Trasa\n")
    for i in range(NUMBER_OF_ROUTES_TO_CHANGE):
        routeToChange = random.choice(Routes)
        stationsOnRoute = getStationsOnRoute(StationRoute, routeToChange.ID)
        for sr in stationsOnRoute:
            if random.random() < STATION_ON_ROUTE_CHANGE_CHANCE:
                randomStation = random.choice(Stations)
                secondSnapshot.write(sr.update(randomStation.name))

        distance = 0
        for j in range(1, len(stationsOnRoute)):
            distance += getDistance(Distances, stationsOnRoute[j].Nazwa_Stacji, stationsOnRoute[j-1].Nazwa_Stacji)
        predkoscOdchylenie = random.randint(-TRAIN_SPEED_FLUCTUATION, TRAIN_SPEED_FLUCTUATION)
        godziny = int(distance // (TRAIN_SPEED + predkoscOdchylenie))
        minuty = int(distance % (TRAIN_SPEED + predkoscOdchylenie) * 60 / 100)

        routeToChange.dlugosc = round(distance, 2)
        routeToChange.czasTrwania = f"{godziny}:{0 if minuty < 10 else ''}{minuty}"
        secondSnapshot.write(routeToChange.update())
pass