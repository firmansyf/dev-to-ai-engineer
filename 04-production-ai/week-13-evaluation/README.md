# Minggu 13: Evaluasi

> **Fase 4: Production AI** · [⬅ Minggu 12](../../03-llm-engineering/week-12-tool-use-agents/) · [Kurikulum](../../README.md) · [Minggu 14 ➡](../week-14-observability-guardrails/)

"Kelihatannya sudah bagus" bukan standar production. Minggu ini Anda membangun cara **mengukur** kualitas aplikasi LLM, sehingga setiap perubahan prompt, model, atau retrieval bisa dibandingkan secara objektif. Anggap eval sebagai unit test untuk perilaku yang non-deterministik.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Menyusun eval dataset yang representatif, termasuk edge case dan pertanyaan yang seharusnya ditolak.
- Memilih metode evaluasi: exact match, aturan berbasis kode, similarity, LLM-as-judge, dan review manusia.
- Mengevaluasi retrieval (hit rate, MRR) secara terpisah dari generation (faithfulness, relevansi).
- Membangun LLM-as-judge dengan rubrik yang jelas, lalu memvalidasinya terhadap penilaian manusia.
- Menjalankan eval sebagai regression test sebelum mengubah prompt atau model.

## Topik

- Mengapa eval sulit: non-determinisme dan jawaban terbuka
- Eval dataset: sumber, ukuran, labeling, versioning
- Metrik berbasis kode vs berbasis model
- Metrik RAG: retrieval (hit rate @k, MRR) dan generation (faithfulness, answer relevance)
- LLM-as-judge: rubrik, skala, bias, dan kalibrasi terhadap penilaian manusia
- Pairwise comparison (A/B) antar versi prompt atau model
- Menjalankan eval di CI: threshold dan laporan
- Trade-off kualitas, biaya, dan latensi
- Framework eval yang ada (gambaran umum) vs eval harness sederhana buatan sendiri

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Eval dataset.** Kembangkan set pertanyaan dari Milestone 3 menjadi minimal 30 kasus berlabel, termasuk edge case dan pertanyaan di luar cakupan.
2. **Eval harness.** Buat script yang menjalankan seluruh dataset, menghitung metrik, lalu menyimpan hasilnya (CSV/JSON) per versi.
3. **Retrieval eval.** Ukur hit rate @k dan MRR untuk pipeline retrieval Anda, lalu coba satu perbaikan dan ukur ulang.
4. **LLM-as-judge.** Tulis judge prompt dengan rubrik untuk faithfulness. Bandingkan skornya dengan penilaian manual Anda pada 15 contoh dan hitung tingkat kesesuaiannya.
5. **Regression check.** Ubah prompt sistem, jalankan eval, lalu buat laporan perbandingan sebelum vs sesudah.

**Kriteria selesai:** Anda bisa menjawab "apakah perubahan ini membuat aplikasi lebih baik?" dengan angka.

## Referensi

- [scikit-learn: Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html): dasar metrik evaluasi (precision, recall, dll.).
- <!-- TODO --> _Placeholder: panduan evaluasi aplikasi LLM dari penyedia LLM pilihan Anda._
- <!-- TODO --> _Placeholder: artikel tentang LLM-as-judge (kontribusi diterima)._
- <!-- TODO --> _Placeholder: dokumentasi framework eval open source (opsional)._
