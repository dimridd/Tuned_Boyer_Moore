#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:42:28 2018

@author: divyanshu
"""

#%%
table = [0]*256
rest = []

def bc1(pat, m):
	for i in range(len(table)):
		table[i] = m
	
	for i in range(m):
		pre = table[ord(pat[i])-65]
		table[ord(pat[i])-65] = m-i-1;
		if table[ord(pat[i])-65] == 0:
			table[ord(pat[i])-65] = pre
			
	return table	

text = "GCATCGCAGAGAGTATACAGTACG"
pat = "GCAGAGAG"
sigma = "ACGT"
match = 0
bc = bc1(pat.upper(), len(pat))	


def append(text, char, no_of_times):
	for i in range(no_of_times):
		text += char
  
	return text


def cmp(pat, text, j, m):
	count = 0
	for i in range(m):
		if pat[i] == text[i+j]:
			count += 1
	
	if count == m:
		return 1
	else:
		return 0
	
def TUNEDBM(pat, m, text, n):
	j = 0
	k = 0
	matches = 0
	
	bc = bc1(pat.upper(), len(pat))	
	shift = bc[ord(pat[m-1])-65]
	bc[ord(pat[m-1])-65] = 0
	
	text = append(text, pat[m-1], m)
	
	while j < n:
		k = bc[ord(text[j+m-1])-65]
		
		while k != 0:
			j += k
			k = bc[ord(text[j+m-1])-65]
			
			j += k
			k = bc[ord(text[j+m-1])-65]
			
			j += k
			k = bc[ord(text[j+m-1])-65]
			
		if cmp(pat, text, j, m-1) and j<n:
			matches += 1
			
		
		j += shift 	
	
	return matches	 
		
def main():
	text = "GCATCGCAGAGAGTATACAGTACG"
	pat = "GCAGAGAG"
	
	
	print(TUNEDBM(pat, len(pat), text, len(text)))

if __name__ == '__main__':
	main()	
	
	
	
	
	
	
	
	
	
	
	