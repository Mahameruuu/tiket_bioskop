from conn import connect

def pesan_tiket():
    db = connect()

    film = input("Masukkan judul film: ")
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))
    nama_pengunjung = input("Masukkan nama pengunjung: ")

    pemesanan = {
        'film': film,
        'jumlah_tiket': jumlah_tiket,
        'nama_pengunjung': nama_pengunjung
    }

    doc_id, doc_rev = db.save(pemesanan)

    print(f"Tiket berhasil dipesan! ID Pemesanan: {doc_id}")
