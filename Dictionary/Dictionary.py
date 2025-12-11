#Nama	: Mahmuddin Mursalim
#Nim	: D0425509
#Kelas	: B Sistem Informasi

#Dictionary adalah kumpulan data yang diakses berdasarkan kunci, bukan berdasarkan indeks seperti array atau list.

mahasiswa = {
    "nama": "Mahmuddin Mursalim",
    "nim": "D0425509",
    "prodi": "Sistem Informasi",
    "kelas": " B ",
    "angkatan": 2025,
    "alamat": "Pambusuang, Balanipa",

    "nilai": {
        "algoritma_pemrograman": 98,
        "struktur_data": 78,
        "basis_data": 80,
        "pemrograman_python": 90
    },

    "mata_kuliah_diambil": [
        "Algoritma Pemrograman",
        "Basis Data",
        "Pemrograman Python",
        "Kalkulus Informatika"
    ]
}

# Menampilkan seluruh data
print("\nData Mahasiswa:", mahasiswa)

# Mengakses data
print("Nama         :", mahasiswa["nama"])
print("Kelas        :", mahasiswa["kelas"])
print("Nilai Python :", mahasiswa["nilai"]["pemrograman_python"])

# Update nilai
mahasiswa["nilai"]["pemrograman_python"] = 98
print("Nilai Python Setelah Update:", mahasiswa["nilai"]["pemrograman_python"])