from conn import connect

def update_pemesanan(doc_id):
    db = connect()

    pemesanan = db[doc_id]

    film = input("Masukkan judul film baru: ")
    jumlah_tiket = int(input("Masukkan jumlah tiket baru: "))
    nama_pengunjung = input("Masukkan nama pengunjung baru: ")

    pemesanan['film'] = film
    pemesanan['jumlah_tiket'] = jumlah_tiket
    pemesanan['nama_pengunjung'] = nama_pengunjung

    db.save(pemesanan)

    print(f"Pemesanan berhasil diperbarui! ID Pemesanan: {doc_id}")