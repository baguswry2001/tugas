def dua_dimensi():
    def menu():
        print("+==================================+")
        print("|       BAGUN 2 DIMENSI           |")
        print("|================================ |")
        print("|1. menghitung luas segitiga      |")
        print("|2. menghitung luas jajar genjang |")
        print("|3. menghitung luas lingkaran     |")
        print("+=================================+")
    def menghitung_luas_segitiga():
        def hitung_luas(alas, tinggi):
            return 0.5 * alas * tinggi
        def hitung_keliling(sisi1, sisi2, sisi3):
            return sisi1 + sisi2 + sisi3
        alas = float(input("Masukkan alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        sisi1 = float(input("Masukkan panjang sisi pertama: "))
        sisi2 = float(input("Masukkan panjang sisi kedua: "))
        sisi3 = float(input("Masukkan panjang sisi ketiga: "))
        luas = hitung_luas(alas, tinggi)
        keliling = hitung_keliling(sisi1, sisi2, sisi3)
        print(f"Luas segitiga: {luas}")
        print(f"Keliling segitiga: {keliling}")
    def menghitung_jajar_genjang():
        def hitung_luas(alas, tinggi):
            return alas * tinggi
        def hitung_keliling(alas, sisi_miring):
            return 2 * (alas + sisi_miring)
        alas = float(input("Masukkan panjang alas jajar genjang: "))
        tinggi = float(input("Masukkan tinggi jajar genjang: "))
        sisi_miring = float(input("Masukkan panjang sisi miring jajar genjang: "))
        luas = hitung_luas(alas, tinggi)
        keliling = hitung_keliling(alas, sisi_miring)
        print(f"Luas jajar genjang: {luas}")
        print(f"Keliling jajar genjang: {keliling}")
    def menghitung_lingkaran():
        def hitung_luas_lingkaran(jari_jari):
            pi = 3.14
            return pi * jari_jari ** 2
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = hitung_luas_lingkaran(jari_jari)
        print(f"Luas lingkaran: {luas}")
    def main():
        menu()
        a = input("Masukan pilihan =>")
        if a == "1":
            menghitung_luas_segitiga()
        elif a== "2":
            menghitung_jajar_genjang()
        elif a == "3":
            menghitung_lingkaran()
    main()
def bagun_3_dimensi():
    def menu():
        print("+==================================+")
        print("|       BAGUN 3 DIMENSI           |")
        print("|================================ |")
        print("|1. menghitung volume kubus       |")
        print("|2. menghitung volume balok       |")
        print("|3. menghitung volume bola        |")
        print("+=================================+")
    def kubus():
        def hitung_volume_kubus(sisi):
            return sisi ** 3
        def hitung_luas_permukaan_kubus(sisi):
            return 6 * (sisi ** 2)
        sisi = float(input("Masukkan panjang sisi kubus: "))
        volume = hitung_volume_kubus(sisi)
        luas_permukaan = hitung_luas_permukaan_kubus(sisi)
        print(f"Volume kubus: {volume}")
        print(f"Luas permukaan kubus: {luas_permukaan}")
    def volume_balok():
        def hitung_volume_balok(panjang, lebar, tinggi):
            return panjang * lebar * tinggi
        def hitung_luas_permukaan_balok(panjang, lebar, tinggi):
            return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        volume = hitung_volume_balok(panjang, lebar, tinggi)
        luas_permukaan = hitung_luas_permukaan_balok(panjang, lebar, tinggi)
        print(f"Volume balok: {volume}")
        print(f"Luas permukaan balok: {luas_permukaan}")
    def bola():
        def hitung_volume_bola(jari_jari):
            pi = 3.14
            return (4 / 3) * pi * (jari_jari ** 3)
        def hitung_luas_permukaan_bola(jari_jari):
            pi = 3.14
            return 4 * pi * (jari_jari ** 2)
        jari_jari = float(input("Masukkan jari-jari bola: "))
        volume = hitung_volume_bola(jari_jari)
        luas_permukaan = hitung_luas_permukaan_bola(jari_jari)
        print(f"Volume bola: {volume}")
        print(f"Luas permukaan bola: {luas_permukaan}")
    menu()
    a = input("Masukan pilihan =>")
    if a == "1":
        kubus()
    elif a =="2":
        volume_balok()
    elif a == "3":
        bola()
def utama():
        print("+==================================+")
        print("|       menu pilihan              |")
        print("|================================ |")
        print("|1. rumus 2 dimensi               |")
        print("|2. rumus 3 dimensi               |")
        print("+=================================+")
        nilai = input("Masukan pilihan =>")
        if nilai == "1":
            dua_dimensi()
        elif nilai == '2':
            bagun_3_dimensi()
        else:
            print("Pilihan Tidak Valid")
            utama()
if __name__=="__main__":
    utama()