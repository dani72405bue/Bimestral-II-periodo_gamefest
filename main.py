import os
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, RECORD_FILE, SOUND_DIR
from scr.fondo import Fondo
from scr.personaje import Personaje
from scr.carro import Carro


def leer_record():
    if os.path.exists(RECORD_FILE):
        try:
            with open(RECORD_FILE, "r", encoding="utf-8") as archivo:
                texto = archivo.read().strip()
                return float(texto) if texto else 0.0
        except ValueError:
            return 0.0
    return 0.0


def guardar_record(score):
    with open(RECORD_FILE, "w", encoding="utf-8") as archivo:
        archivo.write(str(int(score)))


def dibujar_texto(pantalla, texto, tamaño, x, y, color=(255, 255, 255)):
    fuente = pygame.font.Font(None, tamaño)
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))


def main():
    pygame.init()
    try:
        pygame.mixer.init()
    except pygame.error:
        pass

    pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Cruzando la carretera")
    reloj = pygame.time.Clock()

    fondo = Fondo()
    jugador = Personaje()
    obstaculos = [Carro(SCREEN_WIDTH + 250), Carro(SCREEN_WIDTH + 600), Carro(SCREEN_WIDTH + 950)]
    record = leer_record()
    tiempo_inicio = pygame.time.get_ticks()
    juego_terminado = False
    score = 0
    logro_tocado = set()
    sonido_salto = pygame.mixer.Sound(os.path.join(SOUND_DIR, "salto.mp3"))
    sonido_perder = pygame.mixer.Sound(os.path.join(SOUND_DIR, "perder.mp3"))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    if juego_terminado:
                        jugador = Personaje()
                        obstaculos = [Carro(SCREEN_WIDTH + 250), Carro(SCREEN_WIDTH + 600), Carro(SCREEN_WIDTH + 950)]
                        tiempo_inicio = pygame.time.get_ticks()
                        juego_terminado = False
                        score = 0
                        logro_tocado = set()
                    else:
                        jugador.jump()
                        sonido_salto.play()

        if not juego_terminado:
            fondo.update()
            jugador.update()
            tiempo_actual = (pygame.time.get_ticks() - tiempo_inicio) / 1000
            score = int(tiempo_actual)
            velocidad = 6 + score // 5

            for obstaculo in obstaculos:
                obstaculo.update(velocidad)
                if jugador.rect.colliderect(obstaculo.rect):
                    juego_terminado = True
                    sonido_perder.play()
                    if score > record:
                        record = score
                        guardar_record(record)
                    break

            if score > 0 and score % 10 == 0 and score not in logro_tocado:
                logro_tocado.add(score)
                sonido_salto.play()

        pantalla.fill((0, 0, 0))
        fondo.draw(pantalla)
        jugador.draw(pantalla)
        for obstaculo in obstaculos:
            obstaculo.draw(pantalla)

        dibujar_texto(pantalla, f"Tiempo: {score} s", 28, 16, 16)
        dibujar_texto(pantalla, f"Récord: {int(record)} s", 28, 16, 50)
        dibujar_texto(pantalla, "Presiona ESPACIO para saltar", 24, 16, SCREEN_HEIGHT - 70)

        if juego_terminado:
            dibujar_texto(pantalla, "Perdiste. Presiona ESPACIO para reiniciar", 32, 170, SCREEN_HEIGHT // 2 - 20, (255, 210, 0))

        pygame.display.flip()
        reloj.tick(FPS)


if __name__ == "__main__":
    main()
