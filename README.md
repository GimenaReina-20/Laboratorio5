# Laboratorio 5: Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet

## Introdución: 
En este laboratorio se analizó la variabilidad de la frecuencia cardíaca a partir de señales ECG registradas en un experimento durante 5 minutos, donde el primer minuto correspondió a un estado de frecuencia cardíaca elevada y los siguientes minutos a reposo; el objetivo fue identificar y comparar los cambios en las frecuencias características del ritmo cardíaco por medio de la transformada Wavelet, esta es una herramienta matemática que permite descomponer señales biológicas en el dominio tiempo-frecuencia, facilitando la detección de variaciones rápidas y patrones asociados a la actividad simpática y parasimpática, lo que resulta útil para comprender la dinámica temporal de la señal cardíaca y la respuesta automática del organismo

## Paso a paso:
1. Causar estrés a la persona para aumentar la frecuencia cardiaca.
2. Conectar los electrodos y capturar la señal de ecg.
3. Procesar la señal aplicandole la envolvente y un filtro pasa altas de 20 Hz (filtro IIR).
4. Incluír la aplicación de la transformada Walvet a la señal.
5. Interpretación de los resultados.

## Programación y datos: 
1. Carga de la señal ECG:
Se carga el archivo de la captura de la señal con los datos de 5 minutos de ecg en los que el primero presenta fc alta y luego va disminuyendo hasta llegar a los 5, en el excel se muestra tiempo (eje temporal) y ecg (valores crudos del ECG).

archivo = r"C:\Users\majo1\OneDrive\Escritorio\señales\lab señales\lab 4\ecg_data.csv"
datos = np.loadtxt(archivo, delimiter=",", skiprows=1)

tiempo = datos[:, 0]
ecg = datos[:, 1]

Eliminamos el desplazamiento de la señal con el valor medio. 

ecg_sin_dc = ecg - np.mean(ecg)

Se le aplica un filtro IIR de tipo pasa altas con frecuencia 20 Hz para eliminar los componentes de baja frecuencia como el ruido provocado por el movimiento corporal. 

def filtro_pasa_altas(...):
    # Diseña filtro Butterworth
    b, a = butter(orden, normal, btype='highpass')
    return filtfilt(b, a, senal)

Se le aplica la envolvente de Hilbert con el fin de identificar los picos R. 

envolvente = np.abs(hilbert(ecg_filtrada))

También la transformada de Fourier para analizar el contenido frecuenaial de la señal filtrada

magnitudes = np.abs(fft(ecg_filtrada))[:N//2]

Por otro lado se genera archivos Excel con datos crudos, filtrados y la envolvente.

guardar_excel("ecg_original.xlsx", tiempo, ecg, "ECG Original")

Estas señales se ven así:

![image](https://github.com/user-attachments/assets/4328d458-fc8b-49e2-8b8f-a16337ec3248)

![image](https://github.com/user-attachments/assets/f96a2589-74b6-448a-8c6b-0dfec529953b)

![image](https://github.com/user-attachments/assets/c19422dd-4a37-41cc-aa14-d1e3196657cb)

Para la detección de los picos R se buscan máximos locales con una distancia mínima de 0.6 s entre picos para evitar falsos positivos. 

picos_R, _ = find_peaks(ecg_filtrada, distance=fs*0.6, ...)

![image](https://github.com/user-attachments/assets/579a1114-b13b-4e38-acd0-8f34f1a41f49)

Por último aplicamos la transformada wavelet para analizar los componentes frecuenciales a lo largo del tiempo con un rango de frecuancias de  0.04–0.5 Hz ya que es la banda de interés para HRV. 

coef, _ = pywt.cwt(ecg_filtrada, scales, 'cmor1.5-1.0', ...)

![image](https://github.com/user-attachments/assets/9097f53d-6d35-49de-8106-a57a6c5801c4)[

## Análisis de resultados:


## Conclusiones:

## Referencias:










