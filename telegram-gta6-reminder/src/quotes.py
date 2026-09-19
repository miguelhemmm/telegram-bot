"""Random philosophy quotes appended to the daily Telegram message.

Edit QUOTES freely: (text, author). Used by app.build_message().
"""

from __future__ import annotations

import random

QUOTES: list[tuple[str, str]] = [
    ("Solo sé que no sé nada, y el saber que nada sé me hace más sabio que quienes creen saberlo todo", "Sócrates"),
    ("Una vida sin examen no merece ser vivida, pues el hombre que no reflexiona sobre sí mismo vive como un extraño en su propia casa", "Sócrates"),
    ("La ignorancia es la semilla de todo mal, porque nadie que conozca verdaderamente el bien elegiría de forma voluntaria el mal", "Platón"),
    ("El comienzo es la parte más importante del trabajo, sobre todo cuando se trata de algo joven y tierno, pues es entonces cuando mejor se moldea y toma la forma que uno quiera imprimirle", "Platón"),
    (
        "Somos lo que hacemos repetidamente. La excelencia, entonces, no es un acto, sino un hábito, y por eso la virtud no se alcanza de una vez, sino que se forja día tras día en nuestras acciones",
        "Aristóteles",
    ),
    ("El sabio no dice todo lo que piensa, pero siempre piensa todo lo que dice, porque mide sus palabras con la misma prudencia con que mide sus actos", "Aristóteles"),
    ("Conócete a ti mismo, y solo entonces podrás conocer a los dioses y al universo, pues quien se ignora a sí mismo lo ignora todo", "Tales de Mileto"),
    ("Todo es agua, y de ella nace y a ella vuelve cuanto existe, porque el principio de todas las cosas es aquello sin lo cual nada puede vivir", "Tales de Mileto"),
    ("Nadie se baña dos veces en el mismo río, porque ni el río es el mismo ni el hombre es el mismo: todo fluye y nada permanece", "Heráclito"),
    ("Lo que no me mata me hace más fuerte, pues de la escuela de guerra de la vida sale fortalecido todo aquel que aprende a resistir el sufrimiento", "Nietzsche"),
    ("Quien tiene un porqué para vivir puede soportar casi cualquier cómo, porque un propósito verdadero convierte hasta el dolor más grande en algo que merece la pena atravesar", "Nietzsche"),
    (
        "Hasta que no hagas consciente lo inconsciente, dirigirá tu vida y lo llamarás destino, sin darte cuenta de que gran parte de aquello que atribuyes a la suerte no es más que el reflejo de lo que aún no te has atrevido a mirar dentro de ti",
        "Jung",
    ),
    ("Todo lo que nos irrita de los demás puede llevarnos a entendernos a nosotros mismos, porque aquello que juzgamos en otro suele ser la sombra de algo que no aceptamos en nuestro propio interior", "Jung"),
    ("No es que tengamos poco tiempo, es que perdemos mucho: la vida es lo bastante larga si se sabe emplear, pero se nos escapa entre las manos cuando la malgastamos en cosas vanas", "Séneca"),
    ("No te dañan las cosas, sino tu opinión sobre ellas, y por eso, cuando algo te perturbe, recuerda que está en tu poder cambiar el juicio con que lo miras", "Epicteto"),
    ("Actúa solo según aquella máxima por la cual puedas querer al mismo tiempo que se convierta en ley universal, pues solo así tu conducta será digna de un ser racional y libre", "Kant"),
    ("El hombre está condenado a ser libre; condenado porque no se ha creado a sí mismo, y sin embargo libre, porque una vez arrojado al mundo es responsable de todo lo que hace", "Sartre"),
        # Estoicos y clásicos
    ("La felicidad de tu vida depende de la calidad de tus pensamientos, así que cuida de las ideas que albergas, pues el alma se tiñe del color de aquello en lo que piensa con frecuencia", "Marco Aurelio"),
    ("Muy poco se necesita para tener una vida feliz; todo está dentro de ti, en tu manera de pensar y en la serenidad con que aceptas lo que no depende de ti", "Marco Aurelio"),
    ("Ningún viento es favorable para quien no sabe a dónde va, pues de nada sirve la fortuna a quien carece de un rumbo y de un puerto al que dirigir su travesía", "Séneca"),
    ("A veces, incluso vivir es un acto de valentía, porque hay circunstancias en las que seguir adelante exige más coraje que buscar una salida fácil", "Séneca"),
    ("Ningún hombre es libre si no es dueño de sí mismo, pues quien no gobierna sus propias pasiones vive esclavo por muchas cadenas de oro que lo adornen", "Epicteto"),
    ("No arruines lo que tienes deseando lo que no tienes; recuerda que lo que ahora posees fue una vez algo que solo esperabas alcanzar", "Epicuro"),
    ("El carácter es el destino del hombre, porque no son los dioses ni la suerte, sino nuestra propia forma de ser, la que va tejiendo el curso de nuestra vida", "Heráclito"),
    ("Apártate, que me tapas el sol; nada más deseo de ti ni de todo tu poder, pues ya poseo cuanto necesito para ser libre", "Diógenes"),
    ("Dadme un punto de apoyo y moveré el mundo, pues con la palanca y la razón adecuadas no hay peso que no pueda vencerse", "Arquímedes"),

    # Oriente
    ("Un viaje de mil millas comienza con un solo paso, y por eso lo grande nunca debe intimidarnos: basta con dar hoy el primer paso y no dejar de caminar", "Lao-Tsé"),
    ("Quien conoce a los demás es sabio; quien se conoce a sí mismo es iluminado; quien vence a los demás es fuerte, pero quien se vence a sí mismo posee la verdadera fortaleza", "Lao-Tsé"),
    ("El hombre que cometió un error y no lo corrige comete otro error mayor, porque persistir en la falta por orgullo es peor que la falta misma", "Confucio"),
    ("No importa lo lento que vayas, siempre que no te detengas, pues incluso el paso más pequeño, si se repite sin descanso, termina llevándote más lejos que cualquier arranque que se apaga pronto", "Confucio"),

    # Modernos
    ("El corazón tiene razones que la razón no entiende, y en las cosas del amor y de la fe hay una lógica del sentimiento que ningún argumento puede abarcar del todo", "Pascal"),
    ("No reír, no llorar, ni maldecir, sino comprender: esa es la actitud del sabio ante los asuntos humanos, que en lugar de juzgar busca entender las causas de todo cuanto sucede", "Spinoza"),
    ("El sentido común no es tan común como su nombre nos hace creer, pues lo que a unos parece evidente a otros les resulta absurdo, según la educación y las costumbres de cada cual", "Voltaire"),
    ("La duda es incómoda, pero la certeza es ridícula: solo los necios y los fanáticos están completamente seguros de todo, mientras que el sabio convive con la incertidumbre", "Voltaire"),
    ("Ten el valor de servirte de tu propio entendimiento: esa es la divisa de la Ilustración, la salida del hombre de la minoría de edad de la que él mismo es culpable", "Kant"),
    ("La salud no lo es todo, pero sin ella todo lo demás es nada, pues de poco sirven las riquezas y los honores a quien carece de la fuerza para disfrutarlos", "Schopenhauer"),
    ("La vida solo puede comprenderse mirando hacia atrás, pero debe vivirse mirando hacia adelante, y en esa tensión entre entender y avanzar transcurre toda nuestra existencia", "Kierkegaard"),

    # Siglo XX
    ("Los límites de mi lenguaje son los límites de mi mundo, porque aquello que no podemos nombrar tampoco podemos pensarlo con claridad ni compartirlo con los demás", "Wittgenstein"),
    ("En medio del invierno, por fin aprendí que había en mí un verano invencible, y eso me hizo comprender que, pase lo que pase, dentro de mí hay algo más fuerte que cualquier adversidad", "Camus"),
    ("El infierno son los otros, no porque los demás sean malos, sino porque a través de su mirada nos vemos juzgados y convertidos en aquello que ellos deciden que somos", "Sartre"),
    ("Yo soy yo y mi circunstancia, y si no salvo a mi circunstancia no me salvo yo, pues no somos seres aislados, sino que estamos entretejidos con el mundo que nos rodea", "Ortega y Gasset"),
    ("Caminante, no hay camino, se hace camino al andar; al andar se hace camino, y al volver la vista atrás se ve la senda que nunca se ha de volver a pisar", "Antonio Machado"),

    # Bonus para un dev
    ("La simplicidad es un prerrequisito para la fiabilidad, porque cuanto más sencillo es un sistema, menos lugares hay donde los errores puedan esconderse", "Dijkstra"),
    ("Hablar es barato; enséñame el código, porque las buenas intenciones y las grandes promesas no compilan: al final lo único que importa es lo que realmente funciona", "Linus Torvalds"),
    ("Los programas deben escribirse para que la gente los lea, y solo de paso para que las máquinas los ejecuten, pues el código lo lee mucha más gente de la que jamás lo escribió", "Abelson y Sussman"),

    # Más citas largas
    ("La libertad no es un estado que se alcanza de una vez para siempre, sino una conquista diaria que exige valentía para decidir y responsabilidad para asumir las consecuencias de lo que uno elige", "Simone de Beauvoir"),
    ("No podemos resolver nuestros problemas con el mismo nivel de pensamiento que teníamos cuando los creamos, y por eso el verdadero progreso empieza cuando nos atrevemos a cuestionar nuestras propias certezas", "Einstein"),
    ("Aquel que tiene un porqué lo bastante fuerte puede soportar casi cualquier cómo, porque el sufrimiento deja de ser insoportable en el instante en que encuentra un sentido dentro de una historia mayor", "Viktor Frankl"),
    ("Entre estímulo y respuesta hay un espacio, y en ese espacio reside nuestro poder de elegir la respuesta; en esa elección se encuentran nuestro crecimiento y nuestra libertad como seres humanos", "Viktor Frankl"),
    ("La vida no es la que uno vivió, sino la que uno recuerda y cómo la recuerda para contarla, pues la memoria selecciona, transforma y da forma a aquello que llamamos nuestra propia existencia", "Gabriel García Márquez"),
    ("El hombre superior es modesto en sus palabras, pero se excede en sus acciones, porque considera vergonzoso prometer más de lo que hace y encuentra su honor en cumplir en silencio lo que otros solo anuncian", "Confucio"),
    ("No hay viento favorable para el que no sabe hacia dónde navega, pero quien conoce su rumbo aprovecha hasta la tormenta, porque incluso los obstáculos se convierten en impulso cuando se tiene un destino claro", "Séneca"),
    ("La mayor gloria no está en no caer nunca, sino en levantarse cada vez que caemos, porque el valor de una vida no se mide por la ausencia de tropiezos, sino por la constancia con que uno vuelve a ponerse en pie", "Confucio"),
    ("La felicidad no es algo hecho: proviene de tus propias acciones, y por eso quien la espera pasivamente la aguarda en vano, mientras que quien la construye con pequeños actos cotidianos termina por encontrarla", "Dalái Lama"),
    ("Cuida tus pensamientos, porque se convierten en palabras; cuida tus palabras, porque se convierten en actos; cuida tus actos, porque se convierten en hábitos; cuida tus hábitos, porque se convierten en tu carácter y tu destino", "Proverbio"),
    ("El que no comprende una mirada tampoco comprenderá una larga explicación, porque hay verdades que solo se captan con la sensibilidad y no con la abundancia de argumentos", "Proverbio árabe"),
    ("Dos cosas llenan el ánimo de admiración y respeto, siempre nuevas y crecientes: el cielo estrellado sobre mí y la ley moral dentro de mí, y ambas me recuerdan a la vez mi pequeñez y mi dignidad", "Kant"),
]

_last: tuple[str, str] | None = None


def random_quote() -> str:
    """A formatted quote («text» — author), never the same one twice in a row."""
    global _last
    pool = [q for q in QUOTES if q != _last] or QUOTES
    _last = random.choice(pool)
    text, author = _last
    return f"«{text}» — {author}"
