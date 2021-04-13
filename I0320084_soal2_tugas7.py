sepatu = float(input('Masukkan harga sepatu awal :'))
sandal = float(input('Masukkan harga sandal awal :'))
flatshoes = float(input('Masukkan harga sepatu awal :'))
diskon = int(input('Masukkan diskon(tanpa persen, ct: 20) : '))
import math
sepatu1 = math.ceil(sepatu * ((100-diskon)/100))
sandal1 = math.ceil(sandal * ((100 - diskon) / 100))
flatshoes1 = math.ceil(flatshoes * ((100 - diskon) / 100))
tanya1 = str(input('Apakah anda ingin mengetahui harga setelah diskon utk semua proiduk?(Y/T)'))
if tanya1 == 'Y':
    print('Harga sepatu setelah diskon = ', sepatu1)
    print('Harga sandal setelah diskon = ', sandal1)
    print('Harga flatshoes setelah diskon = ', flatshoes1)
else :
    tanya2 = str(input('Harga terendah/tertingi? '))
    if tanya2 == 'tertinggi' :
        print('Harga tertinggi =', max(sepatu1, sandal1, flatshoes1))
    else :
        print('Harga terendah =', min(sepatu1, sandal1, flatshoes1))

tanya3 = str(input('Utk produk random pilihan dari kami, harga hanya 100000, apakah anda ingin?(Y/T)'))
if tanya3 == 'Y':
    import random
    a = ["sepatu", "sandal", "flatshoes"]
    print('Selamat anda mendapatkan', random.choice(a), 'hanya dengan membayar 100000')

