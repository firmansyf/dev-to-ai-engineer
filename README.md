# dev-to-ai-engineer

Kurikulum 16 minggu untuk **software developer berlatar belakang JavaScript/TypeScript** yang ingin beralih menjadi **AI Engineer** dengan Python.

Repo ini saya ikuti sendiri secara terbuka. Silakan ikut belajar, pakai sebagai referensi, atau berkontribusi.

## Untuk siapa repo ini?

Repo ini cocok untuk Anda jika:

- Sudah nyaman membangun aplikasi dengan JS/TS (frontend, backend, atau full-stack).
- Paham dasar Git, terminal, HTTP/REST, dan testing.
- Belum (atau baru sedikit) menulis Python, dan belum punya latar belakang machine learning.
- Ingin fokus membangun **aplikasi AI yang bisa dipakai**, bukan riset model dari nol.

Repo ini **bukan** kursus data science atau riset ML yang mendalam. Matematika dan ML klasik dibahas secukupnya agar Anda paham apa yang terjadi di balik LLM dan embedding.

## Setelah 16 minggu, Anda bisa…

- Menulis Python yang idiomatik, ter-type, dan teruji, dengan tooling modern (uv, ruff, pytest).
- Membangun API dengan FastAPI dan Pydantic.
- Mengolah data dengan NumPy/pandas serta melatih dan mengevaluasi model sederhana (scikit-learn, PyTorch).
- Membangun aplikasi berbasis LLM: prompting, structured output, embedding, vector search, RAG, tool use, dan agent.
- Mengevaluasi, memantau, dan men-deploy aplikasi AI ke production.
- Menunjukkan **4 project milestone** sebagai portofolio.

## Ringkasan kurikulum

| Minggu | Topik | Konsep utama | Milestone |
|:---:|---|---|---|
| **Fase 1: Python Fundamentals** | | | |
| 1 | [Sintaks & idiom Python](01-python-fundamentals/week-01-syntax-idioms/) | Tipe data, comprehension, unpacking, perbedaan dengan JS | |
| 2 | [Fungsi & OOP](01-python-fundamentals/week-02-functions-oop/) | `*args`/`**kwargs`, decorator, class, dataclass, type hints | |
| 3 | [Tooling & testing](01-python-fundamentals/week-03-tooling-testing/) | uv, ruff, pytest, module/package, exception | |
| 4 | [Async & API](01-python-fundamentals/week-04-async-apis/) | async/await, httpx, FastAPI, Pydantic | 🏁 **M1:** REST API ter-test |
| **Fase 2: Data & ML Foundations** | | | |
| 5 | [NumPy & pandas](02-data-ml-foundations/week-05-numpy-pandas/) | Array, vectorization, DataFrame, data cleaning | |
| 6 | [Matematika untuk ML](02-data-ml-foundations/week-06-math-for-ml/) | Vektor, matriks, dot product, probabilitas, gradient | |
| 7 | [ML klasik](02-data-ml-foundations/week-07-classical-ml/) | scikit-learn, train/test split, overfitting, metrik | |
| 8 | [Neural network](02-data-ml-foundations/week-08-neural-networks/) | Tensor, autograd, training loop dengan PyTorch | 🏁 **M2:** model ML end-to-end |
| **Fase 3: LLM Engineering** | | | |
| 9 | [LLM API & prompting](03-llm-engineering/week-09-llm-apis-prompting/) | Token, context window, prompting, structured output, streaming | |
| 10 | [Embedding & vector search](03-llm-engineering/week-10-embeddings-vector-search/) | Embedding, cosine similarity, vector database | |
| 11 | [RAG](03-llm-engineering/week-11-rag/) | Chunking, retrieval, reranking, grounding, sitasi | |
| 12 | [Tool use & agent](03-llm-engineering/week-12-tool-use-agents/) | Tool calling, agent loop, MCP | 🏁 **M3:** asisten RAG dengan tool use |
| **Fase 4: Production AI** | | | |
| 13 | [Evaluasi](04-production-ai/week-13-evaluation/) | Eval dataset, metrik, LLM-as-judge, regression test | |
| 14 | [Observability & guardrails](04-production-ai/week-14-observability-guardrails/) | Logging/tracing, biaya & latensi, prompt injection | |
| 15 | [Deployment](04-production-ai/week-15-deployment/) | Docker, konfigurasi, caching, rate limiting, CI/CD | |
| 16 | [Capstone](04-production-ai/week-16-capstone/) | Integrasi semua materi | 🏁 **M4:** aplikasi AI di production |

## Cara memakai repo ini

### 1. Setup

Prasyarat: [Git](https://git-scm.com/) dan [uv](https://docs.astral.sh/uv/). uv akan mengunduh Python 3.12 secara otomatis jika belum ada.

```bash
# Fork repo ini dulu, lalu clone fork Anda
git clone https://github.com/<username-anda>/dev-to-ai-engineer.git
cd dev-to-ai-engineer

# Install Python + semua dependency (termasuk dev: ruff, pytest)
uv sync

# Salin template environment variable (diisi mulai minggu 9)
cp .env.example .env
```

Perintah sehari-hari:

```bash
uv run python path/to/script.py   # menjalankan script
uv run pytest                     # menjalankan test
uv run ruff check .               # lint
uv run ruff format .              # format kode
uv add <package>                  # menambah dependency
```

> 💡 **Untuk dev JS/TS:** `uv` kira-kira setara `npm`/`pnpm`, `pyproject.toml` setara `package.json`, `uv.lock` setara `package-lock.json`, dan `.venv/` setara `node_modules/`.

### 2. Alur belajar per minggu

1. Buka `README.md` di folder minggu tersebut, lalu baca **tujuan belajar** dan **topik**.
2. Pelajari materi dari bagian **referensi**.
3. Kerjakan **latihan** di folder minggu tersebut (misalnya `exercises/`). Repo ini sengaja tidak menyertakan solusi resmi; tulis test Anda sendiri.
4. Pastikan `uv run ruff check .` dan `uv run pytest` lulus.
5. Commit hasil Anda, lalu centang progress di bawah.
6. Di minggu milestone, bangun project-nya dan tulis catatan singkat tentang apa yang Anda pelajari.

Ritme yang disarankan: **±10–15 jam per minggu**. Tidak apa-apa lebih lambat. Yang penting konsisten.

## Progress

Fork repo ini dan centang sesuai kemajuan Anda.

- [ ] Minggu 1: Sintaks & idiom Python
- [ ] Minggu 2: Fungsi & OOP
- [ ] Minggu 3: Tooling & testing
- [ ] Minggu 4: Async & API (🏁 M1)
- [ ] Minggu 5: NumPy & pandas
- [ ] Minggu 6: Matematika untuk ML
- [ ] Minggu 7: ML klasik
- [ ] Minggu 8: Neural network (🏁 M2)
- [ ] Minggu 9: LLM API & prompting
- [ ] Minggu 10: Embedding & vector search
- [ ] Minggu 11: RAG
- [ ] Minggu 12: Tool use & agent (🏁 M3)
- [ ] Minggu 13: Evaluasi
- [ ] Minggu 14: Observability & guardrails
- [ ] Minggu 15: Deployment
- [ ] Minggu 16: Capstone (🏁 M4)

## Showcase

Sudah menyelesaikan capstone? Tambahkan project Anda di sini lewat PR.

| Project | Pembuat | Deskripsi singkat |
|---|---|---|
| _Belum ada, jadilah yang pertama!_ | | |

## Berkontribusi

Kontribusi sangat diterima: latihan baru, solusi alternatif, referensi, terjemahan, dan perbaikan. Baca [CONTRIBUTING.md](CONTRIBUTING.md) dan [Kode Etik](CODE_OF_CONDUCT.md) sebelum mulai.

## Lisensi

- **Kode** (semua file `.py`, konfigurasi, dan workflow) dilisensikan di bawah [MIT](LICENSE).
- **Materi tulisan** (file Markdown seperti README, deskripsi latihan, dan catatan) dilisensikan di bawah [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Anda bebas membagikan dan mengadaptasinya, termasuk untuk keperluan komersial, selama mencantumkan atribusi ke repo ini.
