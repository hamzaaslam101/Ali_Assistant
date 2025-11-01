from fastapi import FastAPI, HTTPException, Depends, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List, Optional
import asyncio
from datetime import datetime

from app import models, schemas, database, auth
from app.database import get_db, engine
from ai_engine.chatbot import AIChatbot
from ai_engine.vulnerability_analyzer import VulnerabilityAnalyzer
from scanners.reconnaissance import ReconScanner
from scanners.port_scanner import PortScanner
from scanners.web_scanner import WebScanner
from scanners.vulnerability_scanner import VulnScanner
from utils.logger import setup_logger

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Ali - AI Security Engineer",
    description="Autonomous AI-powered penetration testing platform for bug bounty automation",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()

# Initialize AI components
logger = setup_logger(__name__)
chatbot = AIChatbot()
vuln_analyzer = VulnerabilityAnalyzer()
recon_scanner = ReconScanner()
port_scanner = PortScanner()
web_scanner = WebScanner()
vuln_scanner = VulnScanner()

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_update(self, message: dict):
        for connection
