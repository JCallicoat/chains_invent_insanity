#!/bin/env python
# coding: utf-8

import os
import optparse
import markovify

from textwrap import fill
from PIL import Image, ImageDraw, ImageFont


US_LETTER = (2550, 3300) # 8.5in x 11in x 300dpi == 2550px x 3300px


def invent(attempts, num_cards, make_sheet=False, no_cards=False):
    if not os.path.isdir('cards'):
        os.mkdir('cards')
    name = 'cards/CII-white-card-{}.png'
    font = ImageFont.truetype('LiberationSans-Bold.ttf', 16, encoding='unic')
    base = Image.open('CAH-blank-white.png').convert('RGBA') # 225px, 315px
    text_model = markovify.Text(open('wordlist.txt').read().decode('utf-8'))

    if make_sheet or no_cards:
        sheets = 0
        row = 0
        column = 0
        sheet = Image.new('RGBA', US_LETTER, (255,255,255,255))
        offset = [20, 20]

    for i in xrange(num_cards):
        card = base.copy()
        text = Image.new('RGBA', base.size, (255,255,255,255))
        draw = ImageDraw.Draw(text)

        sentence = fill(text_model.make_sentence(tries=attempts), 24)
        # sentence = fill("Becoming so rich that you pop a boner.", 24)

        draw.multiline_text((16, 20), sentence, font=font, fill=(0, 0, 0, 255),
                            spacing=10, align='left')
        card = Image.alpha_composite(text, card)

        if not no_cards:
            card.save(name.format(i + 1), None, optimize=True, compress_level=6)

        if make_sheet or no_cards:
            sheet.paste(card, tuple(offset))
            if row == 10:
                row = 0
                column += 1
                offset = [20, offset[1] + 315]
                if column == 10:
                    sheet.save(name.format('sheet-' + str(sheets + 1)), None,
                               optimize=True, compress_level=6)
                    sheet = Image.new('RGBA', US_LETTER, (255,255,255,255))
                    sheets += 1
                    column = 0
                    offset = [20, 20]
            else:
                row += 1
                offset[0] += 225

    if make_sheet or no_cards:
        sheet.save(name.format('sheet-' + str(sheets + 1)), None, optimize=True,
                   compress_level=6)


if __name__ == "__main__":
    parser = optparse.OptionParser(usage='Generate CII cards from markov chains!')
    parser.add_option('-a', None, metavar='ATTEMPTS', default=10000,
                      action='store', type='int', dest='attempts',
                      help='Number of trys for generating sentences from chains [min: 10000]')
    parser.add_option('-n', None, metavar='NUMBER', default=10,
                      action='store', type='int', dest='num_cards',
                      help='Number of cards to generate')
    parser.add_option('-s', '--sheet', default=False, action='store_true',
                      dest='make_sheet', help='Make sheet(s) of cards for US Legal sized paper as well as individual cards')
    parser.add_option('-c', '--no-cards', default=False, action='store_true',
                      dest='no_cards', help="Don't save cards just write sheets [implies -s]")
    (opts, args) = parser.parse_args()

    if opts.attempts < 10000:
        opts.attempts = 10000

    invent(opts.attempts, opts.num_cards, opts.make_sheet, opts.no_cards)
