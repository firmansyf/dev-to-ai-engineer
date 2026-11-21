# Minggu 8: Neural Network

> **Fase 2: Data & ML Foundations** · [⬅ Minggu 7](../week-07-classical-ml/) · [Kurikulum](../../README.md) · [Minggu 9 ➡](../../03-llm-engineering/week-09-llm-apis-prompting/)

LLM adalah neural network yang sangat besar. Minggu ini Anda membangun dan melatih neural network kecil dengan PyTorch agar memahami apa yang terjadi di balik layar, termasuk istilah seperti parameter, loss, epoch, dan inference.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Memakai tensor PyTorch dan menjelaskan hubungannya dengan array NumPy.
- Menjelaskan cara kerja autograd dan backpropagation secara intuitif.
- Menulis training loop lengkap: forward, loss, backward, dan optimizer step.
- Memakai `Dataset` dan `DataLoader`, serta menyimpan dan memuat model.
- Menjelaskan konsep tingkat tinggi transformer dan attention, sebagai jembatan ke LLM.

## Topik

- Tensor, device (CPU/GPU), dan autograd
- `nn.Module`, layer, dan activation function
- Loss function dan optimizer (SGD, Adam)
- Training loop, batch, epoch, serta evaluasi dengan `model.eval()` dan `torch.no_grad()`
- `Dataset` dan `DataLoader`
- Menyimpan dan memuat model (`state_dict`)
- Gambaran umum: tokenization, embedding layer, attention, transformer
- Pretrained model dan transfer learning (konsep)

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Autograd.** Ulangi gradient descent dari minggu 6 dengan PyTorch autograd, lalu bandingkan dengan versi NumPy.
2. **MLP pertama.** Latih multilayer perceptron untuk klasifikasi gambar sederhana (mis. digit tulisan tangan). Plot kurva loss train dan validation.
3. **Eksperimen.** Ubah satu hal setiap kali (jumlah layer, learning rate, batch size) dan catat dampaknya.
4. **Tokenizer.** Pakai tokenizer dari model pretrained untuk men-tokenize beberapa kalimat bahasa Indonesia dan Inggris. Bandingkan jumlah token yang dihasilkan.

## 🏁 Milestone 2: Model ML end-to-end

Bangun pipeline ML lengkap untuk satu problem pilihan Anda (klasifikasi teks, prediksi harga, dll.).

**Persyaratan minimum:**

- Eksplorasi dan pembersihan data (dari minggu 5), dengan kode cleaning yang di-test.
- Baseline dan minimal dua model untuk dibandingkan (ML klasik dan/atau neural network).
- Evaluasi dengan metrik yang tepat pada test set yang tidak dipakai saat training.
- Model terbaik disimpan ke file dan bisa dipakai untuk inference lewat script atau **endpoint FastAPI** (menggunakan ulang materi Milestone 1).
- README berisi problem, data, hasil eksperimen (tabel), kesimpulan, dan keterbatasan model.

## Referensi

- [PyTorch: Learn the Basics](https://pytorch.org/tutorials/beginner/basics/intro.html): tutorial resmi dasar PyTorch.
- [PyTorch documentation](https://pytorch.org/docs/stable/index.html): referensi API.
- [Neural networks (3Blue1Brown)](https://www.3blue1brown.com/topics/neural-networks): termasuk penjelasan visual transformer dan attention.
- <!-- TODO --> _Placeholder: artikel penjelasan transformer untuk pemula (kontribusi diterima)._
