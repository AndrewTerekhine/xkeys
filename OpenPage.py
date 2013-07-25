#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ask for a task name in jira and opens it.

Author Andrew Terekhine
Since 2011-11-23
"""
from Tkinter import Tk
import os
import sys
import tkSimpleDialog
import string
import time
import Common
import SendToUi
import SystemUtil
import Message

if __name__ == "__main__":
        import sys, PythonCall
        PythonCall.PythonCall(sys.argv).execute()

WORD_MARK = "word_mark"
SITE_SEARCH_JIRA = "http://172.16.0.7:8090/browse/" + WORD_MARK
SITE_SEARCH_JIRA_DESCRIPTION = "Open Jira task"
SITE_SEARCH_JIRA_HINT = "Jira task ID:"
SITE_SEARCH_GOOGLE_MAPS = "http://maps.google.com/maps?f=q&hl=en&geocode=&time=&date=&ttype=&q=" + WORD_MARK + "&ie=UTF8&z=10&iwloc=addr&om=1"
SITE_SEARCH_GOOGLE_MAPS_DESCRIPTION = "Searching on Google Maps"
SITE_GOOGLE_MAIL = "https://mail.google.com/mail"
SITE_SEARCH_YANDEX_TRANSLATION = "http://lingvo.yandex.ru/en?text=" + WORD_MARK + "&st_translate=1"
SITE_SEARCH_YANDEX_TRANSLATION_DESCRIPTION = "Yandex translation"
SITE_SEARCH_LEARNERS_DICTIONARY_TRANSLATION = "http://www.learnersdictionary.com/search/" + WORD_MARK
SITE_SEARCH_LEARNERS_DICTIONARY_TRANSLATION_DESCRIPTION = "Learners Dictionary translation"
SITE_SEARCH_TRANSLATION_HINT = "Word:"
SITE_SEARCH_IMDB = "http://www.imdb.com/find?s=all&q=" + WORD_MARK + "&x=0&y=0"
SITE_SEARCH_IMDB_DESCRIPTION = "IMDB search"
SITE_SEARCH_IMDB_HINT = "Film:"
SITE_SEARCH_GOOGLE_IMDB = "http://www.google.ru/search?q=" + WORD_MARK + " site:www.imdb.com"
SITE_SEARCH_GOOGLE_IMDB_DESCRIPTION = "IMDB Google site search"
SITE_SEARCH_GOOGLE = "http://www.google.com/search?q=" + WORD_MARK
SITE_SEARCH_GOOGLE_DESCRIPTION = "Google search"
SITE_SEARCH_GOOGLE_GROUPS = "http://groups.google.com/groups?lnk=hpsg&q=" + WORD_MARK
SITE_SEARCH_GOOGLE_GROUPS_DESCRIPTION = "Google Groups search"

def openExecute(url, text = ' '):
    if text is None or text == "": sys.exit()
    url = string.replace(url, WORD_MARK, text)
    os.popen("firefox " + "'" + url + "'" )

def openPrompt(title, hint, url):
    Tk().withdraw()
    text = tkSimpleDialog.askstring(title, hint)
    openExecute(url, text)

def open(title, url):
    text = SystemUtil.getSelection()
    Message.hint(title + " " + text)
    openExecute(url, text)

def jiraTaskPrompt():
    openPrompt(SITE_SEARCH_JIRA_DESCRIPTION, SITE_SEARCH_JIRA_HINT, SITE_SEARCH_JIRA)

def jiraTask():
    open(SITE_SEARCH_JIRA_DESCRIPTION, SITE_SEARCH_JIRA)

def googleMaps():
    open(SITE_SEARCH_GOOGLE_MAPS_DESCRIPTION, SITE_SEARCH_GOOGLE_MAPS)

def googleMail():
    if Common.isAtiveTitle(Common.INTELLIJ_IDEA_TITLE):
        time.sleep(0.05) # important it won't work without a timeout
        SendToUi.sendKey("alt+F3")
    else:
        openExecute(SITE_GOOGLE_MAIL)

def yandexTranslation():
    open(SITE_SEARCH_YANDEX_TRANSLATION_DESCRIPTION, SITE_SEARCH_YANDEX_TRANSLATION)

def yandexTranslationPrompt():
    openPrompt(SITE_SEARCH_YANDEX_TRANSLATION_DESCRIPTION, SITE_SEARCH_TRANSLATION_HINT, SITE_SEARCH_YANDEX_TRANSLATION)

def learnersDictionaryTranslation():
    open(SITE_SEARCH_LEARNERS_DICTIONARY_TRANSLATION_DESCRIPTION, SITE_SEARCH_LEARNERS_DICTIONARY_TRANSLATION)

def learnersDictionaryTranslationPrompt():
    openPrompt(SITE_SEARCH_LEARNERS_DICTIONARY_TRANSLATION_DESCRIPTION, SITE_SEARCH_TRANSLATION_HINT, SITE_SEARCH_LEARNERS_DICTIONARY_TRANSLATION)

def imdb():
    open(SITE_SEARCH_IMDB_DESCRIPTION, SITE_SEARCH_IMDB)

def imdbPrompt():
    openPrompt(SITE_SEARCH_IMDB_DESCRIPTION, SITE_SEARCH_IMDB_HINT, SITE_SEARCH_IMDB)

def imdbGoogleSiteSearch():
    open(SITE_SEARCH_GOOGLE_IMDB_DESCRIPTION, SITE_SEARCH_GOOGLE_IMDB)

def google():
    open(SITE_SEARCH_GOOGLE_DESCRIPTION, SITE_SEARCH_GOOGLE)

def googleGroups():
    open(SITE_SEARCH_GOOGLE_GROUPS_DESCRIPTION, SITE_SEARCH_GOOGLE_GROUPS)