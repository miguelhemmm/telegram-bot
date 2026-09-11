"""Random philosophy quotes appended to the daily Telegram message.

Edit QUOTES freely: (text, author). Used by app.build_message().
"""

from __future__ import annotations

import random

QUOTES: list[tuple[str, str]] = [
    ("Solo sé que no sé nada", "Sócrates"),
    ("Una vida sin examen no merece ser vivida", "Sócrates"),
    ("La ignorancia es la semilla de todo mal", "Platón"),
    ("El comienzo es la parte más importante del trabajo", "Platón"),
    (
        "Somos lo que hacemos repetidamente. La excelencia no es un acto, sino un hábito",
        "Aristóteles",
    ),
    ("El sabio no dice todo lo que piensa, pero siempre piensa todo lo que dice", "Aristóteles"),
    ("Conócete a ti mismo", "Tales de Mileto"),
    ("Todo es agua", "Tales de Mileto"),
    ("Nadie se baña dos veces en el mismo río", "Heráclito"),
    ("Lo que no me mata me hace más fuerte", "Nietzsche"),
    ("Quien tiene un porqué para vivir puede soportar casi cualquier cómo", "Nietzsche"),
    (
        "Hasta que no hagas consciente lo inconsciente, dirigirá tu vida y lo llamarás destino",
        "Jung",
    ),
    ("Todo lo que nos irrita de los demás puede llevarnos a entendernos a nosotros mismos", "Jung"),
    ("Pienso, luego existo", "Descartes"),
    ("No es que tengamos poco tiempo, es que perdemos mucho", "Séneca"),
    ("No te dañan las cosas, sino tu opinión sobre ellas", "Epicteto"),
    ("Actúa solo según aquella máxima que puedas querer que se convierta en ley universal", "Kant"),
    ("El hombre está condenado a ser libre", "Sartre"),
        # Estoicos y clásicos
    ("La felicidad de tu vida depende de la calidad de tus pensamientos", "Marco Aurelio"),
    ("Muy poco se necesita para tener una vida feliz", "Marco Aurelio"),
    ("Ningún viento es favorable para quien no sabe a dónde va", "Séneca"),
    ("A veces, incluso vivir es un acto de valentía", "Séneca"),
    ("Ningún hombre es libre si no es dueño de sí mismo", "Epicteto"),
    ("No arruines lo que tienes deseando lo que no tienes", "Epicuro"),
    ("El carácter es el destino", "Heráclito"),
    ("Apártate, que me tapas el sol", "Diógenes"),
    ("Dadme un punto de apoyo y moveré el mundo", "Arquímedes"),

    # Oriente
    ("Un viaje de mil millas comienza con un solo paso", "Lao-Tsé"),
    ("Quien conoce a los demás es sabio; quien se conoce a sí mismo es iluminado", "Lao-Tsé"),
    ("El hombre que cometió un error y no lo corrige comete otro error mayor", "Confucio"),
    ("No importa lo lento que vayas, siempre que no te detengas", "Confucio"),

    # Modernos
    ("El corazón tiene razones que la razón no entiende", "Pascal"),
    ("No reír, no llorar: comprender", "Spinoza"),
    ("El sentido común no es tan común", "Voltaire"),
    ("La duda es incómoda, pero la certeza es ridícula", "Voltaire"),
    ("Ten el valor de servirte de tu propio entendimiento", "Kant"),
    ("La salud no lo es todo, pero sin ella todo lo demás es nada", "Schopenhauer"),
    ("La vida solo puede comprenderse hacia atrás, pero debe vivirse hacia adelante", "Kierkegaard"),
    ("Sin música, la vida sería un error", "Nietzsche"),

    # Siglo XX
    ("Los límites de mi lenguaje son los límites de mi mundo", "Wittgenstein"),
    ("En medio del invierno aprendí que había en mí un verano invencible", "Camus"),
    ("El infierno son los otros", "Sartre"),
    ("Yo soy yo y mi circunstancia", "Ortega y Gasset"),
    ("Caminante, no hay camino: se hace camino al andar", "Antonio Machado"),

    # Bonus para un dev
    ("La simplicidad es un prerrequisito para la fiabilidad", "Dijkstra"),
    ("Hablar es barato; enséñame el código", "Linus Torvalds"),
    ("Los programas deben escribirse para que la gente los lea, y solo de paso para que las máquinas los ejecuten", "Abelson y Sussman"),
]

_last: tuple[str, str] | None = None


def random_quote() -> str:
    """A formatted quote («text» — author), never the same one twice in a row."""
    global _last
    pool = [q for q in QUOTES if q != _last] or QUOTES
    _last = random.choice(pool)
    text, author = _last
    return f"«{text}» — {author}"
