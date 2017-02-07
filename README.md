# Chains Invent Insanity
A Markov Chain-based [Cards Against Humanity](https://cardsagainsthumanity.com) answer card generator.

This is a CLI version of [the original version using flask](https://github.com/tuxotaku/chains-invent-insanity).

Pillow is used to generate the individual card images or a sheet / sheets of cards on US Legal sized paper (8.5 inches x 11 inches) for printing.

The cards / sheets are output in a "cards" subdirectory in the current working directory.

## Usage:

```
$ ./invent.py -h
Usage: Generate CII cards from markov chains!

Options:
  -h, --help      show this help message and exit
  -a ATTEMPTS     Number of trys for generating sentences from chains [min:
                  10000]
  -n NUMBER       Number of cards to generate
  -s, --sheet     Make sheet(s) of cards for US Legal sized paper as well as
                  individual cards
  -c, --no-cards  Don't save cards just write sheets [implies -s]
  -d DPI          Generate US Legal sheets at this DPI
  -w WORDFILE     Use this word file to generate markov chains from
  ```
Try using custom_wordlist.txt with all the answers from [the custom expansions here](https://github.com/z64/dah-cards) for even more hilarity.

## TODO:

* Add ability to generate sheets from a directory of individual cards, so cards can be generated then hand picked to add to a sheet for printing.
