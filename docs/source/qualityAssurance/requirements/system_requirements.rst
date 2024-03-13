.. _system_requirements:

System Requirements
===================

Minimum Requirements
--------------------

Minimum Requirements
********************

.. req:: Computer
    :id: OM001

    Any portable operating system interface (POSIX) (or POSIX-like) system.

.. req:: RAM
    :id: OM002

    2GB per core execution (depending on the type of analysis and data generated)

.. req:: Language
    :id: OM003

    Python 3.9 or above


Functional Requirements
-----------------------

Framework, I/O, Execution Control
*********************************

.. req:: Optimization
    :id: OF001

    The ORCA plug-in shall enable the use of custom instructions to manage the execution phases of the real-time optimization workflow.

.. req:: Output
    :id: OF002

    The ORCA plug-in shall allow the creation of custom output formats for both simulation and experimental data.

Usability Requirements
----------------------


.. req:: Character Set
    :id: ID100

    ORCA must support the same character set as RAVEN.


.. req:: Error Readability
    :id: ID101

    Errors must result in a human-readable error statement with hints about possible resolutions.


Economical Analysis
*******************

System Interfaces
-----------------

Interface with external Applications
************************************

System Operations
-----------------

Human System Integration Requirements
*************************************

Maintainability
***************


Information Management
----------------------

.. req:: Generate Matrices from CSV
    :id: REQ002
    :links: TEST001

    ORCA shall be able to generate matrices from comma-separated-value (CSV) files.

