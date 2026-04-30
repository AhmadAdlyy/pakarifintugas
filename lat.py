class AkunBank:
 def __init__(self, saldo):
    self.__saldo = saldo # Private attribute
 def cek_saldo(self):
     return self.__saldo
 def setor(self, jumlah):
     if jumlah > 0:
         self.__saldo += jumlah
# Contoh penggunaan kelas AkunBank
def ambil_saldo(self, jumlah):
       if 0 < jumlah <= self.__saldo:
           self.__saldo -= jumlah
           return jumlah
       else:
           print("Saldo tidak mencukupi.")
rekening = AkunBank(1000)
rekening.setor(500)
rekening.ambil_saldo(200)
print(rekening.cek_saldo()) # Output: 1300
# print(rekening.__saldo) # Ini akan Error! Tidak bisa akses langsung.