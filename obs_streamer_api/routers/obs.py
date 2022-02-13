import asyncio
from datetime import datetime

import psutil as psutil
from pydantic import BaseModel

from obs_streamer_api.dependencies import get_obs_ws

from fastapi import APIRouter, HTTPException
from fastapi.logger import logger

from obs_streamer_api.config import config

router = APIRouter(
    prefix='/obs'
)


class OBSState(BaseModel):
    pid: int
    name: str


class ProcessKilled(BaseModel):
    pid: int
    name: str
    date: datetime


@router.post("/run")
async def run_obs() -> OBSState:
    try:
        process = psutil.Popen([config.OBS.EXE, '--minimize-to-tray'], cwd=config.OBS.FOLDER)
        process.name()
        return OBSState(
            pid=process.pid,
            name=process.name()
        )
    except Exception as exc:
        raise exc


@router.post("/stop")
async def stop_obs(state: OBSState):
    for proc in psutil.process_iter():
        if proc.name() == state.name and proc.pid == state.pid:
            proc.kill()
            return ProcessKilled(
                pid=proc.pid,
                name=proc.name(),
                date=datetime.utcnow()
            )
    raise HTTPException(status_code=404, detail="Process not found")


async def run_obs_ws_command(command):
    event_loop = asyncio.get_event_loop()
    obs_ws = get_obs_ws(event_loop)
    try:
        await obs_ws.connect()
        result = await obs_ws.call(command)
        return result
    finally:
        await obs_ws.disconnect()


@router.post("/recording/start")
async def start_recording():
    logger.info("Starting recording...")
    result = await run_obs_ws_command("StartRecording")
    return {
        "message": "Started recording",
        "result": result
    }


@router.post("/recording/stop")
async def stop_recording():
    logger.info("Starting recording...")
    result = await run_obs_ws_command("StopRecording")
    return {
        "message": "Stopped recording",
        "result": result
    }


@router.post("/stream/start")
async def start_stream():
    logger.info("Starting recording...")
    result = await run_obs_ws_command("StartStream")
    return {
        "message": "Started recording",
        "result": result
    }


@router.post("/stream/stop")
async def stop_stream():
    logger.info("Starting recording...")
    result = await run_obs_ws_command("StopStream")
    return {
        "message": "Stopped recording",
        "result": result
    }
