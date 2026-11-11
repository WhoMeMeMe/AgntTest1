# Cara memakai kit ini dengan Claude Code

Kit untuk Mas Hanief. Isinya mengajari Claude **polanya** (formula ZacD + alur kerja Tensaikun), supaya ia bisa menyiapkan skill sendiri dan memperbaiki diri dari catatan. Bahasa kerja Claude: **Inggris**. File ini saja yang disusun singkat dalam bahasa Indonesia.

**Legal:** salin formula dan alur, bukan klip, naskah, karakter, logo, atau watermark Tensaikun maupun Zack D. Films.

---

## Isi zip

| File | Fungsi |
|---|---|
| `CLAUDE.md` | Instruksi induk. Claude wajib membacanya di awal sesi. |
| `skills/style-guide.md` | Look channel (palet, kamera, caption — dalam angka). |
| `skills/script-writer.md` | Cara menulis naskah 75–95 kata. |
| `skills/shot-planner.md` | Shot list + format prompt Higgsfield. |
| `skills/review-checklist.md` | Review, catatan berulang, gerbang sebelum kredit. |
| `skills/thumbnail.md` | Judul, deskripsi, cover — tugas terpisah. |
| `LESSONS.md` | Log pelajaran (Claude menambah entri sendiri). |
| `known-mistakes.md` | Daftar kesalahan yang sudah jadi aturan. |

---

## Urutan pakai (sesi pertama)

1. Buka folder proyek di **Claude Code** (atau unggah/extract zip ini ke folder kerja).
2. Pastikan `CLAUDE.md` ada di akar proyek yang dibuka Claude, atau tempel isinya dan bilang: *Read CLAUDE.md and bootstrap the kit.*
3. Jangan tempel semua file sekaligus sebagai satu prompt panjang jika Claude Code sudah bisa membaca folder. Cukup arahkan: *Read CLAUDE.md, then the files in skills/, then LESSONS.md.*
4. Jika Anda **tidak** memakai Claude Code (hanya chat biasa):
   1. tempel `CLAUDE.md`
   2. tempel kelima file di `skills/`
   3. tempel `LESSONS.md` dan `known-mistakes.md`
   4. perintah: *Bootstrap. Confirm the rules. Propose a 20-second style test. Do not generate a full video yet.*
5. Biarkan Claude mengecek folder, skill yang hilang, dan alat (mis. FFmpeg). Ia diminta **tidak** langsung merender Short penuh.
6. Setujui **uji gaya 20 detik** (satu objek, start-frame dulu). Tonton, tulis catatan (boleh bahasa Indonesia).
7. Minta Claude: *Update the skill, log LESSONS.md, do not only fix the one frame.* Ulangi 3–4 kali sampai look terasa konsisten — ini nasihat Tensaikun yang kami pakai.
8. Baru berikan topik Short yang sesungguhnya. Ia harus jalan sesuai pipeline: naskah → (suara) → shot list → review start-frame → baru kredit gerak Higgsfield → rakit → thumbnail terpisah.

## Sesi-sesi berikutnya

- Mulai dengan: *New video. Read CLAUDE.md, skills, LESSONS.md, and known-mistakes.md first.*
- Satu sesi / satu video (aturan Tensaikun). Skill dan `LESSONS.md` yang membawa gaya ke sesi baru.
- Setiap kali Anda bilang “ini salah lagi,” pastikan Claude **menulis aturan ke skill**, bukan hanya mengganti satu klip.
- Thumbnail dan judul: tugas terpisah, setelah gambar kunci atau naskah kunci sudah ada.

## Yang tidak perlu Anda tiru

- Jangan minta Claude meniru Video Hub, film Hiroshima, atau merek lime Tensaikun.
- Jangan minta naskah / wajah / watermark Zack D. Films.
- Jangan biarkan Claude menekan “langsung buat video” tanpa naskah dan review.

Dokumen sumber (jika masih ada di mesin): `DNA_ZacD_FINAL.md` dan `Analisa_x6ZjVTK8aI.md`. Kit ini sudah memuat aturan yang dipakai; file sumber bersifat cadangan, bukan wajib diunggah setiap sesi.
