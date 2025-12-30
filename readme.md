# Multi-Client Chatbot Server

![Project Banner](demo.png)

A Python-based client-server chatbot application that enables multiple clients to connect simultaneously and interact with an AI-powered chatbot using Google's Gemini API. Built with socket programming and multi-threading for concurrent client handling.

## 🎓 University Project

This project was developed as part of our university coursework by:
- **Bahaa Saeed**
- **Bahaa Elsheikh**
- **Abdelrahman Elmadah**
- **Abdelrahman Emad**
- **Abdallah Seleem**
- **ElSayed ElSawaf**

## ✨ Features

- **Multi-threaded Server**: Handles multiple client connections simultaneously
- **AI-Powered Responses**: Integrates Google Gemini 2.5 Flash model for intelligent conversations
- **Persistent Chat History**: Maintains separate conversation context for each connected client
- **Fixed-Length Protocol**: Uses 1024-byte fixed message length for reliable communication
- **Graceful Disconnection**: Supports clean exit with "exit" or "quit" commands
- **Error Handling**: Robust error handling for connection issues and API quota limits

## 🏗️ Architecture

The project consists of three main components:

1. **Server (`server.py`)**: Multi-threaded TCP server that listens for client connections
2. **Client (`client.py`)**: Command-line interface for users to interact with the chatbot
3. **Chatbot (`chatbot.py`)**: AI integration layer that communicates with Google Gemini API

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key
- Required Python packages (see Installation)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chatbot-server.git
cd chatbot-server
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your API key:
```bash
export API_KEY="your_google_gemini_api_key_here"
```
On Windows:
```cmd
set API_KEY=your_google_gemini_api_key_here
```

### Usage

1. **Start the Server**:
```bash
python server.py
```
The server will start listening on `127.0.0.1:5050`

2. **Connect a Client**:
In a new terminal window:
```bash
python client.py
```

3. **Start Chatting**:
Type your messages and press Enter. The chatbot will respond using AI.
Type `exit` or `quit` to disconnect.

### Standalone Chatbot

You can also test the chatbot functionality directly without the client-server setup:
```bash
python chatbot.py
```

## 🔧 Configuration

Key configuration parameters in the code:

- `PORT`: Server port (default: 5050)
- `SERVER`: Server IP address (default: 127.0.0.1)
- `MSG_LENGTH`: Fixed message size in bytes (default: 1024)
- `MODEL`: Gemini model version (default: gemini-2.5-flash)

## 📝 Protocol Details

The application uses a fixed-length message protocol:
- All messages are exactly 1024 bytes
- Messages shorter than 1024 bytes are padded with null bytes
- Messages longer than 1024 bytes are truncated
- Ensures reliable message boundaries over TCP

## 🛠️ Technical Stack

- **Language**: Python 3
- **Networking**: Socket programming (TCP)
- **Concurrency**: Threading module
- **AI Model**: Google Gemini 2.5 Flash
- **HTTP Client**: Requests library

## 📄 License

This project is available for educational purposes.

## ⚠️ Notes

- Ensure your API key has sufficient quota for the Gemini API
- The server handles quota exceeded errors gracefully
- Each client maintains its own conversation history
- Connection issues are logged for debugging