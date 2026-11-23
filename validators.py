def validasi_jumlah(jumlah):
    if not isinstance(jumlah, int) or jumlah <= 0:
        raise ValueError("Jumlah harus bilangan bulat lebih dari 0")
    return jumlah


def validasi_harga(harga):
    if not isinstance(harga, (int, float)) or harga < 0:
        raise ValueError("Harga tidak boleh negatif")
    return harga
