# Đọc sô n (n < 1000) được nhập vào thành chữ, sử dụng if-else

def read(a):
    list = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    return list[a]

n = int(input("Nhập n: ")) #ép sang int vì mặc định input nhập vào sẽ thành string
if(n < 10):
    print(read(n))
elif(n < 100):
    hang_chuc = n // 10
    hang_dv = n % 10
    if(hang_chuc == 1):
        if(hang_dv == 0):
            print("mười")
        else:
            print("mười " + read(hang_dv))
    else:
        if(hang_dv == 0):
            print(read(hang_chuc) + " mươi")
        elif(hang_dv == 1):
            print(read(hang_chuc) + " mốt")
        else:
            print(read(hang_chuc) + " " + read(hang_dv))
else:
    hang_tram = n // 100
    hang_chuc = (n // 10) % 10
    hang_dv = n % 10
    if(hang_chuc == 0):
        if(hang_dv == 0):
            print(read(hang_tram) + " trăm")
        else:
            print(read(hang_tram) + " trăm linh " + read(hang_dv))
    elif(hang_chuc == 1):
        if(hang_dv == 0):
            print("mười")
        else:
            print(read(hang_tram) + " trăm mười " + read(hang_dv))
    else:
        if(hang_dv == 0):
            print(read(hang_tram) + " trăm " + read(hang_chuc) + " mươi")
        elif(hang_dv == 1):
            print(read(hang_tram) + " trăm " + read(hang_chuc) + " mốt")
        else:
            print(read(hang_tram) + " trăm " + read(hang_chuc) + " " + read(hang_dv))




