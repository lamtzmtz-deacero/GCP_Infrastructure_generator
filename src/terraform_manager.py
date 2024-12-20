import subprocess
import os

class TerraformManager:
    def __init__(self):
        self.terraform_dir = "terraform"
        
    def init(self):
        """Inicializa Terraform"""
        subprocess.run(["terraform", "init"], check=True)
        
    def apply(self):
        """Aplica la configuración de Terraform"""
        subprocess.run(["terraform", "apply", "-auto-approve"], check=True)
        
    def destroy(self):
        """Destruye la infraestructura"""
        subprocess.run(["terraform", "destroy", "-auto-approve"], check=True) 