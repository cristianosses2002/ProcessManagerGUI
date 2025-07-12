# Guía de Uso

## 🚀 Inicio Rápido

### Ejecutar la Aplicación

```bash
python test.py
```

### Interfaz Principal

La aplicación tiene 4 pestañas principales:

1. **🔍 Procesos** - Gestión de procesos del sistema
2. **⚙️ Servicios** - Gestión de servicios de Windows
3. **💡 Recomendaciones** - Servicios seguros para desactivar
4. **🚀 Optimización** - Optimización para gaming

## 📊 Gestión de Procesos

### Ver Procesos

1. **Abre la pestaña "🔍 Procesos"**
2. **Los procesos se muestran ordenados por CPU**
3. **Información mostrada:**
   - PID (ID del proceso)
   - Nombre del proceso
   - Usuario que lo ejecuta
   - Uso de CPU (%)
   - Uso de memoria (%)
   - Estado del proceso
   - Recomendación de seguridad

### Filtrar Procesos

1. **Usa el campo "Filtrar"** en la parte superior
2. **Escribe el nombre del proceso** que buscas
3. **La lista se actualiza automáticamente**

### Terminar Procesos

#### Terminación Segura
1. **Selecciona el proceso** en la lista
2. **Click en "❌ Terminar"**
3. **Confirma la acción**

#### Terminación Forzada
1. **Selecciona el proceso** en la lista
2. **Click en "⚠️ Forzar"**
3. **Confirma la acción** (¡CUIDADO!)

### Ver Detalles del Proceso

1. **Doble-click en un proceso**
2. **Se abre una ventana con:**
   - Ruta del ejecutable
   - Fecha de creación
   - Memoria utilizada
   - Hilos activos
   - Archivos abiertos
   - Conexiones de red

### Auto-Refresh

1. **Marca la casilla "Auto-refrescar"**
2. **La lista se actualiza cada 5 segundos**
3. **Útil para monitoreo continuo**

## ⚙️ Gestión de Servicios

### Ver Servicios

1. **Abre la pestaña "⚙️ Servicios"**
2. **Información mostrada:**
   - Nombre del servicio
   - Nombre mostrado
   - Estado actual
   - Tipo de inicio
   - Recomendación de seguridad

### Controlar Servicios

#### Iniciar Servicio
1. **Selecciona el servicio**
2. **Click en "▶️ Iniciar"**

#### Detener Servicio
1. **Selecciona el servicio**
2. **Click en "⏹️ Detener"**

#### Desactivar Servicio
1. **Selecciona el servicio**
2. **Click en "🚫 Desactivar"**
3. **Confirma la acción**

### Recomendaciones de Seguridad

- **🟢 Verde**: Muy seguro desactivar
- **🟡 Amarillo**: Seguro con precaución
- **🔴 Rojo**: CRÍTICO - No tocar
- **🔵 Azul**: Alto consumo de recursos

## 💡 Sistema de Recomendaciones

### Servicios Seguros para Desactivar

La pestaña "💡 Recomendaciones" muestra servicios que puedes desactivar de forma segura:

#### Servicios Obsoletos
- **Fax** - Servicio de fax obsoleto
- **TapiSrv** - API de telefonía
- **TabletInputService** - Para tablets (innecesario en PC)

#### Servicios de Rendimiento
- **SysMain** - Superfetch (precarga aplicaciones)
- **WSearch** - Windows Search (indexado)
- **Themes** - Gestión de temas visuales

#### Servicios de Privacidad
- **DiagTrack** - Telemetría de Windows
- **dmwappushservice** - Enrutamiento de mensajes WAP

### Desactivar Servicios Recomendados

#### Desactivar Individual
1. **Selecciona el servicio** en la lista
2. **Click en "✅ Desactivar Seleccionado"**
3. **Confirma la acción**

#### Desactivar Todos los Seguros
1. **Click en "🔄 Desactivar Todos los Seguros"**
2. **Confirma la acción**
3. **La aplicación desactivará múltiples servicios**

### Crear Punto de Restauración

1. **Click en "📂 Crear Punto de Restauración"**
2. **Espera a que se complete**
3. **Confirma el mensaje de éxito**

## 🎮 Optimización para Gaming

### Optimización Completa

1. **Ve a la pestaña "🚀 Optimización"**
2. **Click en "🎯 Optimización Completa Gaming"**
3. **Confirma la acción**

La aplicación realizará automáticamente:
- ✅ Crear backup del sistema
- ✅ Cerrar procesos innecesarios
- ✅ Limpiar archivos temporales
- ✅ Optimizar memoria
- ✅ Aplicar configuraciones de gaming

### Procesos para Gaming

La lista muestra procesos que se pueden cerrar para optimizar gaming:

#### Navegadores
- Chrome, Firefox, Edge, Opera, Brave

#### Comunicación
- Discord, Teams, Skype, Zoom, Slack

#### Multimedia
- Spotify, iTunes, VLC, Media Player

#### Productividad
- Outlook, Thunderbird, OneDrive, Dropbox

#### Software de Hardware
- NVIDIA GeForce Experience, AMD Software
- MSI Afterburner, Corsair iCUE, NZXT CAM

### Control Manual de Procesos

#### Cerrar Seleccionados
1. **Selecciona los procesos** que quieres cerrar
2. **Click en "🎯 Cerrar Seleccionados"**
3. **Confirma la acción**

#### Cerrar Todos
1. **Click en "🎮 Cerrar Todos los Procesos de Gaming"**
2. **Confirma la acción**
3. **La aplicación cerrará todos los procesos de la lista**

### Backup del Sistema

#### Crear Backup
1. **Click en "📦 Crear Backup del Sistema"**
2. **Espera a que se complete**
3. **El backup se guarda en Desktop/Gaming_Backups/**

#### Restaurar desde Backup
1. **Click en "🔄 Restaurar desde Backup"**
2. **Selecciona el backup** de la lista
3. **Click en "🔄 Restaurar Seleccionado"**
4. **Confirma la acción**

### Optimizaciones Automáticas

#### Limpiar Archivos Temporales
1. **Click en "🧹 Limpiar Archivos Temporales"**
2. **La aplicación limpiará:**
   - %TEMP%
   - %WINDIR%\Temp
   - %WINDIR%\Prefetch

#### Optimizar Memoria
1. **Click en "💾 Optimizar Memoria"**
2. **La aplicación:**
   - Forzará recolección de basura
   - Terminará procesos pesados
   - Liberará memoria del sistema

#### Desfragmentar Registro
1. **Click en "🔧 Desfragmentar Registro"**
2. **La aplicación optimizará el registro de Windows**

## 🔧 Configuración Avanzada

### Información del Sistema

La pestaña "🚀 Optimización" muestra información en tiempo real:

- **CPU**: Núcleos y uso actual
- **Memoria RAM**: Total, disponible y uso
- **Disco Duro**: Total, libre y uso
- **Procesos Activos**: Número de procesos
- **Hora del Sistema**: Timestamp actual

### Optimizaciones Aplicadas

Cuando ejecutas optimización para gaming, se aplican:

#### Configuración de Energía
- **Alto rendimiento** automático
- **Optimización para gaming**

#### Servicios Desactivados
- **SysMain** - Superfetch
- **WSearch** - Windows Search
- **Themes** - Temas visuales
- **TabletInputService** - Tablet PC Input
- **Fax** - Servicio de fax
- **TapiSrv** - Telephony

#### Configuración de Red
- **Optimización TCP** para gaming
- **Reducción de latencia**

## 🛡️ Seguridad y Protecciones

### Procesos Críticos Protegidos

La aplicación protege automáticamente:
- `Winlogon` - Inicio de sesión
- `csrss` - Runtime Process
- `wininit` - Inicialización
- `services` - Control Manager
- `lsass` - Security Authority
- `smss` - Session Manager
- `explorer` - Windows Explorer

### Confirmaciones de Seguridad

- **Antes de terminar procesos** críticos
- **Antes de desactivar servicios** importantes
- **Antes de optimizaciones** masivas
- **Antes de crear backups** del sistema

### Logs de Actividad

La aplicación registra:
- **Acciones realizadas**
- **Errores encontrados**
- **Procesos terminados**
- **Servicios modificados**

## 📊 Monitoreo y Estadísticas

### Barra de Estado

La barra inferior muestra:
- **Estado actual** de la aplicación
- **Procesos cargados**
- **Servicios cargados**
- **Última acción realizada**

### Información en Tiempo Real

- **Uso de CPU** por proceso
- **Uso de memoria** por proceso
- **Estado de servicios**
- **Recomendaciones** de seguridad

## 🔍 Solución de Problemas

### Problemas Comunes

#### La aplicación no inicia
1. **Verifica Python 3.7+**
2. **Instala dependencias**: `pip install -r requirements.txt`
3. **Ejecuta como administrador**

#### No se pueden ver procesos
1. **Ejecuta como administrador**
2. **Verifica permisos de Windows**
3. **Desactiva temporalmente antivirus**

#### No se pueden controlar servicios
1. **Ejecuta como administrador**
2. **Verifica políticas de grupo**
3. **Comprueba que el servicio existe**

#### Error al crear backup
1. **Verifica espacio en disco**
2. **Comprueba permisos de escritura**
3. **Desactiva temporalmente antivirus**

### Logs de Error

Los logs se guardan en:
```
%APPDATA%\gestor-procesos-avanzado\logs\
```

### Información para Soporte

Al reportar problemas, incluye:
- **Versión de Windows**
- **Versión de Python**
- **Logs de error**
- **Capturas de pantalla**
- **Pasos para reproducir**

## 🎯 Consejos de Uso

### Para Gaming
1. **Ejecuta optimización completa** antes de jugar
2. **Cierra navegadores** y aplicaciones innecesarias
3. **Verifica que no haya procesos pesados** ejecutándose
4. **Usa el auto-refresh** para monitoreo continuo

### Para Mantenimiento
1. **Revisa servicios** regularmente
2. **Limpia archivos temporales** semanalmente
3. **Crea backups** antes de cambios importantes
4. **Monitorea procesos** que consuman muchos recursos

### Para Seguridad
1. **Nunca cierres procesos críticos** del sistema
2. **Usa las recomendaciones** de seguridad
3. **Confirma acciones** antes de ejecutarlas
4. **Crea puntos de restauración** regularmente

---

**¡Disfruta usando el Gestor de Procesos Avanzado!** 🚀 