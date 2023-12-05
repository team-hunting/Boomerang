from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn 

app = FastAPI() 
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD", "TRACE"])
async def boomerang(request: Request):
    '''Mirror the request back to the client.'''
    print(request)
    return {
        "method": request.method,
        "url": request.url,
        "url_path": request.url.path,
        "base_url": request.base_url,
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
        "headers": dict(request.headers),
        "body": await request.body(),
        "client": request.client,
        "client_host": request.client.host,
        "cookies": request.cookies,
        "client": request.client,
        "state": request.state,
        "is_disconnected": request.is_disconnected,
        "receive": request.receive,
        "stream": request.stream,
        } 


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}



if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)