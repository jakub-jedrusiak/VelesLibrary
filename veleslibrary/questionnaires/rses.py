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
        Rosenberg, M. (1965). *Rosenberg Self-Esteem Scale (RSES)* [Database record]. APA PsycTests. <https://doi.org/10.1037/t01038-000>

    ## Score calculation
        A simple sum.

    ## Reverse items
        3, 5, 8, 10

    ## Subscales
        None.

    ## Reliability
        α = .88

    ## Implemented by
        Jędrusiak, Jakub (University of Wrocław)

    Args:
        name (str): Base name for pages and questions. Defaults to "RSES".
        instruction (str): Instruction for the questionnaire. `None` means that the default instruction will be used.
        questionOptions (dict | None): Additional options for questions as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the RSES questionnaire. Use the `*` operator to unpack it to questions.
    """

    if instruction is None:
        instruction = "Below is a list of statements dealing with your general feelings about yourself. Please indicate how strongly you agree or disagree with each statement."

    return vls.page(
        name + "_page",
        vls.info(
            name + "_instruction",
            instruction,
        ),
        vls.radio(
            name,
            """I feel that I am a person of worth, at least on an equal plane with others.
I feel that I have a number of good qualities.
All in all, I am inclined to feel that I am a failure.
I am able to do things as well as most other people.
I feel I do not have much to be proud of.
I take a positive attitude toward myself.
On the whole, I am satisfied with myself.
I wish I could have more respect for myself.
I certainly feel useless at times.
At times I think I am no good at all.""".split(
                "\n"
            ),
            "Strongly Agree; Agree; Disagree; Strongly Disagree".split("; "),
            **questionOptions,
        ),
        **pageOptions,
    )
