def chia(a,b):
    if b == 0:
        return "Lỗi"
    return a/b
try:
    a = float(input("Nhâp số bị chia: "))
    b = float(input("Nhâp số chia: "))

    ket_qua = chia(a,b)
    print("ket qua: ",ket_qua)
except ValueError:
    print("Lôi!: vui lòng chỉ nhập số ")
