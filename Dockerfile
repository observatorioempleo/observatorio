# Etapa 1: Construcción de la imagen base con las dependencias necesarias
FROM python:3.9-slim AS build

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY requirements.txt requirements.txt

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: Imagen final, copiado del código fuente
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /observatorioempleo

# Copiar las dependencias instaladas de la etapa build
COPY --from=build /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copiar el código fuente al contenedor
COPY . .

# Exponer el puerto 5000
EXPOSE 5000

# Establecer la variable de entorno para que Flask use el archivo app.py
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
