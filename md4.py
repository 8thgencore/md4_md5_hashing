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

def md4_hash(file):
	"""
	MD4 hash function
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

	# define F, G, H
	def F(x,y,z): return ((x & y) | ((~x) & z))
	def G(x,y,z): return (x & y) | (x & z) | (y & z)
	def H(x,y,z): return x ^ y ^ z

	# def round function
	def R1(a,b,c,d,k,s): return shift((a + F(b,c,d) + X[k]) & 0xffffffff, s)
	def R2(a,b,c,d,k,s): return shift((a + G(b,c,d) + X[k] + 0x5a827999) & 0xffffffff, s)
	def R3(a,b,c,d,k,s): return shift((a + H(b,c,d) + X[k] + 0x6ed9eba1) & 0xffffffff, s)

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
		A = R1(A,B,C,D, 0, 3)
		D = R1(D,A,B,C, 1, 7)
		C = R1(C,D,A,B, 2, 11)
		B = R1(B,C,D,A, 3, 19)

		A = R1(A,B,C,D, 4, 3)
		D = R1(D,A,B,C, 5, 7)
		C = R1(C,D,A,B, 6, 11)
		B = R1(B,C,D,A, 7, 19)

		A = R1(A,B,C,D, 8, 3)
		D = R1(D,A,B,C, 9, 7)
		C = R1(C,D,A,B, 10, 11)
		B = R1(B,C,D,A, 11, 19)

		A = R1(A,B,C,D, 12, 3)
		D = R1(D,A,B,C, 13, 7)
		C = R1(C,D,A,B, 14, 11)
		B = R1(B,C,D,A, 15, 19)

		# round 2
		A = R2(A,B,C,D, 0, 3)
		D = R2(D,A,B,C, 4, 5)
		C = R2(C,D,A,B, 8, 9)
		B = R2(B,C,D,A, 12, 13)

		A = R2(A,B,C,D, 1, 3)
		D = R2(D,A,B,C, 5, 5)
		C = R2(C,D,A,B, 9, 9)
		B = R2(B,C,D,A, 13, 13)

		A = R2(A,B,C,D, 2, 3)
		D = R2(D,A,B,C, 6, 5)
		C = R2(C,D,A,B, 10, 9)
		B = R2(B,C,D,A, 14, 13)

		A = R2(A,B,C,D, 3, 3)
		D = R2(D,A,B,C, 7, 5)
		C = R2(C,D,A,B, 11, 9)
		B = R2(B,C,D,A, 15, 13)

		# round 3
		A = R3(A,B,C,D, 0, 3)
		D = R3(D,A,B,C, 8, 9)
		C = R3(C,D,A,B, 4, 11)
		B = R3(B,C,D,A, 12, 15)

		A = R3(A,B,C,D, 2, 3)
		D = R3(D,A,B,C, 10, 9)
		C = R3(C,D,A,B, 6, 11)
		B = R3(B,C,D,A, 14, 15)

		A = R3(A,B,C,D, 1, 3)
		D = R3(D,A,B,C, 9, 9)
		C = R3(C,D,A,B, 5, 11)
		B = R3(B,C,D,A, 13, 15)

		A = R3(A,B,C,D, 3, 3)
		D = R3(D,A,B,C, 11, 9)
		C = R3(C,D,A,B, 7, 11)
		B = R3(B,C,D,A, 15, 15)

		# additions
		A = (A + AA) & 0xFFFFFFFF
		B = (B + BB) & 0xFFFFFFFF
		C = (C + CC) & 0xFFFFFFFF
		D = (D + DD) & 0xFFFFFFFF

	return int_to_bytes(A) + int_to_bytes(B) + int_to_bytes(C) + int_to_bytes(D)

