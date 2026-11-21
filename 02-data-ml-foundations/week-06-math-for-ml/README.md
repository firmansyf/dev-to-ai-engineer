# Minggu 6: Matematika untuk ML

> **Fase 2: Data & ML Foundations** · [⬅ Minggu 5](../week-05-numpy-pandas/) · [Kurikulum](../../README.md) · [Minggu 7 ➡](../week-07-classical-ml/)

Anda tidak perlu menjadi ahli matematika untuk menjadi AI Engineer, tetapi Anda perlu **intuisi** tentang vektor, probabilitas, dan optimisasi. Konsep-konsep ini muncul langsung saat Anda memakai embedding, temperature, dan training. Fokus minggu ini adalah intuisi dan implementasi dengan NumPy, bukan pembuktian.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Menjelaskan vektor dan matriks secara geometris, serta melakukan operasinya dengan NumPy.
- Menghitung dot product, norm, dan cosine similarity, dan menjelaskan maknanya.
- Menjelaskan perkalian matriks sebagai transformasi.
- Memahami konsep probabilitas dasar: distribusi, mean/variance, softmax.
- Menjelaskan turunan dan gradient secara intuitif, serta cara kerja gradient descent.

## Topik

- Vektor: penjumlahan, skalar, norm, dot product
- Cosine similarity dan jarak (fondasi pencarian embedding di minggu 10)
- Matriks: perkalian matriks, transpose, matriks identitas, dimensi
- Probabilitas dan statistik dasar: distribusi, mean, variance, standard deviation
- Softmax dan bagaimana temperature mengubah distribusi
- Turunan, gradient, dan chain rule secara intuitif
- Gradient descent dan learning rate

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Vector toolkit.** Implementasikan `dot`, `norm`, dan `cosine_similarity` dengan Python murni, lalu verifikasi hasilnya terhadap NumPy dengan test pytest.
2. **Mini semantic search.** Diberikan beberapa "dokumen" berupa vektor kecil buatan tangan, cari dokumen paling mirip dengan sebuah query vektor memakai cosine similarity.
3. **Softmax & temperature.** Implementasikan softmax dengan parameter temperature. Visualisasikan bagaimana distribusinya berubah untuk temperature 0.1, 1, dan 2.
4. **Gradient descent dari nol.** Cari nilai minimum fungsi `f(x) = (x - 3)^2` dengan gradient descent. Lalu lakukan linear regression sederhana (1 fitur) memakai gradient descent dengan NumPy.
5. **Eksperimen learning rate.** Plot nilai loss terhadap iterasi untuk beberapa learning rate. Jelaskan apa yang terjadi bila learning rate terlalu besar atau terlalu kecil.

**Kriteria selesai:** Anda bisa menjelaskan dengan kata-kata sendiri mengapa cosine similarity dipakai untuk membandingkan embedding.

## Referensi

- [Essence of linear algebra (3Blue1Brown)](https://www.3blue1brown.com/topics/linear-algebra): seri video visual tentang aljabar linear.
- [Neural networks (3Blue1Brown)](https://www.3blue1brown.com/topics/neural-networks): intuisi gradient descent dan backpropagation.
- [NumPy linear algebra (numpy.linalg)](https://numpy.org/doc/stable/reference/routines.linalg.html): referensi fungsi aljabar linear.
- <!-- TODO --> _Placeholder: referensi probabilitas dan statistik untuk pemula (kontribusi diterima)._
