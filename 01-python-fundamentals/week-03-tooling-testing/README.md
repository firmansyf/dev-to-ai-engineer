# Minggu 3: Tooling & Testing

> **Fase 1: Python Fundamentals** · [⬅ Minggu 2](../week-02-functions-oop/) · [Kurikulum](../../README.md) · [Minggu 4 ➡](../week-04-async-apis/)

Minggu ini Anda menyiapkan "toolchain" profesional: mengelola dependency, menyusun project menjadi module/package, menangani error, dan menulis test.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Mengelola project dan dependency dengan uv (`uv add`, `uv sync`, `uv run`, `uv.lock`).
- Menyusun kode menjadi module dan package, serta memahami cara kerja `import`.
- Memakai ruff untuk lint dan format.
- Menangani dan mendefinisikan exception dengan benar.
- Menulis test dengan pytest: assertion, fixture, parametrize, dan mocking dasar.
- Memakai `logging` sebagai pengganti `print` untuk diagnostik.

## Topik

- uv: `pyproject.toml`, dependency group, lockfile, `.python-version`, virtual environment
- Module vs package, `__init__.py`, absolute vs relative import, layout `src/`
- ruff: rule set, auto-fix, integrasi dengan editor
- Exception: `try`/`except`/`else`/`finally`, custom exception, `raise ... from ...`
- pytest: test discovery, `assert`, `pytest.raises`, fixture, `@pytest.mark.parametrize`, `tmp_path`
- Mocking dengan `unittest.mock` / `monkeypatch`
- Modul `logging`
- Membuat CLI sederhana dengan `argparse`
- (Opsional) type checking statis dengan mypy atau pyright

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Package kecil.** Ubah latihan word counter dari minggu 1 menjadi package dengan beberapa module (mis. `reader`, `counter`, `cli`) yang bisa dijalankan sebagai CLI.
2. **Test suite.** Tulis test pytest untuk package tersebut, termasuk test parametrize dan test yang memakai `tmp_path` untuk file sementara.
3. **Error handling.** Definisikan hierarki exception sendiri (mis. `ConfigError`, `ValidationError`). Pastikan CLI menampilkan pesan error yang ramah tanpa traceback.
4. **Mocking.** Tulis fungsi yang membaca waktu sekarang atau environment variable, lalu test fungsi itu dengan `monkeypatch`.
5. **Code kata dengan TDD.** Implementasikan fungsi validasi password (minimal panjang, angka, huruf besar, dll.) dengan menulis test-nya **lebih dulu**.

**Kriteria selesai:** `uv run pytest` lulus dan semua kode lulus `ruff check` serta `ruff format --check`.

## Referensi

- [uv documentation](https://docs.astral.sh/uv/): panduan resmi uv, terutama bagian "Projects".
- [Ruff documentation](https://docs.astral.sh/ruff/): linter dan formatter.
- [pytest documentation](https://docs.pytest.org/): mulai dari "Get Started".
- [Modules (Python docs)](https://docs.python.org/3/tutorial/modules.html): module dan package.
- [Errors and Exceptions (Python docs)](https://docs.python.org/3/tutorial/errors.html): penanganan exception.
- [Logging HOWTO (Python docs)](https://docs.python.org/3/howto/logging.html): panduan modul `logging`.
