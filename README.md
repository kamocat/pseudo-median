# pseudo-median
A pseudo running-median filter without the lag



A typical median filter, like an FIR filter, has a group delay of 1/2 the window length, which introduces a constant time lag.
This pseudo-median filter instead maintains a window of *sorted* values, adjusting the window bounds to accomodate the new value.
This reduces the processing time per point from O(N^2) to O(N) by starting with a nearly sorted list. More dramatically, it also 
causes the output to lead the input as the bounds of the noise seem to anticipate where the signal is going.

This lead time is not constant, however. It changes with the amplitude of the noise.
Here we have a moderate lead of 50ms when the the standard deviation of the noise is 1/10 the signal amplitude:
![Noise at 1/10 the signal amplitude](images/noise_0.1.png)
It's more like 100ms with the noise at 1/2 the signal amplitude:
![Noise at 1/2 the signal amplitude](images/noise_0.5.png)
And with the noise almost obscuring the signal, the lead is around 200ms, which is greater than the window length.
![Noise at 1x the signal amplitude](images/noise_1.0.png)

You might well wonder why anyone would want a new median filter when the classic approach removes the noise perfectly.
This is the trouble with simulation. I will see about collecting some real data to test.
