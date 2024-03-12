.. _deviations:

Deviations from PLN-5552
========================

Deviations to the RAVEN quality assurance plan will be described here.

Configuration Management
-------------------------
The source code for ORCA as well as the documentation is maintained in a git repository.  Each source file contains a summary comment that describes its purpose, its limitations, and any requirements that it fulfills.  These comments are automatically gathered and reflected in the Sphinx documentation here: :ref:`configuration-list`.

Software Requirements
-------------------------
Software requirements unique to ORCA are listed here: :ref:`requirements`.
These requirements are written and maintained using the Sphinx documentation system and are stored in the ORCA repository.  Copies are reviewed and archived as part of the release process.  Each requirement has linked to it (in the requirement traceability matrix) an artifact, either in the code or in the documentation, that demonstrates that the requirement has been met in the software as designed.  Further, these verification artifacts may point to test cases and test case results that provide futher validation that the requirement has been met in the published code.

The Use of Sphinx
---------------------
Docuemntation for ORCA for users, developers, and quality assurance auditors is developed and maintained within the ORCA source code repository and utilizes the `Sphinx <https://www.sphinx-doc.org>`_ documentation system.  This documentation is rendered to both html (for users) and pdf (for archivial purposes).  Navigation is primarily performed through the links on the left panel of the html view.  Certain portions of the documentation are static and are contained in the `docs/source` directory, while others are dynamically pulled from the python source code through the use of pydoc comment tags.  This reduces the need to maintain duplicative sources of documentation and promotes quality.

Independent Test System
---------------------
The ORCA test is not integrated to RAVEN continuous integration system (CIS), which is for the multi-stage automated testing suite. The ORCA is designed for loading classes and methods on the Jupyter notebook instead of running the software with the input file of Extensible Markup Language (XML) format. Instead of CIS, unit tests are created for each class and regression tests are created based on use cases.