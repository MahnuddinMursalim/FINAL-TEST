#Nama	: Mahmuddin Mursalim
#Nim	: D0425509
#Kelas	: B Sistem Informasi

#Selection Sort adalah algoritma pengurutan yang bekerja dengan mencari elemen terkecil dari sisa array lalu menukarnya dengan elemen di posisi awal yang belum terurut

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("Selection Sort:", selection_sort([500, 100, 400, 200]))