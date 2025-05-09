"""
# Sscript de MCP para obtener mi perfil de usuario y los detalles de la cuenta
# Este script utiliza la biblioteca FastMCP para crear un servidor MCP que permite
# interactuar con una API externa. El script incluye una función para autenticar al usuario
# y obtener su perfil, así como para manejar errores y mostrar mensajes informativos.
# El script está diseñado para ser ejecutado en un entorno asincrónico, utilizando la biblioteca httpx
# para realizar solicitudes HTTP de manera eficiente.
# El script incluye una función para obtener el perfil del usuario, que se autentica
"""

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import httpx
load_dotenv()

mcp = FastMCP("Profile")
# cargar las variables de entorno desde el archivo .env
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
emial = os.getenv("EMAIL")
base_url = os.getenv("BASE_URL")
# Tool para obtener el token de acceso
@mcp.tool()
async def fetch_token() -> str:
    """Devuelve el token de acceso del usuario autenticado."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            base_url+"auth/",
            json={"username": username, "password": password},
        )
        if response.status_code != 200:
            raise Exception(f"Error de autenticación: {response.text}")
        return response.json().get("token", "")

@mcp.tool()
async def get_resume_profile() -> dict:
    """Devuelve el perfil privado del usuario autenticado."""
    token = await fetch_token()

    try:
        headers = {
            "Authorization": f"Token {token}"
        }

        async with httpx.AsyncClient() as client:
            r = await client.get(
                base_url+"base/userprofile/private/",
                headers=headers
            )
            if r.status_code == 200:
                return r.json()
            else:
                return {
                    "error": f"Fallo al obtener perfil: {r.status_code}",
                    "message": r.text,
                    "token": token
                }

    except Exception as e:
        return {
            "error": "Excepción al obtener perfil",
            "message": str(e)
        }

@mcp.tool()
async def get_projects() -> dict:
    """Devuelve los proyectos del usuario autenticado."""
    token = await fetch_token()

    try:
        headers = {
            "Authorization": f"Token {token}"
        }
        async with httpx.AsyncClient() as client:
            r = await client.get(
                base_url+"portfolio/private/",
                headers=headers
            )
            if r.status_code == 200:
                return r.json()
            else:
                return {
                    "error": f"Fallo al obtener proyectos: {r.status_code}",
                    "message": r.text,
                    "token": token
                }
    except Exception as e:
        return {
            "error": "Excepción al obtener proyectos",
            "message": str(e)
        }
@mcp.tool()
async def get_social() -> dict:
    """Devuelve los enlaces sociales del usuario autenticado."""
    token = await fetch_token()

    try:
        headers = {
            "Authorization": f"Token {token}"
        }
        async with httpx.AsyncClient() as client:
            r = await client.get(
                base_url+"social/private/",
                headers=headers
            )
            if r.status_code == 200:
                return r.json()
            else:
                return {
                    "error": f"Fallo al obtener enlaces sociales: {r.status_code}",
                    "message": r.text,
                    "token": token
                }
    except Exception as e:
        return {
            "error": "Excepción al obtener enlaces sociales",
            "message": str(e)
        }
    
@mcp.tool()
async def get_services() -> dict:
    """Devuelve los servicios de los usuarios authentificados."""
    token = await fetch_token()

    try:
        headers = {
            "Authorization": f"Token {token}"
        }
        async with httpx.AsyncClient() as client:
            r = await client.get(
                base_url+"services/private/",
                headers=headers
            )
            if r.status_code == 200:
                return r.json()
            else:
                return {
                    "error": f"Fallo al obtener educación: {r.status_code}",
                    "message": r.text,
                    "token": token
                }
    except Exception as e:
        return {
            "error": "Excepción al obtener educación",
            "message": str(e)
        }
@mcp.tool()
async def get_education_and_skills() -> dict:
    """Devuelve la educación y habilidades del usuario autenticado."""
    token = await fetch_token()

    try:
        headers = {
            "Authorization": f"Token {token}"
        }
        async with httpx.AsyncClient() as client:
            r = await client.get(
                base_url+"education_and_skills/education_list_private/",
                headers=headers
            )
            if r.status_code == 200:
                return r.json()
            else:
                return {
                    "error": f"Fallo al obtener educación: {r.status_code}",
                    "message": r.text,
                    "token": token
                }
    except Exception as e:
        return {
            "error": "Excepción al obtener educación",
            "message": str(e)
        }
@mcp.tool()
async def enviar_mensaje_email(mensaje: str = "Hola, soy un mensaje de prueba") -> str:
    """Envia un mensaje al correo electrónico del usuario autenticado."""
    token = await fetch_token()

    try:
        headers = {
            "Authorization": f"Token {token}"
        }
        body = {
            "email": emial,
            "name": "MCP Server",
            "message": mensaje
        }
        async with httpx.AsyncClient() as client:
            r = await client.post(
                base_url+"email_service/enviar-correo/",
                headers=headers,
                json=body
            )
            if r.status_code == 200:
                return r.json()
            else:
                return {
                    "error": f"Fallo al enviar mensaje: {r.status_code}",
                    "message": r.text,
                    "token": token
                }
    except Exception as e:
        return {
            "error": "Excepción al enviar mensaje",
            "message": str(e)
        }