s = """Zen tentang Python, oleh Tim Peters

Yang elok lebih baik daripada yang buruk.
Yang eksplisit lebih baik daripada yang implisit.
Yang sederhana lebih baik daripada yang kompleks.
Yang kompleks lebih baik daripada yang rumit.
Yang merata lebih baik daripada yang bersarang.
Yang renggang lebih baik daripada yang padat.
Kemudahan Pembacaan penting.
Kasus khusus tidak cukup istimewa untuk melanggar aturan.
Walaupun kepraktisan lebih penting daripada kemurnian.
Kesalahan tidak boleh dilewatkan diam-diam.
Kecuali didiamkan dengan gamblang.
Jika dihadapkan dengan hal yang ambigu, tolak lah godaan untuk menebak.
Hanya boleh ada satu -- dan kalau bisa satu saja -- cara yang jelas untuk melakukan sesuatu.
Walaupun bisa saja cara tersebut tidak jelas pada awalnya, kecuali anda orang Belanda.
Sekarang lebih baik daripada tidak pernah sama sekali.
Meskipun tidak pernah sama sekali seringkali lebih baik daripada *sekarang*.
Jika implementasinya sulit dijelaskan, maka gagasan tersebut buruk.
Jika implementasinya mudah dijelaskan, maka gagasan tersebut mungkin saja baik.
"Namespace" adalah ide yang sangat baik sekali -- mari gunakan fitur ini lebih dan lebih lagi!

Diterjemahkan oleh Alex Xandra Albert Sim."""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

# print("".join([d.get(c, c) for c in s]))
print(s)
