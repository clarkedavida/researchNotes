# researchNotes
This "book" is a collection of research notes that I made while researching in physics. The first chapters are dedicated to mainly mathematics, and the last chapters are dedicated to mainly physics, with an aim toward lattice field theory. A collection of appendices includes supplementary information that didn't seem to fit in any existing chapter.

You can look into the `0_researchnotes.tex` files to see what packages this uses, but I think if you install `texlive-full`, you should have all the packages you need.

There are three build scripts:
- `./makelatex` — full build with verbose output; use this first or when debugging errors
- `./makelatexQuiet` — full build with filtered output; use this for routine full rebuilds
- `./makelatexFast` — single pdflatex pass, no bibliography or index rebuild; use this when iterating on prose

Run `./distclean` to remove auxiliary files when desired. Feel free to make an Issue if you have any problems!
