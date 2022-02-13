import simpleobsws

from obs_streamer_api.config import config


def get_obs_ws(event_loop):
    obs_ws = simpleobsws.obsws(host=config.OBS.WEBSOCKET.ADDRESS, port=config.OBS.WEBSOCKET.PORT,
                               password=config.OBS.WEBSOCKET.PASSWORD,
                               loop=event_loop)
    return obs_ws
