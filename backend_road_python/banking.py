def cek_status_keuangan(username, saldo_awal, is_active):
    if not is_active:
        return f"DITOLAK: Akun {username} sedang di bekukan."
    if saldo_awal > 0 and saldo_awal < 20000:
        return f"WARNING: Halo {username}, saldo kritis: Rp {saldo_awal:.2f}"
    return f"SUCCESS: Halo {username}, saldo aman: Rp {saldo_awal:.2f}"


pesan1 = cek_status_keuangan("rijal", 150000, True)
pesan2 = cek_status_keuangan("budi", 1000, True)
pesan3 = cek_status_keuangan("udin", 99999, False)

print(pesan1)
print(pesan2)
print(pesan3)