#!/bin/bash

echo "🛡️  Setting up Ali Security Engineer..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p backend/logs
mkdir -p frontend/dist

# Copy environment file if not exists
if [ ! -f backend/.env ]; then
    echo "📝 Creating environment file..."
    cp backend/.env.example backend/.env
    
    # Generate random secret key
    SECRET_KEY=$(openssl rand -hex 32)
    sed -i "s/your-super-secret-key-change-this-in-production/$SECRET_KEY/" backend/.env
    echo "✅ Generated secure SECRET_KEY"
fi

# Build and start containers
echo "🐳 Building Docker containers..."
docker-compose build

echo "🚀 Starting Ali Security Engineer..."
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 10

# Check if services are running
if docker-compose ps | grep -q "Up"; then
    echo "✅ Ali Security Engineer is running!"
    echo ""
    echo "🌐 Access the application:"
    echo "   Frontend: http://localhost"
    echo "   Backend API: http://localhost:8000"
    echo "   API Docs: http://localhost:8000/docs"
    echo ""
    echo "📖 View logs: docker-compose logs -f"
    echo "🛑 Stop: docker-compose down"
else
    echo "❌ Failed to start services. Check logs with: docker-compose logs"
    exit 1
fi
