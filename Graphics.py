import matplotlib.pyplot as plt


def showGraph():
    infile = open("times.txt")
    date = infile.readline().strip().split()
    problemaRegineBGK = []
    for x in date:
        problemaRegineBGK.append(float(x))

    date = infile.readline().strip().split()
    problemaRegineALP = []
    for x in date:
        problemaRegineALP.append(float(x))

    date = infile.readline().strip().split()
    problemaRegineCS = []
    for x in date:
        problemaRegineCS.append(float(x))

    date = infile.readline().strip().split()
    problemaRegineAG = []
    for x in date:
        problemaRegineAG.append(float(x))

    date = infile.readline().strip().split()
    marime_tabla_sah = []
    for x in date:
        marime_tabla_sah.append(int(x))

    inp = input("Doriti sa adaugati datele pentru problema reginelor folosing backtracking in grafic? YES / NO - ")
    if inp == "YES":
        plt.plot(marime_tabla_sah, problemaRegineBGK, label="Algo regine BGK")
    inp = input("Doriti sa adaugati datele pentru problema reginelor folosing hill climbing in grafic? YES / NO - ")
    if inp == "YES":
        plt.plot(marime_tabla_sah, problemaRegineALP, label="Algo regine HillClimb")
    inp = input("Doriti sa adaugati datele pentru problema reginelor folosing calirea simulata in grafic? YES / NO - ")
    if inp == "YES":
        plt.plot(marime_tabla_sah, problemaRegineAG, label="Algo regine CS")
    inp = input("Doriti sa adaugati datele pentru problema reginelor folosing algoritmul genetic in grafic? YES / NO - ")
    if inp == "YES":
        plt.plot(marime_tabla_sah, marime_tabla_sah, label="Algo regine Genetic")

    plt.xlabel("Marime tabla de sah")
    plt.ylabel("Timp(s)")
    plt.xticks(marime_tabla_sah)
    plt.grid()
    plt.legend()
    plt.show()




