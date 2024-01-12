from conn import connect

def lihat_pemesanan():
    db = connect()
    result = db.view('_all_docs', include_docs=True)
    pemesanan_list = [row['doc'] for row in result.rows]

    print("Daftar Pemesanan Tiket:")
    for pemesanan in pemesanan_list:
        print(f"ID: {pemesanan['_id']}, Film: {pemesanan['film']}, Jumlah Tiket: {pemesanan['jumlah_tiket']}, Nama Pengunjung: {pemesanan['nama_pengunjung']}")