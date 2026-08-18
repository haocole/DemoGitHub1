def factorical (number):
    if number <= 0:
        return 1
    else:
        return factorical (number) * factorical(number - 1)
    
def nCr_caculation(val_n, val_r):
    if val_r > val_n or val_n < 0:
        return 0
    elif val_n == 0 or val_r == 0:
        return 1
    return factorical (val_n) / factorical(val_r) * factorical(val_n - val_r)

while True:
    try:
        val_1 = int(input("Nhập giá trị thứ nhất: "))
        val_2 = int(input("Nhập giá trị thức hai: "))
        print(f"Tổ hợp chập {val_2} của {val_1} phần tử là: {factorical(val_1, val_2)}")
        break
    except ValueError:
        print("Giá trị phải là một số. Vui lòng thử lại!")