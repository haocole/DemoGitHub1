def chia(a,b):
    if b == 0:
        return "Lỗi không chia cho 0!"
    return a/b
try:
    a = float(input("Nhâp số bị chia: "))
    b = float(input("Nhâp số chia: "))

    ket_qua = chia(a,b)
    print("ket qua: ",ket_qua)
except ValueError:
    print("Lôi!: vui lòng chỉ nhập số ")
