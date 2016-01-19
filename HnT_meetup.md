# PDF Steganography
_(five minute hack-and-tell version)_

*[Travis Hoppe](http://thoppe.github.io/)* / [@metasemantic](https://twitter.com/metasemantic)
----------
[https://github.com/thoppe/PDF_steganography](https://github.com/thoppe/PDF_steganography)

====*

### First presented at Data Wranglers DC
## [Black Hat Data Wrangling](http://www.meetup.com/Data-Wranglers-DC/events/225710555/)
!(images/DW.jpg) <<transparent; height:150px>>


[http://thoppe.github.io/Presentation-Black-Hack-Data-Wrangling](http://thoppe.github.io/Presentation-Black-Hack-Data-Wrangling/BHDW_DW_meetup.html/)

====

### Steganography

> Steganography (US ￼i/ˌstɛ.ɡʌnˈɔː.ɡrʌ.fi/) is the practice of concealing a file, message, image, or video within another file, message, image, or video. The word steganography combines the Greek words steganos (στεγανός), meaning "covered, concealed, or protected", and graphein (γράφειν) meaning "writing".

### PDF
> Portable Document Format. Subset of postscript. Bane of data wranglers.

====*

(side note)
## Postscript is Turing complete.


Game of Life in Postscript:
!(images/life.gif) [https://www.tjhsst.edu/~edanaher/pslife/](https://www.tjhsst.edu/~edanaher/pslife/)

====

## PDF *+* Steganography

Hide text from machines/humans, make them readable to humans/machines.

====*

## How does it work?
### Lies. Lies everywhere.


A typical PDF document maps [character codes](https://en.wikipedia.org/wiki/Character_encoding) (e.g. `A -> 65`) 
to specific locations on the page. 

When you copy, the reader only knows the character code.

Make a new font that lies about the mapping.

====*

### What does a font _look like_?
`cmr12.pl`

    (FAMILY CMR12)
    (CODINGSCHEME FONTSPECIFIC)
    (DESIGNSIZE R 10.0)
    (CHECKSUM O 35567353517)
    (FONTDIMEN
       (SLANT R 0.0)
       (SPACE R 0.326)
       (STRETCH R 0.3)
       (SHRINK R 0.1)
       (XHEIGHT R 0.431)
       (QUAD R 1.0)
       )
    (CHARACTER O 0
       (CHARWD R 0.611)
       (CHARHT R 0.673)
       )
    (CHARACTER O 1
       (CHARWD R 0.815)
       (CHARHT R 0.703)
       )
    ...

====*

### What does a letter _look like_?
Letter `b` from `cmr12`

    /b {
	18 380 hsbw
	-10 22 hstem
	402 29 hstem
	595 20 hstem
	85 65 vstem
	286 22 vstem
	150 402 rmoveto
	141 hlineto
	29 vlineto
	-141 hlineto
	184 vlineto
	-22 hlineto
	-1 -94 -36 -96 -91 -3 rrcurveto
	-20 vlineto
	85 hlineto
	-278 vlineto
	-111 74 -23 53 vhcurveto
	63 33 62 72 hvcurveto
	57 vlineto
	-22 hlineto
	-55 vlineto
	-72 -29 -42 -39 vhcurveto
	-68 0 93 17 hvcurveto
	closepath
	endchar
	} ND


====

# [example.pdf](example.pdf)

Copy and paste the text in the PDF.

====*

## Limitations
Currently only alpha-numeric (easy to fix).
Mapping is a simple [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) (can make multiple fonts).

<br>

====+
## Uses
Being awesome.
Hiding text from machines.
Making an interactive PDF "story" (see me if want to do this).

====

# Thanks, you!
[@metasemantic](https://twitter.com/metasemantic)
