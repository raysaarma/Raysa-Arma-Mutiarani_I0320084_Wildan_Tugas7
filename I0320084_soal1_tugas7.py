intro = 'Perbaikan-perbaikan penulisan kalimat di bawah ini'
intro2 = intro.center(80, '*')
print(intro2)
kalimat1 = '"bapak AGUS = orangtua Dari andre, siska?" bilangnya buguru RATNA'
print(kalimat1)
def baku():
    baku1 = kalimat1.replace('=', 'adalah')
    baku2 = baku1.replace('bilangnya', 'ucap')
    baku3 = baku2.replace('orangtua', 'orang tua')
    baku4 = baku3.replace('buguru', 'ibu guru')
    baku5 = baku4.replace(',', ' dan')
    baku6 = baku5.replace('?', '.')
    print('\nStep 1(Perbaikan kalimat baku) = ', baku6)
    step1 = baku6.lower()
    kapital = step1.replace('bapak', 'Bapak')
    kapital2 = kapital.replace('agus', 'Agus')
    kapital3 = kapital2.replace('andre', 'Andre')
    kapital4 = kapital3.replace('siska', 'Siska')
    kapital5 = kapital4.replace('ibu guru', 'Ibu Guru')
    kapital6 = kapital5.replace('ratna', 'Ratna')
    print('\nStep 2(Perbaikan huruf kapital) =', kapital6)
    tanda1 = kapital.endswith('Ratna.')
    print('\nStep 3(Apakah tanda baca sudah benar?) =', tanda1)
    a = input('Coba benarkan tanda bacanya =')

baku()
