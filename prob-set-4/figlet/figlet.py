from pyfiglet import Figlet
import sys, random

figlet = Figlet()
try:
    if len(sys.argv) == 1:
        figlet.setFont(font=(figlet.getFonts())[random.randint(0,548)])
    elif len(sys.argv) == 3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
        figlet.setFont(font=sys.argv[2])
    else:
        print("Invalid Usage1")
        sys.exit()
    s = input("Input: ")
    print(figlet.renderText(s))
except:
    print("Invalid Usage2")
    sys.exit()
