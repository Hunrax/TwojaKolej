class Kurs:

    def __init__(self, ID, trasa, godzina , data):
        self.ID = ID
        self.trasa = trasa
        self.godzina = godzina
        self.data = data

    def write(self):
        return f"insert into Kurs (\"ID\", \"Trasa\", \"Godzina_Wyruszenia\", \"Data_Wyruszenia\") values ('{self.ID}', '{self.trasa}', '{self.godzina}', '{self.data}');\n"