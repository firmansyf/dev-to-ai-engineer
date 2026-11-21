# Minggu 14: Observability & Guardrails

> **Fase 4: Production AI** · [⬅ Minggu 13](../week-13-evaluation/) · [Kurikulum](../../README.md) · [Minggu 15 ➡](../week-15-deployment/)

Di production, Anda perlu tahu apa yang terjadi di setiap request (observability) dan mencegah aplikasi melakukan hal yang tidak diinginkan (guardrails). Aplikasi LLM menghadapi jenis serangan baru seperti prompt injection, jadi bagian ini tidak boleh dilewati.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Menerapkan structured logging dan tracing untuk setiap request LLM, termasuk prompt, respons, token, latensi, dan biaya.
- Membuat dashboard atau laporan sederhana untuk biaya, latensi, dan tingkat error.
- Menjelaskan risiko keamanan utama aplikasi LLM, terutama prompt injection (langsung maupun tidak langsung).
- Menerapkan guardrail pada input dan output: validasi, filter, batasan topik, dan penanganan PII.
- Merancang feedback loop dari pengguna untuk perbaikan berkelanjutan.

## Topik

- Structured logging (JSON log) dan correlation ID
- Tracing untuk pipeline multi-langkah (RAG, agent) dengan konsep OpenTelemetry
- Metrik: token, biaya, latensi (p50/p95), error rate, cache hit
- Mengurangi biaya: memilih model, prompt caching, response caching, membatasi panjang output
- Keamanan LLM: prompt injection, indirect injection via dokumen RAG, data leakage, aksi tool yang berbahaya
- Guardrail input: validasi, batas panjang, deteksi topik di luar cakupan
- Guardrail output: validasi skema, cek grounding, filter konten
- PII dan privasi: redaksi data sensitif di log
- Mengumpulkan feedback pengguna (👍/👎) dan menjadikannya kasus eval

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Tracing.** Tambahkan tracing ke aplikasi Milestone 3 sehingga satu request bisa ditelusuri dari input → retrieval → tool call → output, lengkap dengan durasi tiap langkah.
2. **Cost report.** Buat script yang membaca log dan menghasilkan laporan total token, biaya, dan latensi p50/p95 per endpoint.
3. **Red teaming.** Tulis 10 percobaan prompt injection (termasuk lewat dokumen yang di-ingest) terhadap aplikasi Anda. Catat mana yang berhasil.
4. **Guardrails.** Terapkan mitigasi untuk serangan yang berhasil pada latihan 3, lalu jadikan serangan tersebut kasus uji permanen.
5. **Redaksi PII.** Pastikan email dan nomor telepon tidak tersimpan mentah di log, dan sertakan test-nya.

**Kriteria selesai:** setiap request punya trace yang bisa ditelusuri, dan ada test suite untuk kasus keamanan.

## Referensi

- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/): daftar risiko keamanan utama aplikasi LLM.
- [OpenTelemetry documentation](https://opentelemetry.io/docs/): standar tracing dan metrik.
- [Logging Cookbook (Python docs)](https://docs.python.org/3/howto/logging-cookbook.html): pola logging lanjutan.
- <!-- TODO --> _Placeholder: dokumentasi mitigasi prompt injection dari penyedia LLM pilihan Anda._
