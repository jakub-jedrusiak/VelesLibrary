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
        <div class="csl-entry">Sternberg, R. J. (1988). <i>The triangle of love: Intimacy, passion, commitment.</i> Basic Books.</div>
        <div class="csl-entry">Sternberg, R. J. (1997). Construct validation of a triangular love scale. <i>European Journal of Social Psychology</i>, <i>27</i>(3), 313–335. <https://doi.org/10.1002/(SICI)1099-0992(199705)27:3&lt;313::AID-EJSP824&gt;3.0.CO;2-4></div>
        </div>
    
    ## Score calculation
        An average.

    ## Reverse items
        None.
    
    ## Subscales
        1.  Intimacy: 5
        2. Passion: 5
        3. Commitment: 5

    ## Reliability
        α = .95

        ### Subscales
            1.  Intimacy: α = .89
            2. Passion: α = .89
            3. Commitment: α = .92

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
        instruction = """W tej części badania, jesteśmy zainteresowani tym, co się dzieje w związkach. Przeczytaj proszę poniższe stwierdzenia, myśląc o osobie, którą kochasz lub na której Ci zależy (Twój chłopak/ Twoja dziewczyna/małżonek/małżonka). Oceń, w jakim stopniu zgadzasz się z każdym ze stwierdzeń, używając poniższej skali i zaznaczając odpowiedni numer od 1 (wcale się nie zgadzam) do 5 (zdecydowanie się zgadzam).
1 - Zdecydowanie nie, 5 – Zdecydowanie tak"""

    if questionOptions is None:
        questionOptions = {}

    if pageOptions is None:
        pageOptions = {}

    items = """Z moim partnerem/moją partnerką łączy mnie bliska relacja.
Otrzymuję znaczące wsparcie emocjonalne od mojego partnera/mojej partnerki.
Bardzo cenię sobie obecność mojego partnera/mojej partnerki w moim życiu.
Mam komfortową relację z moim partnerem/moją partnerką.
Czuję, że mój partner/moja partnerka naprawdę dobrze mnie rozumie.
Związek z moim partnerem/moją partnerką jest bardzo romantyczny.
Uważam, że mój partner/moja partnerka jest bardzo atrakcyjny/a.
Nie potrafię sobie wyobrazić innej osoby, która by mnie tak uszczęśliwiała jak mój partner/moja partnerka.
Jest coś prawie „magicznego” w związku z moim partnerem/moją partnerką.
Związek z moim partnerem/moją partnerką jest pełen pasji.
Jestem pewny/a stabilności związku z moim partnerem/moją partnerką.
Postrzegam swoje zobowiązanie wobec mojego partnera/mojej partnerki jako trwałe.
Jestem pewien/pewna miłości do mojego partnera/mojej partnerki.
Postrzegam związek z moim partnerem/moją partnerką jako trwały.
Mam poczucie odpowiedzialności wobec mojego partnera/mojej partnerki.""".split(
        "\n"
    )

    scale = """1 – Zdecydowanie nie
2
3
4
5 – Zdecydowanie tak""".split(
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
