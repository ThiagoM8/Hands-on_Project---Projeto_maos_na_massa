from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida


restaurante_praca = Restaurante('praça', 'Gourmet')
prato_pao = Prato('Pão Francês', 2.0, 'O melhor da cidade')
prato_pao.aplicar_desconto()
bebida_suco = Bebida('Suco de Melância', 5.0, 'Grande')
bebida_suco.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()