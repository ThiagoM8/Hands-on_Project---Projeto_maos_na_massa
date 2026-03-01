from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Thiago', 10)
restaurante_praca.receber_avaliacao('Van', 8)
restaurante_praca.receber_avaliacao('Marcio', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()