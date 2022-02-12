import simpleobsws


def get_obs_ws(event_loop):
    obs_ws = simpleobsws.obsws(host='127.0.0.1', port=4444, password='',
                               loop=event_loop)
    return obs_ws
