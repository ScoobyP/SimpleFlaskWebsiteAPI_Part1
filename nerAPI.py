import paralleldots as pd
pd.set_api_key('wEFvn5S4ITtTzbI7428fXsKd4ySomEVUDy86xS6ctsE')


def use_of_nerAPI(the_text):
    string = pd.ner(the_text)
    return string

def use_of_saAPI(the_text):
    string = pd.sentiment(the_text)
    return string
