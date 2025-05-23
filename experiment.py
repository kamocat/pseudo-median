# -*- coding: utf-8 -*-
"""
Created on Wed May 21 17:03:49 2025

@author: Marshal
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fft, signal as sig
import random

fs = 1000
f1,f2 = .1,1
duration = 5
t = np.arange(0,duration,1/fs)
n = t.shape[0]
noise = np.random.normal(size=n)
a = sig.chirp(t, f2,duration, f1, method='log')
b = a + noise

def analyze(t,a,b,c):
    # Time series comparison
    plt.figure()
    plt.plot(t,a, label='original')
    #plt.plot(t,b, 'r,', label='noisy')
    plt.plot(t,c, label='filtered')
    plt.legend()

    # Frequency domain comparison
    plt.figure()
    freqs = fft.fftfreq(n, 1/fs)[:n//2]
    x,y,z = [fft.fft(x)[:n//2] for x in [a,b,c]]
    #plt.semilogy(freqs, np.abs(y), label="noisy")
    plt.semilogy(freqs, np.abs(z), label="filtered")
    plt.semilogy(freqs, np.abs(x), label="original")
    plt.legend()

    # Group delay measurement
    s1 = np.argmin(np.abs(freqs-f1))
    s2 = np.argmin(np.abs(freqs-f2))
    phase = np.angle(x) - np.angle(z)
    delay = np.unwrap(phase) / (2*np.pi*freqs) * fs/mlen
    plt.figure()
    plt.plot(freqs[s1:s2], delay[s1:s2])

# %%
# Brute force solution
def classic_median(x, mlen=128)
    return [np.median(b[i:i+mlen]) for i in range(n)]

# %%

def pseudo_median(x, mlen=128):
    arr = np.linspace(-0.1,0.1,mlen)
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

# %%
def compare_noise(amp):
    fs = 1000
    f1,f2 = .1,1
    duration = 5
    t = np.arange(0,duration,1/fs)
    n = t.shape[0]
    noise = np.random.normal(size=n) * amp
    a = sig.chirp(t, f2,duration, f1, method='log')
    b = a + noise
    mlen = 128
    c = [np.median(b[i:i+mlen]) for i in range(n)]
    d = pseudo_median(b, mlen)
    fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)
    plt.title("Comparison of running median")
    ax1.plot(t,b, label='signal with noise')
    ax1.legend()
    [ax2.plot(t,x) for x in [a,c,d]]
    ax2.legend(['original', 'median', 'pseudo-median'])
    plt.savefig(f'noise_{amp:0.1f}.png')

[compare_noise(x) for x in [1,0.5,0.1]]
