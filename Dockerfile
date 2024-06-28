# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido de la carpeta actual al contenedor en /app
COPY . .

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Define el comando por defecto para ejecutar la aplicación
CMD ["python", "ProyectoWeb/manage.py", "runserver", "0.0.0.0:8000"]
