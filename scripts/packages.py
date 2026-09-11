SRC = {
    "opencode": "brew install anomalyco/tap/opencode",
    "pdflatex": "brew install --cask basictex",
    "pdftoppm": "brew install poppler",
}

TEX = {
    "latexmk": "sudo tlmgr install latexmk",
    "amsmath": "sudo tlmgr install amsmath",
    "amsfonts": "sudo tlmgr install amsfonts",
    "amscls": "sudo tlmgr install amscls",
    "mathtools": "sudo tlmgr install mathtools",
    "bm": "sudo tlmgr install bm",
    "babel": "sudo tlmgr install babel",
    "babel-russian": "sudo tlmgr install babel-russian",
    "fontspec": "sudo tlmgr install fontspec",
    "unicode-math": "sudo tlmgr install unicode-math",
    "geometry": "sudo tlmgr install geometry",
    "microtype": "sudo tlmgr install microtype",
    "enumitem": "sudo tlmgr install enumitem",
    "titlesec": "sudo tlmgr install titlesec",
    "fancyhdr": "sudo tlmgr install fancyhdr",
    "setspace": "sudo tlmgr install setspace",
    "parskip": "sudo tlmgr install parskip",
    "graphics": "sudo tlmgr install graphics",
    "xcolor": "sudo tlmgr install xcolor",
    "float": "sudo tlmgr install float",
    "adjustbox": "sudo tlmgr install adjustbox",
    "caption": "sudo tlmgr install caption",
    "subcaption": "sudo tlmgr install subcaption",
    "tools": "sudo tlmgr install tools",
    "booktabs": "sudo tlmgr install booktabs",
    "tabularx": "sudo tlmgr install tabularx",
    "multirow": "sudo tlmgr install multirow",
    "makecell": "sudo tlmgr install makecell",
    "nicematrix": "sudo tlmgr install nicematrix",
    "pgf": "sudo tlmgr install pgf",
    "pgfplots": "sudo tlmgr install pgfplots",
    "forest": "sudo tlmgr install forest",
    "tikz-cd": "sudo tlmgr install tikz-cd",
    "circuitikz": "sudo tlmgr install circuitikz",
    "tkz-euclide": "sudo tlmgr install tkz-euclide",
    "siunitx": "sudo tlmgr install siunitx",
    "esint": "sudo tlmgr install esint",
    "mathrsfs": "sudo tlmgr install mathrsfs",
    "jknapltx": "sudo tlmgr install jknapltx",
    "stmaryrd": "sudo tlmgr install stmaryrd",
    "dsfont": "sudo tlmgr install dsfont",
    "doublestroke": "sudo tlmgr install doublestroke",
    "cancel": "sudo tlmgr install cancel",
    "extarrows": "sudo tlmgr install extarrows",
    "braket": "sudo tlmgr install braket",
    "tcolorbox": "sudo tlmgr install tcolorbox",
    "hyperref": "sudo tlmgr install hyperref",
    "bookmark": "sudo tlmgr install bookmark",
    "cleveref": "sudo tlmgr install cleveref",
    "listings": "sudo tlmgr install listings",
    "algorithm2e": "sudo tlmgr install algorithm2e",
}

TEX_PACKAGES = {
    # Mathematics
    "amsmath.sty": "amsmath",
    "amssymb.sty": "amsfonts",
    "amsthm.sty": "amscls",
    "mathtools.sty": "mathtools",
    "bm.sty": "tools",

    # Language / fonts
    "babel.sty": "babel",
    "russianb.ldf": "babel-russian",
    "fontspec.sty": "fontspec",
    "unicode-math.sty": "unicode-math",

    # Document layout
    "geometry.sty": "geometry",
    "microtype.sty": "microtype",
    "enumitem.sty": "enumitem",
    "titlesec.sty": "titlesec",
    "fancyhdr.sty": "fancyhdr",
    "setspace.sty": "setspace",
    "parskip.sty": "parskip",

    # Graphics
    "graphicx.sty": "graphics",
    "xcolor.sty": "xcolor",
    "float.sty": "float",
    "adjustbox.sty": "adjustbox",
    "caption.sty": "caption",
    "subcaption.sty": "caption",

    # Tables
    "array.sty": "tools",
    "tabularx.sty": "tools",
    "longtable.sty": "tools",
    "booktabs.sty": "booktabs",
    "multirow.sty": "multirow",
    "makecell.sty": "makecell",
    "nicematrix.sty": "nicematrix",

    # Diagrams / plots
    "tikz.sty": "pgf",
    "pgfplots.sty": "pgfplots",
    "forest.sty": "forest",
    "tikz-cd.sty": "tikz-cd",
    "circuitikz.sty": "circuitikz",
    "tkz-euclide.sty": "tkz-euclide",

    # Science
    "siunitx.sty": "siunitx",
    "esint.sty": "esint",

    # Extra math
    "mathrsfs.sty": "jknapltx",
    "stmaryrd.sty": "stmaryrd",
    "dsfont.sty": "doublestroke",
    "cancel.sty": "cancel",
    "extarrows.sty": "extarrows",
    "braket.sty": "braket",

    # Boxes
    "tcolorbox.sty": "tcolorbox",

    # References
    "hyperref.sty": "hyperref",
    "bookmark.sty": "bookmark",
    "cleveref.sty": "cleveref",

    # Code / algorithms
    "listings.sty": "listings",
    "algorithm2e.sty": "algorithm2e",
}
