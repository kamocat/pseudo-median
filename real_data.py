#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 23:41:02 2025

@author: marshal
"""

import pandas as pd
import numpy as np
from scipy import fft, signal as sig
import matplotlib.pyplot as plt

# Brute force solution
def classic_median(x, mlen=128):
    return [np.median(x[max(i-mlen, 0):i+1]) for i in range(n)]

def pseudo_median(x, mlen=128):
    arr = np.linspace(0,2,mlen)
    def pmed(val):
        nonlocal arr
        i = np.argmin(np.abs(arr-val))
        if arr[i] < val:
            i += 1
        arr = np.insert(arr, i, val)
        #if val > random.choice(arr):
        if i > mlen//2:
            arr = arr[1:]
        else:
            arr = arr[:-1]
        return arr[mlen//2]

    return [pmed(v) for v in x]

def fir_sinc(x, wlen):
    w = w = np.sinc(np.linspace(-1, 1, wlen))
    w /= np.sum(w)
    y = np.convolve(x, w, mode='full')
    n = max(x.shape)
    return y[:n]

# %%

a = pd.read_csv('data/fast_sample.csv')
b = pd.to_numeric(a['state'], errors='coerce').dropna()
n = b.shape[0]

mlen = 128
c = classic_median(b, mlen)
d = pseudo_median(b, mlen)
plt.figure()
plt.plot(b, 'k,', label='noisy', markersize=1)
plt.plot(c, label='median')
plt.plot(d, label='pseudo-median')
plt.xlim(mlen, n)
plt.ylim(0.2, 0.7)
plt.legend()
plt.savefig('images/fast_sample.png')

# %%

a = pd.read_csv('data/slow_sample.csv')
b = pd.to_numeric(a['state'], errors='coerce').dropna()
n = b.shape[0]

mlen = 128
c = classic_median(b, mlen)
d = pseudo_median(b, mlen)
e = fir_sinc(b, mlen)
plt.figure()
plt.plot(b, 'k.', label='noisy', markersize=1)
plt.plot(c, label='median')
plt.plot(d, label='pseudo-median')
plt.plot(e, 'g--', label='sinc')
plt.xlim(mlen, n)
plt.ylim(0.9, 1.4)
plt.legend()
plt.savefig('images/slow_sample.png')
