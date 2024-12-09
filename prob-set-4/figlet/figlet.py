import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font_flags = ["-f", "--font"]

def main():
    if len(sys.argv) == 1:
        selected_font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and sys.argv[1] in font_flags and sys.argv[2] in figlet.getFonts():
        selected_font = sys.argv[2]
    else:
        sys.exit("Invalid usage")
    figlet.setFont(font=selected_font)
    print("Output:")
    print(figlet.renderText(input("Input: ")))
 
main()
