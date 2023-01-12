# script per calcolare l'area di un cerchio avendo solo il raggio

import math # libreria che ci permette di utilizzare il pigreco in python

while True: #uso while per ripetere lo script finche l'utente non decida di dire qualcosa  diversa da si

    print("------- Area del cerchio -------")

    raggio_c = float(input("Inserisci il raggio del cerchio : "))  # do la possibilità all'utente di scegliere il raggio

    area_c = raggio_c * raggio_c * math.pi

    print("Area del cerchio = ", area_c)

    continua = input("Vuoi continuare? (si/no) : ") # chiedo all'utente se vuole continuare
    if continua != "si":  # se la risposta è diversa da si essendo un ciclo while il programma smette di funzionare
        break
    else: #altrimenti si ripete tutto da capo
        print("\n")

