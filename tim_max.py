def tim_so_lon_nhat(danh_sach):
    if not danh_sach:
        return None
    return max(danh_sach)

if __name__ == "__main__":
    numbers = [5, 12, 9, 24, 3]
    print(f"Danh sach: {numbers}")
    print(f"So lon nhat la: {tim_so_lon_nhat(numbers)}")