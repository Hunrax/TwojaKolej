class Stacja:

    def __init__(self, name, town):
        self.name = name
        self.town = town

    def write(self):
        return f"insert into Stacja (\"Nazwa\", \"Miejscowosc\") values ('{self.name}', '{self.town}');\n"

def load_stations():
    stations_data = []
    with open("stacje.txt",'r', encoding="utf8") as data_file:
        for line in data_file:
            data = line.split()
            data_line = []
            for word in data:
                if (word[0].isupper() and word != "TAK" and word != "NIE"):
                    data_line.append(word)
            if data_line:
                stations_data.append(data_line)

    Stations = []
    for station in stations_data:
        if len(station) == 2:
            station_name = station[0]
            station_town = station[1]
        elif len(station) == 3:
            station_name = station[0] + " " + station[1]
            station_town = station[2]       
        elif len(station) == 4:
            station_name = station[0] + " " + station[1]
            station_town = station[2] + " " + station[3]   
        elif len(station) == 5:
            station_name = station[0] + " " + station[1] + " "  + station[2]
            station_town = station[3] + " " + station[4]       
        elif len(station) == 6:
            station_name = station[0] + " " + station[1] + " "  + station[2]
            station_town = station[3] + " " + station[4] + " "  + station[5]
        new_station = Stacja(station_name, station_town)
        Stations.append(new_station)
    return Stations