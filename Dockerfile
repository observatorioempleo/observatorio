# Establecer el directorio de trabajo en /app
WORKDIR /observatorioempleo/observatorio

# Copiar el archivo de requerimientos para instalar dependencias
COPY requirements.txt

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente del proyecto a la imagen Docker
COPY . .

# Exponer el puerto en el que Flask va a correr (por defecto es el 5000)
EXPOSE 8000

# Establecer la variable de entorno para indicar que la aplicación Flask está en modo desarrollo
ENV FLASK_ENV=development

# Comando para correr la aplicación
CMD ["flask", "run", "--host=0.0.0.0"]

# Define the entry point for the container
CMD ["flask", "run", "--host=0.0.0.0"]
