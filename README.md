# LLM System Project

## Overview

This project is a multi-container application that integrates a Large Language Model (LLM) backend, a frontend user interface, and a prompt voice memory service. It is designed to provide an interactive playground where users can input prompts, receive generated responses from the LLM backend, and optionally listen to audio responses processed by the voice memory service.

## Architecture

The project consists of three main components, each running in its own Docker container:

- **Backend Container (`backend_container`)**  
  A FastAPI-based backend service that handles prompt requests and generates responses using the LLM. It exposes REST API endpoints for the frontend to interact with.

- **Frontend Container (`frontend_container`)**  
  A static web frontend served by Nginx. It provides a user interface for entering prompts, displaying LLM responses, and playing audio responses. The frontend communicates with the backend and voice memory services via HTTP.

- **Prompt Voice Memory Container (`prompt_voice_memory`)**  
  A service responsible for processing text-to-speech (TTS) requests and managing audio playback sessions.

## Prerequisites

- Docker and Docker Compose installed on your system.
- Sufficient system resources to run multiple containers.

## Getting Started

### Build and Run

From the root directory of the project, run:

```bash
docker-compose up --build
```

This command will build the Docker images and start all services defined in the `docker-compose.yml` file.

### Accessing the Application

- Open your web browser and navigate to:  
  `http://localhost:8080`  
  This will load the frontend interface.

### Using the Application

1. Enter your prompt in the text area.
2. Click the **Ask LLM** button to send the prompt to the backend.
3. The generated response will be displayed below.
4. If audio playback is available, use the **Listen to Response** button to hear the response.

## Project Structure

```
.
├── backend_container/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── __init__.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend_container/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   └── Dockerfile
├── prompt_voice_memory/
│   ├── main.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── audio/
├── docker-compose.yml
└── README.md
```

## Configuration

- Backend service runs on port `8000`.
- Frontend service runs on port `8080`.
- Prompt voice memory service runs on port `8002`.

The services communicate over a Docker network defined in `docker-compose.yml`.

## Troubleshooting

- Ensure Docker daemon is running.
- If ports `8000`, `8002`, or `8080` are in use, stop the conflicting services or update the ports in `docker-compose.yml`.
- Check container logs for errors:
  ```bash
  docker-compose logs backend
  docker-compose logs frontend
  docker-compose logs prompt_voice_memory
  ```

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact the project maintainer.

---
Enjoy using the LLM System Project!
