# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generator.core import LoremGenerator

def main():
    parser = argparse.ArgumentParser(description="Quick Lorem Ipsum Generator")
    parser.add_argument("--paragraphs", "-p", type=int, default=1, help="Number of paragraphs to generate")
    parser.add_argument("--no-start", action="store_true", help="Do NOT start with 'Lorem ipsum dolor sit amet...'")
    
    args = parser.parse_args()

    generator = LoremGenerator()
    text = generator.generate(paragraphs=args.paragraphs, start_with_lorem=not args.no_start)
    
    print(text)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
