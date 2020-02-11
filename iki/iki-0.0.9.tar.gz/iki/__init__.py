s = """The Zen of Python, dening Tim Peters

Ayu luwih becik tinimbang elek.
Eksplisit luwih becik tinimbang implisit.
Prasaja luwih becik tinimbang kompleks.
Komplek luwih becik tinimbang rumit.
Rata luwih becik tinimbang narang.
Arang-arang luwih becik tinimbang padet.
Kewaca kuwi penting.
Kasus khusus ora cukup khusus kanggo nglanggar aturan kasebut.
Sanajan kepraktisan ngalahake kemurnian.
Salah ojo nganti dimenengke wae.
Kajaba pancen dikon meneng.
Menawa bingung, tolak godaan nggo ngira-ira.
Kudune ono siji-- lan yen isa gur siji -- cara cetho sing bisa dilakoni.
Sanajan cara kasebut isa ora cetho nalika wiwitan kajaba sampeyan Walanda.
Saiki luwih apik tinimbang ora nate.
Sanajan ora nate luwih apik tinimbang saiki *banget*.
Yen implementasine angel dijelasake, kuwi ide sing ala.
Yen implementasine gampang diterangake, kuwi isa dadi ide sing apik.
Namespaces minangka salah sawijining ide sing apik banget - ayo padha nindakake!

Dijarwakake dening Ismail Sunni."""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

# print("".join([d.get(c, c) for c in s]))
print(s)
