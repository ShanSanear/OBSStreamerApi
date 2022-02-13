from dataclasses import dataclass
from pathlib import Path

import dacite
import toml


@dataclass
class WEBSOCKET:
    ADDRESS: str
    PORT: int
    PASSWORD: str


@dataclass
class OBS:
    FOLDER: Path
    EXE: Path
    WEBSOCKET: WEBSOCKET


@dataclass
class DISCORD:
    UPDATE_EXE: str


@dataclass
class YOUTUBE:
    CLIENT_SECRET: str
    CHANNEL_ID: str


@dataclass
class STORAGE:
    RECORDING_FOLDER: Path


@dataclass
class API:
    HOST: str


@dataclass
class Config:
    OBS: OBS
    DISCORD: DISCORD
    YOUTUBE: YOUTUBE
    STORAGE: STORAGE
    API: API


config = dacite.from_dict(Config, toml.load('config.toml'),
                          dacite.Config(cast=[Path]))
