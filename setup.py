#!/usr/bin/env python
"""
setup.py file for EPANET2 pyton library  - Assela Pathirana
"""

from distutils.core import  setup, Extension
from itertools import product
import os

with open("README.txt","r") as f:
    README=f.read()


sources=[ "epanettools"+os.sep+"epanet"+os.sep+x for x in ["epanet.c",
                               "hash.c",
                               "hydraul.c",
                               "inpfile.c",
                               "input1.c",
                               "input2.c",
                               "input3.c",
                               "mempool.c",
                               "output.c",
                               "quality.c",
                               "report.c",
                               "rules.c",
                               "smatrix.c"
                                     ]]
sources.append("epanettools"+os.sep+"epanet"+os.sep+"epanet2_wrap.c")

epanet2_module = Extension('_epanet2',
                           sources=sources
                           )


EXAMPLES=["simple"]
EXTS=["inp", "py"]
EXTS.extend([x.upper() for x in EXTS])
EXAMPLES=list(product(EXAMPLES,EXTS))
package_data=[ "examples/"+x[0]+"/*."+x[1] for x in EXAMPLES]
NAME='EPANETTOOLS'
VERSION='0.2.3.0'
SETUPNAME=NAME+"-"+VERSION
LICENSE=u"GNU General Public License version 3"
LONGDISC="""Python interface for the popular urban drainage model EPANET 2.0 engine.
EPANET2 is realeased by United States Environmental Protection Agency to public domain.
This python package is copyrighted by Assela Pathirana and released under %(lc)s.

==========
README.txt
==========

%(rm)s

""" % {"lc": LICENSE, "rm": README}
CLASSIFY=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Environment :: Other Environment",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English"
        ]
setup (name = NAME,
       version = VERSION,
       author      = "Assela Pathirana",
       author_email = "assela@pathirana.net",
       description = """EPANET 2.0  calls from python""",
       packages = ["epanettools"],
	   ext_modules = [epanet2_module],
       package_data={'epanettools': package_data},
       license=LICENSE,
       url=u"http://assela.pathirana.net/EPANET-Python",
       #download_url="http://swmm5-ea.googlecode.com/files/"+SETUPNAME+".zip",
       long_description = LONGDISC,
       classifiers=CLASSIFY
       )
