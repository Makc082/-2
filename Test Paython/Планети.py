# mk - меркурій , vn - венера , er - земля , mr - марс , jp -  юпітер , st - сатурн , ur - уран , nt -  нептун .
mk = 0.055
vn = 0.815
er = 1.00
mr = 0.107
jp = 317.83
st = 95.16
ur = 14.54
nt = 17.15
m = (mk + vn + er + mr + jp + st + ur + nt)
sa = (m / 8)
mk1 = round(mk / m * 100, 3)
vn1 = round(vn / m * 100, 3)
er1 = round(er / m * 100, 3)
mr1 = round(mr / m * 100, 3)
jp1 = round(jp / m * 100, 3)
st1 = round(st / m * 100, 3)
ur1 = round(ur / m * 100, 3)
nt1 = round(nt / m * 100, 3)
x = (m - jp)
R = round(jp / x, 3)
print("Загальна маса планет: " , m)
print("Середнє арефметичне: " , sa)
print("Меркурій %: " , mk1)
print("Венера %: " , vn1)
print("Земля %: " , er1)
print("Марс %: " , mr1)
print("Юпітер %: " , jp1)
print("Сатурн %: " , st1)
print("Уран %: " , ur1)
print("Нептун %: " , nt1)
print("В скільки Юп більш ніж всі інши: " , R)