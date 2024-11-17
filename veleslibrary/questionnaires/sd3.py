"""Short Dark Triad (SD3)"""

import velesresearch as vls
from velesresearch.models import PageModel


def sd3(
    name: str = "SD3",
    instruction: str | None = None,
    questionOptions: dict | None = None,
    pageOptions: dict | None = None,
) -> PageModel:
    """
    ## Short Dark Triad (SD3)
        A short scale measuring the Dark Triad of personality – machiavellianism, narcissism, and psychopathy.

    ## Original
        <div class="csl-bib-body" style="line-height: 2; margin-left: 2em; text-indent:-2em;">
        <div class="csl-entry">Jones, D. N., &amp; Paulhus, D. L. (2014). Introducing the short dark triad (Sd3): A brief measure of dark personality traits. <i>Assessment</i>, <i>21</i>(1), 28–41. <https://doi.org/10.1177/1073191113514105></div>
        </div>

    ## Score calculation
        A simple sum.

    ## Reverse items
        11, 15, 17, 20, 25

    ## Subscales
        1. Machiavellianism: 1, 2, 3, 4, 5, 6, 7, 8, 9
        2. Narcissism: 10, 11, 12, 13, 14, 15, 16, 17, 18
        3. Psychopathy: 19, 20, 21, 22, 23, 24, 25, 26, 27

    ## Reliability
        1. Machiavellianism: α = .77
        2. Narcissism: α = .71
        3. Psychopathy: α = .8

    ## Implemented by
        Jakub Jędrusiak (University of Wrocław)

    Args:
        name (str): Base name for pages and questions. Defaults to "SD3".
        instruction (str): Instruction for the questionnaire. None means that the default instruction will be used.
        questionOptions (dict | None): Additional options for questions as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the SD3 questionnaire. Use the `*` operator to unpack it to questions.
    """
    if instruction is None:
        instruction = """Please indicate how much you agree with each of the following statements."""

    if questionOptions is None:
        questionOptions = {}

    if pageOptions is None:
        pageOptions = {}

    items = """It’s not wise to tell your secrets.
I like to use clever manipulation to get my way.
Whatever it takes, you must get the important people on your side.
Avoid direct conflict with others because they may be useful in the future.
It’s wise to keep track of information that you can use against people later.
You should wait for the right time to get back at people.
There are things you should hide from other people to preserve your reputation.
Make sure your plans benefit yourself, not others.
Most people can be manipulated.
People see me as a natural leader.
I hate being the center of attention.
Many group activities tend to be dull without me.
I know that I am special because everyone keeps telling me so.
I like to get acquainted with important people.
I feel embarrassed if someone compliments me.
I have been compared to famous people.
I am an average person.
I insist on getting the respect I deserve.
I like to get revenge on authorities.
I avoid dangerous situations.
Payback needs to be quick and nasty.
People often say I’m out of control.
It’s true that I can be mean to others.
People who mess with me always regret it.
I have never gotten into trouble with the law.
I enjoy having sex with people I hardly know
I’ll say anything to get what I want.""".split(
        "\n"
    )

    scale = """1 – Disagree strongly
2 – Disagree
3 – Neither agree nor disagree
4 – Agree
5 – Agree strongly""".split(
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
