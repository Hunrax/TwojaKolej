create database TwojBilet collate Latin1_General_CI_AS;
go

use TwojBilet
go

create table Stacja(
    Nazwa varchar(30) primary key,
    Miejscowosc varchar(30) not null
)
go

create table Trasa(
    ID integer primary key,
    Dlugosc decimal not null,
    Czas_Trwania varchar(5) not null
)
go

create table Stacja_Trasa(
    Nazwa_Stacji varchar(30) foreign key references Stacja,
    ID_Trasy integer foreign key references Trasa,
    Numer_Stacji_Na_Trasie integer not null,
    primary key ("Nazwa_Stacji", "ID_Trasy")
)
go

create table Kurs(
    ID integer primary key,
    Trasa integer foreign key references Trasa,
    Godzina_Wyruszenia time not null,
    Data_Wyruszenia date not null
)
go

create table Bilet(
    ID integer primary key,
    Kurs integer foreign key references Kurs,
    Od varchar(30) foreign key references Stacja,
    Do varchar(30) foreign key references Stacja,
    Cena decimal(5, 2) not null,
    Sposob_Zakupu varchar (9) check (Sposob_Zakupu in('Kasa', 'Konduktor', 'Internet')) not null,
    Data_Zakupu date not null,
    Klasa varchar (2) check (Klasa in('I', 'II')) not null,
    Ulga integer check (Ulga >= 0 and Ulga <= 100) not null
)
go