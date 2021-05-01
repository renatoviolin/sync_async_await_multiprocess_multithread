from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

app = FastAPI()


def heavy_workload(job_id):
    n = 15000000
    while n > 0:
        n -= 1
    return f'Job id: {job_id} done!'


@app.get('/api/easy/{request_id}/{sleep}')
async def easy_workload(request_id: str, sleep: int):
    await asyncio.sleep(sleep)
    return JSONResponse(status_code=200, content={'result': f'Request: {request_id} done!'})


@app.get('/api/heavy_single/{n_jobs}')
async def run_single(n_jobs: int):
    results = []
    for i in range(n_jobs):
        results.append(heavy_workload(i))
    return JSONResponse(status_code=200, content={'result': results})


@app.get('/api/heavy_thread/{n_jobs}')
async def run_thread(n_jobs: int):
    with ThreadPoolExecutor() as executor:
        process = executor.map(heavy_workload, range(n_jobs))
        results = [p for p in process]
    return JSONResponse(status_code=200, content={'result': results})


@app.get('/api/heavy_process/{n_jobs}')
async def run_process(n_jobs: int):
    with ProcessPoolExecutor() as executor:
        process = executor.map(heavy_workload, range(n_jobs))
        results = [p for p in process]
    return JSONResponse(status_code=200, content={'result': results})
