# Laboratorio 5: Variabilidad de la Frecuencia Cardiaca usando la Transformada Wavelet

## Introdución: 
En este laboratorio se analizó la variabilidad de la frecuencia cardíaca a partir de señales ECG registradas en un experimento durante 5 minutos, donde el primer minuto correspondió a un estado de frecuencia cardíaca elevada y los siguientes minutos a reposo; el objetivo fue identificar y comparar los cambios en las frecuencias características del ritmo cardíaco por medio de la transformada Wavelet, esta es una herramienta matemática que permite descomponer señales biológicas en el dominio tiempo-frecuencia, facilitando la detección de variaciones rápidas y patrones asociados a la actividad simpática y parasimpática, lo que resulta útil para comprender la dinámica temporal de la señal cardíaca y la respuesta automática del organismo
## Fundamento Teórico:

### Actividad simpática y parasimpática del sistema nervioso autónomo
El sistema nervioso autónomo (SNA) regula funciones involuntarias del cuerpo, como la frecuencia cardíaca, la presión arterial y la digestión. Se divide en dos ramas principales:

- Simpática: Se activa en situaciones de estrés o emergencia (respuesta de lucha o huida), aumentando la frecuencia cardíaca, dilatando las pupilas y desviando el flujo sanguíneo hacia los músculos.

- Parasimpática: Promueve la relajación y el ahorro de energía (respuesta de reposo y digestión), reduciendo la frecuencia cardíaca, estimulando la digestión y promoviendo el descanso.
  
![image](https://github.com/user-attachments/assets/d594d302-1c2b-4ed9-a94c-3ab03cf8148d)


### Efecto de la actividad simpática y parasimpática en la frecuencia cardíaca

La actividad simpática incrementa la frecuencia cardíaca al liberar noradrenalina, que actúa sobre los receptores β1-adrenérgicos del corazón.
La actividad parasimpática disminuye la frecuencia cardíaca a través del nervio vago, liberando acetilcolina que actúa sobre receptores muscarínicos en el nodo sinoauricular.
El equilibrio entre estas dos ramas determina el ritmo basal del corazón y su adaptación frente a estímulos internos o externos.

![image](https://github.com/user-attachments/assets/81a8f0f2-bf9a-4393-9d59-7a64f1cd20a7)

### Variabilidad de la frecuencia cardíaca (HRV)

La HRV es la variación en el tiempo entre latidos cardíacos consecutivos, medido mediante los intervalos R-R en un electrocardiograma (ECG).
Es un marcador no invasivo de la actividad del sistema nervioso autónomo y de la salud cardiovascular.

Frecuencias de interés en HRV:
- Alta frecuencia (HF) (0.15-0.4 Hz): refleja actividad parasimpática. 
- Baja frecuencia (LF) (0.04-0.15 Hz): refleja actividad simpática y parasimpática combinadas.
- Muy baja frecuencia (VLF) (<0.04 Hz): relacionada con mecanismos hormonales y termorregulación.

![image](https://github.com/user-attachments/assets/73099da3-8605-45a2-b2f0-21dd31a0dc2b)

La HRV, medida a través de las fluctuaciones en los intervalos R-R del electrocardiograma, permite analizar la influencia del sistema nervioso autónomo sobre el corazón. Las distintas bandas de frecuencia utilizadas en el análisis de HRV (alta, baja y muy baja frecuencia) proporcionan información valiosa sobre la actividad simpática y parasimpática, y su balance en distintos estados fisiológicos.

Por su parte, el uso de la transformada Wavelet ha permitido un avance significativo en el análisis de señales biológicas. Esta herramienta permite descomponer señales complejas, como las del corazón, en diferentes escalas y frecuencias, facilitando la detección de patrones y cambios que no serían evidentes con otras técnicas. Gracias a su capacidad para trabajar con señales no estacionarias, la transformada Wavelet se ha convertido en un método esencial para el procesamiento y análisis de la HRV y otras señales fisiológicas.

En conjunto, el estudio del sistema nervioso autónomo, la variabilidad de la frecuencia cardíaca y el uso de técnicas modernas de análisis como la transformada Wavelet, no solo amplía nuestra comprensión de la fisiología humana, sino que también mejora las herramientas de diagnóstico y monitoreo en la práctica clínica

## Diagrama de flujo
![image](https://github.com/user-attachments/assets/4580bdea-f575-46fa-8ea0-8af3424bc487)



## Paso a paso:
1. Causar estrés a la persona para aumentar la frecuencia cardiaca.
2. Conectar los electrodos y capturar la señal de ecg.
3. Procesar la señal aplicandole la envolvente y un filtro pasa altas de 20 Hz (filtro IIR).
4. Incluír la aplicación de la transformada Walvet a la señal.
5. Interpretación de los resultados.

## Programación y datos: 
1. Carga de la señal ECG:
Se carga el archivo de la captura de la señal con los datos de 5 minutos de ecg en los que el primero presenta fc alta y luego va disminuyendo hasta llegar a los 5, en el excel se muestra tiempo (eje temporal) y ecg (valores crudos del ECG).

![image](https://github.com/user-attachments/assets/569a6ff7-38ba-487f-a0e6-8f6767c24fe1)


Eliminamos el desplazamiento de la señal con el valor medio. 

![image](https://github.com/user-attachments/assets/ef2a4361-461e-4e7b-a671-4b8866e6a4ae)

Se le aplica un filtro IIR de tipo pasa altas con frecuencia 20 Hz para eliminar los componentes de baja frecuencia como el ruido provocado por el movimiento corporal. 

![image](https://github.com/user-attachments/assets/a3f47cdd-dc56-480f-8dbc-96ec752057a2)

Se le aplica la envolvente de Hilbert con el fin de identificar los picos R. 

![image](https://github.com/user-attachments/assets/b941acad-aaae-482f-a5d5-94ec392b4817)

También la transformada de Fourier para analizar el contenido frecuenaial de la señal filtrada

![image](https://github.com/user-attachments/assets/880e7ab9-78d0-4c5e-a0cb-53b560965ac0)

Por otro lado se genera archivos Excel con datos crudos, filtrados y la envolvente.

![image](https://github.com/user-attachments/assets/051ea1fb-5788-4748-87ce-6772ed0ca7ee)

Estas señales se ven así:

![image](https://github.com/user-attachments/assets/4328d458-fc8b-49e2-8b8f-a16337ec3248)

![image](https://github.com/user-attachments/assets/f96a2589-74b6-448a-8c6b-0dfec529953b)

![image](https://github.com/user-attachments/assets/c19422dd-4a37-41cc-aa14-d1e3196657cb)

Para la detección de los picos R se buscan máximos locales con una distancia mínima de 0.6 s entre picos para evitar falsos positivos. 

![image](https://github.com/user-attachments/assets/04f6073b-af03-4b29-9300-c525b98073d2)

Los cuales se ven así:

![image](https://github.com/user-attachments/assets/579a1114-b13b-4e38-acd0-8f34f1a41f49)

Por último aplicamos la transformada wavelet para analizar los componentes frecuenciales a lo largo del tiempo con un rango de frecuancias de  0.04–0.5 Hz ya que es la banda de interés para HRV. 

![image](https://github.com/user-attachments/assets/bb811ec8-f495-4f52-9f74-c33c435046be)

![image](https://github.com/user-attachments/assets/3fe174ee-0c47-4210-baba-fb82aca518f7)

Se muestra de esta manera:

![image](https://github.com/user-attachments/assets/9097f53d-6d35-49de-8106-a57a6c5801c4)

## Análisis de resultados:
Durante el procesamiento de la señal ECG, se estimó correctamente una frecuencia de muestreo adecuada para análisis cardiaco. Luego, se eliminó el componente DC y se aplicó un filtro pasa altas de 20 Hz, lo cual permitió resaltar de forma más clara los complejos QRS. La obtención de la envolvente mediante la transformada de Hilbert evidenció modulaciones suaves, posiblemente asociadas a la respiración. El análisis en frecuencia a través de la Transformada de Fourier mostró energía distribuida principalmente en bandas del ECG, lo que sugiere una señal de buena calidad. Los picos R fueron detectados con éxito en la señal filtrada, permitiendo calcular los intervalos R-R, cuya media y desviación estándar ofrecen información clave sobre la variabilidad cardíaca (HRV). Finalmente, el análisis tiempo-frecuencia mediante la Transformada Wavelet Continua (CWT) reveló componentes relevantes dentro de las bandas de baja (LF: 0.04–0.15 Hz) y alta frecuencia (HF: 0.15–0.4 Hz), las cuales están relacionadas con la actividad del sistema nervioso autónomo: la banda LF refleja influencia simpática y parasimpática combinadas, mientras que la banda HF se asocia predominantemente a la modulación parasimpática relacionada con la respiración.

## Conclusiones:
El procesamiento realizado permitió extraer información fisiológicamente significativa de la señal ECG. La calidad de la señal filtrada y la correcta detección de picos R permitieron un análisis confiable de la variabilidad del ritmo cardíaco. La HRV obtenida fue coherente con un patrón autónomo estable, y el contenido observado en las bandas LF y HF sugiere una regulación equilibrada entre la actividad simpática y parasimpática del sistema nervioso, lo cual es un indicador positivo de salud cardiovascular. Este tipo de análisis es útil no solo para evaluar el ritmo cardíaco, sino también para interpretar el estado del sistema nervioso autónomo en condiciones de reposo o estrés.











