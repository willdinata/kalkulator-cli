# Kalkulator CLI — Repo GitHub Pertamaku

Program kalkulator baris perintah dari modul Python jalur Fondasi:
menjumlah, mengurang, mengali, dan membagi, dengan penanganan
bagi-dengan-nol yang aman (program tidak crash).

## Cara menjalankan

```bash
python3 kalkulator.py
```

Lalu ketik operasi dengan format `angka operator angka`, contoh:

```
> 12 + 5
12.0 + 5.0 = 17.0
> 10 / 0
Error: tidak bisa membagi dengan nol.
> keluar
```

## Struktur

- `kalkulator.py` — seluruh program (fungsi per operasi + loop CLI).
- `PULL_REQUEST.md` — draf pull request untuk perubahan di branch
  `perbaikan-readme`.
