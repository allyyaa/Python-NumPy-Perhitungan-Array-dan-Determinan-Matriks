import numpy as np

# 1. Jumlahkan 2 array
array_a = np.array([2, 4, 1]) + np.array([4, 8, 7])

# 2. Kalikan 2 array
array_b = np.array([2, 4, 3]) * np.array([3, 2, 3])

# 3. Kurangi 2 array
array_c = np.array([2, 4, 3]) - np.array([1, 2, 1])

# 4. Masukkan array_a, array_b, array_c ke dalam sebuah matriks
matriks = np.array([array_a, array_b, array_c])

# Mencari determinan
determinant = np.linalg.det(matriks)

# Mencari invers
try:
    inverse = np.linalg.inv(matriks)
except np.linalg.LinAlgError:
    inverse = None  # Jika matriks tidak dapat diinvers

# Menampilkan hasil 
print("Hasil Perhitungan:")
print("=" * 30)
print(f"Array A (Penjumlahan): {array_a}")
print(f"Array B (Perkalian):   {array_b}")
print(f"Array C (Pengurangan):  {array_c}")
print("\nMatriks:")
print(matriks)
print("\nDeterminant: {:.2f}".format(determinant))
if inverse is not None:
    print("\nInverse Matriks:")
    print(inverse)
else:
    print("\nMatriks tidak dapat diinvers.")
