import os
import yaml
from terraform_manager import TerraformManager
from config_parser import ConfigParser

def main():
    # Cargar configuración de infraestructura
    with open('infrastructure.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    # Inicializar el parser de configuración
    parser = ConfigParser(config)
    
    # Generar archivos de Terraform
    tf_config = parser.generate_terraform_config()
    
    # Inicializar el gestor de Terraform
    tf_manager = TerraformManager()
    
    # Ejecutar Terraform
    tf_manager.init()
    tf_manager.apply()

if __name__ == "__main__":
    main() 