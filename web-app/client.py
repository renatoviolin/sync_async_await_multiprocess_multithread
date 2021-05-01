from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
import logging
import requests
import time
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# %% --------------------------------------------------------------
app = FastAPI()
app.mount('/static', StaticFiles(directory='templates/static'), name='static')
templates = Jinja2Templates(directory='templates')
SERVER_URL = 'http://localhost:8000/api/easy/%s/%s'
SERVER_WORKLOAD_URL = 'http://localhost:8000/api/%s/%s'
logger = logging.getLogger('uvicorn.error')


# %% --------------------------------------------------------------
def sync_fetch(session, url):
    with session.get(url) as response:
        return response.json()


async def _async_fetch(session, url):
    async with session.get(url) as response:
        r = await response.json()
        return r


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})


# %% --------------------------------------------------------------
@app.post('/easy_sync')
async def easy_sync(request: Request):
    try:
        r = await request.json()
        sleep = int(r.get('sleep'))
        n_requests = int(r.get('n_requests'))

        results = []
        start = time.time()
        with requests.Session() as session:
            for i in range(n_requests):
                r = sync_fetch(session, SERVER_URL % (i, sleep))
                results.append(r['result'])
        end = time.time()
        total = end - start

        return JSONResponse(status_code=200, content={'time': f'{total:.3f} seconds', 'result': results})
    except Exception as ex:
        logger.error(ex)
        return JSONResponse(status_code=400, content={'error': ex})


@app.post('/easy_async')
async def easy_async(request: Request):
    try:
        r = await request.json()
        sleep = int(r.get('sleep'))
        n_requests = int(r.get('n_requests'))

        start = time.time()
        async with aiohttp.ClientSession() as session:
            tasks = [_async_fetch(session, SERVER_URL % (i, sleep)) for i in range(n_requests)]
            results = await asyncio.gather(*tasks)
        end = time.time()
        total = end - start

        return JSONResponse(status_code=200, content={'time': f'{total:.3f} seconds', 'result': results})
    except Exception as ex:
        logger.error(ex)
        return JSONResponse(status_code=400, content={'error': ex})


@app.post('/easy_multiprocess')
async def easy_multiprocess(request: Request):
    try:
        r = await request.json()
        sleep = int(r.get('sleep'))
        n_requests = int(r.get('n_requests'))

        start = time.time()
        with ProcessPoolExecutor() as process_executor:
            with requests.Session() as session:
                _sess = [session] * n_requests
                _url = [SERVER_URL % (i, sleep) for i in range(n_requests)]
                process = process_executor.map(sync_fetch, _sess, _url)
        results = [p['result'] for p in process]

        end = time.time()
        total = end - start
        return JSONResponse(status_code=200, content={'time': f'{total:.3f} seconds', 'result': results})
    except Exception as ex:
        logger.error(ex)
        return JSONResponse(status_code=400, content={'error': ex})


@app.post('/easy_multithread')
async def easy_multithread(request: Request):
    try:
        r = await request.json()
        sleep = int(r.get('sleep'))
        n_requests = int(r.get('n_requests'))

        start = time.time()
        with ThreadPoolExecutor() as thread_executor:
            with requests.Session() as session:
                _sess = [session] * n_requests
                _url = [SERVER_URL % (i, sleep) for i in range(n_requests)]
                process = thread_executor.map(sync_fetch, _sess, _url)
        results = [p['result'] for p in process]

        end = time.time()
        total = end - start
        return JSONResponse(status_code=200, content={'time': f'{total:.3f} seconds', 'result': results})
    except Exception as ex:
        logger.error(ex)
        return JSONResponse(status_code=400, content={'error': ex})


# %% --------------------------------------------------------------
@app.post('/heavy_single')
async def heavy_single(request: Request):
    try:
        r = await request.json()
        n_jobs = int(r.get('n_jobs'))
        start = time.time()
        results = requests.get(SERVER_WORKLOAD_URL % ('heavy_single', n_jobs)).json()['result']
        total = time.time() - start
        return JSONResponse(status_code=200, content={'time': f'{total:.3f} seconds', 'result': results})
    except Exception as ex:
        logger.error(ex)
        return JSONResponse(status_code=400, content={'error': ex})


@app.post('/heavy_thread')
async def heavy_thread(request: Request):
    try:
        r = await request.json()
        n_jobs = int(r.get('n_jobs'))
        start = time.time()
        results = requests.get(SERVER_WORKLOAD_URL % ('heavy_thread', n_jobs)).json()['result']
        total = time.time() - start
        return JSONResponse(status_code=200, content={'time': f'{total:.3f} seconds', 'result': results})
    except Exception as ex:
        logger.error(ex)
        return JSONResponse(status_code=400, content={'error': ex})


@app.post('/heavy_process')
async def heavy_process(request: Request):
    try:
        r = await request.json()
        n_jobs = int(r.get('n_jobs'))
        start = time.time()
        results = requests.get(SERVER_WORKLOAD_URL % ('heavy_process', n_jobs)).json()['result']
        total = time.time() - start
        return JSONResponse(status_code=200, content={'time': f'{total:.3f} seconds', 'result': results})
    except Exception as ex:
        logger.error(ex)
        return JSONResponse(status_code=400, content={'error': ex})
