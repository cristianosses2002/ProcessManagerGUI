# 🔧 Gestor de Procesos Avanzado - Con Recomendaciones de Seguridad

Un gestor de procesos avanzado para Windows con sistema de recomendaciones de seguridad y optimización para gaming.

## 🚀 Características Principales

### 📊 Gestión de Procesos
- **Monitoreo en tiempo real** de procesos del sistema
- **Terminación segura** y forzada de procesos
- **Filtros avanzados** para buscar procesos específicos
- **Auto-refresh** cada 5 segundos
- **Detalles completos** de cada proceso

### ⚙️ Gestión de Servicios
- **Lista completa** de servicios de Windows
- **Iniciar/Detener** servicios del sistema
- **Desactivar permanentemente** servicios seguros
- **Recomendaciones de seguridad** para cada servicio

### 💡 Sistema de Recomendaciones
- **🟢 Verde**: Servicios muy seguros para desactivar
- **🟡 Amarillo**: Seguros con precaución
- **🔴 Rojo**: CRÍTICOS - No tocar
- **🔵 Azul**: Alto consumo de recursos

### 🎮 Optimización para Gaming
- **Cierre automático** de procesos innecesarios
- **Optimización de memoria** y CPU
- **Limpieza de archivos temporales**
- **Backup automático** del sistema
- **Configuraciones específicas** para gaming

## 📋 Requisitos

- **Windows 10/11**
- **Python 3.7+**
- **psutil** (para monitoreo de procesos)
- **tkinter** (interfaz gráfica)

## 🛠️ Instalación

1. **Clona el repositorio:**
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
python Gestor de Procesos - Versión GUI Beta V.1.py
```

## 🎯 Uso

### Gestión de Procesos
1. Abre la pestaña "🔍 Procesos"
2. Selecciona un proceso de la lista
3. Usa "❌ Terminar" para cierre seguro o "⚠️ Forzar" para cierre forzado
4. Activa "Auto-refrescar" para monitoreo continuo

### Optimización para Gaming
1. Ve a la pestaña "🚀 Optimización"
2. Click en "🎯 Optimización Completa Gaming"
3. La aplicación:
   - Crea un backup del sistema
   - Cierra procesos innecesarios
   - Limpia archivos temporales
   - Optimiza memoria y CPU

### Gestión de Servicios
1. Abre la pestaña "⚙️ Servicios"
2. Selecciona un servicio
3. Usa "⏹️ Detener", "▶️ Iniciar" o "🚫 Desactivar"
4. Consulta las recomendaciones de seguridad

## 🛡️ Características de Seguridad

### Protecciones Integradas
- **Verificación de procesos críticos** antes de terminar
- **Confirmaciones** antes de acciones peligrosas
- **Backup automático** antes de optimizaciones
- **Sistema de recomendaciones** basado en seguridad

### Procesos Críticos (NO tocar)
- `Winlogon` - Inicio de sesión de Windows
- `csrss` - Client Server Runtime Process
- `wininit` - Inicialización de Windows
- `services` - Service Control Manager
- `lsass` - Local Security Authority
- `smss` - Session Manager
- `explorer` - Windows Explorer

## 📊 Procesos Optimizados para Gaming

### Navegadores
- Chrome, Firefox, Edge, Opera, Brave

### Comunicación
- Discord, Teams, Skype, Zoom, Slack

### Multimedia
- Spotify, iTunes, VLC, Media Player

### Productividad
- Outlook, Thunderbird, OneDrive, Dropbox

### Gaming
- Steam, Origin, Uplay, Epic Games Launcher

### Software de Hardware
- NVIDIA GeForce Experience, AMD Software
- MSI Afterburner, Corsair iCUE, NZXT CAM
- Logitech Gaming Software, Razer Synapse

## 🔧 Configuración Avanzada

### Optimizaciones Automáticas
- **Limpieza de archivos temporales**
- **Optimización de memoria**
- **Desfragmentación del registro**
- **Configuración de energía para alto rendimiento**

### Servicios Desactivados para Gaming
- `SysMain` - Superfetch
- `WSearch` - Windows Search
- `Themes` - Temas visuales
- `TabletInputService` - Tablet PC Input
- `Fax` - Servicio de fax
- `TapiSrv` - Telephony

## 📁 Estructura del Proyecto

```
gestor-procesos-avanzado/
├── test.py                 # Aplicación principal
├── requirements.txt        # Dependencias
├── README.md              # Este archivo
├── LICENSE                # Licencia
├── .gitignore            # Archivos a ignorar
└── docs/                 # Documentación adicional
    └── screenshots/      # Capturas de pantalla
```

## 🚨 Advertencias Importantes

⚠️ **IMPORTANTE**: 
- Crea un punto de restauración antes de usar
- No cierres procesos críticos del sistema
- Usa las recomendaciones de seguridad
- Haz backup antes de optimizaciones

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- **psutil** - Para el monitoreo de procesos
- **tkinter** - Para la interfaz gráfica
- **Microsoft** - Por la documentación de Windows
- **Comunidad de GitHub** - Por el apoyo y contribuciones

## 📞 Soporte

Si tienes problemas o preguntas:

1. Revisa los [Issues](https://github.com/CristianOsses/gestor-procesos-avanzado/issues)
2. Crea un nuevo Issue si no encuentras solución
3. Contacta al desarrollador

## 🔄 Historial de Versiones

### v1.0.0 (2025-01-XX)
- ✅ Gestión básica de procesos
- ✅ Sistema de recomendaciones
- ✅ Optimización para gaming
- ✅ Gestión de servicios
- ✅ Backup automático
- ✅ Interfaz gráfica completa

---

**⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!** 
