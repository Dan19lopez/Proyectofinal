# Book App Python - Sistema de Gestión de Préstamos

Un sistema completo para gestionar préstamos de objetos entre amigos, desarrollado en Python con MySQL.

## Características

- **Gestión de Amigos**: Crear, listar, actualizar y eliminar amigos
- **Gestión de Categorías**: Organizar objetos por categorías
- **Gestión de Objetos**: Administrar los objetos que se pueden prestar
- **Gestión de Préstamos**: Crear préstamos, devoluciones y seguimiento
- **Reportes**: Resúmenes y estadísticas del sistema
- **Exportación CSV**: Exportar todos los datos a archivos CSV
- **Base de datos MySQL**: Integración completa con XAMPP
- **Inicialización Automática**: Configuración automática de base de datos

## Funcionalidades Detalladas

### 🧑‍🤝‍🧑 Gestión de Amigos

**Crear Amigo**
- Registro completo con nombre, teléfono, email y dirección
- Validación de formato de email
- Asignación automática de rol de usuario
- Verificación de duplicados por email

**Listar Amigos**
- Visualización de todos los amigos registrados
- Información completa: ID, nombre, contacto y rol
- Formato tabular organizado

**Buscar Amigo**
- Búsqueda por ID específico
- Mostrar información detallada del amigo encontrado
- Manejo de casos cuando no se encuentra el amigo

**Actualizar Amigo**
- Modificación de datos existentes
- Validación de nuevo email si se cambia
- Confirmación de cambios realizados

**Eliminar Amigo**
- Verificación de préstamos activos antes de eliminar
- Confirmación de seguridad para evitar eliminaciones accidentales
- Mensaje de confirmación del proceso

### 📂 Gestión de Categorías

**Crear Categoría**
- Registro de nuevas categorías con nombre y descripción
- Validación de nombres únicos
- Categorías predefinidas: Libros, Herramientas, Electrodomésticos, Deportes, Música

**Listar Categorías**
- Visualización completa de todas las categorías
- Información de ID, nombre y descripción
- Contador de objetos por categoría

**Buscar Categoría**
- Búsqueda directa por ID
- Información detallada de la categoría seleccionada

**Actualizar Categoría**
- Modificación de nombre y descripción
- Validación de unicidad en nombres nuevos
- Confirmación de cambios

**Eliminar Categoría**
- Verificación de objetos asociados antes de eliminar
- Protección contra eliminación de categorías en uso
- Confirmación de seguridad

### 📦 Gestión de Objetos

**Crear Objeto**
- Registro completo: descripción, valor, categoría y ubicación
- Selección de categoría desde lista disponible
- Estado inicial automático como "Disponible"
- Validación de datos de entrada

**Listar Objetos**
- Vista completa de todos los objetos
- Información: ID, descripción, valor, categoría, estado y ubicación
- Estados en español: Disponible, Reservado

**Buscar Objeto por ID**
- Búsqueda específica con información detallada
- Mostrar categoría asociada y estado actual

**Actualizar Objeto**
- Modificación de descripción, valor y ubicación
- Cambio de categoría si es necesario
- Preservación del estado actual

**Eliminar Objeto**
- Verificación de préstamos activos
- Confirmación de seguridad
- Protección de integridad de datos

**Listar por Categoría**
- Filtrado de objetos por categoría específica
- Selección interactiva de categoría
- Vista organizada por tipo de objeto

**Listar Objetos Disponibles**
- Filtro automático de objetos prestables
- Lista rápida para crear préstamos
- Estado de disponibilidad en tiempo real

### 📋 Gestión de Préstamos

**Crear Préstamo**
- Selección de amigo desde lista de registrados
- Selección de objeto desde lista de disponibles
- Establecimiento automático de fecha de préstamo
- Definición de fecha de devolución esperada
- Cambio automático de estado del objeto a "Reservado"

**Listar Préstamos**
- Vista completa de todos los préstamos históricos
- Información: ID, amigo, objeto, fechas y estado
- Estados en español: Activo, Retornado, Vencido

**Buscar Préstamo por ID**
- Búsqueda específica con detalles completos
- Información del amigo y objeto asociados
- Estado actual del préstamo

**Devolver Préstamo**
- Proceso de devolución con actualización automática
- Cambio de estado de préstamo a "Retornado"
- Liberación del objeto a estado "Disponible"
- Registro de fecha de devolución real

**Actualizar Préstamo**
- Modificación de fechas de devolución
- Cambio de estado si es necesario
- Validación de coherencia de datos

**Eliminar Préstamo**
- Eliminación con restauración de estado del objeto
- Confirmación de seguridad
- Actualización de disponibilidad

**Listar Préstamos Activos**
- Filtro de préstamos no devueltos
- Vista rápida de préstamos pendientes
- Información para seguimiento

**Listar por Amigo**
- Historial completo de préstamos por persona
- Selección interactiva de amigo
- Vista personalizada de actividad

**Verificar Préstamos Vencidos**
- Detección automática de préstamos atrasados
- Cálculo de días de retraso
- Lista de préstamos que requieren atención

### 📊 Sistema de Reportes

**Resumen General**
- Estadísticas completas del sistema
- Contadores de: amigos, categorías, objetos y préstamos
- Estado de objetos (disponibles vs reservados)
- Estado de préstamos (activos, retornados, vencidos)
- Vista panorámica de la actividad

**Estado de Objetos**
- Desglose detallado por estado
- Contadores por categoría
- Análisis de disponibilidad
- Identificación de objetos más prestados

### 📤 Exportación CSV

**Exportar Amigos**
- Archivo CSV con todos los datos de amigos
- Campos: ID, Nombre, Teléfono, Email, Dirección, Rol
- Nombre de archivo con timestamp
- Codificación UTF-8 para caracteres especiales

**Exportar Categorías**
- Exportación completa de categorías
- Campos: ID, Nombre, Descripción
- Formato compatible con Excel

**Exportar Objetos**
- Lista completa de objetos con detalles
- Campos: ID, Descripción, Valor, Categoría, Estado, Ubicación
- Estados traducidos al español

**Exportar Préstamos**
- Historial completo de préstamos
- Campos: ID, Amigo, Objeto, Fechas, Estado
- Estados traducidos (Activo, Retornado, Vencido)
- Información completa para auditorías

**Exportar Todos los Datos**
- Archivo único con todas las tablas
- Múltiples hojas o secciones separadas
- Backup completo del sistema
- Ideal para respaldos o migración

**Reporte Personalizado**
- Combinación de datos de múltiples tablas
- Información relacional completa
- Análisis cruzado de préstamos con detalles de amigos y objetos
- Formato optimizado para análisis

### 🔧 Funcionalidades del Sistema

**Inicialización Automática de Base de Datos**
- Creación automática de base de datos si no existe
- Verificación y corrección de estructura de tablas
- Inserción de datos de ejemplo si las tablas están vacías
- Compatibilidad con XAMPP por defecto

**Validación de Datos**
- Verificación de formatos de email
- Validación de números y fechas
- Control de datos obligatorios
- Prevención de duplicados

**Manejo de Estados**
- Control automático de disponibilidad de objetos
- Actualización de estados en transacciones
- Consistencia de datos entre préstamos y objetos
- Estados localizados en español

**Interfaz de Usuario**
- Menús intuitivos y organizados
- Navegación clara entre funcionalidades
- Mensajes informativos y de confirmación
- Manejo de errores con mensajes amigables

**Seguridad de Datos**
- Confirmaciones para operaciones críticas
- Validación antes de eliminaciones
- Verificación de relaciones entre datos
- Manejo de excepciones y errores

### 🌐 Localización

**Interfaz en Español**
- Todos los menús y mensajes en español
- Estados de objetos y préstamos traducidos
- Mensajes de error y confirmación localizados
- Formato de fechas apropiado para español

**Estados Localizados**
- Objetos: "Disponible" y "Reservado"
- Préstamos: "Activo", "Retornado" y "Vencido"
- Consistencia en toda la aplicación
- Exportaciones con términos en español

## Estructura del Proyecto

```
book_app_python/
├── domain/                 # Modelos de datos
│   ├── Category.py
│   ├── Friend.py
│   ├── User.py
│   ├── object.py
│   ├── loan.py
│   └── ...
├── repository/            # Capa de acceso a datos
│   ├── Conexion.py
│   ├── Category_Repository.py
│   ├── FriendRepository.py
│   ├── FriendRepositoryDB.py
│   ├── ObjectRepository.py
│   └── LoanRepository.py
├── service/              # Lógica de negocio
│   ├── Category_Service.py
│   ├── FriendService.py
│   ├── ObjectService.py
│   └── LoanService.py
├── view/                 # Interfaz de usuario
│   └── App.py
├── main.py              # Punto de entrada
├── database_setup.sql   # Script de configuración de BD
└── requirements.txt     # Dependencias
```

## Instalación y Configuración

### 1. Prerequisitos

- Python 3.7 o superior
- XAMPP (para MySQL)
- Git (opcional)

### 2. Configurar XAMPP

1. Instala XAMPP desde [https://www.apachefriends.org/](https://www.apachefriends.org/)
2. Inicia el panel de control de XAMPP
3. Inicia los servicios **Apache** y **MySQL**
4. Abre phpMyAdmin (http://localhost/phpmyadmin)

### 3. Configurar la Base de Datos (Automático)

La aplicación ahora configura automáticamente la base de datos. Tienes tres opciones:

#### Opción 1: Configuración automática al ejecutar la app
```bash
python3 main.py
```
La aplicación verificará y creará automáticamente la base de datos si no existe.

#### Opción 2: Configuración manual previa
```bash
python3 setup_database.py
```
Este script solo configura la base de datos sin ejecutar la aplicación.

#### Opción 3: Configuración manual con phpMyAdmin (método anterior)
1. En phpMyAdmin, ve a la pestaña **SQL**
2. Copia y ejecuta el contenido del archivo `database_setup.sql`

**Nota:** Si ya tienes una base de datos `book_app` con estructura diferente, el script automáticamente la corregirá para que sea compatible con la aplicación.

### 4. Instalar Dependencias de Python

```bash
# Navegar al directorio del proyecto
cd book_app_python

# Instalar dependencias
pip install -r requirements.txt

# O instalar manualmente
pip install mysql-connector-python
```

### 5. Configurar la Conexión a la Base de Datos

El archivo `repository/Conexion.py` está configurado con los valores por defecto de XAMPP:

```python
host='localhost'
port=3306
user='root'
password=""  # Sin contraseña por defecto en XAMPP
database='book_app'
```

Si tienes una configuración diferente, modifica estos valores.

## Uso

### Ejecutar la Aplicación

```bash
python3 main.py
```

La aplicación automáticamente:
1. ✓ Verificará la conexión a MySQL
2. ✓ Creará la base de datos `book_app` si no existe
3. ✓ Creará todas las tablas necesarias
4. ✓ Insertará datos de ejemplo si las tablas están vacías
5. ✓ Corregirá la estructura de tablas si es necesario
6. ✓ Iniciará la aplicación

### Solo Configurar la Base de Datos

Si solo quieres configurar la base de datos sin ejecutar la aplicación:

```bash
python3 setup_database.py
```

### Navegación del Menú

La aplicación tiene un menú intuitivo con las siguientes opciones principales:

1. **Gestionar Amigos**
   - Crear, listar, buscar, actualizar y eliminar amigos

2. **Gestionar Categorías**
   - Administrar categorías para clasificar objetos

3. **Gestionar Objetos**
   - Crear y administrar objetos que se pueden prestar
   - Filtrar por categoría y estado

4. **Gestionar Préstamos**
   - Crear nuevos préstamos
   - Procesar devoluciones
   - Verificar préstamos vencidos

5. **Reportes**
   - Resumen general del sistema
   - Estado de objetos

## Estructura de la Base de Datos

### Tablas Principales

- **friend**: Información de los amigos
- **category**: Categorías de objetos
- **object**: Objetos que se pueden prestar
- **loan**: Registro de préstamos

### Relaciones

- Los objetos pertenecen a una categoría
- Los préstamos relacionan amigos con objetos
- Control automático del estado de los objetos

## Funcionalidades Avanzadas

### Estados de Objetos
- `available`: Disponible para préstamo
- `loaned`: Actualmente prestado
- `maintenance`: En mantenimiento
- `damaged`: Dañado

### Estados de Préstamos
- `active`: Préstamo activo
- `returned`: Préstamo devuelto
- `overdue`: Préstamo vencido

### Características Adicionales
- Verificación automática de préstamos vencidos
- Control de disponibilidad de objetos
- Actualización automática de estados
- Validación de datos de entrada

## Solución de Problemas

### Error de Conexión a la Base de Datos

1. Verifica que XAMPP esté ejecutándose
2. Confirma que MySQL esté activo en el panel de XAMPP
3. Verifica las credenciales en `Conexion.py`
4. Asegúrate de que la base de datos `book_app` exista

### Error de Módulos de Python

```bash
pip install --upgrade mysql-connector-python
```

### Problemas de Importación

Asegúrate de ejecutar el script desde el directorio raíz del proyecto:

```bash
python main.py
```

## Datos de Ejemplo

El script de configuración incluye datos de ejemplo:

- **Categorías**: Libros, Herramientas, Electrodomésticos, Deportes, Música
- **Amigos**: Juan Pérez, María García, Carlos López
- **Objetos**: El Quijote, Taladro Eléctrico, Licuadora, etc.

## Desarrollo y Extensión

### Agregar Nuevas Funcionalidades

1. **Dominio**: Crear nuevas clases en `domain/`
2. **Repositorio**: Implementar acceso a datos en `repository/`
3. **Servicio**: Agregar lógica de negocio en `service/`
4. **Vista**: Actualizar menús en `view/App.py`

### Mejoras Sugeridas

- Interfaz gráfica con tkinter o PyQt
- API REST con Flask/FastAPI
- Autenticación de usuarios
- Notificaciones por email
- Exportación de reportes a PDF/Excel
- Sistema de multas por retraso

## Contribución

1. Fork del repositorio
2. Crear una rama para tu función
3. Commit de los cambios
4. Push a la rama
5. Crear un Pull Request

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.