use DataWarehouse
go

INSERT INTO Stacja VALUES('Gdansk Glowyny', 'Gdansk')
INSERT INTO Stacja VALUES('Warszawa Centralna', 'Warszawa')
INSERT INTO Stacja VALUES('Przywidz', 'Przywidz')
INSERT INTO Stacja VALUES('Tczew', 'Tczew')
INSERT INTO Stacja VALUES('Wejherowo', 'Wejherowo')

INSERT INTO Trasa VALUES('Gdansk Glowny-Przywidz', '0-50', '0-1h')
INSERT INTO Trasa VALUES('Warszawa Centralna-Przywidz', '200-500', '3-5h')
INSERT INTO Trasa VALUES('Wejherowo-Przywidz', '50-100', '1-3h')

INSERT INTO Data VALUES('10', 'Lipiec', '2020', 'Sroda', 'Dzien pracy', 'Wakacje', 'Brak swiat', 'Brak swiat')
INSERT INTO Data VALUES('20', 'Styczen', '2023', 'Sobota', 'Dzien wolny', 'Ferie', 'Brak swiat', 'Brak swiat')
INSERT INTO Data VALUES('25', 'Grudzien', '2021', 'Wtorek', 'Dzien wolny', 'Rok szkolny', 'Boze Narodzenie', 'Okolice Bozego Narodzenia')

INSERT INTO Czas VALUES('21', '37', 'Godziny poza szczytem')
INSERT INTO Czas VALUES('16', '20', 'Godziny szczytu')
INSERT INTO Czas VALUES('06', '06', 'Godziny poza szczytem')
INSERT INTO Czas VALUES('07', '40', 'Godziny szczytu')

INSERT INTO Junk VALUES('I', '0%', 'Internet')
INSERT INTO Junk VALUES('II', '51%', 'Kasa')
INSERT INTO Junk VALUES('II', '25%', 'Konduktor')
INSERT INTO Junk VALUES('I', '100%', 'Konduktor')

INSERT INTO Kurs VALUES(1, 1, 1)
INSERT INTO Kurs VALUES(1, 2, 3)
INSERT INTO Kurs VALUES(3, 1, 1)
INSERT INTO Kurs VALUES(3, 3, 3)
INSERT INTO Kurs VALUES(2, 2, 2)
INSERT INTO Kurs VALUES(2, 1, 2)
INSERT INTO Kurs VALUES(3, 2, 1)

INSERT INTO Przewoz_Pasazera VALUES(1, 1, 1, 1, 22.33, 789.1, 1)
INSERT INTO Przewoz_Pasazera VALUES(2, 2, 2, 2, 2.32, 12.2, 2)
INSERT INTO Przewoz_Pasazera VALUES(3, 3, 3, 3, 212.45, 33.3, 3)
INSERT INTO Przewoz_Pasazera VALUES(4, 4, 4, 3, 56.89, 54.4, 4)
INSERT INTO Przewoz_Pasazera VALUES(5, 5, 5, 2, 67.12, 73.5, 1)
INSERT INTO Przewoz_Pasazera VALUES(6, 2, 3, 1, 1.33, 222.6, 2)
INSERT INTO Przewoz_Pasazera VALUES(7, 2, 4, 1, 2.56, 457.7, 3)
INSERT INTO Przewoz_Pasazera VALUES(1, 5, 3, 2, 213.99, 11.8, 4)