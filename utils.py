import pygame

def escalar_img(img, fator):
    tamanho = round(img.get_width() * fator), round(img.get_height() * fator)
    return pygame.transform.scale(img, tamanho)

def mapear_sol_alpha(init_sol, meiodia, end_alpha, end_sol):
    # Loop para calcular e imprimir os valores de A e B
    while init_sol <= end_sol:
        if init_sol <= meiodia:
            init_alpha = (end_alpha * init_sol) / meiodia
        else:
            init_alpha = max(0, end_alpha - ((init_sol - 150) - meiodia))

        return init_alpha