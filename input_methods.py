from abc import ABC, abstractmethod

class InputMethod(ABC):
    @abstractmethod
    def get_input():
        pass


class ConsoleInput(InputMethod):
    def get_input(self, value: str) -> str:
        return input(f'Enter {value}: ')
