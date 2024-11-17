"""Rosenberg Self-Esteem Scale (RSES)"""

import velesresearch as vls
from velesresearch.models import PageModel


def rses(
    name: str = "RSES",
    instruction: str | None = None,
    questionOptions: dict | None = None,
    pageOptions: dict | None = None,
) -> PageModel:
    """
    ## Rosenberg Self-Esteem Scale (RSES)
        One of the most popular self-esteem scales. Measures global self-esteem.

    ## Original
        <div class="csl-bib-body" style="line-height: 2; margin-left: 2em; text-indent:-2em;">
        <div class="csl-entry">Rosenberg, M. (2011). <i>Rosenberg self-esteem scale</i> [Database record]. APA PsycTests. <https://doi.org/10.1037/t01038-000></div>
        </div>

    ## Adaptation:
        <div class="csl-bib-body" style="line-height: 2; margin-left: 2em; text-indent:-2em;">
        <div class="csl-entry">Dzwonkowska, I., Lachowicz-Tabaczek, K., &amp; Łaguna, M. (2008). <i>Samoocena i jej pomiar. Polska adaptacja skali SES M. Rosenberga. Podręcznik</i>. Pracownia Testów Psychologicznych Polskiego Towarzystwa Psychologicznego.</div>
        </div>

    ## Score calculation
        A simple sum.

    ## Reverse items
        3, 5, 8, 9, 10

    ## Subscales
        None.

    ## Reliability
        α = .82

    ## Implemented by
        Jakub Jędrusiak (University of Wrocław)

    Args:
        name (str): Base name for pages and questions. Defaults to "RSES".
        instruction (str): Instruction for the questionnaire. None means that the default instruction will be used.
        questionOptions (dict | None): Additional options for questions as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the RSES questionnaire. Use the `*` operator to unpack it to questions.
    """
    if instruction is None:
        instruction = """Poniżej znajdują się różne stwierdzenia, które odnoszą się do twoich przekonań o sobie. Wskaż, w jakim stopniu zgadzasz się bądź nie zgadzasz się z każdym z tych twierdzeń, otaczając kółkiem jedną z czterech możliwych odpowiedzi. Postaraj się określić to, co naprawdę sądzisz. Liczą się tylko szczere odpowiedzi."""

    if questionOptions is None:
        questionOptions = {}

    if pageOptions is None:
        pageOptions = {}

    items = """Uważam, że jestem osobą wartościową przynajmniej w takim samym stopniu, co inni.
Uważam, że posiadam wiele pozytywnych cech.
Ogólnie biorąc jestem skłonny(a) sądzić, że nie wiedzie mi się.
Potrafię robić różne rzeczy tak dobrze, jak większość innych ludzi.
Uważam, że nie mam wielu powodów, aby być z siebie dumn(ą)ym.
Lubię siebie.
Ogólnie rzecz biorąc, jestem z siebie zadowolon(a)y.
Chciał(a)bym mieć więcej szacunku dla samego siebie.
Czasami czuję się bezużyteczn(a)y.
Niekiedy uważam, że jestem do niczego.""".split(
        "\n"
    )

    scale = """1 – zdecydowanie zgadzam się
2 – zgadzam się
3 – nie zgadzam się
4 – zdecydowanie nie zgadzam się""".split(
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
