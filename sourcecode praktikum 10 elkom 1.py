# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 04:39:29 2021

@author: Hp
"""
print("@@@@  @@@  @@@@  @@@  @   @")
print("@     @ @  @  @  @ @  @   @")
print("@@@@  @@@  @@@@  @@@  @@@@@")
print("   @  @ @  @@    @ @  @   @")
print("   @  @ @  @ @   @ @  @   @")
print("@@@@  @ @  @  @  @ @  @   @")

mahasiswa=[]
def keterangan_masuk():
   nama  = input("Masukkan Nama Mahasiswa: ")
   mark1=int(input("Masukkan Nilai Praktikum 1: "))
   mark2=int(input("Masukkan Nilai Praktikum 2: "))
   mark3=int(input("Masukkan Nilai Praktikum 3: "))
   list=[nama,mark1,mark2,mark3]
   mahasiswa.insert(len(mahasiswa),list)
   main()
def keterangan():
    print(" NAMA |","PRAKTIKUM 1|","PRAKTIKUM 2|","PRAKTIKUM 3|")
    for i in mahasiswa:
        print(i[0],"     ",i[1],"     ",i[2],"     ",i[3])
    main()
def studentgrades():
    for i in range(len(mahasiswa)):
        total=0
        for j in range (1,len(mahasiswa[i])):
            total+=mahasiswa[i][j]
        print(mahasiswa[i][0],"=",total/len(mahasiswa[i]))
    main()
def practicalvalue():
    prak1=0
    prak2=0
    prak3=0
    for i in range(len(mahasiswa)):
        prak1+=mahasiswa[i][1]
        prak2+=mahasiswa[i][2]
        prak3+=mahasiswa[i][3]
    prak1=prak1/len(mahasiswa)
    prak2=prak2/len(mahasiswa)
    prak3=prak3/len(mahasiswa)
    print("Nilai rata-rata 1= ",prak1)
    print("Nilai rata-rata 2= ",prak2)
    print("nilai rata-rata 3= ",prak3)
    main()
def averagevalue():
    nilaimahasiswa=[]
    total=0
    for i in range(len(mahasiswa)):
        total=0
        for x in range (1,len(mahasiswa[i])):
            total+=mahasiswa[i][x]
        nilaimahasiswa.insert(len(nilaimahasiswa),total/5)
    total=0
    for i in nilaimahasiswa:
        total+=i
    total=total/len(nilaimahasiswa)
    print(total)
    main()
def perbarui_mark():
    perbarui=input("Nama Yang Dicari :")
    mark=int(input("Ingin perbarui nilai Praktikum ke-: "))
    mark_new=int(input("Nilai Baru: "))
    for i in mahasiswa:
        if i [0]==perbarui:
            i[mark]=mark_new
    main()
def main():
    print("PROGRAM LIST")
    print("1.masukkan nilai")
    print("2.view data")
    print("3.hitung Nilai rata-rata praktikum tiap mahasiswa")
    print("4.Nilai rata-rata setiap praktikum mahasiswa")
    print("5.Mencari nilai rata-rata praktikum dari setiap mahasiswa")
    print("6.update nilai mahasiswa")
    print("7.exit")
    choose=int(input("Silahkan pilih menu yang tersedia:"))
    if choose==1:
        keterangan_masuk()
    elif choose==2:
        keterangan()
    elif choose==3:
        studentgrades()
    elif choose==4:
        practicalvalue()
    elif choose==5:
        averagevalue()
    elif choose==6:
        perbarui_mark()
    elif choose==7:
        exit()
    else:
        print("the keyword you entered is wrong!")
        choose=int(input("Silahkan pilih menu yang tersedia:"))
main()