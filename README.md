# VerusMobile For Termux
<a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/Python-3.10-blue"></a>
<a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-yello.svg"></a>

## Get Started
<strong>Guide:</strong> [YouTube Tutorial](https://youtube.com/playlist?list=PLI7M2d-VF3y8dPWI_KNEyucpb70GeXVYD)

```shell
pkg update -y && pkg install git python
```
```shell
git clone https://github.com/pigred1/VerusMobile/tree/patch-1
```
```shell
cd VerusMobile
```
```shell
pip install -r requirements.txt
```
```shell
chmod 700 install.sh && ./install.sh
```

## Software Detail
- <strong>Supported CPU instruction sets</strong>
   - arm64-v8a
   - armeabi-v7a
   - x86_64
- <strong>Miner</strong>
   - Miner: [ccminer](https://github.com/monkins1010/ccminer)
   - Android Version: [shmutalov-ccminer](https://github.com/shmutalov/ccminer)
   - Algorithm: [VerusHash](https://veruscoin.io/downloads/VerusVision.pdf)

## Command
   <strong>Internal Setup</strong>
   ```shell
   VerusMobile --setup json '{"mode": "internal", "exec": "ccminer -a verus -o stratum+tcp://ap.luckpool.net:3956 -u RQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.VerusMobile -p x -t 8"}
   ```

   <strong>External Setup</strong>
   ```shell
   VerusMobile --setup json '{"mode": "external", "method": "POST", "url": "https://web.com/api", "tag": "mantvmass"}'
   ```
   ```shell
   VerusMobile --setup json '{"mode": "external", "url": "https://nutders.com/api", "tag": "mantvmass"}'
   ```
   ```shell
   VerusMobile --setup json '{"mode": "external", "tag": "mantvmass"}'
   ```

<strong>View Setup</strong>
```shell
VerusMobile --setup view
```

<strong>Start Mine</strong>
```shell
VerusMobile --start mine autorun
```
```shell
VerusMobile --start mine internal
```
```shell
VerusMobile --start mine external
```

<strong>Switch Autorun</strong>
```shell
VerusMobile --switch autorun internal
```
```shell
VerusMobile --switch autorun external
```

<strong>Switch Arch</strong>
```shell
VerusMobile --switch arch arm64-v8a
```
```shell
VerusMobile --switch arch armeabi-v7a
```
```shell
VerusMobile --switch arch x86_64
```

## Donate
- <strong>Verus Wallet:</strong>
```RQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT```

Thank you for your support
