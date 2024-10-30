"""Ten Item Personality Inventory (TIPI)"""

import velesresearch as vls
from velesresearch.models import PageModel


def tipi(
    name: str = "TIPI",
    instruction: str = "Poniżej przedstawiona jest lista cech, które <u>są lub nie są</u> Twoimi charakterystykami. Zaznacz przy poszczególnych stwierdzeniach, do jakiego stopnia <u>zgadzasz się lub nie zgadzasz</u> z każdym z nich. Oceń stopień, w jakim każde z pytań odnosi się do Ciebie.",
    questionOptions: dict | None = None,
    pageOptions: dict | None = None,
) -> PageModel:
    """
    ## Ten Item Personality Inventory (TIPI)
        Ten item adaptation of Big Five. Measures five personality traits: Extraversion, Agreeableness, Conscientiousness, Emotional Stability and Openness to Experience.

    ## Original
        Gosling, S. D., Rentfrow, P. J., Swann, W. B. Jr. (2003). A very brief measure of the Big-Five personality domains. *Journal of Research in Personality*, *37*, 504–528. <https://doi.org/10.1016/S0092-6566(03)00046-1>

    ## Adaptation
        Sorokowska, A., Słowińska A., Zbieg A., Sorokowski, P. (2014). _Polska adaptacja testu Ten Item Personality Inventory (TIPI) – TIPI-PL – wersja standardowa i internetowa._ Wrocław: WrocLab.

    ## Reverse items
        2, 4, 6, 8, 10

    ## Subscales
        1. Extraversion (1, 6)
        2. Agreeableness (2, 7)
        3. Conscientiousness (3, 8)
        4. Emotional Stability (4, 9)
        5. Openness to Experience (5, 10)

    ## Reliability

        ### Paper and pencil
            1. Extraversion: α = .68
            2. Agreeableness: α = .58
            3. Conscientiousness: α = .75
            4. Emotional Stability: α = .72
            5. Openness to Experience: α = .44

        ### Google Forms
            1. Extraversion: α = .74
            2. Agreeableness: α = .54
            3. Conscientiousness: α = .80
            4. Emotional Stability: α = .83
            5. Openness to Experience: α = .45

        ### Online application
            1. Extraversion: α = .70
            2. Agreeableness: α = .50
            3. Conscientiousness: α = .76
            4. Emotional Stability: α = .65
            5. Openness to Experience: α = .47

    ## Implemented by
        Jędrusiak, Jakub (University of Wrocław)

    Args:
        name (str): Base name for pages and questions. Defaults to "TIPI".
        instruction (str): Instruction for the questionnaire. Defaults to "Poniżej przedstawiona jest lista cech, które <u>są lub nie są</u> Twoimi charakterystykami. Zaznacz przy poszczególnych stwierdzeniach, do jakiego stopnia <u>zgadzasz się lub nie zgadzasz</u> z każdym z nich. Oceń stopień, w jakim każde z pytań odnosi się do Ciebie.".
        questionOptions (dict | None): Additional options for questions as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the TIPI questionnaire.
    """

    items = """Lubiącą towarzystwo innych, aktywną i optymistyczną.
Krytyczną względem innych, konfliktową.
Sumienną, zdyscyplinowaną.
Pełną niepokoju, łatwo wpadającą w przygnębienie.
Otwartą na nowe doznania, w złożony sposób postrzegającą świat.
Zamkniętą w sobie, wycofaną i cichą.
Zgodną, życzliwą.
Źle zorganizowaną, niedbałą.
Niemartwiącą się, stabilną emocjonalnie.
Trzymającą się utartych schematów, biorącą rzeczy wprost.""".split(
        "\n"
    )

    scale = """Zdecydowanie się nie zgadzam
Raczej się nie zgadzam
W niewielkim stopniu się nie zgadzam
Ani się zgadzam, ani się nie zgadzam
W niewielkim stopniu się zgadzam
Raczej się zgadzam
Zdecydowanie się zgadzam""".split(
        "\n"
    )

    return vls.page(
        name + "_page",
        vls.info(name + "_instruction", instruction),
        vls.info(name + "_intro", "**Spostrzegam siebie jako osobę:**"),
        vls.radio(
            name,
            items,
            scale,
            **questionOptions,
        ),
        **pageOptions,
    )
