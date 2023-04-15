import os, time, json
from config import banner
from multiprocessing import cpu_count


cpu_thread = cpu_count()


def OnMiner():

    # connect server confix
    push = {
        'status': "on"
    }
    with open("active.json", "w") as set:
        json.dump(push, set, indent=4)

    banner()
    print("  [ -- SETTING -- ]  ")
    try:
        minerAPI = input("TAG: ")
        if minerAPI == "":
            raise Exception()
        nameMiner  = input("NAME: ")
        if nameMiner == "":
            nameMiner = "miner01"
        cpuT = int(input("CPU: "))
        if cpuT == "":
            cpuT = cpu_thread-1
        elif cpuT < 0:
            raise Exception()
    except:
        os.system("@cls||clear")
        print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
        time.sleep(3)
    push = {
        'status': True,
        'miner': minerAPI,
        'name': nameMiner,
        'cpu': cpuT
    }
    with open("set-miner/online.json", "w") as set:
        json.dump(push, set, indent=4)



    try:
        with open("set-miner/offline.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            wallet = loads['wallet']
            password = loads['pass']
            cpu = loads['cpu']
        push = {
            'status': False,
            'pool': pool,
            'wallet': wallet,
            'pass': password,
            'cpu': cpu
            }
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)

    except:
        push = {
            'status': False,
            'pool': "",
            'wallet': "",
            'pass': "",
            'cpu': ""
        }
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)




def OffMiner():


    # no connect server
    push = {
        'status': "off"
    }
    with open("active.json", "w") as set:
        json.dump(push, set, indent=4)


    banner()
    try:
        print("ตัวอย่าง: \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m")
        pool = input("[-o]: ")

        print("ตัวอย่าง: \033[93mRQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.OMG-MINER\033[00m")
        wallet = input("[-u]: ")

        print("ตัวอย่าง: \033[93mx หรือ ( hybrid เฉพาะ luckpool )\033[00m")
        password = input("[-p]: ")

        print(f"ตัวอย่าง: \033[93mค่าที่ใส่ได้คือ 0 ถึง {cpu_thread}\033[00m")
        cpu = int(input("[-t]: "))
        
        if pool == "" or wallet == "":
            raise Exception()
        if password == "":
            password = "x"
        if cpu == "":
            cpu = 1
    except:
        os.system("@cls||clear")
        print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
        time.sleep(3)

    push = {
        'status': True,
        'pool': pool,
        'wallet': wallet,
        'pass': password,
        'cpu': cpu
    }
    with open("set-miner/offline.json", "w") as set:
        json.dump(push, set, indent=4)

    try:
        with open("set-miner/online.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            minerAPI = loads['miner']
            nameMiner = loads['name']
            cpuT = loads['cpu']

        push = {
        'status': False,
        'miner': minerAPI,
        'name': nameMiner,
        'cpu': cpuT
        }
        with open("set-miner/online.json", "w") as set:
            json.dump(push, set, indent=4)
    except:
        push = {
        'status': False,
        'miner': "",
        'name': "",
        'cpu': ""
        }
        with open("set-miner/online.json", "w") as set:
            json.dump(push, set, indent=4)








while True:
    banner()
    print(f"  [ -- เมนู -- ]  \033[0;37;44mCPU = {cpu_thread}\033[0;37;40m")
    print("  [1] Online")
    print("  [2] Offline")
    print("  [0] ออก")
    try:
        select = int(input(">>> "))
        if select < 0:
            raise Exception()
        elif select > 2:
            raise Exception()
        elif select == 1:
            OnMiner()
        elif select == 2:
            OffMiner()
        elif select == 0:
            break
    except:
        print("\nเลือก 0 - 2 เท่านั้น!")
        time.sleep(3)