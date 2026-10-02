"""Random philosophy quotes appended to the daily Telegram message.

Edit QUOTES freely: (text, author). Used by app.build_message().
"""

from __future__ import annotations

import random

QUOTES: list[tuple[str, str]] = [
    ("Solo sé que no sé nada, y el saber que nada sé me hace más sabio que quienes creen saberlo todo", "Sócrates"),
    ("Si pedimos el éxito preparándonos para el fracaso, sólo obtendremos aquello para lo cual nos preparamos", "Florence Scovel"),
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

    # Estoicos (más)
    ("Al amanecer, dite a ti mismo: hoy me encontraré con gente entrometida, ingrata, arrogante y envidiosa; pero yo, que conozco la naturaleza del bien y del mal, sé que ninguno de ellos puede dañarme, porque nadie puede arrastrarme a lo vergonzoso sin mi consentimiento", "Marco Aurelio"),
    ("El obstáculo para la acción hace avanzar la acción; lo que se interpone en el camino se convierte en el camino, porque la mente sabe adaptar y transformar cada impedimento en materia para su propio propósito", "Marco Aurelio"),
    ("Pierde el tiempo quien vive como si fuera a vivir para siempre; recuerda que cada día puede ser el último y actúa, habla y piensa como quien sabe que en cualquier momento puede partir de esta vida", "Marco Aurelio"),
    ("La mejor venganza es no ser como aquel que te hizo daño, porque responder a la ofensa con la misma moneda es permitir que el otro decida quién eres y en qué te conviertes", "Marco Aurelio"),
    ("Sufrimos más en la imaginación que en la realidad, pues la mayoría de los males que tememos nunca llegan, y aquellos que llegan rara vez son tan terribles como los habíamos pintado en nuestra mente", "Séneca"),
    ("Mientras aplazamos la vida, ella pasa de largo; todo lo demás nos es ajeno, solo el tiempo es nuestro, y sin embargo es lo único que dejamos que cualquiera nos arrebate sin protestar", "Séneca"),
    ("La suerte es lo que sucede cuando la preparación se encuentra con la oportunidad, y por eso quien se prepara cada día no teme al azar, sino que lo espera con las manos listas para aprovecharlo", "Séneca"),
    ("Hay cosas que dependen de nosotros y otras que no dependen de nosotros: de nosotros dependen el juicio, el deseo y la aversión; no dependen de nosotros el cuerpo, la reputación ni el poder, y la paz del alma consiste en no confundir unas con otras", "Epicteto"),
    ("Primero dite a ti mismo lo que quieres ser, y luego haz lo que tengas que hacer, pues sin una idea clara de la persona que deseas llegar a ser, cualquier esfuerzo se dispersa como agua sobre la arena", "Epicteto"),
    ("Si quieres progresar, conténtate con parecer tonto e ignorante en las cosas externas, porque quien pretende aparentar saberlo todo nunca se atreve a aprender nada nuevo", "Epicteto"),

    # Griegos (más)
    ("La muerte no es nada para nosotros, porque mientras existimos la muerte no está presente, y cuando la muerte está presente nosotros ya no existimos; por eso es insensato angustiarse por aquello que nunca vamos a experimentar", "Epicuro"),
    ("De todos los bienes que la sabiduría procura para la felicidad de la vida entera, el mayor con mucho es la amistad, porque un amigo verdadero multiplica las alegrías y divide las penas", "Epicuro"),
    ("La amistad es un alma que habita en dos cuerpos, un corazón que habita en dos almas, y sin amigos nadie querría vivir, aunque poseyera todos los demás bienes del mundo", "Aristóteles"),
    ("Cualquiera puede enfadarse, eso es fácil; pero enfadarse con la persona adecuada, en el grado exacto, en el momento oportuno, con el propósito justo y del modo correcto, eso ciertamente no resulta tan fácil", "Aristóteles"),
    ("El precio de desentenderse de la política es ser gobernado por los peores hombres, porque el espacio que los justos abandonan por indiferencia siempre termina ocupado por quienes buscan el poder para sí mismos", "Platón"),
    ("Vencerse a sí mismo es la primera y la mejor de todas las victorias, mientras que ser vencido por uno mismo es lo más vergonzoso y lo peor de todo, porque la guerra más difícil es la que cada uno libra en su interior", "Platón"),
    ("El camino hacia arriba y el camino hacia abajo son uno y el mismo, y la armonía oculta es mejor que la visible, porque de la tensión entre los contrarios nace el orden del mundo", "Heráclito"),

    # Oriente (más)
    ("El agua es lo más blando y débil que existe, pero nada la supera para vencer a lo duro y fuerte; así, lo flexible prevalece sobre lo rígido, y quien sabe ceder termina por durar más que quien se obstina", "Lao-Tsé"),
    ("Cuando soy capaz de desprenderme de lo que soy, me convierto en lo que podría ser; cuando me desprendo de lo que tengo, recibo lo que necesito, porque el vaso solo es útil gracias a su vacío", "Lao-Tsé"),
    ("Aprender sin reflexionar es malgastar la energía, y reflexionar sin aprender es peligroso, porque el conocimiento sin pensamiento se vuelve memoria muerta y el pensamiento sin conocimiento se pierde en fantasías", "Confucio"),
    ("Elige un trabajo que ames y no tendrás que trabajar ni un día de tu vida, porque cuando la tarea coincide con la vocación, el esfuerzo deja de sentirse como carga y se convierte en expresión de uno mismo", "Confucio"),
    ("Aferrarse a la ira es como agarrar un carbón ardiente con la intención de arrojárselo a otro: eres tú quien acaba quemándose, mientras el otro quizá ni siquiera se entera de tu enojo", "Buda"),
    ("No mores en el pasado, no sueñes con el futuro; concentra la mente en el momento presente, porque es el único lugar donde la vida realmente sucede y donde puedes actuar sobre ella", "Buda"),
    ("La herida es el lugar por donde entra la luz, y por eso no huyas de tu dolor: en él se esconde a menudo la puerta hacia una comprensión más profunda de ti mismo y de los demás", "Rumi"),
    ("Ayer era inteligente, así que quería cambiar el mundo; hoy soy sabio, así que me estoy cambiando a mí mismo, porque he comprendido que toda transformación verdadera empieza desde dentro", "Rumi"),
    ("Conoce a tu enemigo y conócete a ti mismo, y en cien batallas nunca estarás en peligro; si te conoces a ti mismo pero no al enemigo, tus posibilidades de ganar o perder serán iguales", "Sun Tzu"),

    # Renacimiento y modernos (más)
    ("Toda la desgracia de los hombres proviene de una sola cosa: no saber permanecer en reposo en una habitación, porque huimos del silencio para no tener que enfrentarnos a nosotros mismos", "Pascal"),
    ("Pienso, luego existo: de todo puedo dudar, de los sentidos, del mundo y hasta de mi propio cuerpo, pero no puedo dudar de que dudo, y en esa duda misma encuentro la primera certeza firme", "Descartes"),
    ("No basta tener buen ingenio; lo principal es aplicarlo bien, porque las almas más grandes son capaces de los mayores vicios tanto como de las mayores virtudes, y los que avanzan despacio por el camino recto llegan más lejos que los que corren apartándose de él", "Descartes"),
    ("Mi vida ha estado llena de terribles desgracias, la mayoría de las cuales nunca sucedieron, pues el miedo inventa catástrofes que el tiempo casi nunca llega a confirmar", "Montaigne"),
    ("La cosa más importante del mundo es saber pertenecerse a uno mismo, porque quien depende enteramente de la opinión ajena ha entregado a otros las llaves de su propia casa", "Montaigne"),
    ("El hombre nace libre, y sin embargo en todas partes se encuentra encadenado; muchos se creen amos de los demás sin dejar de ser más esclavos que ellos", "Rousseau"),
    ("El talento alcanza un blanco que nadie más puede alcanzar; el genio alcanza un blanco que nadie más puede ver, porque su mirada se adelanta a su tiempo y descubre lo que otros aún no imaginan", "Schopenhauer"),
    ("Quien con monstruos lucha cuide de no convertirse a su vez en monstruo, porque cuando miras largo tiempo a un abismo, también el abismo mira dentro de ti", "Nietzsche"),
    ("Hay que llevar todavía un caos dentro de sí para poder dar a luz una estrella danzarina, pues la creación nace del desorden fecundo y no de la calma estéril de quien nunca se inquieta", "Nietzsche"),
    ("Sin música la vida sería un error, porque hay en ella algo que las palabras no alcanzan: una forma de decir lo indecible y de hacernos sentir que la existencia, pese a todo, merece celebrarse", "Nietzsche"),
    ("La angustia es el vértigo de la libertad, porque cuando el hombre contempla todas las posibilidades abiertas ante sí y comprende que debe elegir, siente el mismo mareo que quien mira al fondo de un precipicio", "Kierkegaard"),

    # Siglo XX (más)
    ("Hay que imaginarse a Sísifo feliz, porque la lucha misma hacia las cumbres basta para llenar el corazón de un hombre, aunque la roca vuelva a caer una y otra vez al fondo del valle", "Camus"),
    ("No camines delante de mí, puede que no te siga; no camines detrás de mí, puede que no te guíe; camina junto a mí y sé simplemente mi amigo", "Camus"),
    ("Al hombre se le puede arrebatar todo salvo una cosa: la última de las libertades humanas, la elección de la actitud personal ante un conjunto de circunstancias, para decidir su propio camino", "Viktor Frankl"),
    ("De lo que no se puede hablar hay que callar, porque hay regiones de la experiencia, como lo ético y lo místico, que no se dejan decir sino solo mostrar", "Wittgenstein"),
    ("La vida buena es una vida inspirada por el amor y guiada por el conocimiento, pues el amor sin conocimiento se vuelve ciego y el conocimiento sin amor se vuelve frío", "Bertrand Russell"),
    ("El problema del mundo es que los estúpidos están completamente seguros de todo, mientras que los inteligentes están llenos de dudas, y así la confianza acaba casi siempre del lado equivocado", "Bertrand Russell"),
    ("Quien no recuerda el pasado está condenado a repetirlo, porque la experiencia que no se convierte en memoria no deja enseñanza, y cada generación vuelve a tropezar con las mismas piedras", "George Santayana"),
    ("No se nace mujer: se llega a serlo, pues ningún destino biológico, psíquico o económico define por sí solo la figura que un ser humano adopta en la sociedad, sino el conjunto de la civilización", "Simone de Beauvoir"),
    ("La tristeza de la época es que la ciencia acumula saber más deprisa de lo que la sociedad acumula sabiduría, y así tenemos cada vez más poder y cada vez menos criterio para usarlo", "Isaac Asimov"),
    ("La vida es aquello que te va sucediendo mientras te empeñas en hacer otros planes, y por eso conviene no aplazar la alegría hasta que todo esté en orden, porque nunca lo estará del todo", "John Lennon"),
    ("El mundo no será destruido por los que hacen el mal, sino por aquellos que los miran sin hacer nada, porque la indiferencia de los buenos es el mejor aliado de cualquier injusticia", "Einstein"),
    ("La vida es como montar en bicicleta: para mantener el equilibrio hay que seguir moviéndose, y quien se detiene por miedo a caer termina cayendo precisamente por haberse detenido", "Einstein"),

    # Literatura hispana
    ("Todo lo que se ha perdido y todo lo que nunca se tuvo sigue estando en la memoria, que es el único paraíso del que no podemos ser expulsados", "Jorge Luis Borges"),
    ("He cometido el peor de los pecados que un hombre puede cometer: no he sido feliz; que los glaciares del olvido me arrastren y me pierdan, despiadados", "Jorge Luis Borges"),
    ("La libertad, Sancho, es uno de los más preciosos dones que a los hombres dieron los cielos; con ella no pueden igualarse los tesoros que encierra la tierra ni el mar encubre", "Cervantes"),
    ("El que lee mucho y anda mucho, ve mucho y sabe mucho, porque los libros y los caminos son las dos grandes escuelas donde el hombre aprende a conocer el mundo y a sí mismo", "Cervantes"),
    ("¿Qué es la vida? Un frenesí. ¿Qué es la vida? Una ilusión, una sombra, una ficción, y el mayor bien es pequeño; que toda la vida es sueño, y los sueños, sueños son", "Calderón de la Barca"),
    ("Andábamos sin buscarnos, pero sabiendo que andábamos para encontrarnos, porque hay encuentros que el azar solo finge organizar y que en verdad llevaban mucho tiempo esperándonos", "Julio Cortázar"),
    ("El secreto de una buena vejez no es otra cosa que un pacto honrado con la soledad, y quien aprende a estar en paz consigo mismo nunca se siente del todo solo", "Gabriel García Márquez"),
    ("Hay golpes en la vida tan fuertes, yo no sé; golpes como del odio de Dios, como si ante ellos la resaca de todo lo sufrido se empozara en el alma", "César Vallejo"),
    ("Podrán cortar todas las flores, pero no podrán detener la primavera, porque lo que nace de la raíz profunda de un pueblo vuelve a brotar aunque intenten arrancarlo mil veces", "Pablo Neruda"),

    # Bonus dev (más)
    ("Depurar es el doble de difícil que escribir el código en primer lugar; por lo tanto, si escribes el código de la forma más ingeniosa posible, por definición no eres lo bastante listo para depurarlo", "Brian Kernighan"),
    ("La optimización prematura es la raíz de todos los males, porque dedicar tiempo a acelerar lo que no importa nos distrae de entender lo que sí importa y llena el código de complejidad innecesaria", "Donald Knuth"),
    ("Cualquier tonto puede escribir código que un ordenador entienda; los buenos programadores escriben código que los humanos puedan entender, porque el software vive mucho más tiempo en manos de quienes lo mantienen que de quien lo creó", "Martin Fowler"),
    ("Hay dos maneras de diseñar software: una es hacerlo tan simple que obviamente no tenga deficiencias, y la otra es hacerlo tan complicado que no tenga deficiencias obvias; la primera es mucho más difícil", "Tony Hoare"),
    ("Primero resuelve el problema, después escribe el código, porque teclear sin haber entendido lo que se quiere construir solo produce más líneas que luego habrá que borrar", "John Johnson"),
    ("La perfección se alcanza no cuando no hay nada más que añadir, sino cuando ya no queda nada que quitar, porque la elegancia de una obra nace de la renuncia a todo lo superfluo", "Antoine de Saint-Exupéry"),
]

_last: tuple[str, str] | None = None


def random_quote() -> str:
    """A formatted quote («text» — author), never the same one twice in a row."""
    global _last
    pool = [q for q in QUOTES if q != _last] or QUOTES
    _last = random.choice(pool)
    text, author = _last
    return f"«{text}» — {author}"
