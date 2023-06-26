"""Defines a function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """A funtion that accepts text argument
    and prints a docstring"""

    if not type(text) is str:
        raise TypeError("text must be a string")

    help_list = []
    help_list2 = []

    for i in text:
        help_list2.append(i)
        if i in ['.', '?', ':']:
            help_list2.append("$")
            help_list.append("".join(help_list2).strip())
            help_list2 = []

    for x in help_list:
        print(x)
        print("$")

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")