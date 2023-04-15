import argparse
import sys
import urllib.request
import json



PROGRAM_NAME = "VerusMobile"
PROGRAM_GITHUB = "https://github.com/mantvmass/VerusMobile"
PROGRAM_VERSION = "3.0"


TERMUX_APP_PACKAGE = "com.termux"
TERMUX_PREFIX = "/data/data/{}/files/usr".format(TERMUX_APP_PACKAGE)



DEV_PREFIX = "/home/mantvmass/Desktop/VerusMobile"
TERMUX_PREFIX = DEV_PREFIX


# internal config style
# python VerusMobile.py --setup json '{"mode": "internal", "exec": "ccminer -a verus -o stratum+tcp://ap.luckpool.net:3956 -u RQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT.VerusMobile -p x -t 8"}'

# external config style
# python VerusMobile.py --setup json '{"mode": "external", "method": "POST", "url": "https://nutders.com/api", "tag": "mantvmass"}'
# python VerusMobile.py --setup json '{"mode": "external", "url": "https://nutders.com/api", "tag": "mantvmass"}'
# python VerusMobile.py --setup json '{"mode": "external", "tag": "mantvmass"}'



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



def StartCommand(args):
    if args.start[0] == "mine":
        pass
    elif args.start[0] == "setup": print("{}: GUI Setup in developments")
    else: print("{}: Unknow {}".format(PROGRAM_NAME, args.start[0]))
    sys.exit(0)



def SetupCommand(args):
    if args.setup[0] == "gui": print("{}: GUI Setup in developments")
    elif args.setup[0] == "json": json_setup(args.setup)
    else: print("{}: Unknow {}".format(PROGRAM_NAME, args.start[0]))
    sys.exit(0)



def Main(args, parser):
    if args.setup != None and args.start != None:
        print("{}: You cannot use '--start' and '--setup' at the same time.")
        sys.exit(0)
    if args.setup != None: SetupCommand(args)
    elif args.start != None: pass
    else: parser.print_help()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = PROGRAM_NAME, description = 'ccminer controller for andriod (Termux)', epilog = 'Follow me: {}'.format(PROGRAM_GITHUB))

    parser.add_argument('-v', '--version', action='version', version='%(prog)s {version}'.format(version = PROGRAM_VERSION))
    # parser.add_argument('-c', '--create-new', action='store_true', default=False, help="Create new database")
    parser.add_argument('--setup', nargs='+', help="Command setup: %(prog)s --setup 'option', option lists: [ gui, json, view ]")
    parser.add_argument('--start', nargs='+', help="Command start: %(prog)s --start 'option', option lists: [ internal, external ]")
    args = parser.parse_args()

    Main(args, parser)
    # print(args)
    # parser.print_help()