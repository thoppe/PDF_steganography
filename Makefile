# Kenring problem with fixed with cleaning?

F = cmr12mod

ORIGINAL_FONT = "cmr12"

CMAP_FILE       = gen/CMAP.key
ORIGINAL_TEX    = quote.tex
SUBSTITUTED_TEX = gen/sub_message.tex

all:
	make clean

#	# Generate the original pl file
	cp org/$(ORIGINAL_FONT).pfm gen
	cp org/$(ORIGINAL_FONT).pfb gen

	pf2afm gen/$(ORIGINAL_FONT).pfb 
	afm2tfm gen/$(ORIGINAL_FONT).afm gen/$(ORIGINAL_FONT).tfm
	tftopl gen/$(ORIGINAL_FONT).tfm gen/$(ORIGINAL_FONT).pl

	rm gen/$(ORIGINAL_FONT).afm gen/$(ORIGINAL_FONT).tfm
	rm gen/$(ORIGINAL_FONT).pfm gen/$(ORIGINAL_FONT).pfb

#	# Disassemble the font and apply the cipher
	t1disasm org/$(ORIGINAL_FONT).pfb > gen/font.raw

	python sub_cipher.py --f_raw_in gen/font.raw --f_raw_out gen/modified_font.raw --CMAP $(CMAP_FILE)

	python replace_sub.py --f_text_in $(ORIGINAL_TEX) --f_cmap_in $(CMAP_FILE) --f_text_out $(SUBSTITUTED_TEX)

	t1asm gen/modified_font.raw gen/$(F).pfb
	cp org/cmr12.pfm gen/$(F).pfm
	pf2afm gen/$(F).pfb
	afm2tfm gen/$(F).afm gen/$(F).tfm

	tftopl gen/$(F).tfm gen/$(F).pl

	cp gen/$(F).tfm .
	cp gen/$(F).pfb .

	pdflatex example.tex	
	rm -f *.aux *.log *.pfb *.tfm

	evince example.pdf 2>/dev/null &


clean:
	rm -f *~ *.raw \#*
	rm -f *.pl  *.tmf *.afm *.pfm *.pfb *.pdf *.tfm *.vpl
	rm -f *.log *.aux *.pdf
	rm -f gen/*
	mkdir -p gen
