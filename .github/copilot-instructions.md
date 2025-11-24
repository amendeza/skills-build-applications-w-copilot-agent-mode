# Instrucciones para agentes (Copilot) — OctoFit Tracker

Este archivo contiene la información esencial para que un agente AI sea productivo rápidamente en este repositorio.

- **Big picture**: proyecto OctoFit Tracker — frontend en `octofit-tracker/frontend` (React.js) y backend en `octofit-tracker/backend` (Django REST). La persistencia objetivo es MongoDB (uso de `djongo`/`pymongo`). Ver `docs/octofit_story.md` para el propósito y la pila.

- **Entorno y comandos comunes**:
  - Crear entorno virtual (si trabajas localmente):
    ```bash
    python3 -m venv octofit-tracker/backend/venv
    source octofit-tracker/backend/venv/bin/activate
    pip install -r octofit-tracker/backend/requirements.txt
    ```
  - Frontend: los comandos deben apuntar siempre a `octofit-tracker/frontend`:
    ```bash
    npm install --prefix octofit-tracker/frontend
    npm start --prefix octofit-tracker/frontend
    ```

- **No cambies de directorio en comandos automatizados**: las instrucciones del repositorio insisten en usar rutas completas en lugar de `cd`. Siempre pasa la ruta con `--prefix` o rutas relativas completas.

- **Puertos expuestos (Codespaces / ejecución)**:
  - `8000` backend (Django)
  - `3000` frontend (React)
  - `27017` MongoDB (privado)

- **Patrones y convenciones del backend (Django)**:
  - `settings.py` debe incluir `ALLOWED_HOSTS` con lógica para `CODESPACE_NAME` (buscar esta comprobación en `.github/instructions/octofit_tracker_django_backend.instructions.md`).
  - Las rutas (`urls.py`) usan la variable de entorno `CODESPACE_NAME` para construir `base_url` — mantén este patrón cuando añadas URL útiles para la documentación o pruebas.
  - Serializadores: convierte campos `ObjectId` a `str` antes de exponerlos en JSON (ver instrucciones de `serializers.py`).

- **Pruebas manuales / integración**:
  - Usa `curl` para validar endpoints de la API (recomendación del backend). Ejemplo:
    ```bash
    curl -v "$BASE_URL/api/health/"
    ```
  - Al documentar endpoints, muestra ejemplos `curl` y URLs construidas con `CODESPACE_NAME`.

- **Frontend**:
  - El proyecto usa React + Bootstrap en `octofit-tracker/frontend`. Coloca import de Bootstrap en `src/index.js` como indican las instrucciones.
  - Usa `react-router-dom` para rutas cliente.

- **Archivos y lugares clave**:
  - `docs/octofit_story.md` — contexto del producto, requisitos y pila.
  - `.github/instructions/*.instructions.md` — contienen normas operativas (frontend/backend/setup). Úsalos como fuente canónica para scripts y comandos.
  - `README.md` — resumen del ejercicio y enlaces útiles.

- **Comportamiento esperado del agente**:
  - Antes de ejecutar cambios, busca y respeta patrones en `.github/instructions/`.
  - Prefiere cambios pequeños y localizados; evita reordenar grandes secciones de código sin motivo.
  - Cuando modifiques `settings.py`, documenta explícitamente la razón y muestra cómo probar en Codespaces.

- **Ejemplos concretos detectados**:
  - Virtualenv esperado: `octofit-tracker/backend/venv`.
  - Requisitos: `octofit-tracker/backend/requirements.txt` (instalar con `pip install -r ...`).
  - Frontend: agregar `import 'bootstrap/dist/css/bootstrap.min.css';` en `octofit-tracker/frontend/src/index.js`.

Si algo en estas notas está incompleto o quieres que amplíe con ejemplos de archivos concretos, dime qué sección mejorar y lo actualizo.
