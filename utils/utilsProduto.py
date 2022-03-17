def formata_preco(val):
    return f'R${val:.2f}'.replace('.', ',')\


def formata_numero_pedido(val):
    return f'FM{str(val).zfill(6)}'

def formata_codigo_produto(val):
    return f'{str(val).zfill(5)}'