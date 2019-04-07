from typos import Word


def common(words):
    """{'the', 'teh'} => {'the'}"""
    return set(words) & NLP_WORDS

def spell(word):
    """most likely correction for everything up to a double typo"""
    w = Word(word)
    candidates = (common([word]) or 
                  common(w.typos()) or 
                  common(w.double_typos()) or 
                  [word])
    return max(candidates, key=NLP_COUNTS.get)