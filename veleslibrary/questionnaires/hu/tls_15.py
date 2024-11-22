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
        <div class="csl-entry">Sternberg, R. J. (1988). <i>The triangle of love: Intimacy, passion, commitment</i>. Basic Books.</div>
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
        Jakub Jędrusiak (University of Wrocław)

    Args:
        name (str): Base name for pages and questions. Defaults to "TLS_15".
        instruction (str): Instruction for the questionnaire. None means that the default instruction will be used.
        questionOptions (dict | None): Additional options for questions as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the TLS-15 questionnaire. Use the `*` operator to unpack it to questions.
    """
    if instruction is None:
        instruction = """A kérdőív jelen szakaszában párkapcsolatokban végbemenő folyamatokra vagyunk kíváncsiak. Az alábbi állítások olvasása közben kérjük, gondoljon arra a személyre, akibe szerelmes vagy akihez szorosan kötődik (a párjára/házastársára).Értékelje az állításokkal való egyetértésének mértékét az alábbi skála segítségével és válassza ki a megfelelő számot 1 (egyáltalán nem értek egyet) és 5 (teljes mértékben egyetértek) között.
1 - Egyáltalán nem értek egyet, 5 - Teljes mértékben egyetértek"""

    if questionOptions is None:
        questionOptions = {}

    if pageOptions is None:
        pageOptions = {}

    items = """Szerető kapcsolatot ápolok a párommal.
Jelentős érzelmi támogatást kapok a páromtól.
Nagyra becsülöm a páromat az életemben.
Kellemes a kapcsolatom a párommal.
Úgy érzem, a párom valóban megért engem.
A párommal való kapcsolatom rendkívül romantikus.
A páromat rendkívül vonzónak találom.
Elképzelhetetlennek tartom, hogy valaki más olyan boldoggá tudjon tenni, mint a párom.
Van valami szinte “varázslatos” a párommal való kapcsolatban.
A párommal való kapcsolatom szenvedélyes.
Biztos vagyok a párommal való kapcsolatom stabilitásában.
A párom iránti elkötelezettségemet szilárdnak érzem.
Biztos vagyok a párom iránt érzett szerelmemben.
A párommal való kapcsolatomat tartósnak látom.
Úgy érzem, felelősséggel tartozom a párom iránt.""".split(
        "\n"
    )

    scale = """1 – Egyáltalán nem értek egyet
2
3
4
5 – Teljes mértékben egyetértek""".split(
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
