quduqChuqurligi = float(input("Quduq chuqurligini kiriting: "))
kunlikKotarilish = float(input("Baqani kunlik ko'tarilish balandligini kiriting: "))
kechasiSirganish = float(input("Baqani kechasi sirg'anishini kiriting: "))
kun=0
if kunlikKotarilish>kechasiSirganish:
    while quduqChuqurligi>0:
        quduqChuqurligi-=kunlikKotarilish
        if quduqChuqurligi<=0:
            quduqChuqurligi
        else:
            quduqChuqurligi+=kechasiSirganish
        kun+=1
    print(f"Qurbaqa {kun}-kuni quduqdan chiqib ketadi!")
else:
    print("Qurbaqa bu holatda quduqdan hech qachon chiqa olmaydi!!!")
