'''
Created on 31 May 2013

@author: euan
'''

from django.utils.translation import ugettext_lazy as _

QUESTIONNAIRE_QUESTION_TYPE_RATING = 0
QUESTIONNAIRE_QUESTION_TYPE_RADIO = 1
QUESTIONNAIRE_QUESTION_TYPE_CHECKBOX = 2
QUESTIONNAIRE_QUESTION_TYPE_FREETEXT = 3
QUESTIONNAIRE_QUESTION_TYPE_FREETEXT_BLOB = 4
QUESTIONNAIRE_QUESTION_TYPE_FILE = 5

QUESTIONNAIRE_QUESTION_TYPES = ((QUESTIONNAIRE_QUESTION_TYPE_RATING, _(u'Rating (Select / Dropdown)')),
                                (QUESTIONNAIRE_QUESTION_TYPE_RADIO, _(u'Radio (Pick one)')),
                                (QUESTIONNAIRE_QUESTION_TYPE_CHECKBOX, _(u'Check box (Pick many)')),
                                (QUESTIONNAIRE_QUESTION_TYPE_FREETEXT, _(u'Free-text (Normal input)')),
                                (QUESTIONNAIRE_QUESTION_TYPE_FREETEXT_BLOB, _(u'Free-text (Text area)')),
                                (QUESTIONNAIRE_QUESTION_TYPE_FILE, _(u'File upload (File input)')),
                                )