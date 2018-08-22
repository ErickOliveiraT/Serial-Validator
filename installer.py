import hashlib
import time
import os

install = lambda: os.system("tesseract (password) cpro.exe criptoPro.exe") #just an example
delete = lambda: os.system("del cpro.exe")

def validateSerial(plain):
  serial = hashlib.md5(plain.encode('utf-8')).hexdigest()
  arq = open("data.crp", "r")
  flag = False
  for line in arq:
    read = line.split()
    temp = ""
    for char in read:
      if char != "'" and char and "]" and char != "[":
        temp += char
    if serial == temp:
      flag = True
      break
    else: continue
  return flag

def getMD5sum():
	BLOCKSIZE = 65536
	hasher = hashlib.md5()
	with open('descrypter-program.exe', 'rb') as afile:
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	return hasher.hexdigest()

def getSHA1sum():
	BLOCKSIZE = 65536
	hasher = hashlib.sha1()
	with open('descrypter-program.exe', 'rb') as afile:
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	return hasher.hexdigest()

valid = input("Por favor digite seu serial do Cripto Pro: ")
resp = validateSerial(valid)
if resp == True:
	#O serial foi verfificado como válido
	#Agora vamos conferir a hash do tesseract:

	md5sum = getMD5sum()
	sha1sum = getSHA1sum()

	if md5sum == "Real-MD5" and sha1sum == "Real-SHA-1": ##Insert valid hashes of descrypter program
		install()
		delete()
		print("\nO Cripto Pro foi ativado com sucesso!")
		time.sleep(1000)
	else:
		print("\nDetectamos que sua Cópia do Cripto Pro não é genuína.. O Cripto Pro não será instalado.")
		time.sleep(1000)
else:
	print("\nSerial inválido. Inicie o instalador novamente")
	time.sleep(1000)