nama = input('Masukkan nama Anda: ')
nilai = int(input('Masukkan nilai Anda: '))

if nilai < 60:
    konversi = 'E'
elif nilai <= 64:
    konversi = 'C'
elif nilai <= 69:
    konversi = 'C+'
elif nilai <= 74:
    konversi = 'B'
elif nilai <= 79:
    konversi = 'B+'
elif nilai <= 84:
    konversi = 'A-'
elif nilai <= 100:
    konversi = 'A'

print('Halo,', nama + '! nilai anda setelah dikonversi adalah', konversi)