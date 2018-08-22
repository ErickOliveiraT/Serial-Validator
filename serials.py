from random import choice
import hashlib
import time

def generateSerials(qnt):
  arq = open('data.crp', "w") #for md5
  arq2 = open('plain.txt', "w") #for plain text
  pos ='0A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q7R8S9T0U1V2W3X4Y5Z'
  for i in range(0,qnt):
    serial = ""
    for k in range(0,5):
      for j in range(0,5):
        serial += choice(pos)
      serial += "-"
    aux = ""
    for k in range(0, len(serial)-1):
      aux += serial[k] 
    #print(aux) //Plain text
    #print(hashlib.md5(aux.encode('utf-8')).hexdigest()) //md5
    if i != qnt-1:
      arq2.write(aux+"\n")
      arq.write(hashlib.md5(aux.encode('utf-8')).hexdigest() + "\n") #md5
    else:
      arq2.write(aux)
      arq.write(hashlib.md5(aux.encode('utf-8')).hexdigest()) #md5

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

generateSerials(500)  #500 count in this case
#time.sleep(2)
#resp = validateSerial("A100D-AKJMC-MWV4V-Z3IN8-H73J5")
#print(resp)