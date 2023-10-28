class Bilet:

    def __init__(self, ID, kurs, od, do, cena, sposob_zakupu, data, klasa, ulga):
        self.ID = ID
        self.kurs = kurs
        self.od = od
        self.do = do
        self.cena = cena
        self.sposob_zakupu = sposob_zakupu
        self.data = data
        self.klasa = klasa
        self.ulga = ulga

    def write(self):
        return f"insert into Bilet (\"ID\", \"Kurs\", \"Od\", \"Do\", \"Cena\", \"Sposob_Zakupu\", \"Data_Zakupu\", \"Klasa\", \"Ulga\") values ('{self.ID}', '{self.kurs}', '{self.od}', '{self.do}', '{self.cena}', '{self.sposob_zakupu}', '{self.data}', '{self.klasa}', '{self.ulga}');\n"