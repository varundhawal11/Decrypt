import os,requests,time
import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool  

try:
	import requests
except ModuleNotFoundError:
	os.system('pip insta requests')
	import requests
import requests,os,sys,random
try:
	import requests
except ModuleNotFoundError:
	os.system("pip install requests")
	import requests

b="\033[1;34m"#----------𝗯𝗹𝘂𝗲
bl="\033[1;30m"#--------𝗯𝗹𝗮𝗰𝗸
c="\033[1;36m"#----------𝗰𝘆𝗮𝗻
g="\033[1;32m"#----------𝗴𝗿𝗲𝗲𝗻
p="\033[1;35m"#----------𝗽𝘂𝗿𝗽𝗹𝗲
r="\033[1;31m"#----------𝗿𝗲𝗱
y="\033[1;33m"#----------𝘆𝗲𝗹𝗹𝗼𝘄
w="\033[1;37m"#----------𝘄𝗵𝗶𝘁𝗲 {𝗲𝗻𝗱}
S = '\033[1;37m';A = '\x1b[38;5;208m';R = '\x1b[38;5;46m';F = '\x1b[38;5;48m';Z = '\033[1;33m';A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';h = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';W = '\x1b[38;5;196m';hh = '\033[34;1m'
import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except:
    os.system("pip install requests")
    import requests 

  

os.system('clear')
name = input(f"{R}[{G1}+{R}]{G1} ENTER YOUR NAME : ").upper()
logo = f"""
{G1}
 

██╗  ██╗ █████╗ ██╗  ██╗   ██╗ █████╗ ███╗   ██╗    
██║ ██╔╝██╔══██╗██║  ╚██╗ ██╔╝██╔══██╗████╗  ██║    
█████╔╝ ███████║██║   ╚████╔╝ ███████║██╔██╗ ██║    
██╔═██╗ ██╔══██║██║    ╚██╔╝  ██╔══██║██║╚██╗██║    
██║  ██╗██║  ██║███████╗██║   ██║  ██║██║ ╚████║    
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝     
                                                         
{R}[{G1}+{R}]{G1}Decode{G1}━{R}>{G1}Marshal.Zlib.Decompress.Base64.B64decode
{R}[{G1}+{R}]{G1}Yourname{G1}━{R}>{G1}{name}
"""
def main_dec():
	os.system('clear')
	print(logo)
	try:
		open("/data/data/com.termux/files/usr/bin/pycdc")
		open("/data/data/com.termux/files/usr/lib/python3.11/minopyc.py", "r").read()
		open("/data/data/com.termux/files/usr/bin/pycdas")
	except:
		os.system("curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/pycdc")
		os.system("curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/pycdas")
		os.system("curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/minopyc.py")
		os.system("mv pycdc /data/data/com.termux/files/usr/bin/")
		os.system("mv pycdas /data/data/com.termux/files/usr/bin/")
		os.system("mv minopyc.py /data/data/com.termux/files/usr/lib/python3.11/")
		os.system("chmod 777 /data/data/com.termux/files/usr/lib/python3.11/minopyc.py")
		os.system("chmod 777 /data/data/com.termux/files/usr/bin/pycdc")
		os.system("chmod 777 /data/data/com.termux/files/usr/bin/pycdas")
	try:
		file=input(f"{R}[{G1}+{R}]{G1} INPUT YOUR FILE : ")
		open(file)
		os.system(f"cp {file} .b.py")
	except:
		exit('Nawaka Hallaya')
	try:
		open(file).read()
	except:
		os.system(f"pycdc .b.py > .a.py")
		files = open(".a.py", "r").read()
		if "exec(str(chr" in files:
			c= files.split(']')[0]+"]\nprint(''.join([chr(i) for i in _]))"
			files = open(".a.py", "w").write(c)
			os.system("python3 .a.py > .b.py")
		else:
			os.system("mv .a.py .b.py")
			pass
	print(f'{R}[{G1}+{R}]{G1} PLEASE WAIT I WILL TRYING TO DECODING')
	while True:
		file = open(".b.py", "r").read()
		if "(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(b" in file:
			filer = file.split("exec(")[1]
			open(".b.py", "w").write("import minopyc,marshal\ncode =("+filer+"\nminopyc.dump_to_pyc(code, '.a.py')")
			os.system("python3 .b.py;pycdc .a.py > .b.py")
		elif "(__import__('marshal').loads(__import__('marshal').loads(__import__('marshal').loads(" in file:
			filer = file.split("exec(")[1]
			open(".b.py", "w").write("import minopyc,marshal\ncode =("+filer+"\nminopyc.dump_to_pyc(code, '.a.py')")
			os.system("python3 .b.py;pycdc .a.py > .b.py")
		elif "exec(_(" in file:
			
			c= file.split('exec(_(')[1]
			l = ("import marshal,zlib,base64,minopyc\nx = (("+c+"\ny = x[:: -1]\nb = marshal.loads(zlib.decompress(base64.b64decode(y)))\nminopyc.dump_to_pyc(b,'.a.py') ")
			open(".b.py","w").write(l)
			os.system("python .b.py")
			os.system("pycdc .a.py > .b.py")
		elif "exec((_)(" in file:
			c= file.split('exec((_)(')[1]
			l = ("import marshal,zlib,base64,minopyc\nx = (("+c+"\ny = x[:: -1]\nb = marshal.loads(zlib.decompress(base64.b64decode(y)))\nminopyc.dump_to_pyc(b,'.a.py') ")
			open(".b.py","w").write(l)
			os.system("python .b.py")
			os.system("pycdc .a.py > .b.py")
		elif "exec(marshal.loads" in file:
			filer = file.replace("exec(", "code=(")
			open(".b.py", "w").write("import minopyc,marshal\n"+filer+"\nminopyc.dump_to_pyc(code, '.a.py')")
			os.system("python3 .b.py;pycdc .a.py > .b.py")
		elif "exec((lambda __," in file:
			filer = file.replace("exec(", "print(")
			open(".a.py", "w").write(filer)
			os.system("python2 .a.py > .b.py")
		else:
			c= open(".b.py","r").read()
			if c == '':
				print(f'{R}[{G1}+{R}]{G1}THE TOOL CAN JUST DECODED DATA')
				save=input(f"{R}[{G1}+{R}]{G1}ENTER PATH TO SAVE FROM : ")
				os.system(f"pycdas .a.py > {save}")
				os.system("rm .a.py;rm .b.py")
			elif "WARNING: Decompyle incomplete" in c:
				print(f'{R}[{G1}+{R}]{G1}THE TOOL CAN JUST DECODED DATA')
				save=input(f"{R}[{G1}+{R}]{G1}ENTER PATH TO SAVE FROM : ")
				os.system(f"pycdas .a.py > {save}")
			else:
				print(f'{R}[{G1}+{R}]{G1}THE TOOL DECODED')
				save=input(f"{R}[{G1}+{R}]{G1}ENTER PATH TO SAVE FROM : ")
				open(save, "w").write(c)
				break
			break
	try:
		open(".a.py")
		os.system("rm .a.py")
		try:
			open(".b.py")
			os.system("rm .b.py")
		except:pass
	except:pass
	exit(f"{R}[{G1}+{R}]{G1}DECODE DONE🤑🤑Kalyan mitro")
def contact_admin():
	os.system('xdg-open https://facebook.com/groups/1036123894351028/')

app = ('''

     _    ____  ____  ____   _____     ___    _     
    / \  |  _ \|  _ \|  _ \ / _ \ \   / / \  | |    
   / _ \ | |_) | |_) | |_) | | | \ \ / / _ \ | |    
  / ___ \|  __/|  __/|  _ <| |_| |\ V / ___ \| |___ 
 /_/   \_\_|   |_|   |_| \_\\___/  \_/_/   \_\_____|
                                                    
''')
main_dec()
