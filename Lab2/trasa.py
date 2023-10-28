class Trasa:

    def __init__(self, ID, dlugosc, czasTrwania):
        self.ID = ID
        self.dlugosc = dlugosc
        self.czasTrwania = czasTrwania

    def write(self):
        return f"insert into Trasa (\"ID\", \"Dlugosc\", \"Czas_Trwania\") values ('{self.ID}', '{self.dlugosc}', '{self.czasTrwania}');\n"

    def update(self):
        return f"update Trasa set \"Dlugosc\" = '{self.dlugosc}', \"Czas_Trwania\" = '{self.czasTrwania}' where \"ID\" = '{self.ID}';\n"

class StacjaTrasa:
    def __init__(self, Nazwa_Stacji, ID_Trasy, Numer_Stacji_Na_Trasie):
        self.Nazwa_Stacji = Nazwa_Stacji
        self.ID_Trasy = ID_Trasy
        self.Numer_Stacji_Na_Trasie = Numer_Stacji_Na_Trasie
    
    def write(self):
        return f"insert into Stacja-Trasa (\"Nazwa_Stacji\", \"ID_Trasy\", \"Numer_Stacji_Na_Trasie\") values ('{self.Nazwa_Stacji}', '{self.ID_Trasy}', '{self.Numer_Stacji_Na_Trasie}');\n"

    def update(self, nowaNazwa):
        staraNazwa = self.Nazwa_Stacji
        self.Nazwa_Stacji = nowaNazwa
        return f"update Stacja-Trasa set \"Nazwa_Stacji\" = '{self.Nazwa_Stacji}' where \"Nazwa_Stacji\" = '{staraNazwa}' and \"ID_Trasy\" = '{self.ID_Trasy}';\n"
