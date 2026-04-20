from dataclasses import dataclass
@dataclass

class brinquedo:
    def __init__(self, id: int, nome: str, categoria: str,
          faixa_etaria_minima: int, disponivel: bool = True, atraso: bool = True):
        pass