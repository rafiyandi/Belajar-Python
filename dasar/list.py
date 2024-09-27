# 1. CREATE: Menambahkan elemen ke dalam list
data = []  # Membuat list kosong
data.append("Apple")   # Menambah elemen "Apple" ke dalam list
data.append("Banana")  # Menambah elemen "Banana" ke dalam list
data.extend(["Cherry", "Date"])  # Menambah beberapa elemen sekaligus

print("List setelah CREATE:", data)  # Output: ['Apple', 'Banana', 'Cherry', 'Date']

# 2. READ: Membaca elemen-elemen dalam list
print("READ seluruh elemen:", data)  # Membaca semua elemen dalam list
print("READ elemen pertama:", data[0])  # Membaca elemen pertama (Apple)
print("READ elemen terakhir:", data[-1])  # Membaca elemen terakhir (Date)

# 3. UPDATE: Mengubah elemen dalam list
data[1] = "Blueberry"  # Mengubah elemen kedua (Banana) menjadi Blueberry
print("List setelah UPDATE:", data)  # Output: ['Apple', 'Blueberry', 'Cherry', 'Date']

# 4. DELETE: Menghapus elemen dari list
data.remove("Cherry")  # Menghapus elemen "Cherry" dari list
print("List setelah DELETE dengan remove():", data)  # Output: ['Apple', 'Blueberry', 'Date']

del data[0]  # Menghapus elemen pertama (Apple)
print("List setelah DELETE dengan del:", data)  # Output: ['Blueberry', 'Date']

data.pop()  # Menghapus elemen terakhir (Date)
print("List setelah DELETE dengan pop():", data)  # Output: ['Blueberry']
