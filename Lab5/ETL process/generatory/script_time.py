with open("time.sql", "w", encoding="utf8") as sqlFile:
    szczyt = "Godziny szczytu"
    nie = "Godziny poza szczytem"
    for i in range(24):
        for j in range(60):
            sqlFile.write(f"insert into Czas (\"Godzina\", \"Minuta\", \"Godziny_Szczytu\") values ('{0 if i < 10 else ''}{i}', '{0 if j < 10 else ''}{j}', '{szczyt if (i >= 7 and i < 9) or (i >= 15 and i < 17) else nie}');\n")