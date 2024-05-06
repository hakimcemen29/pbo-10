from modul10 import Persegi,PersegiPanjang,Lingkaran,JajarGenjang,Segitiga
print("==========================")
print("Muhammad Hakim")
print("064002300027")
print("==========================")
persegi = Persegi(5)
print(f"luas persegi : {persegi.hitung_luas()}")

persegiPanjang = PersegiPanjang(5,10)
print(f"luas persegi panjang : {persegiPanjang.hitung_luas()}")

lingkaran = Lingkaran(7)
print(f"luas lingkaran : {lingkaran.hitung_luas()}")

jargen = JajarGenjang(10,15)
print(f"luas jajar genjang : {jargen.hitung_luas()}")

segitiga = Segitiga(5,10)
print(f"luas segitiga : {segitiga.hitung_luas()}")