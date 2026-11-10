.. tests.rst

    Copyright The GOLDS-UFSC Contributors.

    GOLDS-UFSC Documentation

    This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
    International License. To view a copy of this license,
    visit http://creativecommons.org/licenses/by-sa/4.0/.

.. _ch:test-plan:

************************
Test Plan and Procedures
************************

The GOLDS-UFSC test plan is structured into four phases: Module tests, FlatSat, Engineering integration, and Flight integration. This plan is summarized in the :numref:`tab:test-plan` and includes the components under test for each phase. 

.. _tab:test-plan:

.. list-table:: Test plan phases and tested components.
   :header-rows: 1

   * - **Phase**
     - **Components**
   * - Module tests
     - OBDH module
   * - Module tests
     - EPS module
   * - Module tests
     - TTC module
   * - Module tests
     - BATC4 board
   * - Module tests
     - IIP boards
   * - Module tests
     - PC104-ADPT boards
   * - Module tests
     - ACS components (simulation)
   * - Module tests
     - Mechanical (CAD assessment)
   * - FlatSat
     - Satellite core (OBDH+EPS+TTC+BATC4)
   * - FlatSat
     - Satellite core + GRS
   * - FlatSat
     - Satellite core + Payloads
   * - FlatSat
     - Satellite core + Payloads + GRS
   * - FlatSat
     - Satellite (long-term evaluation)
   * - Engineering integration (clean room preferable)
     - Mechanical assembly (repeated when required)
   * - Engineering integration (clean room preferable)
     - Satellite core + Payloads + GRS
   * - Engineering integration (clean room preferable)
     - Satellite (long-term evaluation)
   * - Engineering integration (clean room preferable)
     - Satellite + Solar Panels
   * - Engineering integration (clean room preferable)
     - Preliminary environmental tests
   * - Flight integration (clean room mandatory)
     - Mechanical assembly (flight components)
   * - Flight integration (clean room mandatory)
     - Satellite (short-term evaluation)
   * - Flight integration (clean room mandatory)
     - Satellite + Antenna (deployment)
   * - Flight integration (clean room mandatory)
     - Mechanical reassembly for flight
   * - Flight integration (clean room mandatory)
     - Satellite (long-term evaluation)
   * - Flight integration (clean room mandatory)
     - Qualification environmental tests

This section provides an overview of the planned testing workflow and a description of the strategies to accomplish the mission objectives. The module tests focus on the individual module's operation and behavior, in which a general template is provided in this document, and each module applies it for its needs. The FlatSat phase is the first module integration in a debug platform to validate the system from a development perspective (described with more details in :cite:`flatsat`). Finally, the engineering integration is the final development campaign aiming to validate the system from a mission perspective. The flight integration is the actual CubeSat assembly using the flight components and final assessments to prepare the satellite for launch. The integration details, procedures, and qualification process are described with more depth in the :ref:`ch:ait`. 

Module tests
============

The first phase is the foundation for the satellite, consolidating the base design for each subsystem and shaping their relations. Therefore, several techniques were employed to ensure a solid test strategy: several inspections of the boards' design and manufacturing quality; manual experimental assessments of various hardware, electrical, mechanical, and behavioral parameters; remotely automated tests using a continuous integration (CI) (Continuos Integration) approach; semi-automated tests using a hardware-in-the-loop (HIL) (Hardware-In-the-Loop) strategy; simulations; and CAD models assessment.

Workflow
--------

The following topics list the template workflow used to create the procedures for each subsystem. Each module documentation has its test chapter describing the process in detail, from procedures to success criteria.

Visual Inspection
~~~~~~~~~~~~~~~~~
 

#. Packaging quality assessment
#. Board manufacturing and assembly quality
#. 3D model comparison
#. Layers marker
#. Labels (schematics comparison)
#. High resolution photos for documentation

Mechanical Inspection
~~~~~~~~~~~~~~~~~~~~~

#. Board dimensions and mounting holes positioning
#. Board weight measurement

Integration Inspection
~~~~~~~~~~~~~~~~~~~~~~

#. Check connectors pinout against the documentation (not schematics)
#. Check connectors positioning (if applicable)

Electrical Inspection
~~~~~~~~~~~~~~~~~~~~~

#. Solder shorts
#. Missing components
#. Lifted pins
#. Poor soldering
#. Swapped components
#. Components part number
#. Components polarity (schematic comparison)
#. Components defined to not be soldered (DNP)

Electrical Testing
~~~~~~~~~~~~~~~~~~

#. Continuity test
#. Power up procedures (check LEDs and test points)
#. Average input power consumption measurement
#. Average output power source measurement (if applicable)
#. Power tracks temperature (if applicable)
#. Simple signal integrity (if applicable)

Functional Testing
~~~~~~~~~~~~~~~~~~

#. Run a simple test code (if applicable)
#. Run the system code (if applicable and available)
#. Check the system hardware self-test flags (if applicable and available)
#. Monitor basic LEDs behavior (if applicable)
#. Monitor the debug serial port logs (if applicable)

Module Testing
~~~~~~~~~~~~~~

#. Run simulations and review results (if applicable)
#. Review operation behavior against the documentation (if applicable)
#. Review features and requirements fulfillment
#. Review communication buses configuration and protocol (if applicable)
#. Review data packages, power buses, and control signals
#. Review and evaluate operation edge cases
#. Run remote automated code tests (if applicable)
#. Run system test codes in the board (if applicable)
#. Run the latest stable code version, monitor logs, and qualify behavior (if applicable)

Continuos Integration
---------------------

In order to detect errors and bugs in the early stages of development, a continuous integration workflow was set up for automated firmware tests focusing on small-scope verifications (i.e., unit tests). Instead of executing the code in the target processor, the tests are executed remotely in a host computer using a unit testing framework called “cmocka” :cite:`cmocka`. This tool allows abstracting the inherent hardware dependencies of embedded systems to enable firmware tests without errors introduced by hardware problems (execution in a consolidated platform, the computer), which provides an optimal behavioral assessment of the code implementations. This approach supports remote testing and promotes continuous test execution, which is essential for detecting errors and architectural issues. “GitHub Actions” drive the integration of these procedures :cite:`gh-actions`, which provides a host machine and a dashboard inside the same environment of the already used version control, source distribution, and management tool.

The unit tests follow a layered structure accordingly to the firmware layers. This is used alongside mockups (i.e., interfaces that abstract what the layer receive as input without having to implement the underlying functionality), which allows independency between the layers and abstract the actual hardware dependencies with an emulated behavior.

Hardware-In-the-Loop
--------------------

In the context of embedded systems, many errors are caused by hardware issues and limitations. Then, it is important to assess the system operating in the existing hardware platform. The hardware-in-the-loop strategy brings these elements into a more controlled and automated test environment. The idea is to execute the firmware in the board with an emphasis on evaluating the general behavior and operation flow since several log messages are used to report the system's current status or action across the execution.

Flatsat
=======

To test all modules during the development of the projet, a flatsat platform was developed. The FlatSat Platform is a testbed for CubeSat PCB modules. FlatSats enable a more straightforward, faster, and secure method for independently testing subsystems while being integrated in a flat design before integrating on a CubeSat form factor. The PCB can support up to 7 modules; all PC-104 pins are interconnected to flexibilize its use; only the particularity connection between modules needs to be taken into account. One PC-104 has an inverted pinout; the board also makes it possible to have two separate power supplies, a UART to USB converter for 4 modules, kill-switches activation though SPDTs, Remove Before Flight (RBF) pin header, a connector for charging batteries and SMA connectors for antennas. A picture of the flatsat board can be seen in :numref:`fig:flatsat-top`. In :numref:`fig:flatsat-fsat2` there is a picture of the flatsat, including the core modules and the payloads.

.. _fig:flatsat-top:

.. figure:: figures/flatsat-top.jpg
   :width: 100%
   :align: center
   :alt: Top view of the flatsat board.

   Top view of the flatsat board.

.. _fig:flatsat-fsat2:

.. figure:: figures/flatsat.jpg
   :width: 100%
   :align: center
   :alt: Flatsat of the GOLDS-UFSC.

   Flatsat of the GOLDS-UFSC.

Besides the hardware platform itself, during the FlatSat phase, a setup is used with the same structure as the hardware-in-the-loop strategy herein mentioned. Instead of using logs of one board, the analysis is performed from the perspective of all modules under test, which provides an evaluation of a complete system (satellite). More information about the Flatsat hardware platform and procedure details can be found in :cite:`flatsat`.

Engineering integration
=======================

The engineering model integration is the final development campaign since it connects the satellite design in the actual CubeSat form factor, allowing the assessment not only of the system from a behavioral perspective (as performed in the FlatSat), but also from the application and mission point of view. This is achieved due to additional elements (e.g., actual mechanical frame), environmental tests and execution of use cases. Also, it is possible to evaluate electrical, mechanical and behavioral compliance fulfillment early.

During this phase, the FlatSat process and test methodology are repeated in a condensed manner since the system was already tested and some preliminary procedures can be skipped. The mechanical assembly is performed several times until the design and the related documentation are settled. The environmental tests are a simplified version of the final process for qualification but open opportunities for early assessments and more destructive procedures. Also, long-term testing provides a comprehensive knowledge of the satellite's reliability and robustness. Further details are provided in the :ref:`ch:ait` section.

Flight integration
==================

The flight model integration performs the final arrangements before launch in a clean room, including evaluation assembly with all final parts; the last test campaign, the same as executed in the engineering integration; reassembly with definitive parts, placement, and resin; environmental qualification tests; and flight-ready procedures (packaging, transport and pre-launch) :cite:`marcelino2021`.
