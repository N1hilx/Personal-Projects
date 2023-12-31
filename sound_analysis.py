from numpy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numpy as np

# Your list of values
signal_values = [ 1.,          3.15404623,  2.71883628,  2.92089515, -0.65109876,  0.35355339,
 -0.97211852,  2.34883375,  2.02043515,  2.48154772,  0.5,        -1.37255425,
 -0.60822041, -0.50526822,  3.28113552,  2.35355339,  3.60215528,  0.06679319,
  0.09018072, -0.70005573,  1.,          2.70005573,  1.90981928,  1.93320681,
 -1.60215528, -0.35355339, -1.28113552,  2.50526822,  2.60822041,  3.37255425,
  1.5,        -0.48154772, -0.02043515, -0.34883375,  2.97211852,  1.64644661,
  2.65109876, -0.92089515, -0.71883628, -1.15404623,  1.,          3.15404623,
  2.71883628,  2.92089515, -0.65109876,  0.35355339, -0.97211852,  2.34883375,
  2.02043515,  2.48154772,  0.5,        -1.37255425, -0.60822041, -0.50526822,
  3.28113552,  2.35355339,  3.60215528,  0.06679319,  0.09018072, -0.70005573,
  1.,          2.70005573,  1.90981928,  1.93320681, -1.60215528, -0.35355339,
 -1.28113552,  2.50526822,  2.60822041,  3.37255425,  1.5,        -0.48154772,
 -0.02043515, -0.34883375,  2.97211852,  1.64644661,  2.65109876, -0.92089515,
 -0.71883628, -1.15404623,  1.,          3.15404623,  2.71883628,  2.92089515,
 -0.65109876,  0.35355339, -0.97211852,  2.34883375,  2.02043515,  2.48154772,
  0.5,        -1.37255425, -0.60822041, -0.50526822,  3.28113552,  2.35355339,
  3.60215528,  0.06679319,  0.09018072, -0.70005573]

# Sampling rate
sampling_rate = 0.015

# Calculate the number of data points
N = len(signal_values)

# Generate the time values based on the sampling rate
x = np.linspace(0.0, (N-1)*sampling_rate, N, endpoint=False)

# Apply FFT to the signal
yf = fft(signal_values)

# Generate frequency values
xf = fftfreq(N, sampling_rate)[:N//2]

# Plot the spectrum
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
