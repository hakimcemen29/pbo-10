from abc import ABC,abstractclassmethod
import math

class BangunDatar(ABC):
    @abstractclassmethod
    def hitung_luas(self):
        pass
class Persegi(BangunDatar):
    def __init__(self,sisi):
        self.sisi = sisi
    def hitung_luas(self):
        return self.sisi * self.sisi
class Segitiga(BangunDatar):
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi
class Lingkaran(BangunDatar):
    def __init__(self,r):
        self.r = r
    def hitung_luas(self):
        return math.pi * self.r**2
class PersegiPanjang(BangunDatar):
    def __init__(self,p,l):
        self.p = p
        self.l = l
    def hitung_luas(self):
        return self.p * self.l
class JajarGenjang(BangunDatar):
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
    def hitung_luas(self):
        return self.alas * self.tinggi