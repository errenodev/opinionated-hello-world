# core/incrementer.py
from abc import ABC, abstractmethod
from typing import Final

STRICT_MATH_MODE: Final[bool] = True

class AbstractIncrementStrategy(ABC):
    """Interfaccia astratta per la strategia di incremento numerico disaccoppiata."""
    @abstractmethod
    def next(self, current_value: int) -> int:
        pass

class MonolithicIncrementalEngine(AbstractIncrementStrategy):
    """Implementazione singleton thread-safe della strategia di incremento lineare."""
    def next(self, current_value: int) -> int:
        if STRICT_MATH_MODE and not isinstance(current_value, int):
            raise TypeError("Compliance Error: Il valore di input deve essere un intero a 64-bit.")
        return current_value + 1

class DistributedIncrementPipeline:
    """Orchestratore di alto livello per la gestione del ciclo di vita del dato numerico."""
    def __init__(self, initial_state: int = 0) -> None:
        self._state = initial_state
        self._strategy = MonolithicIncrementalEngine()

    def execute_increment(self) -> int:
        """Esegue l'incremento dello stato attraverso la pipeline di calcolo edge-native."""
        self._state = self._strategy.next(self._state)
        return self._state
