# AUTO RUN CCMINER IN TERMUX
<a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
<br>
## การติดตั้งแบบรวดเร็ว
```
apt-get update -y && apt-get install git -y && git clone https://github.com/mantvmass/auto-run-ccminer && cd auto-run-ccminer && chmod +x setup.sh && sh setup.sh
```

## การติดตั้งตามขั้นตอน
```
apt-get update -y
```
```
apt-get install git -y
```
```
git clone https://github.com/mantvmass/auto-run-ccminer
```
```
cd auto-run-ccminer
```
```
chmod +x setup.sh && sh setup.sh
```
* หลังจากเปิดไฟล์ bash.bashrc เพิ่มบรรทัดแรกเป็น
- ```run-miner```
* แล้ว save

## เพิ่มเติมการใช้โปรแกรม
* หากต้องการหยุดขุดให้ใช้กด ```CTRL + C```
* หากต้องการเปลี่ยน TAG ใช้คำสั่ง ```edit-miner```
* หากต้องการเปิดขุด ใช้คำสั่ง ```run-miner```
* หากต้องการอัพเดทโปรแกรม ใช้คำสั่ง ```cd && cd ../etc/mobile-mining && python3 update.py && cd```

## สนับสนุนนักพัฒนา
- ชื่อ ```ภูมินท์ มะลิวรรณ```
- กสิกรไทย ```0608905863```
- พร้อมเพย์ ```0639723211```

## ติดต่อ
* [Facebook](https://www.facebook.com/PhuminMaliwan)
* YouTube
   * [MANTVMASS](https://www.youtube.com/channel/UCYJk0E1wwY3zX-i8tn95mhw)
   * [MOBILE MINING](https://www.youtube.com/channel/UCevNnlKLgRTg-cku5JQ2Ahw) 
