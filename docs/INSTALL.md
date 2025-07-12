# Guía de Instalación

## 📋 Requisitos Previos

### Sistema Operativo
- **Windows 10** (versión 1903 o superior)
- **Windows 11** (cualquier versión)

### Python
- **Python 3.7** o superior
- **pip** (incluido con Python)

### Permisos
- **Administrador** (recomendado para todas las funcionalidades)
- **Usuario normal** (funcionalidades limitadas)

## 🛠️ Instalación

### Método 1: Instalación Directa

1. **Descarga el proyecto:**
```bash
git clone https://github.com/CristianOsses/gestor-procesos-avanzado.git
cd gestor-procesos-avanzado
```

2. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecuta la aplicación:**
```bash
python test.py
```

### Método 2: Instalación con pip

```bash
pip install gestor-procesos-avanzado
```

### Método 3: Instalación desde código fuente

```bash
git clone https://github.com/CristianOsses/gestor-procesos-avanzado.git
cd gestor-procesos-avanzado
pip install -e .
```

## 🔧 Configuración

### Configuración Inicial

1. **Ejecuta como Administrador** (recomendado):
   - Click derecho en el ejecutable
   - "Ejecutar como administrador"

2. **Permisos de Windows:**
   - Permite acceso cuando Windows lo solicite
   - Confirma las acciones de seguridad

3. **Configuración de Firewall:**
   - Permite la aplicación en el firewall
   - Confirma las conexiones de red

### Configuración Avanzada

#### Variables de Entorno

```bash
# Configurar directorio de backups
set GAMING_BACKUP_DIR=C:\Backups\Gaming

# Configurar nivel de logging
set LOG_LEVEL=INFO

# Configurar auto-refresh (en segundos)
set AUTO_REFRESH_INTERVAL=5
```

#### Archivo de Configuración

Crea un archivo `config.json` en el directorio del proyecto:

```json
{
    "backup_directory": "C:\\Backups\\Gaming",
    "auto_refresh_interval": 5,
    "log_level": "INFO",
    "gaming_processes": [
        "chrome.exe",
        "discord.exe",
        "spotify.exe"
    ],
    "critical_processes": [
        "winlogon.exe",
        "csrss.exe",
        "services.exe"
    ]
}
```

## 🚀 Primeros Pasos

### 1. Verificar Instalación

```bash
python test.py --version
```

### 2. Ejecutar en Modo Prueba

```bash
python test.py --test-mode
```

### 3. Verificar Permisos

La aplicación verificará automáticamente:
- Permisos de administrador
- Acceso a procesos del sistema
- Permisos de servicios de Windows

## 🔍 Solución de Problemas

### Error: "psutil no encontrado"

```bash
pip install psutil
```

### Error: "tkinter no disponible"

En Windows, tkinter viene incluido con Python. Si falta:

```bash
# Reinstalar Python con tkinter
# O usar una distribución que incluya tkinter
```

### Error: "Permisos insuficientes"

1. **Ejecutar como Administrador**
2. **Verificar políticas de grupo**
3. **Desactivar temporalmente antivirus**

### Error: "No se pueden listar servicios"

1. **Verificar permisos de administrador**
2. **Comprobar que el servicio está ejecutándose**
3. **Reiniciar el servicio de Windows**

### Error: "No se puede crear backup"

1. **Verificar espacio en disco**
2. **Comprobar permisos de escritura**
3. **Desactivar temporalmente antivirus**

## 📊 Verificación de Instalación

### Comandos de Verificación

```bash
# Verificar Python
python --version

# Verificar dependencias
pip list | grep psutil

# Verificar permisos
python -c "import psutil; print('psutil OK')"

# Verificar tkinter
python -c "import tkinter; print('tkinter OK')"
```

### Pruebas Automáticas

```bash
# Ejecutar tests
python test.py --run-tests

# Verificar funcionalidades
python test.py --check-features
```

## 🔄 Actualización

### Actualizar desde Git

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

### Actualizar con pip

```bash
pip install gestor-procesos-avanzado --upgrade
```

## 🗑️ Desinstalación

### Desinstalar con pip

```bash
pip uninstall gestor-procesos-avanzado
```

### Limpiar archivos

```bash
# Eliminar backups
rmdir /s "C:\Users\%USERNAME%\Desktop\Gaming_Backups"

# Eliminar configuraciones
del config.json
```

## 📞 Soporte

### Logs de Error

Los logs se guardan en:
```
%APPDATA%\gestor-procesos-avanzado\logs\
```

### Información del Sistema

Para reportar problemas, incluye:
- Versión de Windows
- Versión de Python
- Logs de error
- Capturas de pantalla

### Contacto

- **Issues**: [GitHub Issues](https://github.com/CristianOsses/gestor-procesos-avanzado/issues)
- **Discusiones**: [GitHub Discussions](https://github.com/CristianOsses/gestor-procesos-avanzado/discussions)
- **Email**: cristian.osses@ejemplo.com

---

**¡Instalación completada!** 🎉 