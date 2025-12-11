#Nama	: Mahmuddin Mursalim
#Nim	: D0425509
#Kelas	: B Sistem Informasi

#Bubble Sort adalah algoritma pengurutan yang bekerja dengan membandingkan elemen yang berdekatan dan menukarnya jika urutannya salah.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Bubble Sort:", bubble_sort([5, 1, 4, 2]))