#Tugas Cycom 0001

#converter suhu fahrenheit

print ('selamat datang di converter fahrenheit')
print('pilih jenis suhu yang ingin diubah ke dalam fahrenheit ')
print('1.celcius')
print('2.reamur')
print('3.kelvin')



while True:
    # Take input from the user
    choice = input("Masukan pilihan (1/2/3):")   # input user dari pilihan di atas 

    if choice == '1': # if user pick number 1. the program will start here
        Celc = float(input('tentukan angka celcius :'))
        CtoFahr = (9/5 * Celc) + 32  # rumus konversi suhu 
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
        break # break mean end so after u input the numbers and got number output the script will end 


        
        #notes for cycom members
        #kalo mau copas silahkan tapi ganti variable nya jadi  suhu lain dulu 
        








