import os
import json
import time
import pip
from config import banner



# check import module
try:
    from progress.spinner import MoonSpinner
except ImportError:
    pip.main(['install', '--user', 'progress'])
    from progress.spinner import MoonSpinner

try:
    import requests
except ImportError:
    pip.main(['install', '--user', 'requests'])
    import requests


def connectNetwork():
    url = "https://nutders.com"
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False


# install miner function 
def install():
    try:
        # os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
        os.system("git clone --single-branch -b ARM https://github.com/mantvmass/ccminer")
        os.system("@cls||clear")
        print("\nกำลังติดตั้ง...\n")
    except:
        print("ติดตั้งไม่สำเร็จ!")


zergpool = ["stratum+tcp://verushash.mine.zergpool.com:3300","stratum+tcp://verushash.na.mine.zergpool.com:3300","stratum+tcp://verushash.eu.mine.zergpool.com:3300","stratum+tcp://verushash.asia.mine.zergpool.com:3300"]
# run miner function
def runOnline():

    if connectNetwork() == True:
        banner()
        with open("set-miner/online.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            miner = loads['miner']
            nameMiner = loads['name']
            cpu = loads['cpu']
    
        try:
            url = f"https://nutders.com/api/v1/get-read-specific.php?tag_name={miner}"
            receive = requests.get(url)
            s = receive.json()

            print("\033[1;34;40m")   
            print("TAG    =  ",s['tag_name'])
            print("WALLET =  ",s['wallet']+"."+nameMiner)
            print("POOL   =  ",s['pool'])
            print("CPU    =  ",cpu)


            if s["pool"] in zergpool:

                print("PASS   =  ",s['password']+",ID="+nameMiner)
                print("\033[00m\n")

                time.sleep(2)
                os.system(f"cd ccminer && ./ccminer -a verus -o {s['pool']} -u {s['wallet']}.{nameMiner} -p {s['password']},ID={nameMiner} -t {cpu}")
            else:

                print("PASS   =  ",s['password'])
                print("\033[00m\n")

                time.sleep(2)
                os.system(f"cd ccminer && ./ccminer -a verus -o {s['pool']} -u {s['wallet']}.{nameMiner} -p {s['password']} -t {cpu}")
        except:
            # push = {'status': False,'miner': '','name': '','cpu': 1}
            # with open("set-miner/online.json", "w") as set:
            #     json.dump(push, set, indent=4)
            os.system("@cls||clear")
            print("\n\n\033[1;31;40mไม่พบการตั้งค่านี้บนเว็บ กรุณาตั้งค่าที่ nutders.com \nและตั่งค่าบนมือถือใหม่ด้วยคำสั่ง edit-miner\033[0m\n\n")

    else:
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการเชื่อมต่ออินเตอร์เน็ต!\033[0m\n\n")


    # print(s['id'])
    # print(s['tag_name'])
    # print(s['pool'])
    # print(s['wallet'])
    # print(s['password'])





def runOffline():
    banner()
    try:
        with open("set-miner/offline.json", encoding="utf-8") as set:
            load = set.read()
            loads = json.loads(load)
            pool = loads['pool']
            wallet = loads['wallet']
            password = loads['pass']
            cpu = loads['cpu']
        if pool == "" or wallet == "":
            print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")
            return
        print("\033[1;34;40m")   
        print("WALLET =",wallet)
        print("POOL   =",pool)
        print("CPU    =",cpu)
        print("PASS   =",password)
        print("\033[00m\n")


        os.system(f"cd ccminer && ./ccminer -a verus -o {pool} -u {wallet} -p {password} -t {cpu}")
    except:
        push = {'status': False,'pool': '','wallet': '','pass': '','cpu': ''}
        with open("set-miner/offline.json", "w") as set:
            json.dump(push, set, indent=4)
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า หรือ การตั้งค่าไม่ถูกต้อง\nกรุณาตั้งค่าใหม่โดยใช้คำสั่ง edit-miner\033[0m\n\n")




while True:
    os.system("@cls||clear")
    with MoonSpinner("กำลังทำงาน...") as bar:
        for i in range(100):
            time.sleep(0.05)
            bar.next()
    if os.path.exists("ccminer") == False:
        install()
        break
    # if os.path.isfile("active.json") == True:
    with open("active.json", encoding="utf-8") as set:
        load = set.read()
        loads = json.loads(load)
        status = loads['status']
    if status == "on":
        runOnline()
        break
    elif status == "off":
        runOffline()
        break
    else:
        os.system("@cls||clear")
        print("\n\n\033[1;31;40mไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner\033[0m\n\n")
        break


    # else:
    #     os.system("@cls||clear")
    #     print("\n\n\033[1;31;40mไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner\033[0m\n\n")
    #     break






























# import os, json, time, pip
# from config import banner



# # check import module
# try:
#     from progress.spinner import MoonSpinner
# except ImportError:
#     pip.main(['install', '--user', 'progress'])
#     from progress.spinner import MoonSpinner






# # install miner function 
# def install():
#     try:
#         # os.system("git clone --single-branch -b ARM https://github.com/monkins1010/ccminer")
#         os.system("git clone https://github.com/mantvmass/ccminer_mmv")
#         os.system("@cls||clear")
#         print("ติดตั้งสำเร็จ")
#     except:
#         print("ติดตั้งไม่สำเร็จ!")


# # run miner function
# def run():
#     banner()
#     with open("set-miner/miner.json", encoding="utf-8") as set:
#         load = set.read()
#         loads = json.loads(load)
#         pool = loads['Pool']
#         wallet = loads['Wallet']
#         password = loads['Pass']
#         cpu = loads['Cpu']
#     if pool == "" or wallet == "":
#         print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")
#         return
#     print("ccminer CPU3.7 for VerusHash v2.1 - 2.2 by Monkins1010 based on ccminer")
#     print("Originally based on Christian Buchner and Christian H. project")
#     os.system(f"cd ccminer_mmv && ./ccminer -a verus -o {pool} -u {wallet} -p {password} -t {cpu}")




# while True:
#     os.system("@cls||clear")
#     with MoonSpinner("กำลังทำงาน...") as bar:
#         for i in range(100):
#             time.sleep(0.05)
#             bar.next()
#     if os.path.exists("ccminer_mmv") == False:
#         install()
#         break
#     if os.path.exists("set-miner") == True:
#         if os.path.isfile("set-miner/miner.json") == True:
#             run()
#             break
#         else:
#             os.system("@cls||clear")
#             print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")
#     else:
#         os.system("@cls||clear")
#         print("ไม่พบการตั้งค่า miner กรุณาตั้งค่าโดยใช้คำสั่ง edit-miner")
