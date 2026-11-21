# Minggu 15: Deployment

> **Fase 4: Production AI** · [⬅ Minggu 14](../week-14-observability-guardrails/) · [Kurikulum](../../README.md) · [Minggu 16 ➡](../week-16-capstone/)

Aplikasi baru bernilai jika bisa dipakai orang lain. Minggu ini Anda mengemas aplikasi AI dalam container, mengelola konfigurasi dan secret, serta men-deploy-nya dengan CI/CD. Sebagai developer, banyak hal di sini sudah familier. Fokuslah pada hal yang khas aplikasi AI.

## Tujuan belajar

Setelah minggu ini, Anda dapat:

- Membuat Dockerfile yang efisien untuk aplikasi Python berbasis uv.
- Mengelola konfigurasi dan secret dengan aman di setiap environment.
- Men-deploy API ke platform cloud dan menyiapkan health check.
- Menangani karakteristik khas aplikasi AI: request yang lama, streaming, rate limit penyedia, dan timeout.
- Menyiapkan pipeline CI/CD yang menjalankan lint, test, dan eval sebelum deploy.

## Topik

- Docker: multi-stage build, image Python yang ramping, uv di dalam container, `.dockerignore`
- Docker Compose untuk development lokal (API + vector database)
- Konfigurasi: 12-factor app, environment variable, secret manager
- Pilihan platform deployment (PaaS, container service, serverless) dan trade-off-nya
- Server: uvicorn dan worker, concurrency untuk workload async
- Streaming lewat SSE di production, timeout di proxy atau load balancer
- Rate limiting, antrean (queue) untuk tugas panjang, dan background job
- Caching respons dan embedding
- CI/CD dengan GitHub Actions: lint → test → eval → build → deploy
- Model lokal vs API (gambaran umum self-hosting)

## Latihan

Kerjakan di folder `exercises/`. Repo ini tidak menyertakan solusi resmi.

1. **Dockerize.** Buat Dockerfile multi-stage untuk aplikasi Milestone 3. Bandingkan ukuran image sebelum dan sesudah optimasi.
2. **Compose.** Buat `compose.yaml` yang menjalankan API beserta vector database secara lokal dengan satu perintah.
3. **Deploy.** Deploy API ke platform pilihan Anda, lengkap dengan health check endpoint dan secret yang dikelola platform (bukan di image).
4. **Rate limit & cache.** Tambahkan rate limiting per pengguna/IP dan cache untuk query yang identik. Ukur dampaknya pada biaya dan latensi.
5. **Pipeline.** Perluas workflow CI agar menjalankan eval (subset kecil) dan build image di setiap PR.

**Kriteria selesai:** aplikasi bisa diakses publik, dan deploy ulang cukup dengan merge ke `main`.

## Referensi

- [Docker: Get started](https://docs.docker.com/get-started/): dasar Docker resmi.
- [uv: Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/): panduan resmi uv untuk Docker.
- [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/): deploy FastAPI dengan Docker.
- [GitHub Actions documentation](https://docs.github.com/en/actions): CI/CD.
- [The Twelve-Factor App](https://12factor.net/): prinsip aplikasi cloud-native.
