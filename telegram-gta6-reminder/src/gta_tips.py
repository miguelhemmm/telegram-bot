"""Random spoiler-free GTA 6 tips appended to the daily Telegram message.

Edit TIPS freely: one string each, no trailing period (random_tip() adds it).
Used by app.build_message(), same as quotes.random_quote().

Only controls, mechanics and systems: no missions, story beats or endings.
Buttons use PlayStation names.

Sources (checked Nov 2026): IGN "Secret Controls", PC Gamer "15 hidden
controls", Lifehacker "10 hidden controls", RockstarINTEL "30+ hidden
controls", Eurogamer "16 spoiler-free tips", Red Bull "beginner's guide".
"""

from __future__ import annotations

import random

TIPS: list[str] = [
    # Manejo
    "En el coche, toca R3 para insultar a los demás conductores",
    "Mantén R3 mientras conduces para mirar hacia atrás",
    "Toca dos veces Triángulo al bajarte y el motor, las luces y la radio se quedan encendidos para una huida rápida",
    "Mantén Círculo al volante para agacharte y esconderte de la policía",
    "Toca Cuadrado dentro del coche para abrir la puerta de golpe y tumbar a quien esté al lado",
    "Toca Círculo al conducir para encender los faros o poner las largas",
    "Izquierda o Derecha en la cruceta activan los intermitentes",
    "Toca dos veces Izquierda en la cruceta para apagar o encender la radio",
    "Mantén Izquierda en la cruceta y mueve el stick derecho para bajar ventanillas, poner las luces de emergencia o quitar el techo",
    "Para el piloto automático, marca un destino, mantén Abajo en la cruceta, pulsa Options y luego mantén Círculo",
    "Si vuelcas el coche, pulsa L3 y mantén Cuadrado para ponerlo otra vez sobre las ruedas",
    "Puedes empujar coches a pie con L3, y si mantienes Cuadrado les das un buen empujón",
    "Antes de robar un coche, abre la app Waink y mira qué alarma y qué rastreador tiene",
    "Un rastreador avanzado avisa a la policía si alejas el coche; la única forma de cortarlo es ir rápido",
    "Guarda un conjunto de ropa en el maletero para cambiarte tras un golpe",
    "Revisa los maleteros, sobre todo los de la policía; a veces hay armas o botín",
    "En un coche patrulla, mantén L3 y empuja el stick izquierdo para cambiar el tono de sirena",
    # A pie
    "Corre hacia un coche y pulsa Equis junto al capó para deslizarte por encima",
    "Mantén Círculo para apoyarte en una pared o sentarte en un muelle a mirar la vista",
    "Pulsa Arriba en la cruceta para sacar el móvil y ver la hora",
    "Compra auriculares en Zeke's Gadgets por unos 150 dólares y escucha la radio a pie",
    "Sin arma en la mano, apunta a alguien con L2 y mantén R1 para hacerle una peineta",
    "Mientras fumas, mantén R2 para lanzar la colilla hacia delante",
    "Mantén L2 y pulsa R3 para mirar en primera persona; así lees carteles y encuentras códigos de cajas fuertes",
    "Con un objeto en la mano, Izquierda en la cruceta lo pasa a la otra mano",
    # Combate
    "Si tu arma lleva mira, pulsa R3 al apuntar para usarla en primera persona",
    "Al apuntar, Izquierda en la cruceta cambia el arma de hombro",
    "Pulsa los dos sticks a la vez para el Modo Foco: marca enemigos en rojo, objetos en amarillo y dinero en verde",
    "En Modo Foco, una puerta blanca se puede abrir y una roja tiene alarma",
    "Una marca de impacto amarilla significa herido y fuera de combate; roja significa muerto",
    "En una pelea, agarra con R2, mantén Cuadrado y púlsalo repetidamente para hacer una llave",
    "En bici o moto, toca Cuadrado para dar una patada a quien tengas al lado",
    "Un silenciador te da más tiempo, porque la policía acude cuando alguien reporta disparos",
    # Botes y vuelo
    "Toca dos veces Triángulo en el timón y el barco sigue recto mientras paseas por cubierta",
    "Si una moto de agua queda varada, ponte detrás y mantén R1 para empujarla",
    "Al saltar de un avión o helicóptero llevas paracaídas de reserva; ábrelo con Equis en caída libre",
    "En vuelo, pulsa L3 para subir o bajar el tren de aterrizaje",
    "Da marcha atrás con una camioneta hasta un remolque de barco y se engancha solo; bájalo por una rampa para botarlo",
    # General
    "Mete el dinero en el banco cuanto antes; el efectivo se pierde si mueres o te arrestan",
    "Guarda la partida a menudo y en varias ranuras distintas",
    "Levantar pesas sube la Salud, el cardio sube la Resistencia y pescar o jugar al billar sube el Foco",
    "Dormir, ducharte y comer en casa te dan mejoras temporales de Salud, Resistencia y Foco",
    "Si Jason y Lucia entrenan juntos en el gimnasio, los dos mejoran aunque solo controles a uno",
    "Cambiar de personaje es el viaje rápido más barato: el otro suele esperarte cerca del refugio",
    "Con la app RydeMe puedes saltarte el trayecto pagando 100 dólares extra",
    "En el mapa, los edificios azul oscuro tienen interior; los azul claro son decorado",
    "La policía te sigue por la cara, la ropa, el arma y el coche; cámbialos sin que te vean para perderla",
    "Ponte gorra y pañuelo durante un golpe y quítatelos al salir",
    "Si robas en pareja, pulsa Derecha en la cruceta y luego Círculo para pasarle las bolsas de botín",
    "Si mueres, pierdes el efectivo y las bolsas de botín que lleves encima",
    "Toca Círculo para rechazar una llamada sin abrir el móvil",
    "Tu perfil criminal empeora si matas sin necesidad; jugar sin matar te mantiene como Profesional",
    "El perfil Irredimible es permanente, así que no te quedes demasiado tiempo como Psicópata",
]

_last: str | None = None


def random_tip() -> str:
    """A formatted tip (💡 Tip GTA 6: ...), never the same one twice in a row."""
    global _last
    pool = [t for t in TIPS if t != _last] or TIPS
    _last = random.choice(pool)
    return f"💡 Tip GTA 6: {_last}."
