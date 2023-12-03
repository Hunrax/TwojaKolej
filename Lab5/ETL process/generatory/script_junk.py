with open("junk.sql", "w", encoding="utf8") as sqlFile:
    MethodsOfPurchase = ["Kasa", "Konduktor", "Internet"]
    ClassChoice = ["I", "II"]
    DiscountOptions = [0, 25, 33, 37, 49, 50, 51, 78, 80, 93, 95, 100]
    for method in MethodsOfPurchase:
        for discount in DiscountOptions:
            for choice in ClassChoice:
                    sqlFile.write(f"insert into Junk (\"Klasa\", \"Ulga\", \"Sposob_Zakupu\") values ('{choice}', '{discount}%', '{method}');\n")