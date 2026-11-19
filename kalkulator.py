# kalkulator.py — Kalkulator CLI (+, -, x, /) dengan penanganan bagi-nol.


def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        return None  # penanda: tidak bisa dibagi nol
    return a / b


OPERASI = {"+": tambah, "-": kurang, "*": kali, "x": kali, "/": bagi}


def hitung(a, op, b):
    """Hitung satu operasi; kembalikan string hasil atau pesan error."""
    fungsi = OPERASI.get(op)
    if fungsi is None:
        return f"Error: operator '{op}' tidak dikenal (pakai + - * /)."
    hasil = fungsi(a, b)
    if hasil is None:
        return "Error: tidak bisa membagi dengan nol."
    return f"{a} {op} {b} = {hasil}"


def main():
    print("=== KALKULATOR CLI ===")
    print("Ketik: angka operator angka (contoh: 12 + 5). 'keluar' untuk berhenti.")
    while True:
        baris = input("> ").strip()
        if baris.lower() in ("keluar", "exit", "q"):
            print("Sampai jumpa!")
            break
        bagian = baris.split()
        if len(bagian) != 3:
            print("Format salah. Contoh yang benar: 12 + 5")
            continue
        try:
            a = float(bagian[0])
            b = float(bagian[2])
        except ValueError:
            print("Itu bukan angka yang valid.")
            continue
        print(hitung(a, bagian[1], b))


if __name__ == "__main__":
    main()
