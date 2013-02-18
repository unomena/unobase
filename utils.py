__author__ = 'michael'

def get_choice_value(choice_display, choices):
    choices_dict = dict(choices)

    for key in choices_dict.keys():
        if choices_dict[key] == choice_display:
            return key

    return None
