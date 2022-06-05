def formata_preco(val):
    return f'R${val:.2f}'.replace('.', ',')\


def formata_numero_pedido(val):
    return f'FM{str(val).zfill(6)}'

def formata_numero_cliente(val):
    return f'CL{str(val).zfill(6)}'

def formata_data(val):
    return f"{val:%d/%m/%Y}"



def formata_codigo_produto(val):
    return f'{str(val).zfill(5)}'

def formata_cpf(val):
    return f'{str(val).zfill(5)}'