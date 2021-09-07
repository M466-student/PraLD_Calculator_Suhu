#Tugas Cycom 0001

#converter suhu fahrenheit

print ('selamat datang di converter fahrenheit')
print('pilih jenis suhu yang ingin diubah ke dalam fahrenheit ')
print('1.celcius')
print('2.reamur')
print('3.kelvin')



while True:
    # Take input from the user
    choice = input("Masukan pilihan (1/2/3):")

    if choice == '1':
        Celc = float(input('tentukan angka celcius :'))
        CtoFahr = (9/5 * Celc) + 32
        print(CtoFahr, 'fahrenheit')

    if choice == '2':
        Ream = float(input('tentukan angka reamur : '))
        ReamToFahr = (9/4 * Ream) + 32
        print(ReamToFahr, 'fahrenheit')

    if choice  == '3':
        Kelv = float(input('tentukan angka kelvin : '))
        KelvToFahr = float(Kelv - 273.15) * 9/5 + 32
        print(KelvToFahr, 'fahrenheit')



    else:
        break










