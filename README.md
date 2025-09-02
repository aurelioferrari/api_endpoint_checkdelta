Options Manager API – FastAPI Project

This project provides a simple REST API built with FastAPI to manage a list of options.
It also includes scripts to check for newly added options and add new ones via API.

Project Structure

main_teste.py – Starts the FastAPI server and exposes endpoints to list and add options.

endpoint_origem.py – Contains the data model (Geral) and the initial options list.

checa_delta.py – Periodically checks the API for newly added options.

add_opcao.py – Sends a new option to the API via a POST request.

Requirements

Python 3.8+

Dependencies:

pip install fastapi uvicorn requests pydantic

How to Run
1. Start the FastAPI server
python main_teste.py


The server will run at:
http://localhost:8000

2. Retrieve the current options
curl http://localhost:8000/opcoes


Sample response:

[
  {"id": 1, "nome": "Opção 1"},
  {"id": 2, "nome": "Opção 2"},
  {"id": 3, "nome": "Opção 3"}
]

3. Add a new option

Run:

python add_opcao.py


Or via curl:

curl -X POST "http://localhost:8000/opcoes" \
-H "Content-Type: application/json" \
-d '{"id": 10, "nome": "Opção 10"}'

4. Monitor for new options

checa_delta.py checks the API every 30 seconds for newly added options and prints any updates:

python checa_delta.py

API Endpoints

GET /opcoes – Returns all available options.

POST /opcoes – Adds a new option to the list.

Possible Improvements

Add a database (e.g., SQLite, PostgreSQL) instead of in-memory storage.

Add error handling for invalid inputs.

Containerize the project with Docker for easier deployment.

Add authentication for secure modifications.
