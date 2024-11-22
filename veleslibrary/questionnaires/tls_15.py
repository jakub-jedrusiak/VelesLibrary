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
       Sternberg's triangular love theory questionnaire. A shorter version of TLS-45, that measures three components of love: intimacy, passion, and commitment.

    ## Original
        Kowal, M., et al., (2024). Validation of the Short Version (TLS-15) of the Triangular Love Scale (TLS-45) across 37 Languages. _Archives of Sexual Behavior_, _53_, 839-857. <https://doi.org/10.1007/s10508-023-02702-7>

        Sternberg, R. J. (1997). Construct validation of a triangular love scale. _European Journal of Social Psychology_, _27_(3), 313-335. <https://doi.org/10.1002/(SICI)1099-0992(199705)27:3%3C313::AID-EJSP824%3E3.0.CO;2-4>

        Sternberg, R. J. (1988). _The triangle of love: Intimacy, passion, commitment._ Basic Books.

    ## Score calculation
        An average. Can be calculated separately for the subscales or for the whole questionnaire.

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
            2. Passion: α =.89
            3. Commitment: α = 0.92

    ## Implemented by
        Ksawery Łakomy (University of Wrocław)

    Args:
        name (str): Base name for pages and questions. Defaults to "TLS_15".
        instruction (str): Instruction for the questionnaire. `None` means that the default instruction will be used.
        questionOptions (dict | None): Additional options for questions as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the TLS-15 questionnaire. Use the `*` operator to unpack it to questions.
    """

    if instruction is None:
        instruction = "In this part of the survey, we are interested in processes that happen within relationships. Read each of the following statements, thinking about one person you love or care for deeply (your boyfriend/girlfriend/spouse). Rate your agreement with each statement according to the following scale and mark the appropriate number between 1 (not at all) and 5 (extremely)."

    if questionOptions is None:
        questionOptions = {}

    if pageOptions is None:
        pageOptions = {}

    return vls.page(
        name + "_page",
        vls.info(
            name + "_instruction",
            instruction,
        ),
        vls.radio(
            name,
            """I have a warm relationship with my partner.
I receive considerable emotional support from my partner.
I value my partner greatly in my life.
I have a comfortable relationship with my partner.
I feel that my partner really understands me.
My relationship with my partner is very romantic.
I find my partner to be very personally attractive.
I cannot imagine another person making me as happy as my partner does.
There is something almost “magical” about my relationship with my partner.
My relationship with my partner is passionate.
I have confidence in the stability of my relationship with my partner.
I view my commitment to my partner as a solid one.
I am certain of my love for my partner.
I view my relationship with my partner as permanent.
I feel a sense of responsibility toward my partner.""".split(
                "\n"
            ),
            "1 – Not at all; 2; 3; 4; 5 – Extremely".split("; "),
            **questionOptions,
        ),
        **pageOptions,
    )
