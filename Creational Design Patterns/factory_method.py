
class FrenchLocalizer:
    """Returns the French Version"""
    
    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }
        
    def localize(self, msg):
        # change the message using the translations
        return self.translations.get(msg, msg)


class SpanishLocalizer:
    """Returns the Spanish Version"""
    
    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }
        
    def localize(self, msg):
        # change the mesage using translations
        return self.translations.get(msg, msg)
    

class EnglishLocalizer:
    """Simply returns the same message"""
    
    def localize(self, msg):
        return msg
    
    
def factory(language="English"):
    # Factory Method
    localizers = {
        "English": EnglishLocalizer,
        "French": FrenchLocalizer,
        "Spanish": SpanishLocalizer
    }
    return localizers[language]()

if __name__ == "__main__":
    e = factory()
    f = factory("French")
    s = factory("Spanish")
    
    messages = ["car", "bike", "cycle"]
    
    for message in messages:
        print("English: ", e.localize(message))
        print("French: ", f.localize(message))
        print("Spanish: ", s.localize(message), "\n")
