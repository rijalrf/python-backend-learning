def cek_masuk(nama, umur, bawa_ktp):
    if umur < 18 :
        return f"maaf {nama}, kamu belum cukup umur"
    elif umur >= 18 and not bawa_ktp:
        return f"maaf {nama}, wajib tunjukan ktp"
    else:
        return f"silahkan masuk, {nama}. selamat menonton!"
    
hasil1 = cek_masuk("rijal", 18, False)
print(hasil1)