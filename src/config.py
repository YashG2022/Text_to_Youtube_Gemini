from dataclasses import dataclass
from pathlib import Path
from typing import Union

from yaml import safe_load


@dataclass
class Config:
    GEMINIAI_API_KEY: str
    GEMINIAI_PROMPTS_PATH: str
    SOURCE_DIR: str
    PROCESS_DIR: str
    OUTPUT_DIR: str
    YT_PROBA: int


def get_config(path: Union[str, Path] = None) -> Config:
    if path is None:
        path = Path(__file__).parent.parent.joinpath("env.yaml")
    if not Path(path).exists():
        path = Path(__file__).parent.parent.joinpath("example.env.yaml")
    with open(path, encoding="utf-8") as f:
        config = Config(**safe_load(f))
    return config


cfg = get_config()
