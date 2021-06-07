# program lulus tidak lulus pake int
nilai_teori = int(input("Masukkan nilai ujian teori anda: "))
nilai_praktek = int(input("Masukkan nilai ujian praktek anda: "))

#percabangan if else
if nilai_teori >= 70 and nilai_praktek >= 70:
    print("Selamat, anda lulus!")
elif nilai_teori >= 70 and nilai_praktek < 70:
    print("anda harus mengulang ujian praktek.")
elif nilai_teori < 70 and nilai_praktek >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")
