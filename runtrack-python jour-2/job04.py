nombre = int(input("peux tu me donner un nombre ? "))
for table in range (1, nombre+1):
        print("----Table de", table, "---")
        for i in range(1,11):
            print(i, "*", table, "=", i * table)
        print()
            




