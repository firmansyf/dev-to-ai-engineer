# Minggu 9: LLM API & Prompting

> **Fase 3: LLM Engineering** · [⬅ Minggu 8](../../02-data-ml-foundations/week-08-neural-networks/) · [Kurikulum](../../README.md) · [Minggu 10 ➡](../week-10-embeddings-vector-search/)

Mulai minggu ini Anda membangun aplikasi dengan LLM. Fokusnya adalah memperlakukan LLM sebagai komponen software yang bisa diprogram, diuji, dan diandalkan, bukan sekadar chatbot.

> ⚠️ Mulai minggu ini Anda membutuhkan API key dari penyedia LLM. Simpan di `.env` (jangan di-commit) dan dokumentasikan nama variabelnya di `.env.example`. Pantau pemakaian dan biaya Anda.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Menjelaskan konsep dasar LLM: token, context window, sampling (temperature, top-p), serta biaya per token.
- Memanggil LLM lewat SDK resmi: system prompt, percakapan multi-turn, dan streaming.
- Menulis prompt yang jelas dan terstruktur, termasuk few-shot examples.
- Mendapatkan structured output (JSON) yang divalidasi dengan Pydantic.
- Menangani error, timeout, rate limit, dan retry.

## Topik

- Cara kerja LLM secara ringkas: next-token prediction, tokenization, context window
- Parameter: `temperature`, `max_tokens`, stop sequence
- SDK penyedia LLM: message format, peran system/user/assistant
- Prompt engineering: instruksi yang jelas, delimiter/tag, few-shot, chain-of-thought, persona
- Structured output dan validasi dengan Pydantic
- Streaming response, baik di CLI maupun lewat endpoint FastAPI
- Error handling, retry dengan exponential backoff, dan rate limit
- Menghitung token dan memperkirakan biaya
- Prompt sebagai kode: menyimpan prompt sebagai template dan memberinya versi

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Hello LLM.** Buat CLI chat multi-turn sederhana di terminal dengan streaming output.
2. **Eksperimen sampling.** Jalankan prompt yang sama 5 kali dengan temperature berbeda. Catat variasi hasilnya dan kapan masing-masing setting cocok dipakai.
3. **Structured extraction.** Ekstrak data terstruktur (mis. nama, tanggal, jumlah) dari teks bebas seperti email atau invoice, lalu validasi hasilnya dengan model Pydantic. Tangani kasus ketika output tidak valid.
4. **Klasifikasi dengan few-shot.** Bandingkan prompt zero-shot dan few-shot untuk tugas klasifikasi, lalu ukur akurasinya pada 20 contoh berlabel buatan Anda.
5. **Endpoint LLM.** Tambahkan endpoint FastAPI yang memanggil LLM dengan streaming, timeout, dan retry.

**Kriteria selesai:** tidak ada API key yang ter-commit, dan test memakai mock sehingga tidak memanggil API sungguhan.

## Referensi

- [Prompt Engineering Guide](https://www.promptingguide.ai/): kumpulan teknik prompting.
- <!-- TODO --> _Placeholder: dokumentasi resmi SDK dan prompt engineering dari penyedia LLM pilihan Anda (mis. Anthropic, OpenAI, Google)._
- <!-- TODO --> _Placeholder: dokumentasi structured output / tool-based JSON dari penyedia LLM pilihan Anda._
