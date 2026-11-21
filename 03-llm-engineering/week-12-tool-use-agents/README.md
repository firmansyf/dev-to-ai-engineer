# Minggu 12: Tool Use & Agent

> **Fase 3: LLM Engineering** · [⬅ Minggu 11](../week-11-rag/) · [Kurikulum](../../README.md) · [Minggu 13 ➡](../../04-production-ai/week-13-evaluation/)

Dengan tool use, LLM tidak hanya menghasilkan teks tetapi juga bisa **mengambil tindakan**: memanggil fungsi, API, atau database. Agent adalah loop yang membiarkan LLM memilih tool secara berulang sampai tugasnya selesai.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Mendefinisikan tool dengan JSON Schema dan menangani tool call dari LLM.
- Mengimplementasikan agent loop sederhana dari nol.
- Mendesain tool yang baik: nama dan deskripsi yang jelas, input tervalidasi, serta error yang informatif.
- Menjelaskan Model Context Protocol (MCP) dan membuat MCP server sederhana.
- Mengidentifikasi risiko agent (aksi berbahaya, loop tanpa akhir, biaya) dan cara membatasinya.

## Topik

- Tool/function calling: skema, eksekusi, dan mengembalikan hasil ke model
- Agent loop: observe → think → act, kondisi berhenti, batas iterasi
- Desain tool dan validasi input dengan Pydantic
- Menjadikan RAG sebagai tool (retrieval sebagai salah satu aksi agent)
- Memory: riwayat percakapan, ringkasan, dan pengelolaan context window
- Model Context Protocol (MCP): konsep server/client, tool, dan resource
- Workflow vs agent: kapan alur deterministik lebih baik
- Keamanan: konfirmasi untuk aksi berisiko, sandboxing, dan prinsip least privilege

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Tool pertama.** Beri LLM tool kalkulator dan tool "waktu sekarang". Tangani satu maupun beberapa tool call dalam satu respons.
2. **Agent loop dari nol.** Implementasikan agent loop dengan batas iterasi, logging setiap langkah, dan penanganan error tool.
3. **MCP server.** Buat MCP server sederhana yang mengekspos 2–3 tool (mis. membaca catatan dari API Milestone 1), lalu uji dengan MCP client.
4. **Workflow vs agent.** Selesaikan satu tugas multi-langkah dengan dua cara: workflow deterministik dan agent. Bandingkan keandalan, biaya, dan latensinya.

## 🏁 Milestone 3: Asisten RAG dengan tool use

Bangun asisten berbasis LLM yang bisa menjawab pertanyaan dari dokumen **dan** mengambil tindakan.

**Persyaratan minimum:**

- Pipeline RAG (ingestion + query) atas sekumpulan dokumen nyata, dengan sitasi sumber.
- Minimal 2 tool selain retrieval (mis. mencari data via API, membuat catatan, menghitung sesuatu).
- Agent loop dengan batas iterasi dan logging setiap langkah.
- Diakses lewat API (FastAPI) atau CLI, dengan streaming.
- Set pertanyaan uji (minimal 15) beserta jawaban yang diharapkan.
- Test untuk logika non-LLM (chunking, tool, parsing) dengan LLM di-mock.
- README berisi arsitektur (diagram sederhana), cara menjalankan, keterbatasan, dan perkiraan biaya per query.

## Referensi

- [Model Context Protocol](https://modelcontextprotocol.io/): dokumentasi resmi MCP.
- [JSON Schema](https://json-schema.org/): dasar JSON Schema untuk mendefinisikan tool.
- <!-- TODO --> _Placeholder: dokumentasi tool use dari penyedia LLM pilihan Anda._
- <!-- TODO --> _Placeholder: artikel tentang pola desain agent (kontribusi diterima)._
