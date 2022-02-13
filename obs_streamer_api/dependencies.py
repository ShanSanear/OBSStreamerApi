from typing import Optional

import psutil
import simpleobsws

from obs_streamer_api.config import config


def get_obs_ws(event_loop):
    obs_ws = simpleobsws.obsws(host=config.OBS.WEBSOCKET.ADDRESS, port=config.OBS.WEBSOCKET.PORT,
                               password=config.OBS.WEBSOCKET.PASSWORD,
                               loop=event_loop)
    return obs_ws


def get_process_by_name(process_name: str) -> Optional[psutil.Process]:
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return proc
    return None
