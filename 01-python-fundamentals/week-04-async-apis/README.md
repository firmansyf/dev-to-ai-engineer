# Minggu 4: Async & API

> **Fase 1: Python Fundamentals** · [⬅ Minggu 3](../week-03-tooling-testing/) · [Kurikulum](../../README.md) · [Minggu 5 ➡](../../02-data-ml-foundations/week-05-numpy-pandas/)

Minggu ini menghubungkan Python dengan dunia yang sudah Anda kenal: HTTP, API, dan async. Hampir semua aplikasi AI berkomunikasi lewat API, jadi materi ini menjadi fondasi fase 3.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Menjelaskan model `asyncio` dan membandingkannya dengan event loop / Promise di JavaScript.
- Menulis kode async dengan `async`/`await`, `asyncio.gather`, dan timeout.
- Memanggil API eksternal dengan httpx (sync dan async).
- Memvalidasi data dengan Pydantic.
- Membangun REST API dengan FastAPI, lengkap dengan validasi, error handling, dan test.
- Mengelola konfigurasi lewat environment variable.

## Topik

- `asyncio`: coroutine, event loop, `await`, `gather`, `TaskGroup`, `wait_for`
- Kapan async berguna (I/O-bound) dan kapan tidak (CPU-bound)
- httpx: request, timeout, retry, async client
- Pydantic: model, validasi, serialisasi, `pydantic-settings` untuk konfigurasi
- FastAPI: routing, path/query/body parameter, dependency injection, response model, error handling
- Testing API dengan `TestClient`
- Environment variable dan file `.env`

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Concurrent fetch.** Ambil data dari 10 URL publik secara sequential, lalu secara concurrent dengan `httpx.AsyncClient` dan `asyncio.gather`. Bandingkan waktunya.
2. **Validasi Pydantic.** Modelkan payload JSON yang kompleks (nested object, list, field opsional, validator custom) dan tulis test untuk input valid maupun tidak valid.
3. **Rate-limited client.** Buat wrapper async yang membatasi jumlah request paralel dengan `asyncio.Semaphore`.

## 🏁 Milestone 1: REST API ter-test

Bangun REST API dengan FastAPI untuk domain pilihan Anda (mis. catatan, bookmark, atau to-do).

**Persyaratan minimum:**

- CRUD minimal untuk satu resource, dengan model Pydantic untuk request dan response.
- Penyimpanan sederhana (in-memory, file JSON, atau SQLite).
- Error handling yang konsisten (404, 422, dll.).
- Konfigurasi dibaca dari environment variable.
- Test pytest untuk setiap endpoint; `uv run pytest` lulus.
- README singkat: cara menjalankan, contoh request, dan hal yang Anda pelajari.

**Bonus:** satu endpoint yang memanggil API eksternal secara async.

## Referensi

- [asyncio (Python docs)](https://docs.python.org/3/library/asyncio.html): referensi resmi asyncio.
- [HTTPX documentation](https://www.python-httpx.org/): HTTP client sync/async.
- [Pydantic documentation](https://docs.pydantic.dev/latest/): validasi data.
- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/): tutorial resmi FastAPI.
- [FastAPI: Testing](https://fastapi.tiangolo.com/tutorial/testing/): menguji aplikasi FastAPI.
