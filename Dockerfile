FROM hashicorp/terraform:latest

# Instalar dependencias
RUN apk add --no-cache python3 py3-pip bash

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Configurar directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Establecer el punto de entrada
ENTRYPOINT ["python3", "src/main.py"]