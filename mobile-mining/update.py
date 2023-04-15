from distutils.version import Version
import os, requests, json
from config import versionApp


error = 0

try:
    url1 = "https://nutders.com/api/app_update/versionApp.php"
    receive = requests.get(url1)
    verApp = receive.json()
    url2 = "https://nutders.com/api/app_update/set_update.php"
    receive = requests.get(url2)
    app = receive.json()
    print("\nกำลังอัพเดทเป็นเวอร์ชั่น", verApp[0])
    err = False
except:
    print("ไม่สามารถเชื่อมต่อกับ server!")
    err = True

if verApp[0] == versionApp():
    print("\nเวอร์ชั่นของคุณเป็นเวอร์ชั่นปัจจุบันอยู่แล้ว!")

else:
    if err == False:
        try:
            for i in range(1,len(app)):

                try:
                    update_url = f'https://nutders.com/api/app_update/{app[0]}/{app[i]}'
                    wr = requests.get(update_url, allow_redirects=True)
                    open(f'{app[i]}', 'wb').write(wr.content)
                except:
                    print("\nเกิดข้อผิดพลาดระหวางการอัพเดท!")
                    error += 1

                # try:
                #     if os.path.isfile(app[i]) == True:
                #         os.system(f"rm -rf {app[i]}")
                #         os.system(f"wget http://mobile-mining.tk/api/app_update/{app[0]}/{app[i]}")
                #     else:
                #         os.system(f"wget http://mobile-mining.tk/api/app_update/{app[0]}/{app[i]}")
                # except:
                #     print("\nเกิดข้อผิดพลาดระหวางการอัพเดท!")
                #     error += 1

        except:
            print("\nเกิดข้อผิดพลาดระหวางการอัพเดท!")
            error += 1
    if error == 0:
        push = {
            'version': verApp[0]
        }
        with open("version.json", "w") as version:
            json.dump(push, version, indent=4)
        print("\nอัพเดทแล้ว!")