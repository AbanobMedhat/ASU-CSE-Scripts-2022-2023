#!/usr/bin/python3
# Intial Input
RCL = 8
S = [0,1,2,3,4,5,6,7]
T = [0,1,2,3,4,5,6,7]

# Input as ASCII
K = [72, 101, 108, 108, 111, 87, 111, 114]

# Initialization 
for i in range(0,8,1):
	S[i] = i;
	T[i] = K[i];

print("Intial Permutation")

#  Initial Permutation of S 
j = 0;
for i in range(0, 8, 1):
	j = (j + S[i] + T[i]) % RCL;
	S[i], S[j] = S[j], S[i]
	print(S)

# Stream Generator
print("Stream Generator")

i = 0
j = 0
t = 0
key = []
for i in range(0, 8, 1):
	i = (i + 1) % RCL
	j = (j + S[i]) % RCL
	S[i], S[j] = S[j], S[i]
	print(S)
	t = (S[i] + S[j]) % RCL
	key.append(S[t])

print("Key")
print(key)
