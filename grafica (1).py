import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, hilbert
from scipy.fft import fft, fftfreq
import xlsxwriter
from scipy.signal import find_peaks
import pywt
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


# === Cargar archivo ===
archivo = r"C:\Users\majo1\OneDrive\Escritorio\señales\lab señales\lab 4\ecg_data.csv"
datos = np.loadtxt(archivo, delimiter=",", skiprows=1)

tiempo = datos[:, 0]
ecg = datos[:, 1]

# === Frecuencia de muestreo ===
fs = int(1 / (tiempo[1] - tiempo[0]))
print(f"Frecuencia de muestreo estimada: {fs} Hz")

# === Remover DC ===
ecg_sin_dc = ecg - np.mean(ecg)

# === Filtro pasa altas ===
def filtro_pasa_altas(senal, fs, corte=20, orden=4):
    nyquist = 0.5 * fs
    normal = corte / nyquist
    b, a = butter(orden, normal, btype='highpass')
    return filtfilt(b, a, senal)

ecg_filtrada = filtro_pasa_altas(ecg_sin_dc, fs)

# === Envolvente de Hilbert ===
envolvente = np.abs(hilbert(ecg_filtrada))

# === Espectro FFT ===
N = len(ecg_filtrada)
frecuencias = fftfreq(N, 1/fs)[:N//2]
magnitudes = np.abs(fft(ecg_filtrada))[:N//2]

# === Guardar Excel ===
def guardar_excel(nombre_archivo, tiempo, señal, nombre_columna):
    workbook = xlsxwriter.Workbook(nombre_archivo)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "Tiempo (s)")
    worksheet.write(0, 1, nombre_columna)
    for i in range(len(tiempo)):
        worksheet.write(i + 1, 0, tiempo[i])
        worksheet.write(i + 1, 1, señal[i])
    workbook.close()

guardar_excel("ecg_original.xlsx", tiempo, ecg, "ECG Original")
guardar_excel("ecg_filtrada.xlsx", tiempo, ecg_filtrada, "ECG Filtrada")
guardar_excel("envolvente.xlsx", tiempo, envolvente, "Envolvente")

print("Archivos Excel generados correctamente.")

# === GRAFICAR señal original + envolvente para los 300 s ===
plt.figure(figsize=(20, 4))  # más ancho para más resolución
plt.plot(tiempo, ecg, label="Original", color='gray', linewidth=0.5, alpha=0.7)
plt.plot(tiempo, envolvente, label="Envolvente Hilbert", color='red', linewidth=1)
plt.title("Señal ECG + Envolvente (300 segundos)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# === GRAFICAR señal filtrada ===
plt.figure(figsize=(20, 4))
plt.plot(tiempo, ecg_filtrada, color='orange', linewidth=0.6)
plt.title("Señal ECG Filtrada (Pasa Altas desde 20 Hz)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)
plt.tight_layout()
plt.show()

# === GRAFICAR FFT ===
plt.figure(figsize=(12, 4))
plt.plot(frecuencias, magnitudes, color='blue')
plt.title("Transformada de Fourier")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid(True)
plt.tight_layout()
plt.show()

# === 1. Identificación de picos R ===
# Se asume que el ECG filtrado tiene picos positivos representativos
picos_R, _ = find_peaks(ecg_filtrada, distance=fs*0.6, height=np.mean(ecg_filtrada) + 0.5*np.std(ecg_filtrada))
tiempos_R = tiempo[picos_R]
intervalos_RR = np.diff(tiempos_R)

# === 2. HRV en el dominio del tiempo ===
media_RR = np.mean(intervalos_RR)
std_RR = np.std(intervalos_RR)
print(f"Media de intervalos R-R: {media_RR:.4f} s")
print(f"Desviación estándar de intervalos R-R: {std_RR:.4f} s")

# === Graficar picos R sobre la señal filtrada ===
plt.figure(figsize=(20, 4))
plt.plot(tiempo, ecg_filtrada, label='ECG Filtrada', color='orange')
plt.plot(tiempos_R, ecg_filtrada[picos_R], 'rx', label='Picos R')
plt.title("Detección de Picos R")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
# === Verifica que la señal no esté vacía ===
plt.figure()
plt.plot(tiempo, ecg_filtrada)
plt.title("Señal ECG Filtrada")
plt.xlabel("Tiempo (s)")
plt.grid(True)
plt.show()

frecuencia_min = 0.04  
frecuencia_max = 0.5    
num_frecuencias = 50   
escala_color_max = None 


frequencies = np.linspace(frecuencia_min, frecuencia_max, num_frecuencias)
scales = (1 / pywt.scale2frequency('cmor1.5-1.0', frequencies)) * fs
scales = scales[np.isfinite(scales)] 

print(f"Escalas generadas: {scales[:5]} ... Total: {len(scales)}")
# Submuestreo para reducir la carga de memoria
factor = 10
tiempo = tiempo[::factor]
ecg_filtrada = ecg_filtrada[::factor]
fs = fs // factor  # Ajustar frecuencia de muestreo
# Cortar la señal a 120 segundos
max_tiempo = 120
indices = tiempo < max_tiempo
tiempo = tiempo[indices]
ecg_filtrada = ecg_filtrada[indices]

# === TRANSFORMADA WAVELET ===
coef, _ = pywt.cwt(ecg_filtrada, scales, 'cmor1.5-1.0', sampling_period=1/fs)

# === GRAFICAR CWT ===
plt.figure(figsize=(16, 6))
plt.imshow(np.abs(coef), extent=[tiempo[0], tiempo[-1], frequencies[-1], frequencies[0]],
           aspect='auto', cmap='jet', origin='upper', vmin=0, vmax=escala_color_max)
plt.colorbar(label='Magnitud')
plt.title("Transformada Wavelet Continua (Hz)")
plt.ylabel("Frecuencia (Hz)")
plt.xlabel("Tiempo (s)")
plt.tight_layout()
plt.show()
