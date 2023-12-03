import pytest
from deposito_comentado import Tinta, LojaDeTintas

# Testes para a classe Tinta
def teste_criar_tinta():
    tinta = Tinta(id=1, nome='Tinta A teste', cor='Azul', quantidade_peso=20.00, quantidade_estoque=20, preco=100.00)
    assert tinta.id == 1
    assert tinta.nome == 'Tinta A teste'
    assert tinta.cor == 'Azul'
    assert tinta.quantidade_peso == 20.00
    assert tinta.quantidade_estoque == 20
# Verifica se os valores são maiores ou igual a zero
    assert tinta.preco > 0
    assert tinta.id > 0
    assert tinta.quantidade_peso > 0
    assert tinta.quantidade_estoque >= 0

    assert tinta.observacao is None


# Testes para a classe LojaDeTintas
def teste_se_tinta_foi_adicionada():
    loja = LojaDeTintas()
    tinta = Tinta(id=1, nome='Tinta A teste', cor='Azul', quantidade_peso=20.00, quantidade_estoque=20, preco=100.00)
    loja.adicionar_tinta(tinta)
    assert len(loja.tintas) == 1
    assert loja.tintas[0] == tinta

def teste_listar_tintas(capsys):
    loja = LojaDeTintas()
    tinta1 = Tinta(id=1, nome='Tinta A teste', cor='Azul', quantidade_peso=20.00, quantidade_estoque=20, preco=100.00)
    tinta2 = Tinta(id=2, nome='Tinta B teste', cor='Rosa', quantidade_peso=18.00, quantidade_estoque=30, preco=200.00)
    loja.adicionar_tinta(tinta2)
    loja.adicionar_tinta(tinta1)
    loja.listar_tintas()
    captured = capsys.readouterr()
    assert "Product ID: 1" in captured.out
    assert "Product ID: 2" in captured.out

def teste_get_tinta_by_id(capsys):
    loja = LojaDeTintas()
    tinta1 = Tinta(id=1, nome='Tinta A teste', cor='Azul', quantidade_peso=20.00, quantidade_estoque=20, preco=100.00)
    loja.adicionar_tinta(tinta1)

    # Testar o caso em que a tinta é encontrada
    with capsys.disabled():
        assert loja.get_tinta_by_id(1).id == 1

    # Testar o caso em que a tinta não é encontrada
    with capsys.disabled():
        assert loja.get_tinta_by_id(3) is None

def teste_atualizar_tinta_by_id():
    loja = LojaDeTintas()
    tinta1 = Tinta(id=1, nome='Tinta A teste', cor='Azul', quantidade_peso=20.00, quantidade_estoque=20, preco=100.00)
    loja.adicionar_tinta(tinta1)

    # Testar a atualização bem sucedida
    assert loja.atualizar_info_tinta_por_id(1, 'NovaTinta', 'Verde', 30.00, 10, 150.00) == "Tinta atualizada com sucesso!"

    # Testar a atualização de uma tinta não existente
    assert loja.atualizar_info_tinta_por_id(2, 'NovaTinta', 'Verde', 8.0, 20, 80.0) == "Tinta não encontrada."

def teste_excluir_tinta_by_id():
    loja = LojaDeTintas()
    tinta1 = Tinta(id=1, nome='Tinta A teste', cor='Azul', quantidade_peso=20.00, quantidade_estoque=20, preco=100.00)
    loja.adicionar_tinta(tinta1)

    # Testar a exclusão bem sucedida
    assert loja.excluir_tinta_by_id(1) == "Tinta excluída com sucesso!"
    assert len(loja.tintas) == 0

    # Testar a exclusão de uma tinta não existente
    assert loja.excluir_tinta_by_id(2) == "Tinta não encontrada."