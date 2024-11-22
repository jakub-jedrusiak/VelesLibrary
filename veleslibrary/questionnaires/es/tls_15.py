"""Triangular Love Scale (TLS-15)"""
import velesresearch as vls
from velesresearch.models import PageModel


def tls_15(
    name: str = "TLS_15",
    instruction: str | None = None,
    questionOptions: dict | None = None,
    pageOptions: dict | None = None,
) -> PageModel:
    """
    ## Triangular Love Scale (TLS-15)
        Sternberg’s triangular love theory questionnaire. A shorter version of TLS-45, that measures three components of love: intimacy, passion, and commitment.

    ## Original
        <div class="csl-bib-body" style="line-height: 2; margin-left: 2em; text-indent:-2em;">
        <div class="csl-entry">Kowal, M., Sorokowski, P., Dinić, B. M., Pisanski, K., Gjoneska, B., Frederick, D. A., Pfuhl, G., Milfont, T. L., Bode, A., Aguilar, L., García, F. E., Roberts, S. C., Abad-Villaverde, B., Kavčič, T., Miroshnik, K. G., Ndukaihe, I. L. G., Šafárová, K., Valentova, J. V., Aavik, T., … Sternberg, R. J. (2024). Validation of the short version (TLS-15) of the triangular love scale (TLS-45) across 37 languages. <i>Archives of Sexual Behavior</i>, <i>53</i>(2), 839–857. <https://doi.org/10.1007/s10508-023-02702-7></div>
        <div class="csl-entry">Sternberg, R. (1988). <i>The triangle of love: Intimacy, passion, commitment.</i> Basic Books.</div>
        <div class="csl-entry">Sternberg, R. J. (1997). Construct validation of a triangular love scale. <i>European Journal of Social Psychology</i>, <i>27</i>(3), 313–335. <https://doi.org/10.1002/(SICI)1099-0992(199705)27:3&lt;313::AID-EJSP824&gt;3.0.CO;2-4></div>
        </div>

    ## Score calculation
        An average.

    ## Reverse items
        None.

    ## Subscales
        1. Intimacy: 1, 2, 3, 4, 5
        2. Passion: 6, 7, 8, 9, 10
        3. Commitment: 11, 12, 13, 14, 15

    ## Reliability
        α = .95

        ### Subscales
            1. Intimacy: α = .89
            2. Passion: α = .89
            3. Commitment: α = .92

    ## Implemented by
        Piotr  Jędrusik (University of Wrocław)

    Args:
        name (str): Base name for pages and questions. Defaults to "TLS_15".
        instruction (str): Instruction for the questionnaire. None means that the default instruction will be used.
        questionOptions (dict | None): Additional options for questions as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the TLS-15 questionnaire. Use the `*` operator to unpack it to questions.
    """
    if instruction is None:
        instruction = """En esta parte del cuestionario, nos interesamos por lo que pasa dentro de lasrelaciones. Lea cada una de las siguientes frases, rellenando los espacios blancos y conteste pensandoen la persona que ama o a la que le tiene mucho cariño (su pareja, su enamorado(a) o compañera(o) de vida).Evalúe cada una de las frases con la siguiente escala, marcando el número que corresponda entre 1 (para nada) y 5 (extremamente).
1 - Para nada, 5 - Extremadamente"""

    if questionOptions is None:
        questionOptions = {}

    if pageOptions is None:
        pageOptions = {}

    items = """Tengo una relación afectuosa con mi pareja.
Mi pareja me da un apoyo emocional considerable.
Valoro mucho a mi pareja dentro de mi vida.
Tengo una relación agradable con mi pareja.
Creo que mi pareja realmente me entiende,
Mi relación con mi pareja es muy romántica.
Encuentro a mi pareja muy atractiva.
No puedo imaginar a otra persona que me haga tan feliz como mi pareja.
Hay algo casi “mágico” en mi relación con mi pareja.
Mi relación con mi pareja es apasionada.
Tengo confianza que la relación con mi pareja es estable.
Considero que mi compromiso con mi pareja es sólido.
Estoy seguro(a) de mi amor hacia mi pareja.
Considero que mi relación con mi pareja es permanente.
Tengo un sentimiento de responsabilidad hacia mi pareja.""".split(
        "\n"
    )

    scale = """1 – Para nada
2
3
4
5 – Extremadamente""".split(
        "\n"
    )

    return vls.page(
        name + "_page",
        vls.info(name + "_instruction", instruction),
        vls.radio(
            name,
            items,
            scale,
            **questionOptions,
        ),
        **pageOptions,
    )
