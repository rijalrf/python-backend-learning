username = "rijal"
umur = 25
saldo_awal = 14500.10
is_active = True


if is_active:
    if saldo_awal > 0 and saldo_awal < 20000:
        print(f"halo {username}, saldo anda tinggal Rp {saldo_awal:.2f}, segera isi ulang!")
    else:
        print(f"halo {username}, saldo aman: Rp {saldo_awal:.2f}.")
else:
    print(f"akun {username} sedang di bebukan. Hubungi CS.")