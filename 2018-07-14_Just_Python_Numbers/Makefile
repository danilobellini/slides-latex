all: slides.pdf

slides.pdf:
	pdflatex -shell-escape slides.tex
	pdflatex -shell-escape slides.tex

clean:
	rm -rf _minted-slides slides.pyg \
	       slides.aux slides.nav slides.out slides.snm slides.toc slides.vrb \
	       slides.log \
	       slides.pdf

.PHONY: all clean
