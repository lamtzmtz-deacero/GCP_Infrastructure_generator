# Despliegue de Infraestructura en GCP con Terraform y Docker

Este proyecto automatiza el despliegue de infraestructura en Google Cloud Platform (GCP) utilizando Terraform como herramienta de Infrastructure as Code (IaC). Todo el proceso se ejecuta dentro de contenedores Docker para garantizar un entorno consistente y reproducible.

## Descripción General

El proyecto permite desplegar recursos en GCP de forma automatizada mediante archivos de configuración de Terraform. Utiliza una cuenta de servicio de GCP previamente configurada para autenticar y autorizar las operaciones.

## Requisitos Previos

- Docker y Docker Compose instalados en la máquina local
- Una cuenta de GCP activa 
- Una cuenta de servicio de GCP con los siguientes permisos:
  - Compute Admin
  - Service Account User
  - Project IAM Admin
- Archivo de credenciales JSON de la cuenta de servicio

## Estructura del Proyecto

    .
    ├── docker/                  # Archivos relacionados con Docker
    │   ├── Dockerfile          # Definición de la imagen Docker
    │   └── docker-compose.yml  # Configuración de servicios
    ├── terraform/              # Archivos de configuración de Terraform
    │   ├── main.tf            # Configuración principal de recursos
    │   ├── variables.tf       # Definición de variables
    │   └── outputs.tf         # Definición de salidas
    ├── credentials/           # Directorio para credenciales (ignorado por git)
    │   └── gcp-credentials.json
    └── scripts/              # Scripts de utilidad
        └── deploy.sh         # Script de despliegue

## Configuración Inicial

1. **Preparar Credenciales GCP**:
   ```bash
   # Crear directorio de credenciales
   mkdir -p credentials
   
   # Copiar archivo de credenciales
   cp /ruta/a/tu/credencial.json credentials/gcp-credentials.json
   ```

2. **Configurar Variables de Entorno**:
   ```bash
   # Copiar archivo de ejemplo
   cp .env.example .env
   
   # Editar variables
   nano .env
   ```

## Uso

1. **Construir y Levantar Contenedores**:
   ```bash
   docker-compose up --build
   ```

2. **Inicializar Terraform**:
   ```bash
   docker-compose exec terraform init
   ```

3. **Planear Despliegue**:
   ```bash
   docker-compose exec terraform plan
   ```

4. **Aplicar Cambios**:
   ```bash
   docker-compose exec terraform apply
   ```

## Variables de Configuración

Las siguientes variables pueden ser configuradas a través de variables de entorno o en el archivo .env:

```
PROJECT_ID=mi-proyecto-gcp
REGION=us-central1
ZONE=us-central1-a
MACHINE_TYPE=e2-medium
INSTANCE_NAME=mi-instancia
```

## Seguridad

- Las credenciales sensibles se almacenan localmente y nunca se suben al control de versiones
- Los archivos de credenciales requieren permisos restrictivos (600)
- Se utilizan variables de entorno para la configuración sensible
- La cuenta de servicio tiene permisos mínimos necesarios

## Solución de Problemas

1. **Error de Autenticación**:
   - Verificar que el archivo de credenciales existe y tiene los permisos correctos
   - Confirmar que la cuenta de servicio tiene los permisos necesarios
   - Validar que las variables de entorno están configuradas correctamente

2. **Error en el Despliegue**:
   - Revisar los logs de Terraform para identificar el problema
   - Verificar que las variables de entorno son correctas
   - Comprobar conectividad con GCP

## Contribuir

1. Fork del repositorio
2. Crear una rama para tu feature
3. Commit de tus cambios
4. Push a la rama
5. Crear un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.