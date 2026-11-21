# Minggu 2: Fungsi & OOP

> **Fase 1: Python Fundamentals** · [⬅ Minggu 1](../week-01-syntax-idioms/) · [Kurikulum](../../README.md) · [Minggu 3 ➡](../week-03-tooling-testing/)

Minggu ini membahas cara Python mengorganisir kode: fungsi sebagai first-class object, decorator, class, dan type hints yang akan sering Anda pakai di library AI.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Menulis fungsi dengan default argument, keyword-only argument, `*args`, dan `**kwargs`.
- Menjelaskan closure dan scope (LEGB), serta jebakan mutable default argument.
- Membuat dan memakai decorator sederhana.
- Mendesain class dengan `__init__`, method, property, dan dunder method (`__repr__`, `__eq__`, dll.).
- Memilih antara class biasa, `@dataclass`, `NamedTuple`, dan `Enum`.
- Menulis type hints yang akurat, termasuk `list[str]`, `dict[str, int]`, `X | None`, `Callable`, dan `Protocol`.

## Topik

- Fungsi: parameter positional/keyword, default, `*args`/`**kwargs`, keyword-only (`*`)
- Lambda dan higher-order function; kapan comprehension lebih baik
- Scope, closure, `nonlocal`
- Decorator: fungsi pembungkus, `functools.wraps`, decorator dengan argumen
- Generator dan `yield`, iterator protocol
- Class: atribut instance vs class, `@property`, `@classmethod`, `@staticmethod`
- Dunder method dan data model Python
- Inheritance vs composition; `abc.ABC` dan `typing.Protocol` (duck typing ala interface TS)
- `@dataclass`, `Enum`, `NamedTuple`
- Type hints dan perbedaannya dengan TypeScript (hints tidak dicek saat runtime)

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Decorator `@timer` dan `@retry`.** Buat `@timer` untuk mencetak durasi eksekusi fungsi. Buat juga `@retry(times=3)` untuk mengulang fungsi yang melempar exception.
2. **Lazy pipeline.** Dengan generator, buat pipeline yang membaca file besar baris demi baris, memfilter baris kosong, lalu menghasilkan batch berisi N baris, tanpa memuat seluruh file ke memori.
3. **Inventory.** Modelkan `Product` (dataclass) dan `Inventory` (class) dengan method tambah, hapus, cari, dan total nilai stok. Implementasikan `__len__`, `__contains__`, dan `__repr__`.
4. **Protocol.** Definisikan `Protocol` bernama `Notifier` dengan method `send(message: str) -> None`, lalu buat dua implementasi (mis. console dan file) tanpa inheritance.
5. **Refactor typing.** Ambil satu latihan dari minggu 1 dan tambahkan type hints lengkap pada semua fungsinya.

**Kriteria selesai:** semua latihan memiliki type hints dan lulus `uv run ruff check .`.

## Referensi

- [Defining Functions (Python docs)](https://docs.python.org/3/tutorial/controlflow.html#defining-functions): fungsi dan jenis-jenis argumen.
- [Classes (Python docs)](https://docs.python.org/3/tutorial/classes.html): class, inheritance, iterator, dan generator.
- [dataclasses (Python docs)](https://docs.python.org/3/library/dataclasses.html): referensi `@dataclass`.
- [typing (Python docs)](https://docs.python.org/3/library/typing.html): referensi type hints, termasuk `Protocol`.
- [Data model (Python docs)](https://docs.python.org/3/reference/datamodel.html): daftar dunder method.
- <!-- TODO --> _Placeholder: artikel atau video tentang decorator (kontribusi diterima)._
