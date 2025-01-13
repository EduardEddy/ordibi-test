# FastAPI Location and Category API

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente instalado:

- Python 3.10 o superior
- Gestor de paquetes `pip`
- Base de datos relacional compatible (SQLite, PostgreSQL, MySQL, etc.)
- **Opcional**: Entorno virtual (`venv`) para aislar las dependencias

---

## 🚀 Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/EduardEddy/ordibi-test.git
   cd ordibi-test

## 🚀 Levantando el proyecto

2. **Crear el entorno virtual

`python -m venv venv`
# Linux/macOS 
`source venv/bin/activate`

# Windows
`venv\Scripts\activate`

Crear un archivo `.env` basado en el `.env.template`

# Instalar las dependencias
``` 
pip install -r requirements.txt
```

# Correra las migraciones
1.
```
alembic revision --autogenerate -m "name migration"
```
2.
```
alembic upgrade head
```

# Levantar el servidor
`uvicorn main:app --reload`