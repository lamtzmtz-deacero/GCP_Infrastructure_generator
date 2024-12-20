# Credenciales de GCP

Este directorio es donde debes colocar tu archivo de credenciales de la cuenta de servicio de Google Cloud Platform.

## Instrucciones

1. Ve a la consola de GCP (https://console.cloud.google.com)
2. Navega a "IAM & Admin" > "Service Accounts"
3. Crea una nueva cuenta de servicio o selecciona una existente
4. Genera una nueva clave en formato JSON
5. Descarga el archivo de credenciales
6. Renómbralo a `credentials.json` y colócalo en este directorio

## Importante

- NO subas el archivo real de credenciales al control de versiones
- Mantén el archivo de credenciales seguro y no lo compartas
- El archivo `service-account-template.json` es solo una plantilla para referencia
- Asegúrate de que la cuenta de servicio tenga los permisos necesarios:
  - Compute Admin
  - Network Admin
  - Service Account User

## Estructura del archivo de credenciales

El archivo de credenciales debe tener una estructura similar a la mostrada en `service-account-template.json`. 