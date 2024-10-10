Resumen del Script de Mantenimiento y Actualización de Kali Linux
Este script realiza una serie de tareas de mantenimiento y actualización en Kali Linux para asegurar que el sistema esté optimizado y libre de problemas. A continuación se detalla la funcionalidad de cada sección del script:

1. Registro de Actividades
LOG_FILE: Define la ubicación del archivo de log (/var/log/system_update_maintenance.log) donde se registran todas las actividades del script.
DATE: Obtiene y muestra la fecha y hora actual al iniciar el mantenimiento.
2. Función check_status
Descripción: Verifica el estado de cada comando ejecutado.
Funcionalidad:
Si el comando se ejecuta correctamente ($? -eq 0), registra un mensaje de éxito en la terminal y en el archivo de log.
Si hay un error, registra una advertencia pero permite que el script continúe.
3. Actualización de Repositorios y Paquetes
Comando: sudo apt update && sudo apt upgrade -y
Descripción: Actualiza la lista de paquetes disponibles y realiza la actualización de los paquetes instalados.
4. Actualización del Kernel
Comando: sudo apt dist-upgrade -y
Descripción: Actualiza el kernel y otros paquetes del sistema, manejando dependencias de manera más efectiva que upgrade.
5. Limpieza de Paquetes Innecesarios
Comandos:
sudo apt autoremove -y
sudo apt autoclean -y
Descripción: Elimina paquetes y dependencias que ya no son necesarios y limpia los archivos .deb obsoletos.
6. Reparación de Dependencias Rojas
Comando: sudo apt --fix-broken install -y
Descripción: Intenta corregir problemas de dependencias rotas que puedan haber surgido.
7. Verificación y Reconfiguración de Paquetes
Comando: sudo dpkg --configure -a
Descripción: Verifica y reconfigura paquetes para asegurarse de que estén correctamente instalados.
8. Limpieza de Caché de APT
Comando: sudo rm -rf /var/cache/apt/archives/*.deb
Descripción: Elimina archivos de caché de APT para liberar espacio en disco.
9. Verificación del Sistema de Archivos
Comando: sudo fsck -Af -M
Descripción: Verifica y corrige errores en el sistema de archivos, asegurando la integridad del sistema.
10. Trim en SSD
Comando: sudo fstrim -v /
Descripción: Realiza una operación de "trim" en discos SSD para liberar espacio no utilizado, mejorando el rendimiento.
11. Verificación de Reinicio
Descripción: Comprueba si se requiere un reinicio del sistema al buscar el archivo /var/run/reboot-required.
Funcionalidad: Si se requiere un reinicio, el script lo ejecuta después de 30 segundos. Si no, notifica al usuario que no es necesario reiniciar.
12. Finalización
Descripción: Muestra un mensaje final indicando que el mantenimiento del sistema se ha completado exitosamente.
