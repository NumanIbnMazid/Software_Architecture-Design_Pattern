# Factory Method

Allows an interface or class to create an object, but let's subclasses decide which class or object to instantiate.
Objects are created without exposing the logic to the client and for creating the new type of object, the client uses the same commoon interface.
Factory Method replaces the straight forward object construction calls with calls to the special `factory method`.

## Problems we face without using Factory Method

Let’s understand the concept with one more example which is related to the translations and localization of the different languages. 
Suppose we have created an app whose main purpose is to translate one language into another and currently our app works with 10 languages only. Now our app has become widely popular among people but the demand has grown suddenly to include 5 more languages. 
It’s a piece of great news! only for the owner not for the developers. They have to change the whole code because now most part of the code is coupled with the existing languages only and that’s why developers have to make changes to the entire codebase which is really a difficult task to do.
Let’s look at the code for the problem which we may face without using the factory method.

Following code is using without using the factory method.

```python
# Python Code for Object
# Oriented Concepts without
# using Factory method

class FrenchLocalizer:

    """ it simply returns the french version """

    def __init__(self):

        self.translations = {"car": "voiture", "bike": "bicyclette",
                            "cycle":"cyclette"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):

        self.translations = {"car": "coche", "bike": "bicicleta",
                            "cycle":"ciclo"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg

if __name__ == "__main__":

    # main method to call others
    f = FrenchLocalizer()
    e = EnglishLocalizer()
    s = SpanishLocalizer()

    # list of strings
    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))

```

## Solution using the Facotry Method

Its solution is to replace the straightforward object construction calls with calls to the special factory method. Actually, there will be no difference in the object creation but they are being called within the factory method.
For example Our Two_Wheeler, Three_Wheeler, and Four_wheeler classes should implement the ridesharing interface which will declare a method called a ride. Each class will implement this method uniquely.

Using the factory method.

```python
# Python Code for factory method
# it comes under the creational
# Design Pattern

class FrenchLocalizer:

    """ it simply returns the french version """

    def __init__(self):

        self.translations = {"car": "voiture", "bike": "bicyclette",
                            "cycle":"cyclette"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                            "cycle":"ciclo"}

    def localize(self, msg):

        """change the message using translations"""
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    """Simply return the same message"""

    def localize(self, msg):
        return msg

def Factory(language ="English"):

    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()

if __name__ == "__main__":

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
```
