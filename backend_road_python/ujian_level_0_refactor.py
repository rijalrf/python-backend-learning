def hitung_diskon_otomatis(total_belanja, is_member):
    if not is_member:
        return f"User membayar Rp {total_belanja:.2f}"

    diskon_persen = 0
    
    if total_belanja >= 500000:
        diskon_persen = 0.20
    elif total_belanja >= 100000:
        diskon_persen = 0.10

    potongan = total_belanja * diskon_persen
    total_bayar = total_belanja - potongan

    return f"User membayar Rp {total_bayar:.2f}"


hitung1 = hitung_diskon_otomatis(100000, True)
hitung2 = hitung_diskon_otomatis(650000, False)
hitung3 = hitung_diskon_otomatis(900000, True)
        
print(hitung1)
print(hitung2)
print(hitung3)