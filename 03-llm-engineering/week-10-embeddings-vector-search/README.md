# Minggu 10: Embedding & Vector Search

> **Fase 3: LLM Engineering** · [⬅ Minggu 9](../week-09-llm-apis-prompting/) · [Kurikulum](../../README.md) · [Minggu 11 ➡](../week-11-rag/)

Embedding mengubah teks menjadi vektor sehingga "kemiripan makna" bisa dihitung. Konsep cosine similarity dari minggu 6 kini dipakai sungguhan. Minggu ini adalah fondasi untuk RAG.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Menjelaskan apa itu embedding dan mengapa teks yang maknanya mirip menghasilkan vektor yang berdekatan.
- Menghasilkan embedding dengan API maupun model lokal.
- Membangun semantic search, mulai dari NumPy murni sampai vector database.
- Menjelaskan trade-off antara exact search dan approximate nearest neighbor (ANN).
- Membandingkan semantic search dengan keyword search (BM25) dan memahami hybrid search.

## Topik

- Embedding: dimensi, normalisasi, model embedding (API vs lokal/open source)
- Similarity metric: cosine, dot product, Euclidean
- Brute-force search dengan NumPy
- Vector database dan index (mis. pgvector, Chroma, Qdrant, FAISS), beserta metadata filtering
- ANN index (konsep HNSW) dan trade-off akurasi vs kecepatan
- Keyword search (BM25) dan hybrid search
- Batasan embedding: bahasa, domain, panjang teks
- Clustering dan visualisasi embedding (opsional)

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Similarity matrix.** Buat embedding untuk 20 kalimat (campuran topik dan bahasa Indonesia/Inggris), hitung similarity matrix-nya, lalu tampilkan sebagai heatmap.
2. **Search dari nol.** Bangun semantic search untuk ±500 dokumen pendek hanya dengan NumPy. Sediakan fungsi `search(query, k)` yang mengembalikan top-k beserta skornya.
3. **Pakai vector database.** Pindahkan data dari latihan 2 ke sebuah vector database, lengkap dengan metadata filter (mis. kategori atau tanggal).
4. **Keyword vs semantic.** Siapkan 10 query uji. Bandingkan hasil BM25, semantic search, dan hybrid. Catat kapan masing-masing unggul.
5. **Caching.** Simpan embedding ke disk agar tidak dihitung ulang, dengan cache key berdasarkan hash konten.

**Kriteria selesai:** Anda bisa menjelaskan, dengan contoh dari eksperimen Anda, kapan semantic search gagal.

## Referensi

- <!-- TODO --> _Placeholder: penjelasan konseptual tentang embedding (kontribusi diterima)._
- <!-- TODO --> _Placeholder: dokumentasi embedding dari penyedia LLM pilihan Anda._
- <!-- TODO --> _Placeholder: dokumentasi resmi vector database pilihan (pgvector / Chroma / Qdrant / FAISS)._
- [NumPy linear algebra (numpy.linalg)](https://numpy.org/doc/stable/reference/routines.linalg.html): untuk implementasi search dari nol.
