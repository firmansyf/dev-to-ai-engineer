# Minggu 1: Sintaks & Idiom Python

> **Fase 1: Python Fundamentals** · [Kurikulum](../../README.md) · [Minggu 2 ➡](../week-02-functions-oop/)

Minggu ini Anda "menerjemahkan" pengetahuan JS/TS ke Python dan mulai menulis kode yang terasa *Pythonic*, bukan sekadar JavaScript dengan sintaks Python.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Menjalankan script Python dengan `uv run` dan memakai REPL untuk eksperimen.
- Menjelaskan perbedaan utama Python dan JS/TS: indentasi, truthiness, `None` vs `null`/`undefined`, `==` vs `is`, mutability.
- Memakai tipe data bawaan (`str`, `int`, `float`, `bool`, `list`, `tuple`, `dict`, `set`) beserta method umumnya.
- Menulis list/dict/set comprehension dan memakai unpacking.
- Memakai idiom umum seperti `enumerate`, `zip`, f-string, slicing, dan `with`.

## Topik

- Setup: `uv run`, REPL, struktur script, `if __name__ == "__main__":`
- Variabel, tipe data dasar, dan dynamic typing (dibandingkan dengan TypeScript)
- String: f-string, method string, slicing
- Collection: `list`, `tuple`, `dict`, `set`, beserta kapan memakai masing-masing
- Control flow: `if`/`elif`/`else`, `for`, `while`, `match` (structural pattern matching)
- Truthiness, `None`, `is` vs `==`
- Comprehension: list, dict, set, dan generator expression
- Unpacking: tuple unpacking, `*rest`, swap variabel
- Idiom: `enumerate`, `zip`, `sorted` dengan `key`, `any`/`all`, `in`
- File I/O dasar dan context manager (`with open(...)`)

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **JS → Python.** Terjemahkan 5 snippet JavaScript yang memakai `map`, `filter`, `reduce`, destructuring, dan template literal menjadi Python idiomatik (pakai comprehension dan unpacking, bukan `map`/`lambda`).
2. **Word counter.** Baca sebuah file teks, hitung frekuensi tiap kata (abaikan kapitalisasi dan tanda baca), lalu tampilkan 10 kata teratas.
3. **Grouping.** Diberikan list of dict berisi data transaksi (`name`, `category`, `amount`), kelompokkan total `amount` per `category` dan urutkan dari yang terbesar.
4. **Matrix tools.** Tanpa library tambahan, tulis fungsi transpose dan flatten untuk list of list memakai comprehension dan `zip`.
5. **Pattern matching.** Tulis fungsi yang menerima "command" berbentuk tuple/dict (mis. `("move", x, y)`, `{"action": "quit"}`) dan memprosesnya dengan `match`.

**Kriteria selesai:** semua script berjalan, `uv run ruff check .` lulus, dan Anda bisa menjelaskan 5 perbedaan utama Python dan JS.

## Referensi

- [The Python Tutorial](https://docs.python.org/3/tutorial/): tutorial resmi, baca bab 3–5 dan 7.
- [Data Structures (Python docs)](https://docs.python.org/3/tutorial/datastructures.html): list, tuple, dict, set, dan comprehension.
- [PEP 8: Style Guide for Python Code](https://peps.python.org/pep-0008/): konvensi penulisan kode Python.
- [PEP 636: Structural Pattern Matching Tutorial](https://peps.python.org/pep-0636/): tutorial `match`.
- <!-- TODO: tambahkan referensi "Python untuk developer JavaScript" yang terverifikasi --> _Placeholder: panduan Python untuk developer JS/TS (kontribusi diterima)._
