# importamos el paquete
import arcade
import math
import cmath

# definicion de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Hola Arcade"


def drawflower2(xspot, yspot):
 for angle in range(0, 360, 45):
    r = 65
    phi = math.radians(angle)
    center_c = cmath.rect(r, phi)
    arcade.draw_circle_filled(
        int(center_c.real + xspot),
        int(center_c.imag + yspot),
        30,
        arcade.color.RED_ORANGE
        )

    arcade.draw_circle_filled(xspot, yspot, 50, arcade.color.YELLOW)

def drawcat(xspot, yspot):
 arcade.draw_circle_filled(xspot, yspot, 40, arcade.color.GRAY_ASPARAGUS)
 arcade.create_triangles_filled_with_colors([1,2,3], arcade.color.GRAY_ASPARAGUS)
 arcade.create_triangles_filled_with_colors([4,5,6], arcade.color.GRAY_ASPARAGUS)
 


if __name__ == "__main__":
    # Crear nueva ventana
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    # Cambiar el color de fondo
    arcade.set_background_color(arcade.color.WHITE)

    # iniciar render
    arcade.start_render()

    # Funciones para dibujar
    drawflower2(300,400)
    drawflower2(100,200)
    drawflower2(500,330)
    drawflower2(85,600)

    # finalizar render
    arcade.finish_render()

    # Correr el programa
    arcade.run()
