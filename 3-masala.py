balandlik=100 # o'zim uchun 1000 o'rniga 100 qilib oldim ustoz
tortishish=0

# Kemani muvaffaqqiyatli qo'ndirish uchun qo'llanma :
# 1-marta: 0
# 2-marta: 0
# 3-marta: 0
# 4-marta: 33
# 5-marta: 11
# 6-marta: 12
# 7-marta: 12
# 8-marta: 11
# 9-marta: 10
# bundan keyingi qadamlarga faqat 10 kiritib ketish kerak!!!

while balandlik>0:
    qarshilik = int(input("Qarshilik tezlgini kiriting: "))
    tortishish+=10-qarshilik
    balandlik-=tortishish
    print(tortishish)
    print(balandlik)
if(tortishish>5):
    print("Kema halokatga uchradi!!!")
else:
    print("Kema muvaffaqqiyatli qo'ndi!!!")