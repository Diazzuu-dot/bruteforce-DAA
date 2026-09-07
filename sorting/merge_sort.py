def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    tengah = len(arr) // 2

    kiri = merge_sort(arr[:tengah])
    kanan = merge_sort(arr[tengah:])

    return merge(kiri, kanan)


def merge(kiri, kanan):
    hasil = []

    i = 0
    j = 0

    while i < len(kiri) and j < len(kanan):
        if kiri[i] <= kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])

    return hasil


data = [38, 27, 43, 3, 9, 82, 10]

print("Data sebelum sorting :", data)

hasil = merge_sort(data)

print("Data setelah sorting :", hasil)  