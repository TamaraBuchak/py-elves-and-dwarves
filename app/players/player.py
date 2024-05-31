from typing import Any
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def player_info(self) -> Any:
        pass

    @abstractmethod
    def get_rating(self) -> Any:
        pass
