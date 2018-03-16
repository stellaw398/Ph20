#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:26:49 2018

@author: apple
"""
p = 997 ## use a modulus
g = 7 ## define a corresponding base
def modulus(x):
    return g^x % p

Alice = 813
Bob = 623
B = modulus(Bob)
A = modulus(Alice)
if (B^Alice)% p == (A^Bob)% p:
    print "Shared key is %d" %((B^Alice)%p)
## Collision attack
## Eve is an evesdropper; she sees all the communication between Alice and Bob
## she knows the modulus and base and the values of g^a mod p and g^b mod p 
## she does not know Alice or Bob's private key or the public key,
## she only needs one of the private keys to calculate public key
## this is a brute force algorithm that only works for small a modulus <1000 bits
## it will calculate all of the valyes of g modulo p 

for i in range(p): 
    if modulus(i) == B:
        print "COLLISION: key is %d" %((A^i) %p)
        break
    if modulus(i) == A:
        print "COLLISION: key is %d" %((B^i) %p)
        break

        
