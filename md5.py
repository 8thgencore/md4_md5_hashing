import math

def int_to_bytes(x):
	"""
	int ---> bytes (little end)
	"""
	return x.to_bytes((x.bit_length() + 7) // 8, 'little')

def int_from_bytes(xbytes):
	""" 
	int <--- bytes (little end)
	"""
	return int.from_bytes(xbytes, 'little')

def md5_hash(file):
	"""
	MD5 hash function
	"""
	length = len(file)

	# step 1
	# padding to 512 % 448 bits (64 % 56 byte)
	if (len(file) % 64) != 56:
		file += b'\x80'
		while (len(file) % 64) != 56:
			file += b'\x00'

	assert len(file) % 64 == 56

	# step 2
	# len file + 64 bytes
	len64 = int_to_bytes(length * 8 & 0xffffffff)
	file += len64.ljust(8, b'\x00')

	# step 3
	# init md buffer (little endian)
	A = 0x67452301
	B = 0xefcdab89
	C = 0x98badcfe
	D = 0x10325476

	# generate T_i
	T = [int(abs(math.sin(i)) * 2**32) for i in range(0, 65)]

	# define F, G, H, I
	def F(x,y,z): return ((x & y) | ((~x) & z))
	def G(x,y,z): return ((x & z) | ((~z) & y))
	def H(x,y,z): return x ^ y ^ z
	def I(x,y,z): return y ^ ((~z) | x)

	# def round function
	def R1(a,b,c,d,k,s,i): return (b + shift((a + F(b,c,d) + X[k] + T[i]) & 0xffffffff, s)) & 0xffffffff
	def R2(a,b,c,d,k,s,i): return (b + shift((a + G(b,c,d) + X[k] + T[i]) & 0xffffffff, s)) & 0xffffffff
	def R3(a,b,c,d,k,s,i): return (b + shift((a + H(b,c,d) + X[k] + T[i]) & 0xffffffff, s)) & 0xffffffff
	def R4(a,b,c,d,k,s,i): return (b + shift((a + I(b,c,d) + X[k] + T[i]) & 0xffffffff, s)) & 0xffffffff

	# 3 bits shift <<<
	def shift(x, s): return ((x << s) & 0xffffffff) | (x >> (32-s))

	# file to words
	M = [int_from_bytes(file[i: i+4]) for i in range(0, len(file), 4)]

	# 
	for i in range(0, len(M), 16):
		X = M[i: i+16]

		# save registr
		AA = A
		BB = B
		CC = C
		DD = D

		# round 1
		A = R1(A,B,C,D, 0, 7, 1)
		D = R1(D,A,B,C, 1, 12, 2)
		C = R1(C,D,A,B, 2, 17, 3)
		B = R1(B,C,D,A, 3, 22, 4)

		A = R1(A,B,C,D, 4, 7, 5)
		D = R1(D,A,B,C, 5, 12, 6)
		C = R1(C,D,A,B, 6, 17, 7)
		B = R1(B,C,D,A, 7, 22, 8)

		A = R1(A,B,C,D, 8, 7, 9)
		D = R1(D,A,B,C, 9, 12, 10)
		C = R1(C,D,A,B, 10, 17, 11)
		B = R1(B,C,D,A, 11, 22, 12)

		A = R1(A,B,C,D, 12, 7, 13)
		D = R1(D,A,B,C, 13, 12, 14)
		C = R1(C,D,A,B, 14, 17, 15)
		B = R1(B,C,D,A, 15, 22, 16)

		# round 2
		A = R2(A,B,C,D, 1, 5, 17)
		D = R2(D,A,B,C, 6, 9, 18)
		C = R2(C,D,A,B, 11, 14, 19)
		B = R2(B,C,D,A, 0, 20, 20)

		A = R2(A,B,C,D, 5, 5, 21)
		D = R2(D,A,B,C, 10, 9, 22)
		C = R2(C,D,A,B, 15, 14, 23)
		B = R2(B,C,D,A, 4, 20, 24)

		A = R2(A,B,C,D, 9, 5, 25)
		D = R2(D,A,B,C, 14, 9, 26)
		C = R2(C,D,A,B, 3, 14, 27)
		B = R2(B,C,D,A, 8, 20, 28)

		A = R2(A,B,C,D, 13, 5, 29)
		D = R2(D,A,B,C, 2, 9, 30)
		C = R2(C,D,A,B, 7, 14, 31)
		B = R2(B,C,D,A, 12, 20, 32)

		# round 3
		A = R3(A,B,C,D, 5, 4, 33)
		D = R3(D,A,B,C, 8, 11, 34)
		C = R3(C,D,A,B, 11, 16, 35)
		B = R3(B,C,D,A, 14, 23, 36)

		A = R3(A,B,C,D, 1, 4, 37)
		D = R3(D,A,B,C, 4, 11, 38)
		C = R3(C,D,A,B, 7, 16, 39)
		B = R3(B,C,D,A, 10, 23, 40)

		A = R3(A,B,C,D, 13, 4, 41)
		D = R3(D,A,B,C, 0, 11, 42)
		C = R3(C,D,A,B, 3, 16, 43)
		B = R3(B,C,D,A, 6, 23, 44)

		A = R3(A,B,C,D, 9, 4, 45)
		D = R3(D,A,B,C, 12, 11, 46)
		C = R3(C,D,A,B, 15, 16, 47)
		B = R3(B,C,D,A, 2, 23, 48)

		# round 4
		A = R4(A,B,C,D, 0, 6, 49)
		D = R4(D,A,B,C, 7, 10 ,50)
		C = R4(C,D,A,B, 14, 15, 51)
		B = R4(B,C,D,A, 5, 21, 52)

		A = R4(A,B,C,D, 12, 6, 53)
		D = R4(D,A,B,C, 3, 10, 54)
		C = R4(C,D,A,B, 10, 15, 55)
		B = R4(B,C,D,A, 1, 21, 56)

		A = R4(A,B,C,D, 8, 6, 57)
		D = R4(D,A,B,C, 15, 10, 58)
		C = R4(C,D,A,B, 6, 15, 59)
		B = R4(B,C,D,A, 13, 21, 60)

		A = R4(A,B,C,D, 4, 6, 61)
		D = R4(D,A,B,C, 11, 10, 62)
		C = R4(C,D,A,B, 2, 15, 63)
		B = R4(B,C,D,A, 9, 21, 64)

		# additions
		A = (A + AA) & 0xFFFFFFFF
		B = (B + BB) & 0xFFFFFFFF
		C = (C + CC) & 0xFFFFFFFF
		D = (D + DD) & 0xFFFFFFFF

	return int_to_bytes(A) + int_to_bytes(B) + int_to_bytes(C) + int_to_bytes(D)