# utiliza una imagen base de Python
FROM python:alpine

# establece el directorio de trabajo en /app
WORKDIR  /app

# copia el contenido del directorio actual al contenedor
COPY . /app

# instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# expone el puerto del contenedor
EXPOSE 5000

# inicia la aplicación Flask usando el servidor web gunicorn
CMD ["gunicorn", "app:app", "-c", "gunicorn.conf.py"]
