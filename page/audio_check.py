import librosa
import librosa.display
import matplotlib.pyplot as plt
# Load a wav file
y, sr = librosa.load('C:\\Audio\\26_DTS_44.1KHz_1411.2Kbps_24Bit_2ch.wav', sr=None)
# extract mel spectrogram feature
melspec = librosa.feature.melspectrogram(y, sr, n_fft=1024, hop_length=512, n_mels=128)
# convert to log scale
logmelspec = librosa.power_to_db(melspec)
print(logmelspec.shape)
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
print(mfccs.shape)
plt.figure()
plt.subplot(2, 1, 1)
librosa.display.waveplot(y, sr)
plt.title('Beat wavform')
plt.subplot(2, 1, 2)
librosa.display.specshow(logmelspec, sr=sr, x_axis='time', y_axis='mel')
plt.title('Mel spectrogram')
plt.tight_layout() #保证图不重叠
plt.show()
