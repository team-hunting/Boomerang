Run with Docker: ```docker compose build``` -> ```docker compose up```  
  
Hot Reloading: ```uvicorn main:app --reload --port 8000```  
('main' = name of file, 'app' = name of FastApi() instance - declared with ```app = FastAPI()```)  
  
Swagger docs: ```http://127.0.0.1:8000/docs```  
OpenAPI Spec: ```http://127.0.0.1:8000/openapi.json```