
from langdetect import detect
import re
from os.path import join, dirname

class Filter:
    _blocked_languages = []
    _blocked_words = []
    def set_blocked_languages(self,lang):
        self._blocked_languages.append(lang)
    def set_keywords(self,*args):
        check = [str.lower(x) for x in args]
        if (not self._blocked_words): self._blocked_words = check
        else: self._blocked_words = self._blocked_words + check

    def filter_by_blockedwords(self,text):
        check_pattern = '(?:{})'.format('|'.join(self._blocked_words))
        return bool(re.search(check_pattern,str.lower(text),flags=re.I))

    def filter_by_language(self,text):
        return detect(text) in self._blocked_languages
       
