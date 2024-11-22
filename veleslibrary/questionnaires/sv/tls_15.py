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
        Kowal, Marta, i in. „Validation of the Short Version (TLS-15) of the Triangular Love Scale (TLS-45) across 37 Languages”. Archives of Sexual Behavior, t. 53, nr 2, luty 2024, s. 839–57. DOI.org (Crossref), https://doi.org/10.1007/s10508-023-02702-7.
        
        <div class="csl-bib-body" style="line-height: 2; margin-left: 2em; text-indent:-2em;">
        <div class="csl-entry">Kowal, M., Sorokowski, P., Dinić, B. M., Pisanski, K., Gjoneska, B., Frederick, D. A., Pfuhl, G., Milfont, T. L., Bode, A., Aguilar, L., García, F. E., Roberts, S. C., Abad-Villaverde, B., Kavčič, T., Miroshnik, K. G., Ndukaihe, I. L. G., Šafárová, K., Valentova, J. V., Aavik, T., … Sternberg, R. J. (2024). Validation of the short version (TLS-15) of the triangular love scale (TLS-45) across 37 languages. <i>Archives of Sexual Behavior</i>, <i>53</i>(2), 839–857. <https://doi.org/10.1007/s10508-023-02702-7></div>
        <div class="csl-entry">Sternberg , R. J. (1988). <i>The triangle of love: Intimacy, passion, commitment.</i> Basic Books.</div>
        <div class="csl-entry">Sternberg, R. J. (1997a). Construct validation of a triangular love scale. <i>European Journal of Social Psychology</i>, <i>27</i>(3), 313–335. <https://doi.org/10.1002/(SICI)1099-0992(199705)27:3&lt;313::AID-EJSP824&gt;3.0.CO;2-4></div>
        <div class="csl-entry">Sternberg, R. J. (1997b). Construct validation of a triangular love scale. <i>European Journal of Social Psychology</i>, <i>27</i>(3), 313–335. <https://doi.org/10.1002/(SICI)1099-0992(199705)27:3&lt;313::AID-EJSP824&gt;3.0.CO;2-4></div>
        </div>
        
        Sternberg, Robert J. „Construct Validation of a Triangular Love Scale”. European Journal of Social Psychology, t. 27, nr 3, maj 1997, s. 313–35. DOI.org (Crossref), <https://doi.org/10.1002/(SICI)1099-0992(199705)27:3><313::AID-EJSP824>3.0.CO;2-4.
    
    ## Score calculation
        An average.

    ## Reverse items
        None.
    
    ## Subscales
        1. Intimacy: 5
        2. Commitment: 5
        3. Passion: 5

    ## Reliability
        α = .95

        ### Subscales
            1. Intimacy: α = .89
            2. Commitment: α = .92
            3. Passion: α = .89

    ## Implemented by
        Julia Jankowska (University of Wrocław)

    Args:
        name (str): Base name for pages and questions. Defaults to "TLS_15".
        instruction (str): Instruction for the questionnaire. None means that the default instruction will be used.
        questionOptions (dict | None): Additional options for questions as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the TLS-15 questionnaire. Use the `*` operator to unpack it to questions.
    """
    if instruction is None:
        instruction = """I den här delen av enkäten är vi intresserade av processer som sker inom förhållanden. Läs vart och ett av följande påståenden, och fyll i blankstegen med namnet på en person som du älskar eller bryr dig mycket om (din pojkvän/flickvän/make/maka). Ange i vilken utsträckning du håller med om varje påstående enligt följande skala och välj ett nummer från 1 (inte alls) till 5 (extremt mycket).
1 - Inte alls, 5 - Extremt mycket"""

    if questionOptions is None:
        questionOptions = {}

    if pageOptions is None:
        pageOptions = {}

    items = """Jag har ett varmt förhållande med min partner.
Jag får mycket känslomässigt stöd från min partner.
Jag värdesätter min partner mycket i mitt liv.
Jag har ett bekvämt förhållande med min partner.
Jag känner att min partner verkligen förstår mig.
Mitt förhållande med min partner är väldigt romantiskt. Jag tycker att min partner är mycket attraktiv personligen.
Jag kan inte föreställa mig en annan person som skulle göra mig lika lycklig som min partner gör.
Det finns något nästan "magiskt" med mitt förhållande med min partner.
Mitt förhållande med min partner är passionerat.
Jag har förtroende för att mitt förhållande med min partner är stabilt.
Jag ser mitt engagemang för min partner som stabilt.
Jag är säker på min kärlek till min partner.
Jag ser mitt förhållande med min partner som permanent.
Jag har en känsla av ansvar gentemot min partner.""".split(
        "\n"
    )

    scale = """1 – Inte alls
2
3
4
5 – Extremt mycket""".split(
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
