# Minggu 11: Retrieval-Augmented Generation (RAG)

> **Fase 3: LLM Engineering** · [⬅ Minggu 10](../week-10-embeddings-vector-search/) · [Kurikulum](../../README.md) · [Minggu 12 ➡](../week-12-tool-use-agents/)

RAG menggabungkan retrieval (minggu 10) dengan generation (minggu 9) agar LLM bisa menjawab berdasarkan dokumen Anda sendiri. Ini salah satu pola paling umum di aplikasi AI production.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Menjelaskan arsitektur RAG dan kapan RAG lebih tepat daripada fine-tuning atau long-context prompting.
- Membangun pipeline ingestion: memuat dokumen, chunking, embedding, dan indexing.
- Membangun pipeline query: retrieval, (opsional) reranking, menyusun prompt, dan generation.
- Membuat jawaban yang grounded, lengkap dengan sitasi sumber, dan menolak menjawab bila konteks tidak cukup.
- Mendiagnosis apakah sebuah kesalahan terjadi di tahap retrieval atau generation.

## Topik

- Arsitektur RAG end-to-end
- Memuat dokumen: Markdown, HTML, PDF
- Strategi chunking: ukuran, overlap, chunking berdasarkan struktur dokumen
- Metadata dan sitasi sumber
- Retrieval: top-k, hybrid search, query rewriting
- Reranking (konsep dan implementasi sederhana)
- Prompt untuk RAG: menyisipkan konteks, instruksi grounding, jawaban "tidak tahu"
- Mode kegagalan umum: chunk tidak relevan, konteks terpotong, halusinasi
- Membangun sendiri vs memakai framework (mis. LangChain, LlamaIndex): pahami dulu cara membangunnya sendiri

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **RAG minimal dari nol.** Tanpa framework, bangun RAG untuk sekumpulan dokumen Markdown (mis. dokumentasi sebuah library open source). Batasi kode intinya sekitar 200 baris.
2. **Eksperimen chunking.** Bandingkan 3 strategi chunking pada 10 pertanyaan uji. Ukur apakah chunk yang benar ikut ter-retrieve (hit rate @k).
3. **Sitasi.** Buat jawaban mencantumkan sumber (nama file atau judul bagian) dan verifikasi bahwa sumber tersebut benar-benar ada di konteks.
4. **Uji "tidak tahu".** Siapkan 5 pertanyaan yang jawabannya **tidak** ada di dokumen. Pastikan sistem menolak menjawab alih-alih berhalusinasi.
5. **Debug retrieval.** Untuk setiap jawaban yang salah, catat apakah masalahnya ada di retrieval atau generation. Perbaiki satu masalah, lalu ukur ulang.

**Kriteria selesai:** Anda memiliki set pertanyaan uji kecil yang bisa dijalankan ulang untuk membandingkan versi RAG Anda. Set ini akan dipakai lagi di minggu 13.

## Referensi

- <!-- TODO --> _Placeholder: paper atau artikel pengantar RAG (kontribusi diterima)._
- <!-- TODO --> _Placeholder: panduan strategi chunking._
- <!-- TODO --> _Placeholder: dokumentasi RAG / retrieval dari penyedia LLM pilihan Anda._
