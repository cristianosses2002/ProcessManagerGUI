# Guía de Contribución

¡Gracias por tu interés en contribuir al Gestor de Procesos Avanzado! 

## 🤝 Cómo Contribuir

### Reportar Bugs

1. **Busca en Issues existentes** para ver si el bug ya fue reportado
2. **Crea un nuevo Issue** con:
   - Título descriptivo
   - Descripción detallada del problema
   - Pasos para reproducir
   - Información del sistema (Windows version, Python version)
   - Capturas de pantalla si es relevante

### Solicitar Features

1. **Busca en Issues existentes** para ver si la feature ya fue solicitada
2. **Crea un nuevo Issue** con:
   - Título descriptivo
   - Descripción detallada de la feature
   - Casos de uso
   - Beneficios esperados

### Contribuir Código

1. **Fork el repositorio**
2. **Crea una rama** para tu feature:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. **Haz tus cambios** siguiendo las guías de código
4. **Prueba tu código** exhaustivamente
5. **Commit tus cambios**:
   ```bash
   git commit -m "feat: agregar nueva funcionalidad"
   ```
6. **Push a tu fork**:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
7. **Crea un Pull Request**

## 📋 Guías de Código

### Estilo de Código

- **Python**: Sigue PEP 8
- **Nombres**: Usa nombres descriptivos en español
- **Comentarios**: Documenta funciones complejas
- **Docstrings**: Usa docstrings para todas las funciones

### Estructura del Proyecto

```
gestor-procesos-avanzado/
├── test.py                 # Aplicación principal
├── requirements.txt        # Dependencias
├── setup.py              # Configuración del paquete
├── README.md             # Documentación principal
├── LICENSE               # Licencia
├── CHANGELOG.md          # Historial de cambios
├── CONTRIBUTING.md       # Esta guía
├── .gitignore           # Archivos a ignorar
└── docs/               # Documentación adicional
```

### Convenciones de Commit

Usa [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Cambios de formato
- `refactor:` Refactorización de código
- `test:` Agregar o modificar tests
- `chore:` Cambios en build o herramientas

### Ejemplos de Commits

```bash
git commit -m "feat: agregar optimización de memoria automática"
git commit -m "fix: corregir error al cerrar procesos críticos"
git commit -m "docs: actualizar README con nuevas funcionalidades"
git commit -m "style: mejorar formato del código"
```

## 🧪 Testing

### Antes de Contribuir

1. **Prueba en Windows 10/11**
2. **Verifica que no rompas funcionalidades existentes**
3. **Prueba casos edge** (procesos críticos, permisos, etc.)
4. **Verifica la interfaz de usuario**

### Checklist de Testing

- [ ] La aplicación inicia correctamente
- [ ] Todas las pestañas funcionan
- [ ] Los procesos se listan correctamente
- [ ] Los servicios se gestionan sin errores
- [ ] Las optimizaciones funcionan
- [ ] Los backups se crean correctamente
- [ ] No hay errores en la consola
- [ ] La interfaz es responsiva

## 🔒 Seguridad

### Directrices de Seguridad

- **NUNCA** permitas cierre de procesos críticos del sistema
- **SIEMPRE** pide confirmación antes de acciones peligrosas
- **VERIFICA** permisos antes de modificar servicios
- **DOCUMENTA** cualquier cambio que afecte la seguridad

### Procesos Críticos (NO tocar)

- `Winlogon` - Inicio de sesión de Windows
- `csrss` - Client Server Runtime Process
- `wininit` - Inicialización de Windows
- `services` - Service Control Manager
- `lsass` - Local Security Authority
- `smss` - Session Manager
- `explorer` - Windows Explorer

## 📝 Documentación

### Actualizar Documentación

- **README.md**: Para cambios importantes
- **CHANGELOG.md**: Para todas las versiones
- **Comentarios en código**: Para funciones complejas
- **Docstrings**: Para todas las funciones públicas

### Estilo de Documentación

- Usa emojis para mejor legibilidad
- Mantén un tono profesional pero amigable
- Incluye ejemplos cuando sea posible
- Documenta casos edge y limitaciones

## 🚀 Proceso de Release

### Para Maintainers

1. **Actualiza versiones** en setup.py y CHANGELOG.md
2. **Crea un tag** para la nueva versión
3. **Genera release notes** desde CHANGELOG.md
4. **Publica en PyPI** (si aplica)

### Versionado

Seguimos [Semantic Versioning](https://semver.org/):

- **MAJOR**: Cambios incompatibles
- **MINOR**: Nuevas funcionalidades compatibles
- **PATCH**: Correcciones de bugs compatibles

## 🤝 Código de Conducta

### Nuestros Estándares

- **Respeto**: Trata a todos con respeto
- **Constructivo**: Sé constructivo en feedback
- **Inclusivo**: Fomenta la participación de todos
- **Profesional**: Mantén un ambiente profesional

### Reportar Problemas

Si experimentas comportamiento inaceptable:

1. **Contacta al maintainer** directamente: cristian.osses@ejemplo.com
2. **Proporciona detalles** específicos
3. **Mantén confidencialidad** hasta que se resuelva

## 🙏 Agradecimientos

Gracias a todos los contribuidores que hacen este proyecto posible:

- **Desarrolladores**: Por el código y funcionalidades
- **Testers**: Por encontrar bugs y mejorar calidad
- **Documentadores**: Por mantener la documentación actualizada
- **Comunidad**: Por el feedback y sugerencias

---

**¡Gracias por contribuir al Gestor de Procesos Avanzado!** 🚀 