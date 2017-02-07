# Chains Invent Insanity
A Markov Chain-based [Cards Against Humanity](https://cardsagainsthumanity.com) answer card generator.

This is a CLI version of [the original version using flask](https://github.com/tuxotaku/chains-invent-insanity).

Pillow is used to generate the individual card images or a sheet/sheets of cards on A4 sized paper at 300 DPI (11 x 10 cards per sheet).

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
  ```
