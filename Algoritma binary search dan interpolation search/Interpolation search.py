#Nama	: Mahmuddin Mursalim
#Nim	: D0425509
#Kelas	: B Sistem Informasi

#Interpolation Search adalah algoritma pencarian pada data terurut yang bekerja dengan memperkirakan posisi nilai yang dicari menggunakan rumus perbandingan nilai (mirip metode interpolasi pada matematika).

def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        pos = low + ((x - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

data2 = [100, 200, 300, 400, 500]
print("Interpolation Search (cari 400):", interpolation_search(data2, 400))