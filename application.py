import os, hashlib

from keyauth import api

def getchecksum():
	path = os.path.basename(__file__)
	if not os.path.exists(path):
		path = path[:-2] + "exe"
	md5_hash = hashlib.md5()
	a_file = open(path,"rb")
	content = a_file.read()
	md5_hash.update(content)
	digest = md5_hash.hexdigest()
	return 

auth = api(name = "Hyperium Optimizer", ownerid = "VGXmDe9CbK", secret = "ff079f0677ef10022f960819d53f5ecd791090d7cfbc277882d61d5d866f252c", version = "1.0", hash_to_check = getchecksum())