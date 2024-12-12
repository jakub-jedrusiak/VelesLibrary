"""Brief COPE (Mini-COPE)"""

import velesresearch as vls
from velesresearch.models import PageModel


def mini_cope(
    name: str = "Mini_COPE",
    instruction: str | None = None,
    questionOptions: dict | None = None,
    pageOptions: dict | None = None,
) -> PageModel:
    """
    ## Brief COPE (Mini-COPE)
        The questionnaire is used to assess ways of coping with stress. It is intended mainly for research purposes, but it can also be used in practice, in screening and preventive studies, and in assessing the effectiveness of therapeutic interventions. The Brief COPE omits two scales of the full COPE, reduces others to two items per scale, and adds one scale.

    ## Original
        <div class="csl-bib-body" style="line-height: 2; margin-left: 2em; text-indent:-2em;">
        <div class="csl-entry">Carver, C. S. (1997). You want to measure coping but your protocol’s too long: Consider the brief cope. <i>International Journal of Behavioral Medicine</i>, <i>4</i>(1), 92–100. <https://doi.org/10.1207/s15327558ijbm0401_6></div>
        </div>

    ## Score calculation
        An average.

    ## Reverse items
        None.

    ## Subscales
        1. Active Coping: 1, 2
        2. Planning: 3, 4
        3. Positive Refraining : 5, 6
        4. Acceptance: 7, 8
        5. Humor: 9, 10
        6. Religion: 11, 12
        7. Using Emotional Support: 13, 14
        8. Using Instrumental Support: 15, 16
        9. Self-Distraction: 17, 18
        10. Denial: 19, 20
        11. Venting: 21, 22
        12. Substance Use: 23, 24
        13. Behavioral Disengagement: 25, 26
        14. Self-Blame: 27, 28

    ## Reliability
        1. Active Coping: α = .68
        2. Planning: α = .73
        3. Positive Refraining : α = .64
        4. Acceptance: α = .57
        5. Humor: α = .73
        6. Religion: α = .82
        7. Using Emotional Support: α = .71
        8. Using Instrumental Support: α = .64
        9. Self-Distraction: α = .71
        10. Denial: α = .54
        11. Venting: α = .5
        12. Substance Use: α = .9
        13. Behavioral Disengagement: α = .65
        14. Self-Blame: α = .69

    ## Implemented by
        Julia Jankowska (University of Wrocław)

    Args:
        name (str): Base name for pages and questions. Defaults to "Mini_COPE".
        instruction (str): Instruction for the questionnaire. None means that the default instruction will be used.
        questionOptions (dict | None): Additional options for questions as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the Mini-COPE questionnaire. Use the `*` operator to unpack it to questions.
    """
    if instruction is None:
        instruction = """The following questions ask how you have sought to cope with a hardship in your life. Read the statements and indicate how much you have been using each coping style. """

    if questionOptions is None:
        questionOptions = {}

    if pageOptions is None:
        pageOptions = {}

    items = """I've been concentrating my efforts on doing something about the situation I'm in.
I've been taking action to try to make the situation better.
I've been trying to come up with a strategy about what to do.
I've been thinking hard about what steps to take.
I've been trying to see it in a different light, to make it seem more positive.
I've been looking for something good in what is happening.
I've been accepting the reality of the fact that it has happened.
I've been learning to live with it.
I've been making jokes about it.
I've been making fun of the situation.
I've been trying to find comfort in my religion or spiritual beliefs.
I've been praying or meditating.
I've been getting emotional support from others.
I've been getting comfort and understanding from someone.
I've been trying to get advice or help from other people about what to do.
I've been getting help and advice from other people.
I've been turning to work or other activities to take my mind off things.
I've been doing something to think about it less, such as going to movies, watching TV, reading, daydreaming, sleeping, or shopping.
I've been saying to myself "this isn't real."
I've been refusing to believe that it has happened.
I've been saying things to let my unpleasant feelings escape.
I've been expressing my negative feelings.
I've been using alcohol or other drugs to make myself feel better.
I've been using alcohol or other drugs to help me get through it.
I've been giving up trying to deal with it.
I've been giving up the attempt to cope.
I've been criticizing myself.
I've been blaming myself for things that happened.""".split(
        "\n"
    )

    scale = """0 – I haven't been doing this at all
1
2
3 – I've been doing this a lot""".split(
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
