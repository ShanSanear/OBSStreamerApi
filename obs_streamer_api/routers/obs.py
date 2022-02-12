import asyncio
import subprocess
from pathlib import Path

from obs_streamer_api.dependencies import get_obs_ws

from fastapi import APIRouter
from fastapi.logger import logger

router = APIRouter(
    prefix='/obs'
)

OBS_FOLDER = Path(r"D:\obs-studio\bin\64bit")

OBS_EXE = OBS_FOLDER / "obs64.exe"


@router.post("/run")
async def run_obs():
    try:
        subprocess.Popen([OBS_EXE, '--minimize-to-tray'], cwd=OBS_FOLDER)
    except Exception as exc:
        raise exc


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