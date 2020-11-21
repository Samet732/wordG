import argparse
import core
import numpy
import string_methods
import time

def app(args):
    try:
        words = core.readWords(args.words_path)
        wordlist = core.readWordlistForExtending(args.extend_path)

        if not wordlist:
            words = numpy.append(words, wordlist)
        def_words = words

        # capitalize first letter
        words = np.append(core.elementary_generator(words, lambda a : a.capitalize()))
        # capitalize all letters
        words = np.append(core.elementary_generator(words, lambda a : a.upper()))
        # capitalize letter of odd index number
        words = np.append(core.elementary_generator(words, lambda a : string_methods.compare_capitals(a, a[1::2])))
        # capitalize letter of even index number
        words = np.append(core.elementary_generator(words, lambda a : string_methods.compare_capitals(a, a[::2])))

        # basic generator (one degree more complex than elementary generator)
        words = np.append(core.basic_generator(words))

        # save
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

    print("Program successfully finished at", end - begin, "second(s).")