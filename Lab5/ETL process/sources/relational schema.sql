 -- drop database DataWarehouse

create database DataWarehouse collate Latin1_General_CI_AS;
go

use DataWarehouse
go

create table Trasa(
    ID_Trasy int identity(1, 1) primary key,
    Nazwa varchar(70) unique not null,
    Dlugosc varchar(12) check (Dlugosc in('0-50', '50-100', '100-200', '200-500', 'powyzej 500')) not null,
    Czas_Trwania varchar(12) check (Czas_Trwania in('0-1h', '1-3h', '3-5h', '5-10h', 'powyzej 10h')) not null
)

create table Stacja(
    ID_Stacji int identity(1, 1) primary key,
    Nazwa varchar(30) not null,
    Miejscowosc varchar(30) not null
)

create table Data(
    ID_Daty int identity(1, 1) primary key,
    Dzien char(2) check (Dzien like '[0-3][0-9]') not null,
    Miesiac varchar(11) check (Miesiac in('Styczen', 'Luty', 'Marzec', 'Kwiecien', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpien', 'Wrzesien', 'Pazdziernik', 'Listopad', 'Grudzien')) not null,
    Miesiac_No int not null, 
	Rok char(4) check (Rok like '[0-9][0-9][0-9][0-9]') not null,
    Dzien_Tygodnia varchar(12) check (Dzien_Tygodnia in('Poniedzialek', 'Wtorek', 'Sroda', 'Czwartek', 'Piatek', 'Sobota', 'Niedziela')) not null,
    Dzien_Pracy varchar(11) check (Dzien_Pracy in('Dzien pracy', 'Dzien wolny')) not null,
    Wakacje varchar(11) check (Wakacje in('Wakacje', 'Ferie', 'Rok szkolny')) not null,
    Swieta varchar(50) check (Swieta in('Boze Narodzenie', 'Wielkanoc', 'Wszystkich Swietych', 'Nowy Rok', 'Brak swiat')) not null,
    Okolice_Swiat varchar(60) check (Okolice_Swiat in('Okolice Bozego Narodzenia', 'Okolice Wielkanocy', 'Okolice Wszystkich Swietych', 'Okolice Nowego Roku', 'Brak swiat')) not null 
)

create table Czas(
    ID_Czasu int identity(1, 1) primary key,
    Godzina char(2) check (Godzina like '[0-2][0-9]') not null,
    Minuta char(2) check (Minuta like '[0-5][0-9]') not null,
    Godziny_Szczytu varchar(21) check (Godziny_Szczytu in('Godziny szczytu', 'Godziny poza szczytem')) not null
)

create table Junk(
    ID_Junk int identity(1, 1) primary key,
    Klasa varchar(2) check (Klasa in('I', 'II')) not null, 
    Ulga varchar(4) check (Ulga in('0%', '25%', '33%', '37%', '49%', '50%', '51%', '78%', '80%', '93%', '95%', '100%')) not null,
    Sposob_Zakupu varchar(9) check (Sposob_Zakupu in('Kasa', 'Konduktor', 'Internet')) not null
)

create table Kurs(
    ID_Kursu int identity(1, 1) primary key,
    ID_Trasy int foreign key references Trasa,
    ID_Daty int foreign key references Data,
    ID_Czasu int foreign key references Czas
)


create table Przewoz_Pasazera(
    Numer_biletu int unique,
    ID_Kursu int foreign key references Kurs,
    ID_Stacja_Poczatkowa int foreign key references Stacja,
    ID_Stacja_Koncowa int foreign key references Stacja,
    ID_Daty int foreign key references Data,
    Cena money not null,
    Dystans decimal not null,
    ID_Junk int foreign key references Junk
)