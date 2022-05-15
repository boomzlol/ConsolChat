import rich
import os
import time
import random

# List of letters allowed
Allowed = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Rich Setup
from rich.console import Console
console = Console()


# The Starting Page
console.print("[green]Terminal[/green] [red]Chatting[/red]", style= "bold")
console.print("     [[cyan]Enter[/cyan]]")
input()
os.system("cls")
# Input User

console.print("[magenta] Username? [/magenta]")
print("(Uppercase letters will be turned lowercase.)")
print("(Anything longer than 9 characters will be deleted.)")
print("(Special characters are allowed.)")
hostname = input(">> ")[:9]
hostname.lower()


input()

