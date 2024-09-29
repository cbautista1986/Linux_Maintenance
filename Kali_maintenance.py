# Actualización y Mantenimiento de Kali Linux

# Archivo de log
LOG_FILE="/var/log/system_update_maintenance.log"

# Fecha y hora actual
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "===================================="
echo "Mantenimiento de sistema iniciado: $DATE"

# Función para verificar si un comando fue exitoso
check_status() {
    if [ $? -eq 0 ]; then
        echo "[OK] $1 completado." | tee -a $LOG_FILE
    else
        echo "[WARNING] Ocurrió un problema con $1, pero el script continuará." | tee -a $LOG_FILE
        # Eliminar 'exit 1' para que el script no se detenga en caso de error.
    fi
}

# Actualizar lista de paquetes y el sistema
echo "Actualizando repositorios y paquetes..."
sudo apt update && sudo apt upgrade -y  true
check_status "Actualización de repositorios y paquetes"

# Actualización de kernel (si es necesario)
echo "Actualizando el kernel (si es necesario)..."
sudo apt dist-upgrade -y  true
check_status "Actualización del kernel"

# Limpiar paquetes innecesarios
echo "Limpiando paquetes y dependencias no utilizadas..."
sudo apt autoremove -y  true
sudo apt autoclean -y  true
check_status "Limpieza de paquetes"

# Reparar dependencias rotas
echo "Reparando dependencias rotas..."
sudo apt --fix-broken install -y  true
check_status "Reparación de dependencias"

# Verificar y reconfigurar paquetes
echo "Verificando y reconfigurando paquetes..."
sudo dpkg --configure -a  true
check_status "Reconfiguración de paquetes"

# Limpiar caché de APT
echo "Limpiando caché de APT..."
sudo rm -rf /var/cache/apt/archives/*.deb  true
check_status "Limpieza de caché de APT"

# Verificación del sistema de archivos
echo "Verificando y corrigiendo errores en el sistema de archivos..."
sudo fsck -Af -M  true
check_status "Verificación del sistema de archivos"

# Trim en SSD para liberar espacio en discos SSD (si es necesario)
echo "Realizando trim en discos SSD (si aplica)..."
sudo fstrim -v / || true
check_status "Liberación de espacio en SSD con fstrim"

# Verificar si se requiere reiniciar el sistema
if [ -f /var/run/reboot-required ]; then
    echo "Se requiere reiniciar el sistema para completar las actualizaciones."
    echo "Reiniciando el sistema en 30 segundos..."
    sleep 30
    sudo reboot
else
    echo "No se requiere reiniciar el sistema."
fi

echo "Mantenimiento del sistema completado exitosamente."