from abc import ABC, abstractmethod

class InputMethod(ABC):
    @abstractmethod
    def get_input(self, prompt: str) -> str:
        pass


class ConsoleInput(InputMethod):
    def get_input(self, prompt: str) -> str:
        return input(f'Enter {prompt}: ')
