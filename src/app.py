import argparse
import core
import numpy
import string_methods
import time

def app(args):
    try:
        words = string_methods.removeNewLineCharacter(core.readWords(args.words_path))
        wordlist = core.readWordlistForExtending(args.extend_path)

        if numpy.size(wordlist):
            words = numpy.append(words, string_methods.removeNewLineCharacter(wordlist))
        def_words = words

        # following codes processes on 'def_words' variable

        # basic generator (one degree more complex than elementary generator)
        words = numpy.append(words, core.basic_generator(def_words))

        # following codes processes on 'words' variable

        capitals = numpy.array([], dtype=str)
        # capitalize first letter
        capitals = numpy.append(capitals, core.elementary_generator(words, lambda a : a.capitalize()))
        # capitalize all letters
        capitals = numpy.append(capitals, core.elementary_generator(words, lambda a : a.upper()))
        # capitalize letter of odd index number
        capitals = numpy.append(capitals, core.elementary_generator(words, lambda a : string_methods.compare_capitals(a, a[1::2].upper())))
        # capitalize letter of even index number
        capitals = numpy.append(capitals, core.elementary_generator(words, lambda a : string_methods.compare_capitals(a, a[::2].upper())))

        # save
        words = numpy.append(words, capitals)
        core.writeWordlist(args.passwords_path, words)
    except Exception as e:
        if hasattr(e, 'message'):
            print(e.message)
        else: print(e)

if __name__ == "__main__":
    begin = time.time()
    parser = argparse.ArgumentParser(description="A powerful word generator for hackers. Generates passwords with input words.")

    parser.add_argument('words_path', type=str, help="Path of input file (words)")
    parser.add_argument('passwords_path', type=str, help="Path of output file (passwords)")
    parser.add_argument('extend_path', type=str, help="Path of adding other wordlist file (for extending passwords)")

    print("Starting...")
    app(parser.parse_args())
    end = time.time()

    print("Program finished at", end - begin, "second(s).")