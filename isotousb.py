"""Making a bootable USB key 
from an .iso image on Mac OS X ...
"""

import os
import subprocess
import termcolor

OUTPUT_FILENAME = "iso.img"
INPUT_FILENAME = "iso.iso"

try:
    print (termcolor.colored(
        "Remember that to make this script work you need to rename your iso in iso.iso",
        'red', attrs=['bold']
    ))

    input(termcolor.colored(
        'Press ENTER to continue or CTRL-C to abort... : ',
        'red',attrs=['bold']
        ))

    print (termcolor.colored(
        "Script is started...",
        'green', attrs=['bold']
        ))

    folder = input(termcolor.colored(
        'Enter your iso s folder like /user/folder... : ',
        'red', attrs=['bold']
        ))

    if not os.path.exists(folder):
        print (termcolor.colored(
            "Oops, your folder doesn't exist...",
            'blue', attrs=['bold']
            ))
        exit(1)

    filename = os.path.join(folder, INPUT_FILENAME)
    output = os.path.join(folder, OUTPUT_FILENAME)

    if not os.path.exists(filename):
        print (termcolor.colored(
            "Oops, iso.iso is missing...",
            'blue', attrs=['bold']
            ))
        exit(1)

    print (termcolor.colored(
        "Script changed folder and start hdiutil",
        'green', attrs=['bold']
        ))

    x = subprocess.call(["hdiutil", "convert", "-format", "UDRW", "-o", output, filename])

    print (x)

    if x == 0:
        print (termcolor.colored(
            "convert to iso.img OK",
            'green', attrs=['bold']
            ))

    else :
        print (termcolor.colored(
            "error, try again or file already converted ...",
            'blue', attrs=['bold']
            ))

    x = subprocess.call(["diskutil", "list"])

    disk = input(termcolor.colored(
        'insert your destination disk identifier...: ',
        'red', attrs=['bold']
        ))

    x = subprocess.call(["diskutil", "unmountDisk", "{}".format(disk)])

    x = subprocess.call(["dd", "if={}.dmg".format(output), "of=/dev/r{}".format(disk), "bs=1m"])

    x = subprocess.call(["diskutil", "eject", "{}".format(disk)])

    
except KeyboardInterrupt:
    print("\n")
    exit(0)

finally:
    print (termcolor.colored(
        "Finish!",
        'green', attrs=['bold']
        ))
