hamyonPuli = float(input("Hamyonda qancha pul borligini kiriting: "))
avans = float(input("Hamyondan har safar yechiladigan pulni kiriting: "))
sanoq=0
if (hamyonPuli/2)<avans:
    while hamyonPuli>avans:
        hamyonPuli-=avans
        hamyonPuli*=2
        sanoq+=1
    print(f"Bu hamyondan {sanoq} marta pul yechildi!!!") 
else: 
    print("Cheksiz davom etadi bu holatda!!!")
    
    

