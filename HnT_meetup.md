# PDF Steganography
_(five minute hack-and-tell version)_

*[Travis Hoppe](http://thoppe.github.io/)* / [@metasemantic](https://twitter.com/metasemantic)
----------
[https://github.com/thoppe/PDF_steganography](https://github.com/thoppe/PDF_steganography)

====

### First presented at Data Wranglers DC
## [Black Hat Data Wrangling](http://www.meetup.com/Data-Wranglers-DC/events/225710555/)
!(images/DW.jpg) <<transparent; height:150px>>


[http://thoppe.github.io/Presentation-Black-Hack-Data-Wrangling](http://thoppe.github.io/Presentation-Black-Hack-Data-Wrangling/BHDW_DW_meetup.html/)

=====

### Steganography

> Steganography (US ￼i/ˌstɛ.ɡʌnˈɔː.ɡrʌ.fi/) is the practice of concealing a file, message, image, or video within another file, message, image, or video. The word steganography combines the Greek words steganos (στεγανός), meaning "covered, concealed, or protected", and graphein (γράφειν) meaning "writing".

### PDF
> Portable Document Format. Subset of postscript. Bane of data wranglers.

=====*

(side note)
## Postscript is Turing complete.


Game of Life in Postscript:
!(images/life.gif) [https://www.tjhsst.edu/~edanaher/pslife/](https://www.tjhsst.edu/~edanaher/pslife/)

=====

## PDF *+* Steganography

Hide text from machines/humans, make them readable to humans/machines.

====*

# [example.pdf](example.pdf)

Copy and paste the text in the PDF.

====*

## How does it work?
### Lies. Lies everywhere.


A typical PDF document maps [character codes](https://en.wikipedia.org/wiki/Character_encoding) (e.g. `A -> 65`) 
to specific locations on the page. 

When you copy, the reader only knows the character code.

Make a new font that lies about the mapping.
=====


=====

## Limitations

Currently only alpha-numeric (easy to fix).

Mapping is a simple [caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) (can make multiple fonts).

====


# Thanks, you!
[@metasemantic](https://twitter.com/metasemantic)
