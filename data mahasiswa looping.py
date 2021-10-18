nim=[]
nilai_uts=[]
nilai_uas=[]
total=[]
looping= int(input("Masukkan berapa nilai perulangan : "))
#Process
for i in range(looping):
    print("Data Ke - ", i+1)
    nim.append(input("Masukkan nim anda: "))
    nilai_uts.append (int(input("Masukkan nilai uts anda: ")))
    nilai_uas.append(int(input("Masukkan nilai uas anda : ")))
for i in range(looping):
    total.append(nilai_uts[i]+nilai_uas[i]/2)
#Outtput
print("===========================================================")
print("NIM      NILAI UTS       NILAI UAS       TOTAL")
print("===========================================================")
for i in range(looping):
    print("%s \t %i \t\t %i \t\t\t %i"%(nim[i],nilai_uts[i],nilai_uas[i],total[i]))
print("===========================================================")