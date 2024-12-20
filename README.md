# Despliegue de Infraestructura en GCP con Terraform y Docker

## Descripción
Este proyecto automatiza el despliegue de máquinas virtuales y redes en Google Cloud Platform (GCP) utilizando Terraform. La infraestructura se define en archivos YAML y se despliega a través de contenedores Docker usando Docker Compose.

## Características

- Despliegue automatizado de VMs en GCP usando Terraform
- Configuración de redes y subredes
- Gestión de credenciales segura usando cuenta de servicio de GCP
- Infraestructura como código usando archivos YAML
- Contenerización del proceso usando Docker y Docker Compose

## Prerequisitos

- Cuenta de GCP activa
- Cuenta de servicio de GCP con los siguientes permisos:
    - Compute Admin
    - Network Admin
    - Service Account User
- Archivo de credenciales de la cuenta de servicio (.json)
- Docker y Docker Compose instalados
- Terraform CLI instalado (opcional, se ejecutará desde el contenedor)

## Estructura del Proyecto

    .
    ├── README.md
    ├── docker/
    │   ├── Dockerfile         # Imagen con Terraform y dependencias
    │   └── docker-compose.yml # Configuración de servicios
    ├── infrastructure.yaml    # Definición de infraestructura
    ├── src/                   # Código fuente
    ├── .env.example          # Variables de entorno de ejemplo
    └── .gitignore

## Configuración

1. Copia el archivo `.env.example` a `.env` y configura las variables:
```plaintext
    GCP_PROJECT_ID=tu-proyecto-id
    GCP_REGION=tu-region
    GCP_ZONE=tu-zona
    GOOGLE_CREDENTIALS=/path/to/service-account.json
```
2. Coloca tu archivo de credenciales de la cuenta de servicio en la ubicación especificada

3. Define tu infraestructura en el archivo `infrastructure.yaml`:
    ```yaml
    machines:
      - name: vm-1
        machine_type: e2-medium
        zone: us-central1-a
        network: default
        
    networks:
      - name: custom-network
        auto_create_subnetworks: false
        subnets:
          - name: subnet-1
            region: us-central1
            cidr: 10.0.0.0/24    ```

## Uso

1. Inicia el despliegue:    ```bash
    docker compose up    ```

2. Para destruir la infraestructura:    ```bash
    docker compose run terraform destroy    ```

## Notas de Seguridad

- Nunca compartas o subas al control de versiones tu archivo de credenciales
- Utiliza variables de entorno para información sensible
- Asegúrate de que la cuenta de servicio tenga los permisos mínimos necesarios

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.