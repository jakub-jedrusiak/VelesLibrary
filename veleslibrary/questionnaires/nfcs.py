"""The Need for Closure Scale (NFCS)"""

import velesresearch as vls


def nfcs(
    name: str = "NFCS",
    instruction: str | None = None,
    title: str | None = None,
    matrixOptions: dict | None = None,
    ratingOptions: dict | None = None,
    pageOptions: dict | None = None,
) -> vls.PageModel:
    """
    ## The Need for Closure Scale (NFCS)
        Measures the need for cognitive closure. There are two versions – long (41 items) and short (15 items). This function returns **the long version**. NFCS can be divided into five subscales: the need for order, the need for predictability, decisiveness, avoidance of ambiguity, closed mindedness.

    ## Original
        Webster, D. M., & Kruglanski, A. W. (1994). Individual differences in need for cognitive closure. *Journal of Personality and Social Psychology*, *67*(6), 1049–1062. <https://doi.org/10.1037/0022-3514.67.6.1049>

        Roets, A., & Van Hiel, A. (2007). Separating ability from need: Clarifying the dimensional structure of the need for closure scale. *Personality and Social Psychology Bulletin*, *33*(2), 266-280. <https://doi.org/10.1177/0146167206294744>

        You need to **cite both papers** if you use the NFCS in your research.

    ## Score calculation
        A simple sum.

    ## Reverse items
        2, 5, 18, 19, 20, 24, 27, 28, 34, 37, 41

    ## Subscales
        1. Need for order: 1, 6, 10, 20, 23, 27, 32, 33, 35, 41
        2. Need for predictability: 5, 7, 11, 18, 19, 25, 26, 40
        3. Decisiveness: 12, 13, 15, 16, 17, 22
        4. Avoidance of ambiguity: 3, 8, 14, 21, 29, 30, 31, 36, 38
        5. Closed mindedness: 2, 4, 9, 24, 28, 34, 37, 39

    ## Reliability
        α = .84

        ### Subscales
            1. Need for order: α = .82
            2. Need for predictability: α = .79
            3. Decisiveness: α = .70
            4. Avoidance of ambiguity: α = .67
            5. Closed mindedness: α = .62

    ## Implemented by
        Jędrusiak, Jakub

    Args:
        name (str): Base name for pages and questions. Defaults to "NFCS".
        instruction (str): Instruction for the questionnaire. `None` means that the default instruction will be used.
        title (str): Title for the matrix. Defaults to None.
        matrixOptions (dict | None): Additional options for the matrixDropdown as a dictionary. Defaults to None.
        ratingOptions (dict | None): Additional options for the rating column as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the NFCS long questionnaire. Use the `*` operator to unpack it to questions.
    """

    if matrixOptions is None:
        matrixOptions = {}
    if ratingOptions is None:
        ratingOptions = {}
    if pageOptions is None:
        pageOptions = {}

    if instruction is None:
        instruction = """
<style>
    .nfcsContainer {
        display: grid;
        grid-template-columns: auto auto;
        gap: 20px;
        max-width: 600px;
        margin: 0 auto;
        grid-template-areas:
            "item1 item4"
            "item2 item5"
            "item3 item6";
    }
    .nfcsItem1 { grid-area: item1; }
    .nfcsItem2 { grid-area: item2; }
    .nfcsItem3 { grid-area: item3; }
    .nfcsItem4 { grid-area: item4; }
    .nfcsItem5 { grid-area: item5; }
    .nfcsItem6 { grid-area: item6; }

    .nfcsItem {
        margin: 5px 0;
    }

    @media (max-width: 600px) {
        .nfcsContainer {
            grid-template-columns: 1fr;
            grid-template-areas:
                "item1"
                "item2"
                "item3"
                "item4"
                "item5"
                "item6";
        }
    }
</style>
<p>Read each of the following statements and decide how much you agree with each according to
your beliefs and experiences. Please respond according to the following scale:</p>

<div class="nfcsContainer">
    <div class="nfcsItem nfcsItem1">1 = Strongly disagree</div>
    <div class="nfcsItem nfcsItem4">4 = Slightly agree</div>
    <div class="nfcsItem nfcsItem2">2 = Moderately disagree</div>
    <div class="nfcsItem nfcsItem5">5 = Moderately agree</div>
    <div class="nfcsItem nfcsItem3">3 = Slightly disagree</div>
    <div class="nfcsItem nfcsItem6">6 = Strongly agree</div>
</div>
"""

    NFCS_items = """I think that having clear rules and order at work is essential for success.
Even after I've made up my mind about something, I am always eager to consider a different opinion.
I don't like situations that are uncertain.
I dislike questions which could be answered in many different ways.
I like to have friends who are unpredictable.
I find that a well ordered life with regular hours suits my temperament.
When dining out, I like to go to places where I have been before so that I know what to expect.
I feel uncomfortable when I don't understand the reason why an event occurred in my life.
I feel irritated when one person disagrees with what everyone else in a group believes.
I hate to change my plans at the last minute.
I don't like to go into a situation without knowing what I can expect from it.
When I have made a decision, I feel relieved
When I am confronted with a problem, I’m dying to reach a solution very quickly.
When I am confused about an important issue, I feel very upset.
I would quickly become impatient and irritated if I would not find a solution to a problem immediately.
I would rather make a decision quickly than sleep over it.
Even if I get a lot of time to make a decision, I still feel compelled to decide quickly.
I think it is fun to change my plans at the last moment.
I enjoy the uncertainty of going into a new situation without knowing what might happen.
My personal space is usually messy and disorganized.
In most social conflicts, I can easily see which side is right and which is wrong.
I almost always feel hurried to reach a decision, even when there is no reason to do so
I believe that orderliness and organization are among the most important characteristics of a good student.
When considering most conflict situations, I can usually see how both sides could be right.
I don't like to be with people who are capable of unexpected actions.
I prefer to socialize with familiar friends because I know what to expect from them.
I think that I would learn best in a class that lacks clearly stated objectives and requirements.
When thinking about a problem, I consider as many different opinions on the issue as possible.
I like to know what people are thinking all the time.
I dislike it when a person's statement could mean many different things.
It's annoying to listen to someone who cannot seem to make up his or her mind.
I find that establishing a consistent routine enables me to enjoy life more.
I enjoy having a clear and structured mode of life.
I prefer interacting with people whose opinions are very different from my own.
I like to have a place for everything and everything in its place.
I feel uncomfortable when someone's meaning or intention is unclear to me.
I always see many possible solutions to problems I face.
I'd rather know bad news than stay in a state of uncertainty.
I do not usually consult many different opinions before forming my own view.
I dislike unpredictable situations.
I dislike the routine aspects of my work (studies).""".split(
        "\n"
    )

    return vls.page(
        name + "_page",
        vls.info(name + "_instruction", instruction),
        vls.matrixDropdown(
            name,
            title,
            vls.rating(
                name,
                None,
                **{"rateMax": 6, "minWidth": "min-content"} | ratingOptions,
            ),
            NFCS_items,
            **{
                "titleLocation": "hidden",
                "showHeader": False,
                "rowTitleWidth": "100%",
                "alternateRows": True,
            }
            | matrixOptions,
        ),
        **{"title": "NFCS"} | pageOptions,
    )


def nfcsShort(
    name: str = "NFCS",
    instruction: str | None = None,
    title: str | None = None,
    matrixOptions: dict | None = None,
    ratingOptions: dict | None = None,
    pageOptions: dict | None = None,
) -> vls.PageModel:
    """
    ## The Need for Closure Scale (NFCS)
        Measures the need for cognitive closure. There are two versions – long (41 items) and short (15 items). This function returns **the short version**. NFCS can be divided into five subscales: the need for order, the need for predictability, decisiveness, avoidance of ambiguity, closed mindedness.

    ## Original
        Webster, D. M., & Kruglanski, A. W. (1994). Individual differences in need for cognitive closure. *Journal of Personality and Social Psychology*, *67*(6), 1049–1062. <https://doi.org/10.1037/0022-3514.67.6.1049>

        Pierro, A., & Kruglanski, A.W. (2005). *Revised need for cognitive closure scale.* (Unpublished manuscript). Università di Roma, "La Sapienza", Rome.

        Roets, A., & Van Hiel, A. (2011). Item selection and validation of a brief, 15-item version of the Need for Closure Scale. *Personality and Individual Differences*, *50*(1), 90-94. <https://doi.org/10.1016/j.paid.2010.09.004>

        You need to **cite all published papers** if you use the NFCS in your research.

    ## Score calculation
        A simple sum.

    ## Reverse items
        None.

    ## Subscales
        None.

    ## Reliability
        α = .87

    ## Implemented by
        Jędrusiak, Jakub

    Args:
        name (str): Base name for pages and questions. Defaults to "NFCS".
        instruction (str): Instruction for the questionnaire. `None` means that the default instruction will be used.
        title (str): Title for the matrix. Defaults to None.
        matrixOptions (dict | None): Additional options for the matrixDropdown as a dictionary. Defaults to None.
        ratingOptions (dict | None): Additional options for the rating column as a dictionary. Defaults to None.
        pageOptions (dict | None): Additional options for pages as a dictionary. Defaults to None.

    Returns:
        PageModel: PageModel with the NFCS long questionnaire. Use the `*` operator to unpack it to questions.
    """

    if matrixOptions is None:
        matrixOptions = {}
    if ratingOptions is None:
        ratingOptions = {}
    if pageOptions is None:
        pageOptions = {}

    if instruction is None:
        instruction = """
<style>
    .nfcsContainer {
        display: grid;
        grid-template-columns: auto auto;
        gap: 20px;
        max-width: 600px;
        margin: 0 auto;
        grid-template-areas:
            "item1 item4"
            "item2 item5"
            "item3 item6";
    }
    .nfcsItem1 { grid-area: item1; }
    .nfcsItem2 { grid-area: item2; }
    .nfcsItem3 { grid-area: item3; }
    .nfcsItem4 { grid-area: item4; }
    .nfcsItem5 { grid-area: item5; }
    .nfcsItem6 { grid-area: item6; }

    .nfcsItem {
        margin: 5px 0;
    }

    @media (max-width: 600px) {
        .nfcsContainer {
            grid-template-columns: 1fr;
            grid-template-areas:
                "item1"
                "item2"
                "item3"
                "item4"
                "item5"
                "item6";
        }
    }
</style>
<p>Read each of the following statements and decide how much you agree with each according to
your beliefs and experiences. Please respond according to the following scale:</p>

<div class="nfcsContainer">
    <div class="nfcsItem nfcsItem1">1 = Strongly disagree</div>
    <div class="nfcsItem nfcsItem4">4 = Slightly agree</div>
    <div class="nfcsItem nfcsItem2">2 = Moderately disagree</div>
    <div class="nfcsItem nfcsItem5">5 = Moderately agree</div>
    <div class="nfcsItem nfcsItem3">3 = Slightly disagree</div>
    <div class="nfcsItem nfcsItem6">6 = Strongly agree</div>
</div>
"""

    NFCS_items = """I don't like situations that are uncertain.
I dislike questions which could be answered in many different ways.
I find that a well ordered life with regular hours suits my temperament.
I feel uncomfortable when I don't understand the reason why an event occurred in my life.
I feel irritated when one person disagrees with what everyone else in a group believes.
I don't like to go into a situation without knowing what I can expect from it.
When I have made a decision, I feel relieved
When I am confronted with a problem, I’m dying to reach a solution very quickly.
I would quickly become impatient and irritated if I would not find a solution to a problem immediately.
I don't like to be with people who are capable of unexpected actions.
I dislike it when a person's statement could mean many different things.
I find that establishing a consistent routine enables me to enjoy life more.
I enjoy having a clear and structured mode of life.
I do not usually consult many different opinions before forming my own view.
I dislike unpredictable situations.""".split(
        "\n"
    )

    return vls.page(
        name + "_page",
        vls.info(name + "_instruction", instruction),
        vls.matrixDropdown(
            name,
            title,
            vls.rating(
                name,
                None,
                **{"rateMax": 6, "minWidth": "min-content"} | ratingOptions,
            ),
            NFCS_items,
            **{
                "titleLocation": "hidden",
                "showHeader": False,
                "rowTitleWidth": "100%",
                "alternateRows": True,
            }
            | matrixOptions,
        ),
        **{"title": "NFCS"} | pageOptions,
    )
