from colorama import Fore, Style, init

init(autoreset=True)

__version__ = "1.0.0"
__author__ = "vision-dev1"

BANNER = r"""
 _   _       _       _   _               _    
| | | |     | |     | | | |             | |   
| | | |_   _| |_ __ | |_| | __ ___      | | __
| | | | | | | | '_ \|  _  |/ _` \ \ /\ / |/ /
\ \_/ / |_| | | | | | | | | (_| |\ V  V /|   < 
 \___/ \__,_|_|_| |_\_| |_/\__,_| \_/\_/ |_|\_\
"""

TAGLINE = '"Hunts vulnerabilities in your code before they turn into exploits."'
SEPARATOR = "-" * 60

def display_banner() -> None:
    print(Fore.RED + Style.BRIGHT + BANNER)
    print(Fore.WHITE + Style.DIM + f"  {TAGLINE}")
    print(Fore.CYAN + f"  Author: {__author__}  |  Version: {__version__}")
    print(Fore.WHITE + Style.DIM + f"\n  {SEPARATOR}\n")
