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

.. req:: Dispatch Optimization
    :id: OR001

    The ORCA plug-in shall support the dispatch optimization with largely linear dynamic model.

.. req:: Temperature Control
    :id: OR002

    The ORCA plug-in shall support the temperature control with nonlinear dynamic model.

.. req:: DeepLynx
    :id: OR003

    The ORCA plug-in shall support the communication pipeline to the physical asset through the DeepLynx data warehouse.

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

.. req:: API
    :id: OS001

    The ORCA plug-in shall be able to be coupled with external applications via Python application programming interfaces (API).

System Operations
-----------------

Human System Integration Requirements
*************************************

Maintainability
***************

* The most recent working version, defined as the version that successfully passes all tests within the current regression test suite, must always be accessible through the repository hosting provider. 

* Defects identified within the system shall be reported and monitored using a ticket or issue tracking system. The technical lead or a designated member of the Change Advisory Board (CAB) will assess the severity and priority of all reported issues. The technical lead is responsible for allocating resources, at their discretion, to address and resolve these identified issues.  

* The software maintenance team will review all proposed modifications to the system promptly, ensuring a response time of no more than three business days. 

* The complete ORCA plug-in shall be made available for licensing through the Idaho National Laboratory (INL) GitHub repository system. 


Information Management
----------------------

The ORCA plug-in in its entirety will be made available on an appropriate protected repository hosting site (i.e., INL GitHub). Backups and security services will be provided by the hosting service.

.. req:: Generate Matrices from CSV
    :id: REQ002
    :links: TEST001

    ORCA shall be able to generate matrices from comma-separated-value (CSV) files.

