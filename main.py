from create_tiket import pesan_tiket
from read_tiket import lihat_pemesanan
from update_tiket import update_pemesanan
from delete_tiket import hapus_pemesanan


print("Menu:")
print("1. Pesan Tiket")
print("2. Lihat Pemesanan")
print("3. Update Pemesanan")
print("4. Hapus Pemesanan")

pilihan = input("Masukkan nomor opsi yang dipilih: ")

if pilihan == '1':
    pesan_tiket()
elif pilihan == '2':
    lihat_pemesanan()
elif pilihan == '3':
    doc_id_to_update = input("Masukkan Nama Pemesanan yang ingin diperbarui: ")
    update_pemesanan(doc_id_to_update)
    lihat_pemesanan()
elif pilihan == '4':
    doc_id_to_delete = input("Masukkan ID Pemesanan yang ingin dihapus: ")
    hapus_pemesanan(doc_id_to_delete)
    lihat_pemesanan()
else:
    print("Opsi tidak valid. Program berakhir.")
