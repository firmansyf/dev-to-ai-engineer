# Minggu 7: ML Klasik

> **Fase 2: Data & ML Foundations** · [⬅ Minggu 6](../week-06-math-for-ml/) · [Kurikulum](../../README.md) · [Minggu 8 ➡](../week-08-neural-networks/)

Sebelum masuk ke deep learning dan LLM, pahami dulu alur kerja machine learning secara umum. Konsep seperti train/test split, overfitting, dan metrik evaluasi tetap berlaku saat Anda mengevaluasi aplikasi LLM di fase 4.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Menjelaskan perbedaan supervised dan unsupervised learning, serta classification dan regression.
- Menjalankan alur ML lengkap dengan scikit-learn: data, fitur, training, evaluasi.
- Membagi data dengan benar (train/validation/test) dan menghindari data leakage.
- Mendeteksi overfitting dan underfitting.
- Memilih dan menafsirkan metrik: accuracy, precision, recall, F1, MAE/RMSE.

## Topik

- Jenis-jenis problem ML dan baseline sederhana
- scikit-learn API: `fit`, `predict`, `transform`, `Pipeline`
- Feature engineering dan preprocessing (scaling, encoding kategorikal)
- Model: linear/logistic regression, decision tree, random forest, k-means
- Train/validation/test split, cross-validation
- Overfitting, underfitting, dan regularization
- Metrik klasifikasi dan regresi, confusion matrix
- Representasi teks klasik: bag-of-words dan TF-IDF

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Baseline dulu.** Untuk sebuah dataset klasifikasi, buat baseline "selalu tebak kelas mayoritas", lalu bandingkan dengan logistic regression.
2. **Pipeline.** Bangun `Pipeline` scikit-learn yang menggabungkan preprocessing dan model, lalu evaluasi dengan cross-validation.
3. **Overfitting.** Latih decision tree dengan `max_depth` berbeda. Plot skor train vs validation dan jelaskan polanya.
4. **Klasifikasi teks.** Buat classifier sentimen atau topik sederhana dengan TF-IDF dan logistic regression. Catat contoh-contoh yang salah diklasifikasi.
5. **Metrik yang tepat.** Pada dataset yang tidak seimbang, tunjukkan mengapa accuracy bisa menyesatkan dan metrik apa yang lebih tepat.

**Kriteria selesai:** setiap eksperimen memiliki catatan singkat berisi hasil dan kesimpulan.

## Referensi

- [scikit-learn: Getting Started](https://scikit-learn.org/stable/getting_started.html): pengantar resmi scikit-learn.
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html): referensi lengkap model dan teknik.
- [scikit-learn: Common pitfalls and recommended practices](https://scikit-learn.org/stable/common_pitfalls.html): data leakage dan jebakan umum lainnya.
- <!-- TODO --> _Placeholder: kursus atau buku pengantar ML yang direkomendasikan (kontribusi diterima)._
