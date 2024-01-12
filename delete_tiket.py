from conn import connect

def hapus_pemesanan(doc_id):
    db = connect()

    db.delete(db[doc_id])

    print(f"Pemesanan dengan ID {doc_id} berhasil dihapus.")