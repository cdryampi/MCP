# MCP Python Server — API Wrapper

Este proyecto crea un servidor MCP en Python que expone una herramienta para consultar una API externa. Compatible con Claude Desktop o ChatGPT Desktop que soporten el Model Context Protocol (MCP).

## ✨ Características

- Exposición de una herramienta (tool) vía MCP
- Consulta HTTP a una API externa
- Integración directa con Claude/Desktop vía claude.json

---

## 🚀 Requisitos

- Python 3.9+
- mcp[cli] (instalable vía pip o uv)
- Claude o ChatGPT Desktop (con soporte MCP)

---

## 📁 Estructura del proyecto

```
.
├── server.py           # Servidor MCP con herramienta "consultar_api"
├── .env                # Variables opcionales para auth/API
├── claude.json         # Config. MCP para integrarlo directamente
└── README.md           # Este documento
```

---

## ⚙️ Instalación

### Con pip

```bash
pip install "mcp[cli]"
```

### Con uv (recomendado)

```bash
uv init mcp-api-server
cd mcp-api-server
uv add "mcp[cli]"
```

### Instación del MCP

```bash
mcp install mi_script.py
```

### Inatalación con .env

```bash
mcp install mi_script.py -f .env
```

### Instalación de dependencias

```bash
pip install -r requirements.txt
```

### Variables de entorno

Crea un archivo `.env` en la raíz del proyecto para definir variables de entorno opcionales:

```env
# .env
API_KEY=mi_api_key
API_URL=https://miapi.com/consulta
```

---

## 👷 Rápido Inicio (Quickstart)

### Crear el servidor server.py

```python
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("API Wrapper")

@mcp.tool(description="Consulta una API externa")
async def consultar_api(param: str) -> str:
    """Consulta una API externa con un parámetro y devuelve la respuesta."""
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://miapi.com/consulta?param={param}")
        return r.text
```

### Ejecutar localmente en modo dev

```bash
mcp dev server.py
```

### Ejecutar en modo producción

```bash
mcp run server.py
```

O con uv:

```bash
uv run --with mcp[cli] mcp run server.py
```

---

## 🚀 Integración con Claude/Desktop

Ubica claude.json en la carpeta de configuración de Claude/Desktop:

- En Windows: %APPDATA%\Claude\claude.json
- En Linux/macOS: ~/.claude/claude.json

Ejemplo:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/codigo/backend-curso-inkor/proyectos_memes"
      ]
    },
    "Demo": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "C:\\codigo\\backend-curso-inkor\\MCP\\server.py"
      ]
    }
  }
}
```

---

## 🤖 Uso dentro de Claude/Desktop

Puedes pedirle al modelo:

> Usa la herramienta consultar_api con el parámetro "ping"

Y el modelo usará tu servidor MCP para hacer una llamada HTTP en tiempo real.

---

## 🎁 Bonus: extensión de herramientas

```python
@mcp.tool()
async def traducir(texto: str, lang: str) -> str:
    return f"Traducido: {texto} → {lang}"
```

---

## 🔍 Recursos

- Documentación oficial MCP: https://docs.mcp.run/
- Repositorio SDK Python: https://github.com/modelcontextprotocol/mcp

---

✅ Hecho con amor y httpx 🚀
