#!/usr/bin/python

import argparse
import sys
import urllib.request
import json
import requests
import os


PROGRAM_NAME = "VerusMobile"
PROGRAM_GITHUB = "https://github.com/mantvmass/VerusMobile"
PROGRAM_VERSION = "3.0"


TERMUX_APP_PACKAGE = "com.termux"
TERMUX_PREFIX = "/data/data/{}/files/usr/etc/VerusMobile".format(TERMUX_APP_PACKAGE)
CCMINER_RUNTIME = "/Miner/{architecture}/"


# for developments
# DEV_PREFIX = "/home/mantvmass/Desktop/VerusMobile"
# TERMUX_PREFIX = DEV_PREFIX


# --setup internal config style
# python VerusMobile.py --setup json '{"mode": "internal", "exec": "ccminer -a verus -o stratum+tcp://ap.luckpool.net:3956 -u RQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.VerusMobile -p x -t 8"}'

# --setup external config style
# python VerusMobile.py --setup json '{"mode": "external", "method": "POST", "url": "https://nutders.com/api", "tag": "mantvmass"}'
# python VerusMobile.py --setup json '{"mode": "external", "url": "https://nutders.com/api", "tag": "mantvmass"}'
# python VerusMobile.py --setup json '{"mode": "external", "tag": "mantvmass"}'

# --start mine
# python VerusMobile.py --start mine autorun
# python VerusMobile.py --start mine internal
# python VerusMobile.py --start mine external

# --switch autorun mode
# python VerusMobile.py --switch autorun internal
# python VerusMobile.py --switch autorun external

# --switch autorun mode
# python VerusMobile.py --switch autorun internal
# python VerusMobile.py --switch autorun external

# --switch arch
# python VerusMobile.py --switch autorun internal
# python VerusMobile.py --switch autorun external

# format data form server
# {
#     "status": "ok",
#     "message": "",
#     "exec": "ccminer start"
# }
#
# {
#     "status": "error",
#     "message": "error message",
#     "exec": None
# }

def custom_request(method, url, headers={}, payload={}, timeout=10):
    try:
        return requests.request(method, url, headers=headers, data=payload, timeout=timeout).json()
    except requests.exceptions.ConnectTimeout:
        return { "error": 500, "result": "connect timeout"}
    except requests.exceptions.ReadTimeout:
        return { "error": 500, "result": "read timeout"}



def readjson():
    try:
        with open(TERMUX_PREFIX + "/Miner/config.json", encoding="utf-8") as file:
            loads = json.loads(file.read())
        return loads
    except Exception:
        return False



def internal_update(data, new):
    try:
        data["internal"]["exec"] = new
        with open(TERMUX_PREFIX + "/Miner/config.json", "w") as file:
            json.dump(data, file, indent=4)
        return True
    except Exception:
        return False



def external_update(data, new):
    try:
        for key, value in new.items():
            for k, _ in data["external"].items():
                if k == key:
                    data["external"][key] = value
        with open(TERMUX_PREFIX + "/Miner/config.json", "w") as file:
            json.dump(data, file, indent=4)
        return True
    except Exception:
        return False



def switch_autorun(mode):
    if mode not in ["internal", "external"]:
        print("{}: This function supported mode: 'internal', 'external'".format(PROGRAM_NAME))
        sys.exit(0)
    try:
        j = readjson()
        j["mode"] = mode
        with open(TERMUX_PREFIX + "/Miner/config.json", "w") as file:
            json.dump(j, file, indent=4)
        print("{}: Update autorun mode success.".format(PROGRAM_NAME))
    except Exception:
        print("{}: Can't update autorun mode.".format(PROGRAM_NAME))



def switch_arch(arch):
    if arch not in ["x86_64", "armeabi-v7a", "arm64-v8a"]:
        print("{}: This function supported arch: 'x86_64', 'armeabi-v7a', 'arm64-v8a'".format(PROGRAM_NAME))
        sys.exit(0)
    try:
        j = readjson()
        j["architecture"] = arch
        with open(TERMUX_PREFIX + "/Miner/config.json", "w") as file:
            json.dump(j, file, indent=4)
        print("{}: Update Arch success.".format(PROGRAM_NAME))
    except Exception:
        print("{}: Can't update Arch.".format(PROGRAM_NAME))



def internet(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
    


def json_setup(value):
    if len(value) < 2:
        print('''VerusMobile: This function need parameter, for example: VerusMobile --setup json '{"mode": "internal", "exec": "ccminer -a verus -o stratum+tcp://ap.luckpool.net:3956 -u RQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.VerusMobile -p x -t 8"}' ''')
        sys.exit(0)
    j = json.loads(value[1])
    if j["mode"] == "internal":
        if not internal_update(readjson(), j["exec"]): print("{}: Can't update internal mode.".format(PROGRAM_NAME))
        else: print("{}: Update internal mode success.".format(PROGRAM_NAME))
    elif j["mode"] == "external":
        if not external_update(readjson(), j): print("{}: Can't update external mode.".format(PROGRAM_NAME))
        else: print("{}: Update external mode success.".format(PROGRAM_NAME))
    else: print("{}: Unknow {} mode".format(PROGRAM_NAME, j["mode"]))


def view_setup():
    j = readjson()
    v = """{name} View Setup:
    Mode: {mode}
    Architecture: {arch}
    External:
        Tag: {tag}
        Method: {method}
        Url: {url}
    Internal:
        Exec: {exec}
    """.format(
            name = PROGRAM_NAME,
            mode = j["mode"],
            arch = j["architecture"],
            tag = j["external"]["tag"],
            method = j["external"]["method"],
            url = j["external"]["url"],
            exec = j["internal"]["exec"],
        )
    print(v)


def mine_internal():
    return readjson()["internal"]["exec"] # set exec from internal setting



def mine_external():
    j = readjson()
    if not internet():
        print("{}: Internet no connect.".format(PROGRAM_NAME))
        sys.exit(0)
    request = custom_request(
        method=j["external"]["method"],
        url=j["external"]["url"],
        headers = { 'Content-Type': 'application/json' },
        payload = {"tag": j["external"]["tag"]}
    )
    data = request.json()
    if data["status"] != "ok":
        print("Server Reply: {}".format(data["message"]))
        sys.exit(0)
    return data["exec"]



def mine_autorun():
    j = readjson()
    if j["mode"] == "internal":
        return mine_internal()
    elif j["mode"] == "external":
        return mine_external()



def mine(args):
    if len(args) < 2:
        print("{}: This function need parameter, for example: VerusMobile --start mine internal".format(PROGRAM_NAME))
        sys.exit(0)

    if args[1] == "autorun":
        exec = mine_autorun()
    elif args[1] == "internal":
        exec = mine_internal()
    elif args[1] == "external":
        exec = mine_external() 
    else:
        print("{}: Unknow {} mode.".format(PROGRAM_NAME, args[1]))
        sys.exit(0)

    runtime = TERMUX_PREFIX + CCMINER_RUNTIME.format(architecture = readjson()["architecture"]) + exec
    os.system(runtime)
    sys.exit(0)
    # print(runtime)



def StartCommand(args):
    if args.start[0] == "mine": mine(args.start)
    elif args.start[0] == "setup": print("{}: GUI Setup in developments")
    else: print("{}: Unknow {}".format(PROGRAM_NAME, args.start[0]))
    sys.exit(0)



def SetupCommand(args):
    if args.setup[0] == "gui": print("{}: GUI Setup in developments")
    elif args.setup[0] == "json": json_setup(args.setup)
    elif args.setup[0] == "view": view_setup()
    else: print("{}: Unknow {}".format(PROGRAM_NAME, args.start[0]))
    sys.exit(0)


def SwitchCommand(args):
    if args.switch[0] == "autorun": switch_autorun(args.switch[1])
    elif args.switch[0] == "arch": switch_arch(args.switch[1])
    else: print("{}: Unknow {}".format(PROGRAM_NAME, args.start[0]))
    sys.exit(0)



def Main(args, parser):
    if args.setup != None and args.start != None:
        print("{}: You cannot use '--start' and '--setup' at the same time.".format(PROGRAM_NAME))
        sys.exit(0)
    if args.setup != None: SetupCommand(args)
    elif args.start != None: StartCommand(args)
    elif args.switch != None: SwitchCommand(args)
    else: parser.print_help()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = PROGRAM_NAME, description = 'ccminer controller for andriod (Termux)', epilog = 'Follow me: {}'.format(PROGRAM_GITHUB))

    parser.add_argument('-v', '--version', action='version', version='%(prog)s {version}'.format(version = PROGRAM_VERSION))
    # parser.add_argument('-c', '--create-new', action='store_true', default=False, help="Create new database")
    parser.add_argument('--setup', nargs='+', help="Command setup: %(prog)s --setup 'option', option lists: [ gui, json, view ]")
    parser.add_argument('--start', nargs='+', help="Command start: %(prog)s --start 'option', option lists: [ internal, external ]")
    parser.add_argument('--switch', nargs='+', help="Command start: %(prog)s --switch 'option', option lists: [ arch, autorun-mode ], arch lists: [ x86_64, armeabi-v7a, arm64-v8a ], mode lists: [ internal, external ]")
    args = parser.parse_args()

    Main(args, parser)
    # print(args)
    # parser.print_help()