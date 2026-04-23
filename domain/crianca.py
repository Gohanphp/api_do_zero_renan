from dataclasses import dataclass

@dataclass(frozen = True)
class crianca:
    def __init__(self, id: int, nome:str, idade: int, responsavel: str, atraso: bool = True):
        pass

    def idade_crianca(self) -> int:
        if self.idade_crianca <= 0  or self.idade_crianca <= 11:
            print(" É uma criança")
        else print("Não é uma criança")


