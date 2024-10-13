
## Script de Mantenimiento y Limpieza de Sistema en Linux

Este script está diseñado para realizar mantenimiento y limpieza de sistemas basados en Linux. Automatiza varias tareas comunes de mantenimiento como actualizar paquetes, eliminar archivos temporales, limpiar logs antiguos, y verificar el estado general del sistema.

### Funciones Principales del Script

1. **Archivo de Log**
   - El script crea un archivo de log en `/var/log/system_update_maintenance.log` para registrar todas las operaciones realizadas. Esto permite rastrear el historial de mantenimiento y solucionar posibles errores futuros.

2. **Fecha y Hora**
   - La fecha y hora de inicio del mantenimiento se registran en el log, permitiendo identificar cuándo se ejecutó por última vez el script.

3. **Función `check_status`**
   - Verifica el estado de cada comando ejecutado. Si el comando se ejecuta con éxito, lo registra como `[OK]`. Si ocurre un error, lo marca como `[WARNING]` y continúa con el resto del script.
   - Esto asegura que el script no se detenga en caso de un error, a menos que sea absolutamente necesario.

4. **1. Actualización del Sistema**
   - El script comienza actualizando la lista de repositorios y paquetes mediante el comando `sudo apt update && sudo apt upgrade -y`. Esto garantiza que el sistema esté al día con las últimas versiones de software disponibles.
   - La función `check_status` se utiliza para verificar si la actualización se realizó correctamente.

5. **2. Eliminación de Paquetes No Utilizados**
   - Se ejecuta `sudo apt autoremove -y` para eliminar paquetes y dependencias que ya no son necesarios, lo que libera espacio en disco y mejora el rendimiento.

6. **3. Limpieza de la Caché de APT**
   - Ejecuta `sudo apt clean` para limpiar la caché de APT, lo que elimina archivos innecesarios que podrían estar ocupando espacio.

7. **4. Eliminación de Archivos Temporales**
   - Utiliza el comando `sudo find /tmp -type f -atime +7 -delete` para eliminar archivos temporales que no han sido accedidos en los últimos 7 días. Esto es útil para liberar espacio en la carpeta `/tmp`.

8. **5. Eliminación de Logs Antiguos**
   - El comando `sudo journalctl --vacuum-time=7d` elimina los archivos de logs del sistema que tienen más de 7 días de antigüedad. Esto ayuda a mantener los logs bajo control y evita que consuman mucho espacio en disco.

9. **6. Reparación de Dependencias Rotas**
   - Utiliza `sudo apt --fix-broken install -y` para reparar cualquier dependencia rota en el sistema. Esto asegura que todos los paquetes instalados estén en un estado funcional.

10. **7. Verificación y Reconfiguración de Paquetes**
    - Ejecuta `sudo dpkg --configure -a` para reconfigurar cualquier paquete que haya fallado en el proceso de configuración inicial. Esto es útil cuando hay instalaciones incompletas o fallidas.

11. **8. Verificación de Espacio en Disco**
    - Se utiliza `df -h` para mostrar un resumen del uso de espacio en disco y `du -sh * 2>/dev/null` para listar el espacio ocupado por cada directorio en la carpeta actual. Esto ayuda a identificar qué áreas del sistema están consumiendo más espacio.

12. **9. Reinicio del Sistema**
    - Si el sistema requiere un reinicio después de las actualizaciones, el script lo detecta verificando si existe el archivo `/var/run/reboot-required`. Si es necesario, el script da una advertencia de 30 segundos antes de reiniciar el sistema.
    - Si no se requiere reinicio, el script lo notifica y finaliza el proceso de mantenimiento.

