def ubah():
	huruf_asli =    'abcdefghijklmnopqrstuvwxyz'
	ngindek_satu = huruf_asli.index(soal_satu)
	ngindek_dua = int(soal_dua)-1
	selisih = ngindek_satu - ngindek_dua
	huruf_kedua=huruf_asli[selisih:]+huruf_asli[:selisih]
	hasil = kata.maketrans(huruf_kedua, huruf_asli)
	return kata.translate(hasil)
	
soal_satu, soal_dua = input('masukkan soal(contoh k=2 jadi, k 2): ').split()
print('SOAL SAAT INI:\n', soal_satu, '=', soal_dua)
while True:
	try:
		kata = input('masukkan kata: ')
		print(ubah())
	except KeyboardInterrupt:
		print('\nBYE.. :)')
		break