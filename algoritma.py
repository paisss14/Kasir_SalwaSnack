def linear_search(data, kata, *fields):
    kata = kata.lower()
    hasil = []
    for item in data:
        for f in fields:
            if kata in str(item.get(f, "")).lower():
                hasil.append(item)
                break
    return hasil


def merge_sort(data, key=lambda x: x, reverse=False):
    if len(data) <= 1:
        return list(data)
    tengah = len(data) // 2
    kiri = merge_sort(data[:tengah], key, reverse)
    kanan = merge_sort(data[tengah:], key, reverse)

    hasil = []
    i = j = 0
    while i < len(kiri) and j < len(kanan):
        a, b = key(kiri[i]), key(kanan[j])
        if (a >= b) if reverse else (a <= b):
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1
    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    return hasil