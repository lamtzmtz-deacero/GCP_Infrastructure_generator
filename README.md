# GCP Infrastructure Generator

## Descripción
Este proyecto proporciona una solución automatizada para el despliegue de infraestructura en Google Cloud Platform (GCP) utilizando Terraform y Docker. Permite definir la infraestructura deseada en un archivo YAML simple y realiza el despliegue de manera automatizada a través de contenedores.

## Estructura del Proyecto
```
.
├── credentials/
│   ├── README.md
│   ├── service-account-template.json
│   └── credentials.json (no incluido en git)
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── src/
│   ├── main.py
│   ├── config_parser.py
│   └── terraform_manager.py
├── .env
├── .env.example
├── .gitignore
├── infrastructure.yaml
├── README.md
└── requirements.txt
```

## Componentes Principales

### 1. Sistema de Configuración
- **infrastructure.yaml**: Define la infraestructura deseada (VMs, redes, subredes)
- **.env**: Configuración de variables de entorno
- **credentials/**: Almacena las credenciales de GCP

### 2. Código Fuente (src/)
- **main.py**: Punto de entrada de la aplicación
- **config_parser.py**: Procesa el archivo YAML y genera configuración de Terraform
- **terraform_manager.py**: Gestiona las operaciones de Terraform

### 3. Contenedorización
- **Dockerfile**: Define la imagen del contenedor
- **docker-compose.yml**: Configura el servicio y sus dependencias

## Requisitos Previos

1. Software necesario:
   - Docker Desktop
   - Git
   - Cuenta de GCP activa

2. Credenciales de GCP:
   - Cuenta de servicio con permisos:
     - Compute Admin
     - Network Admin
     - Service Account User

## Configuración Inicial

1. Clonar el repositorio:
```bash
git clone <url-repositorio>
cd gcp-infrastructure-generator
```

2. Configurar credenciales:
   - Copiar el archivo de credenciales de GCP a `credentials/credentials.json`
   - Seguir las instrucciones en `credentials/README.md`

3. Configurar variables de entorno:
```bash
cp .env.example .env
```
Editar `.env` con tus valores:
```plaintext
GCP_PROJECT_ID=tu-proyecto-id
GCP_REGION=tu-region
GCP_ZONE=tu-zona
GOOGLE_CREDENTIALS=/ruta/completa/a/credentials.json
```

4. Personalizar infraestructura:
   - Editar `infrastructure.yaml` según tus necesidades

## Uso

### Desplegar Infraestructura
```bash
docker compose up
```

### Destruir Infraestructura
```bash
docker compose run terraform destroy
```

## Formato del Archivo infrastructure.yaml

```yaml
machines:
  - name: vm-1
    machine_type: e2-medium
    zone: us-central1-a
    network: default
    boot_disk:
      image: debian-cloud/debian-11
      size_gb: 20

networks:
  - name: custom-network
    auto_create_subnetworks: false
    subnets:
      - name: subnet-1
        region: us-central1
        cidr: 10.0.0.0/24
```

## Solución de Problemas

### Errores Comunes

1. Error de Docker en Windows:
```
error during connect: ... docker client must be run with elevated privileges
```
Solución: Ejecutar PowerShell como administrador

2. Error de credenciales:
```
Error: could not load credentials
```
Solución: Verificar la ruta en GOOGLE_CREDENTIALS y permisos del archivo

## Seguridad

- No compartir o subir credenciales al control de versiones
- Mantener el archivo .env fuera del control de versiones
- Usar los permisos mínimos necesarios en la cuenta de servicio
- Revisar regularmente los permisos y accesos

## Contribuciones

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo `LICENSE` para más detalles.

## Contacto

Tu Nombre - [@tuTwitter](https://twitter.com/tuTwitter) - email@ejemplo.com

Link del Proyecto: [https://github.com/tuusuario/gcp-infrastructure-generator](https://github.com/tuusuario/gcp-infrastructure-generator)