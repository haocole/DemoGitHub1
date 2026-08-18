def sqrt_caculation(number):
    return number ** 0.5

while True:
    try:
        val_input = float(input("Nhập giá trị: "))
        if val_input < 0:
            print ("Không thể căn bậc hai của một số âm!")
            continue
        else:
            print(f"Căn bậc hai của {val_input} là {sqrt_caculation(val_input)}")
            break
    except ValueError:
        print("Giá trị nhập vào phải là một số!")