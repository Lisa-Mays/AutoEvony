import multiprocessing as mp

# Tạo mảng với kích thước 3 kiểu integer
arr = mp.Array('i', [1, 2, 3])

# Khóa mảng trước khi truy cập
with arr.get_lock():
    # Thay đổi giá trị của phần tử tại vị trí index 1 thành 42
    arr[1] = 42

# Khi ra khỏi khối với "with", mảng đã được mở khóa tự động

# In giá trị của mảng sau khi đã thay đổi
print(arr[:])
