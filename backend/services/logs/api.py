import datetime

from fastapi import APIRouter, Request, HTTPException

from services.logs.api_func import tail_file

logs_router = APIRouter(
    prefix="/logs"
)


@logs_router.get("/pool")
def get_logs_api(request: Request):
    try:
        lines = request.query_params.get('lines')
        rows = tail_file('files/test.log', int(lines))
        now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return {
            "logs": rows,
            "date_time": now,
        }
    except Exception as ex:
        raise HTTPException(status_code=400, detail="Error")