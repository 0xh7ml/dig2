print("\033[31m▓█████▄  ██▓  ▄████    ▒███████▒      ▒█████") 
print("\033[31m▒██▀ ██▌▓██▒ ██▒ ▀█▒   ▒ ▒ ▒ ▄▀░     ▒██▒  ██▒")
print("\033[31m░██   █▌▒██▒▒██░▄▄▄░   ░ ▒ ▄▀▒░      ▒██░  ██▒")
print("\033[31m░▓█▄   ▌░██░░▓█  ██▓     ▄▀▒   ░     ▒██   ██░")
print("\033[31m░▒████▓ ░██░░▒▓███▀▒   ▒███████▒ ██▓ ░ ████▓▒░")
print("\033[31m ▒▒▓  ▒ ░▓   ░▒   ▒    ░▒▒ ▓░▒░▒ ▒▓▒ ░ ▒░▒░▒░") 
print("\033[31m ░ ▒  ▒  ▒ ░  ░   ░    ░░▒ ▒ ░ ▒ ░▒    ░ ▒ ▒░")
print("\033[31m ░ ░  ░  ▒ ░░ ░   ░    ░ ░ ░ ░ ░ ░   ░ ░ ░ ▒")  
print("\033[31m ░     ░        ░      ░ ░      ░      ░ ░")  
print("\033[31m ░                     ░          ░\033[0m")           
from urllib.request import urlopen as html
import os
def menu():
    print("\033[34;1m [0] All scan")
    print("\033[34;1m [1] Exit")
menu()
site = input(" Enter target name or ip~$")
def who():
    who =("http://api.hackertarget.com/whois/?q="+site)
    wip =html(who).read().decode('utf-8')
    d =open("whois.txt","a")
    d.write(wip)
def ip():
    nip =("http://api.hackertarget.com/nmap/?q="+site)
    pip = html(nip).read().decode('utf-8')
    i =open("portscan.txt","a")
    i.write(pip)
def sub():
    subl =("https://api.hackertarget.com/hostsearch/?q="+site)
    subo =html(subl).read().decode('utf-8')
    b = open("subdomain.txt","a")
    b.write(subo)
def geo():
    geol =("https://api.hackertarget.com/geoip/?q="+site)
    geoo =html(geol).read().decode('utf-8')
    a =open("geolocation.txt","a")
    a.write(geoo)
def mtr():
    mtrl =("https://api.hackertarget.com/mtr/?q="+site)
    mtro =html(mtrl).read().decode('utf-8')
    t = open("traceroute.txt","a")
    t.write(mtro)
def subnet():
    sntl =("https://api.hackertarget.com/subnetcalc/?q="+site)
    snto =html(sntl).read().decode('utf-8')
    id = open("subnet.txt","a")
    id.write(snto)
def dlook():
    dll =("http://api.hackertarget.com/dnslookup/?q="+site)
    dlo =html(dll).read().decode('utf-8')
    k =open("dnslookup.txt","a")
    k.write(dlo)
def crwl():
    cll =("https://api.hackertarget.com/pagelinks/?q="+site)
    clo =html(cll).read().decode('utf-8')
    s = open("link.html","a")
    s.write(clo)
def grab():
   gra =("https://api.hackertarget.com/httpheaders/?q="+site)
   grob =html(gra).read().decode('utf-8')
   head = open("banner.txt","a")
   head.write(grob)
def rip():
   ri = ("https://api.hackertarget.com/reverseiplookup/?q="+site)
   p = html(ri).read().decode('utf-8')
   ata = open("reverseiplist.txt","a")
   ata.write(p)
methods = input("\033[37m Input Methods plz:")
if methods== "0":
   print("\033[37m Ure output dir~$"+"("+"\033[31m"+os.getcwd()+"\033[0m"+")")
   print(who())
   print(ip())
   print(sub())
   print(geo())
   print(mtr())
   print(subnet())
   print(dlook())
   print(crwl())
   print(grab())
   print(rip())
   print("Successfully Done")
if methods== "1":
   print("./ Exit Success ")

   
