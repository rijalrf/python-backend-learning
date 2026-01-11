def hitung_diskon_otomatis(total_belanja, is_member):
    if not is_member:
        return f"User membayar Rp {total_belanja:.2f}"
    else:
        if total_belanja > 500000:
            diskon = total_belanja * (20 / 100)
            return f"User membayar Rp {total_belanja - diskon:.2f}"
        elif total_belanja > 100000 and total_belanja < 500000:
            diskon = total_belanja * (10 / 100)
            return f"User membayar Rp {total_belanja - diskon:.2f}"
        else:
            diskon = total_belanja * (0 / 100)
            return f"User membayar Rp {total_belanja - diskon:.2f}"
        


hitung1 = hitung_diskon_otomatis(100000, True)
hitung2 = hitung_diskon_otomatis(650000, False)
hitung3 = hitung_diskon_otomatis(900000, True)
        
print(hitung1)
print(hitung2)
print(hitung3)