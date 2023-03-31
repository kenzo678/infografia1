import time
import random
class Personaje:
    def __init__(self, nombre, vitalidad):
        self.nombre = nombre
        self.vitalidad = vitalidad
        self.takeCrit = 1
    
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def esta_vivo(self):
        return self.vitalidad>0

class Jugador(Personaje):
    def __init__(self, nombre, vitalidad, daño, habilidades):
        super().__init__(nombre, vitalidad)
        self.daño = daño
        self.habilidades = habilidades
    
    def recibir_daño(self, daño):
        self.vitalidad -= daño

    def listar_habilidades(self):
        for h in self.habilidades:
            print(f"Puedo {h}")

    def countr(self, enemy):
        dmg1 = int(random.randrange(int(self.daño-self.daño*0.3),int(self.daño+self.daño*0.3)));
        if(self.takeCrit > round(random.randrange(0,100))):
            print(f"Critico !!! El dano de {dmg1} se multiplica por 2 !!!");
            dmg1 = dmg1*2;
        print(f"Jugador {self.nombre} atacando al enemigo {enemy.nombre} con daño: {dmg1}");
        enemy.recibir_daño(dmg1)

class Enemigo(Personaje):
    def __init__(self, nombre, vitalidad, daño, ataque_esp):
        super().__init__(nombre, vitalidad)
        self.daño = daño
        self.ataque_esp = ataque_esp
        self.takeCrit = 1

    def recibir_daño(self, daño):
        self.vitalidad -= daño

    def esta_vivo(self):
        return self.vitalidad>0

    #Ahora el dano que va a hacer va a ser dano random.
    #En un rango alrededor del dano base del enemigo
    #Como en pokemon, hay "damage rolls"
    def atacar_jugador(self, jugador):
        dmg1 = int(random.randrange(int(self.daño-self.daño*0.3),int(self.daño+self.daño*0.3)));
        if(self.takeCrit > round(random.randrange(0,100))):
            print(f"Critico !!! El dano de {dmg1} se multiplica por 2 !!!");
            dmg1 = dmg1*2;
        print(f"Enemigo {self.nombre} atacando a jugador {jugador.nombre} con daño: {dmg1}");
        jugador.recibir_daño(dmg1)


jugador = Jugador("Juan", 100, 7, ["atacar", "volar", "esquivar"])
jugador.listar_habilidades()
jugador.saludo()

enemigo = Enemigo("Raul", 50, 10, 70)

while(jugador.esta_vivo() and enemigo.esta_vivo()):
    enemigo.atacar_jugador(jugador)
    print(f"vitalidad {jugador.nombre}: {jugador.vitalidad}")
    #print(f"esta vivo {jugador.nombre}?: {jugador.esta_vivo()}")
    if(jugador.esta_vivo()):
        jugador.countr(enemigo)
        print(f"vitalidad {enemigo.nombre}: {enemigo.vitalidad}")
    #print(f"esta vivo {enemigo.nombre}?: {enemigo.esta_vivo()}")
    time.sleep(2)

if(not enemigo.esta_vivo()):
    print(f"El enemigo {enemigo.nombre} ha muerto")
    print("ganaste!!")


print(f"El jugador {jugador.nombre} ha muerto")

# EJERCICIO:
# Modificar este programa para agregar las siguientes caracteristicas:
# 1. Agregar logica de daño aleatorio al enemigo.
# 2. Agregar lógica de contraataque del jugador.
# 3. Agregar posibilidad de daño crítico en contra ataque del jugador.

