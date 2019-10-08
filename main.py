import hashlib
from md4 import md4_hash
from md5 import md5_hash

def main():
	with open("image.png", "rb") as f:
		file = f.read()

	md4 = md4_hash(file).hex()
	print("md4: ", md4)

	md5 = md5_hash(file).hex()
	assert md5 == hashlib.md5(file).hexdigest()
	print("md5: ", md5)

if __name__ in '__main__':
	main()