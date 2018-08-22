import hashlib

def getMD5sum():
	BLOCKSIZE = 65536
	hasher = hashlib.md5()
	with open('my-software.exe', 'rb') as afile: #Software name
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	return hasher.hexdigest()

def getSHA1sum():
	BLOCKSIZE = 65536
	hasher = hashlib.sha1()
	with open('my-software.exe', 'rb') as afile: #Software name
	    buf = afile.read(BLOCKSIZE)
	    while len(buf) > 0:
	        hasher.update(buf)
	        buf = afile.read(BLOCKSIZE)
	return hasher.hexdigest()

md5sum = getMD5sum()
print(md5sum)
sha1sum = getSHA1sum()
print(sha1sum)