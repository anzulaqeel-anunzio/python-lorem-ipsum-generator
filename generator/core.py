# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import random

class LoremGenerator:
    WORDS = [
        "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
        "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
        "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud",
        "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea",
        "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit",
        "in", "voluptate", "velit", "esse", "cillum", "dolore", "eu", "fugiat", "nulla",
        "pariatur", "excepteur", "sint", "occaecat", "cupidatat", "non", "proident",
        "sunt", "in", "culpa", "qui", "officia", "deserunt", "mollit", "anim", "id",
        "est", "laborum"
    ]

    def __init__(self):
        pass

    def _generate_sentence(self):
        length = random.randint(5, 12)
        words = [random.choice(self.WORDS) for _ in range(length)]
        sentence = " ".join(words)
        return sentence.capitalize() + "."

    def generate(self, paragraphs=1, start_with_lorem=True):
        result = []
        for i in range(paragraphs):
            sentence_count = random.randint(4, 9)
            sentences = [self._generate_sentence() for _ in range(sentence_count)]
            paragraph = " ".join(sentences)
            
            # Force standard start for first paragraph if requested
            if i == 0 and start_with_lorem:
                standard_start = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                # Allow some random variation after the standard start, or just prepend it
                # For simplicity, we'll just replace the beginning or ensure it's there.
                # Let's simple prepend if it's not a match, or just use it as the first sentence.
                # Actually, replacing the first sentence is cleaner.
                sentences[0] = standard_start
                paragraph = " ".join(sentences)
            
            result.append(paragraph)
        
        return "\n\n".join(result)

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
