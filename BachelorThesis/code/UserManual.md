# Manual de Uso del Software

Este manual proporciona instrucciones detalladas para el uso del software que has desarrollado. Siga las instrucciones cuidadosamente para asegurar una correcta instalación y uso del sistema.

## 1. Acceso a Bases de Datos

Para utilizar este software, el usuario debe tener acceso a dos bases de datos específicas:

### 1.1 First Impressions V2 (CVPR'17)
Para obtener acceso a la base de datos First Impressions V2 (CVPR'17):
- Crea y verifica una cuenta en [este enlace](https://chalearnlap.cvc.uab.cat/dataset/24/description/#).

### 1.2 DAIC-WOZ Database
Para obtener acceso a la base de datos DAIC-WOZ:
- Rellena un formulario disponible en [este enlace](https://dcapswoz.ict.usc.edu/), el cual será enviado a la institución responsable del mantenimiento de la base de datos, la Universidad del Sur de California (USC).
- La solicitud será aprobada o denegada. Si es aprobada, recibirás un correo electrónico con una URL para la descarga de la base de datos.

## 2. Instalación de Dependencias

El sistema cuenta con un fichero `requirements.txt` que contiene las dependencias necesarias. Para instalar las dependencias, ejecute el siguiente comando en el directorio donde se pretende ejecutar el sistema:

```bash
$ pip install -r requirements.txt
```

Esto garantizará que todas las librerías y paquetes estén en las versiones correctas para el funcionamiento adecuado del software.

## 3. Estructura del Código

El código está organizado en tres subdirectorios principales:

### 3.1 VisualFeatures

Este directorio contiene cuatro archivos:
- `extraction_openface.py`: Para la extracción de los Action Units usando OpenFace 2.0.
- `extraction_pyfeat.ipynb`: Para la extracción de los Action Units usando Py-Feat.
- `py_of_comparison.ipynb`: Para realizar la comparación estadística entre OpenFace y Py-Feat.
- `random_sampling_first_impressions.ipynb`: Para realizar una selección aleatoria del subset balanceado de videos de la base de datos First Impressions V2 (CVPR'17).

### 3.2 AudioFeatures

Este directorio contiene dos archivos:
- `preprocessing_audio.ipynb`: Para realizar el preprocesado del audio de las consultas clínicas.
- `fusion_video_audio.ipynb`: Para concatenar las características de las modalidades de video y audio.

### 3.3 Modelling

Este directorio contiene dos archivos:
- `daic_woz_statistics.ipynb`: Para extraer las características de la base de datos DAIC-WOZ.
- `model_evaluation.ipynb`: Define la arquitectura del modelo y carga los pesos del modelo entrenado. Nota: Los pesos del modelo no se adjuntan debido a su gran tamaño (> 1GB).

## 4. Uso de Archivos

Todos los archivos están diseñados para ser fácilmente legibles y pueden ser utilizados como puntos de partida para otros proyectos. Se recomienda revisar y comprender cada archivo antes de su ejecución para asegurar su correcta implementación en proyectos futuros.

---

Si tiene alguna pregunta o necesita más información, no dude en contactarnos.
