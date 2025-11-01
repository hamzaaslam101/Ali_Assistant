import asyncio
from typing import Dict, List
import openai
import os
from utils.logger import setup_logger

logger = setup_logger(__name__)

class AIChatbot:
    def __init__(self):
        self.logger = logger
        # Use OpenAI API or local LLM
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        if self.api_key:
            openai.api_key = self.api_key
        
        self.system_prompt = """You are Ali, an AI-powered security engineering assistant specialized in:
        - Bug bounty hunting and vulnerability discovery
        - Web application security testing
        - Reconnaissance and information gathering
        - Exploit development and validation
        - Security best practices and recommendations
        
        You help security researchers automate their workflows, discover vulnerabilities, and provide
        actionable insights. Always prioritize authorized testing and responsible disclosure."""
        
        self.conversation_history: Dict[int, List[Dict]] = {}
    
    async def process_message(self, message: str, user_id: int) -> str:
        """Process user message and generate AI response"""
        try:
            # Initialize conversation history for user
            if user_id not in self.conversation_history:
                self.conversation_history[user_id] = [
                    {"role": "system", "content": self.system_prompt}
                ]
            
            # Add user message
            self.conversation_history[user_id].append({
                "role": "user",
                "content": message
            })
            
            # Generate response based on intent
            intent = self._classify_intent(message)
            
            if intent == "scan_request":
                response = await self._handle_scan_request(message)
            elif intent == "vulnerability_query":
 
