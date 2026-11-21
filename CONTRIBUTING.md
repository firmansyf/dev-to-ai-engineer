# Panduan Kontribusi

Terima kasih sudah tertarik berkontribusi! Repo ini dibuat untuk belajar bersama, jadi kontribusi sekecil apa pun sangat berarti.

Dengan berkontribusi, Anda setuju mengikuti [Kode Etik](CODE_OF_CONDUCT.md) repo ini.

## Apa saja yang bisa dikontribusikan?

| Jenis | Contoh | Mulai dari |
|---|---|---|
| **Latihan baru** | Soal latihan tambahan untuk suatu minggu | Issue "Usulan latihan baru" |
| **Solusi alternatif** | Pendekatan lain untuk latihan yang sudah ada | Langsung PR |
| **Referensi** | Artikel, dokumentasi, video, atau buku yang bermanfaat | Issue "Usulan referensi" |
| **Terjemahan** | Menerjemahkan materi ke bahasa lain | Diskusikan dulu lewat issue |
| **Perbaikan** | Typo, link rusak, penjelasan yang kurang jelas, bug di kode | Issue "Laporan bug" atau langsung PR untuk perbaikan kecil |

Untuk perubahan besar (misalnya mengubah urutan kurikulum atau menambah topik), buka issue dulu supaya bisa didiskusikan sebelum Anda menghabiskan waktu.

### Aturan khusus

- **Latihan:** tulis deskripsi soal, input/output yang diharapkan, dan kriteria selesai. **Jangan sertakan solusi** di `README.md` minggu.
- **Solusi alternatif:** simpan di `<folder-minggu>/solutions/<github-username>/`, misalnya `week-01-syntax-idioms/solutions/octocat/`. Sertakan test dan penjelasan singkat tentang pendekatan Anda.
- **Referensi:** pastikan link bisa diakses dan, sebisa mungkin, gratis. Tulis satu kalimat tentang mengapa referensi itu berguna. Utamakan dokumentasi resmi.
- **Terjemahan:** simpan sebagai file terpisah dengan akhiran kode bahasa, misalnya `README.en.md`.

## Konvensi bahasa dan penamaan

- Dokumentasi ditulis dalam **Bahasa Indonesia**. Istilah teknis (misalnya *comprehension*, *embedding*) boleh tetap dalam bahasa Inggris.
- Nama file dan folder dalam **bahasa Inggris** dengan format **kebab-case**, misalnya `week-05-numpy-pandas`. Pengecualian: modul Python wajib memakai `snake_case.py` agar bisa di-import.
- Kode, nama variabel, dan komentar kode ditulis dalam **bahasa Inggris**.

## Alur kerja

### 1. Setup

```bash
# Fork repo ini di GitHub, lalu:
git clone https://github.com/<username-anda>/dev-to-ai-engineer.git
cd dev-to-ai-engineer
uv sync
```

### 2. Buat branch

Format: `<tipe>/<deskripsi-singkat>` dalam kebab-case.

| Prefix | Untuk |
|---|---|
| `feat/` | Latihan baru atau konten baru |
| `fix/` | Perbaikan bug, typo, atau link rusak |
| `docs/` | Perubahan dokumentasi umum |
| `solution/` | Solusi alternatif |
| `chore/` | Konfigurasi, CI, atau dependency |

Contoh: `feat/week-05-groupby-exercise`, `fix/week-10-broken-link`.

### 3. Commit dengan Conventional Commits

Format: `<tipe>(<scope opsional>): <deskripsi>`

Tipe yang dipakai: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`.

Scope yang disarankan adalah nomor minggu (misalnya `week-05`) atau area (`ci`, `deps`).

```text
feat(week-05): add groupby aggregation exercise
fix(week-10): update broken vector database link
docs: clarify uv setup steps in README
test(week-03): add tests for alternative solution
ci: cache uv dependencies
```

Pesan commit boleh dalam bahasa Inggris atau Indonesia. Usahakan konsisten dalam satu PR.

### 4. Cek sebelum push

```bash
uv run ruff check .
uv run ruff format --check .   # atau `uv run ruff format .` untuk memperbaiki
uv run pytest
```

Ketiga perintah ini juga dijalankan oleh CI di setiap PR.

### 5. Buka Pull Request

1. Push branch ke fork Anda, lalu buka PR ke branch `main`.
2. Isi template PR dan tautkan issue terkait (`Closes #123`).
3. Satu PR untuk satu perubahan yang fokus. PR kecil lebih cepat di-review.
4. Pastikan CI hijau.
5. Tanggapi masukan review. Setelah disetujui, maintainer akan melakukan merge.

## Gaya kode

- Formatter dan linter: **[ruff](https://docs.astral.sh/ruff/)**. Konfigurasinya ada di `pyproject.toml`. Jangan menonaktifkan rule tanpa alasan yang jelas.
- Gunakan **type hints** untuk parameter dan nilai kembalian fungsi.
- Tulis kode yang mudah dibaca pemula. Hindari trik yang terlalu "pintar".
- Setiap kode solusi sebaiknya disertai test pytest (`test_*.py`).
- Jangan pernah meng-commit API key atau secret. Gunakan `.env` (sudah di-ignore) dan dokumentasikan variabel baru di `.env.example`.

## Pertanyaan?

Buka issue atau tanyakan di diskusi PR. Tidak ada pertanyaan yang terlalu dasar.
