# bruteforce-DAA
Tugas Kelompok Algoritma Brute Force

## 1. Pseudocode Prima

## 2. Pseudocode Sorting
function MergeSort(arr : array of integer) → array of integer
{ Membagi larik secara rekursif hingga tiap bagian berisi
  satu elemen, lalu menggabungkannya kembali secara terurut.
  Masukan : arr — larik bilangan bulat sembarang
  Keluaran : larik bilangan bulat terurut menaik
}
Deklarasi
  tengah       : integer
  kiri, kanan  : array of integer

Algoritma:
  if length(arr) ≤ 1 then
    return arr
  endif

  tengah ← length(arr) div 2

  kiri  ← MergeSort(arr[0 .. tengah - 1])
  kanan ← MergeSort(arr[tengah .. length(arr) - 1])

  return Merge(kiri, kanan)

function Merge(kiri, kanan : array of integer) → array of integer
{ Menggabungkan dua larik terurut menjadi satu larik terurut.
  Masukan : kiri  — larik kiri yang sudah terurut
            kanan — larik kanan yang sudah terurut
  Keluaran : hasil — larik gabungan yang terurut menaik
}
Deklarasi
  hasil        : array of integer  { larik kosong }
  i, j         : integer

Algoritma:
  hasil ← []
  i ← 0
  j ← 0

  while i < length(kiri) and j < length(kanan) do
    if kiri[i] ≤ kanan[j] then
      append kiri[i] → hasil
      i ← i + 1
    else
      append kanan[j] → hasil
      j ← j + 1
    endif
  endwhile

  { salin sisa elemen kiri yang belum digabung }
  append kiri[i .. length(kiri) - 1] → hasil

  { salin sisa elemen kanan yang belum digabung }
  append kanan[j .. length(kanan) - 1] → hasil

  return hasil

```diff
## Penjelasan Pseudocode
+Fungsi MergeSort
=> Basis rekursi — Kondisi if length(arr) ≤ 1 adalah titik berhenti rekursi. Larik dengan nol atau satu elemen secara definisi sudah terurut, sehingga langsung dikembalikan tanpa pemrosesan lebih lanjut.

=> Pembagian (Divide) — Variabel tengah dihitung dengan pembagian bulat (div 2) untuk mendapatkan indeks titik tengah larik. Larik kemudian dibagi menjadi dua sublarik: kiri mencakup elemen dari indeks 0 sampai tengah - 1, dan kanan mencakup elemen dari indeks tengah sampai akhir larik.

=> Rekursi — MergeSort dipanggil kembali pada kiri dan kanan secara terpisah. Proses ini terus berlanjut secara rekursif sampai setiap sublarik hanya tersisa satu elemen (memenuhi basis rekursi).

=>Penggabungan (Conquer) — Setelah kedua sisi terurut, Merge(kiri, kanan) dipanggil untuk menggabungkan keduanya menjadi satu larik terurut yang dikembalikan sebagai hasil.

+Fungsi Merge
=> Inisialisasi — Larik hasil disiapkan sebagai larik kosong sebagai tempat menampung elemen yang sudah digabung dan terurut. Dua pencacah i dan j masing-masing menunjuk indeks elemen aktif pada kiri dan kanan, keduanya dimulai dari 0.

=> Perbandingan dan pengisian (loop utama) — Loop while berjalan selama masih ada elemen tersisa di kedua sisi. Pada setiap iterasi, elemen kiri[i] dan kanan[j] dibandingkan; yang lebih kecil (atau sama) dimasukkan lebih dulu ke hasil, dan pencacah sisi tersebut dinaikkan satu. Kondisi ≤ memastikan kestabilan pengurutan — elemen dengan nilai sama mempertahankan urutan relatif aslinya dari sisi kiri.

=>Penyalinan sisa elemen — Ketika salah satu sisi habis duluan, loop utama berhenti. Dua baris append terakhir menyalin sisa elemen dari sisi yang belum habis langsung ke hasil tanpa perbandingan tambahan, karena elemen-elemen tersebut sudah pasti terurut dan lebih besar dari seluruh elemen yang sudah masuk ke hasil.
```

### Contoh Pembuktian

MergeSort([38, 27, 43, 3, 9, 82, 10])
    MergeSort([38, 27, 43])
        MergeSort([38]) → [38] ← basis rekursi
        MergeSort([27, 43])
            MergeSort([27]) → [27] ← basis rekursi
            MergeSort([43]) → [43] ← basis rekursi
            Merge([27], [43]) → [27, 43]
        Merge([38], [27, 43]) → [27, 38, 43]

    MergeSort([3, 9, 82, 10])
        MergeSort([3, 9])
            MergeSort([3]) → [3] ← basis rekursi
            MergeSort([9]) → [9] ← basis rekursi
            Merge([3], [9]) → [3, 9]
        MergeSort([82, 10])
            MergeSort([82]) → [82] ← basis rekursi
            MergeSort([10]) → [10] ← basis rekursi
            Merge([82], [10]) → [10, 82]
        Merge([3, 9], [10, 82]) → [3, 9, 10, 82]

    Merge([27, 38, 43], [3, 9, 10, 82]) → [3, 9, 10, 27, 38, 43, 82]
    