from pathlib import Path
import traceback
import uvicorn

from fastapi import FastApi, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fatapi.staticfiles