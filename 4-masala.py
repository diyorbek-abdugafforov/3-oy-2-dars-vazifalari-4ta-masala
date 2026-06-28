aholi = int(input("Shahar aholisining sonini kiriting: "))
tishlash = int(input("1 ta Zombi 1 kunda nechta odamni tishlashini kiriting: "))
kun=0
zombi=1
print(f"{kun} kuni {zombi} ta zombi")
while zombi<aholi:
    zombi=zombi+zombi*tishlash
    kun+=1  
    print(f"{kun} - kuni {zombi} ta zombi ")
print(f"Shahar aholisi {kun} kunda zombiga aylanadi!!!")   
    