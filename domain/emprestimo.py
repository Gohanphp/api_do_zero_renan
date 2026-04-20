from dataclasses import dataclass
@dataclass

class emprestimo:
    def __init__(self, id: int, crianca_id: int, brinquedo_id: int,
                   datas: str,data_inicio: str, data_fim: str, hora_atual: str, hora_fim: str,
                    status: bool, multa: int) -> None:
        self.id = id
        self.crianca_id = crianca_id
        self.brinquedo_id = brinquedo_id
        self.datas = datas
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.hora_atual = hora_atual
        self.hora_fim = hora_fim
        self.status = status
        self.multa = multa

    def emprestar_brinquedo(self, brinquedo_id: int, status: bool, datas: int, atraso: bool = True ):
        if brinquedo_id:
            status == "True"
        False
        raise ValueError("O brinquedo não esta disponível")
        return "Brinquedo disponível"


    def crianca_emprestimo(self, brinquedo_id, crianca_id,status: bool):
            if brinquedo_id > crianca_id:
                status == "True"
                return "A criança ja tem dois brinquedos."


    def crianca_atrasada(self, crianca_id: int, brinquedo_id,datas: int,hora_atual:str,
                         hora_fim: str, atraso: bool):
        if hora_atual > hora_fim:
            atraso = True
            return "Criança esta atrasada."

    def multa_atraso(self, multa: int):






