# Minggu 5: NumPy & pandas

> **Fase 2: Data & ML Foundations** · [⬅ Minggu 4](../../01-python-fundamentals/week-04-async-apis/) · [Kurikulum](../../README.md) · [Minggu 6 ➡](../week-06-math-for-ml/)

Data adalah bahan baku AI. Minggu ini Anda belajar memanipulasi data numerik dan tabular secara efisien, sekaligus mengenal Jupyter sebagai lingkungan eksplorasi.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Membuat dan memanipulasi array NumPy: shape, indexing, slicing, reshape.
- Menjelaskan vectorization dan broadcasting, serta mengapa keduanya jauh lebih cepat daripada loop Python.
- Memuat, menjelajahi, membersihkan, dan mentransformasi data dengan pandas.
- Melakukan agregasi (`groupby`), join/merge, dan reshape (`pivot`, `melt`).
- Membuat visualisasi dasar untuk eksplorasi data.

## Topik

- Jupyter notebook / JupyterLab (atau notebook di editor) via `uv`
- NumPy: `ndarray`, dtype, shape, axis, indexing (boolean, fancy), broadcasting, fungsi agregasi
- pandas: `Series`, `DataFrame`, `read_csv`, `loc`/`iloc`, filtering, missing value, tipe data
- Transformasi: `apply` vs operasi vectorized, `groupby`, `merge`, `pivot_table`
- Data cleaning: duplikat, outlier, normalisasi teks
- Visualisasi dasar dengan matplotlib atau plotting bawaan pandas
- (Opsional) Polars sebagai alternatif pandas

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Loop vs vectorized.** Hitung jarak Euclidean antara 10.000 pasang titik dengan loop Python, lalu dengan NumPy. Ukur dan bandingkan waktunya.
2. **Broadcasting.** Normalisasi setiap kolom sebuah matriks (z-score) tanpa loop.
3. **EDA dataset publik.** Pilih dataset publik berformat CSV. Lakukan exploratory data analysis: ringkasan statistik, missing value, distribusi kolom penting, dan 3 insight yang Anda temukan.
4. **Cleaning pipeline.** Tulis fungsi `clean(df) -> DataFrame` yang bisa di-test (bukan hanya sel notebook) untuk membersihkan dataset dari latihan 3. Sertakan test pytest.
5. **Agregasi.** Jawab 3 pertanyaan bisnis tentang dataset tersebut memakai `groupby` dan `merge`.

**Kriteria selesai:** notebook EDA dapat dijalankan ulang dari awal, dan fungsi cleaning memiliki test yang lulus.

## Referensi

- [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html): panduan pemula resmi NumPy.
- [NumPy: Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html): penjelasan broadcasting.
- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html): pengantar singkat pandas.
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html): referensi lengkap pandas.
- <!-- TODO --> _Placeholder: sumber dataset publik yang direkomendasikan (kontribusi diterima)._
