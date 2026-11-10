.. conops.rst

    Copyright The GOLDS-UFSC Contributors.

    GOLDS-UFSC Documentation

    This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
    International License. To view a copy of this license,
    visit http://creativecommons.org/licenses/by-sa/4.0/.

.. _ch:conops:

*********************
Concept of Operations
*********************


Introduction
============


This chapter describes the operational concept of the In-Orbit Validation (IoV) mission of the EDC payload of INPE. The mission is focused on the use of a service module based on the FloripaSat-1 platform for the in-orbit validation of the EDC, a module developed for CubeSats capable of receiving data from the data collection stations (Data Collection Platforms, DCPs) of the Brazilian Data Collection System (SBCD) installed throughout the Brazilian territory.

The document defines the mission's structure, the operational mode of the EDC payload and the service module, as well as outlining the operational expectations and responsibilities of the stakeholders.

Mission description
-------------------


The main task of this mission is the In-Orbit Validation (IoV) of the EDC payload of INPE. The EDC is a module specifically developed for CubeSats, designed to receive data from data collection stations (DCPs) of the Brazilian Data Collection System (SBCD) distributed throughout the Brazilian territory.

The service module is based on the FloripaSat-1 platform and its primary function is to transmit the received data to the ground segment through the main communication link provided by the satellite.

A crucial scientific component of the mission is the assessment of radiation effects on electronic devices. Both the EDC and the service platform are based on Commercial Off-The-Shelf (COTS) components, and the evaluation of radiation effects will be carried out by the Radiation instrument, also developed for the FloripaSat-1 mission.

Additionally, the mission will also provide a relay service for the amateur radio community.

Mission objectives
------------------


The main objective of the mission is to validate the functionality and performance of the INPE's EDC payload in orbit. The mission will seek to achieve this objective through the following activities:


* Receive data from DCP stations of the SBCD installed in Brazilian territory.
* Transmit the received data to the ground segment through the satellite's main communication link.
* Evaluate the effects of radiation on COTS electronic devices.
* Provide a relay service for the amateur radio community.



In the next section, we will describe in detail the operational environment and the execution plan to achieve these objectives.

Mission structure
=================



The mission architecture is designed to achieve the objectives set for the satellite mission. It defines the layout of the satellite system, including the different payload modules, the satellite platform, the ground segment, and the communication protocols.

Satellite platform
------------------


The satellite platform is based on the FloripaSat-1 bus, which has a proven track record of reliability and performance. It provides the necessary environment to host and operate the payload modules, as well as the essential systems of the satellite, such as attitude control, power generation, and communications.

Payload modules
---------------


The satellite carries two EDC modules, developed for CubeSats, that are capable of receiving data from the Data Collection Platforms (DCPs) of the Brazilian Data Collection System (SBCD). One of the EDCs acts as a backup for the other, providing redundancy and ensuring mission continuity in the event of a failure.

Also onboard is the Radiation Instrument, developed to assess the effects of radiation on COTS electronic devices. This instrument will be activated when the satellite is out of range of the DCPs in Brazil.

Ground segment
--------------


The ground segment consists of the Data Collection Platforms (DCPs) installed throughout the Brazilian territory and the INPE's Information System (SINDA, Sistema Integrado de Dados Ambientais). The DCPs transmit data that is received by the EDC modules on the satellite and sent back to SINDA for processing and distribution.

Mission control
---------------


The mission control will be carried out by the Federal University of Santa Catarina (UFSC), which will monitor the health and performance of the satellite, execute flight control commands, and plan mission activities.

Communication protocols
-----------------------


The mission uses a reliable communication protocol to ensure the transmission of data between the satellite and the ground segment. The protocol ensures that all transmitted data is received correctly and in order, and allows for error correction in transmission.

Together, the mission architecture ensures that all functions and objectives of the mission can be fulfilled efficiently and effectively.

Mission operation modes
=======================


Deployment mode
---------------


The Launch Mode is the first phase of the mission, during which the satellite is launched into space. During this phase, all satellite functions are disabled to protect the system from any potential mechanical or thermal stress during launch. After a successful launch and separation from the launch vehicle, the satellite automatically enters the Initialization Mode.

Initialization mode
-------------------


In the Initialization Mode, the satellite will automatically power up, going through the system boot process. During this process, the onboard computer of the satellite will initialize all satellite subsystems in a specific sequence to check their status and functionality.

This mode also involves the initial acquisition of satellite orientation (attitude) and the establishment of a communication link with the ground station. Once the communication link has been established and all systems are operating as expected, the satellite transitions to the Nominal Operation Mode.

Nominal operation mode
----------------------


This is the default operational state of the satellite. In the Nominal Operation Mode, the satellite will perform all its intended functions, including receiving data from the DCP stations, transmitting data to the ground segment, evaluating the effects of radiation on COTS electronic devices, and providing relay services for the amateur radio community.

The Nominal Operation Mode also involves maintaining satellite attitude and managing power consumption, ensuring that all systems operate optimally. The satellite will remain in this mode as long as all functions are operating as expected.

EDC activated
~~~~~~~~~~~~~


This is the default operational state of the satellite when it is flying over Brazilian territory. During this period, the EDC is activated to receive and store data from the Data Collection Platforms (DCPs). Additionally, the satellite performs attitude maintenance and power consumption management tasks.

The EDC payload, crucial for receiving data from the DCP stations, is a critical part of the mission. However, to optimize power usage and maximize operational efficiency, the EDC will only be activated when the satellite is passing over Brazilian territory. This will allow the EDC to collect data from the DCPs more effectively and transmit them to the ground segment while conserving energy when data collection is not possible.

The decision of when to activate and deactivate the EDC will be based on the satellite's orbit propagation, which will be calculated using regularly updated Two-Line Elements (TLEs). TLEs are widely used format for describing a satellite's orbit. It consists of two lines of textual data that contain information about the orbital element epoch, inclination, right ascension of the ascending node, eccentricity, argument of perigee, mean anomaly, and mean motion of the satellite.

The satellite's TLEs will be received periodically from the ground segment. The mission control team will calculate the satellite's future position based on the TLEs and determine the period when the satellite will be over Brazil. During this period, the EDC will be activated and begin collecting data from the DCPs. Once the satellite exits the coverage area, the EDC will be deactivated until the next pass over Brazil.

This approach of operating the EDC based on orbit propagation allows for efficient utilization of satellite resources while maximizing the amount of data collected and transmitted to the ground segment.

In addition to data collection, the satellite continues to provide relay services for the amateur radio community. However, priority is given to the operation of the EDC and data collection from the DCPs during this period.

EDC deactivated
~~~~~~~~~~~~~~~


When the satellite is out of reach of Brazil, the EDC is deactivated to save energy. During this period, the focus is on the operation of the radiation measurement instrument, which assesses the effects of radiation on COTS electronic devices.

While the EDC is deactivated, the radiation measurement instrument is activated and begins collecting data. This data is essential for evaluating the effectiveness of COTS electronic devices in radiation environments, providing valuable insights for the future development of satellites.

Additionally, the satellite continues to maintain its attitude and manage its power consumption. It also continues to provide relay services for the amateur radio community, although these may be limited to prioritize radiation data collection.

In both modes, the health and performance of the satellite are continuously monitored by the mission control team to ensure that all operations are being executed as planned. If any issues arise, the satellite can be put into an alternative operational mode for diagnosis and troubleshooting.

Contingency mode
----------------


The Contingency Mode is an operational state that the satellite enters if there is a failure in one of the critical systems or if an anomaly is detected. This includes the failure of one of the Data Collection Payload Modules (EDCs). The mission was designed with two EDCs onboard the satellite to provide redundancy. This means that if one EDC fails, the other can be activated to ensure the continuity of the mission.

EDC failure
~~~~~~~~~~~


In the event of a failure in the primary EDC, the system will automatically switch to the secondary EDC. This backup EDC has the same functionality as the primary EDC and can receive data from the Data Collection Platforms (DCPs) and transmit them to the ground segment. The switch to the backup EDC will be made without interruption in data collection and transmission, ensuring the continuity of the mission.

Recovery procedure
~~~~~~~~~~~~~~~~~~


In case of a failure, the mission control team at the Universidade Federal de Santa Catarina (UFSC) will work to identify the cause of the failure and implement a recovery procedure. This may involve resetting the primary EDC, performing a software update, or executing maneuvers to change the satellite's attitude.

The goal of the Contingency Mode is to ensure the continuity of the mission in the presence of failures or anomalies, minimizing any interruption in data collection and transmission. Thanks to the redundancy of the EDC, the mission is capable of adapting and responding to failures, ensuring that data continues to be collected and transmitted to the ground segment.

Decommissioning mode
--------------------


The Decommissioning Mode is activated at the end of the satellite's lifespan when it is no longer capable of performing its functions or when an irreparable problem is detected. In this mode, all satellite functions are permanently shut down.

Ground segment
==============


The ground segment is an essential component of the mission and includes all the terrestrial infrastructure that will be used to communicate with the satellite, receive data from the EDC payload, and monitor the health and performance of the satellite.

Data collection platforms
-------------------------


The DCPs are ground stations distributed throughout the Brazilian territory. They are responsible for collecting environmental data and other scientific information. Each DCP collects data locally and transmits it to the satellite when it passes over it.

The EDC on board the satellite is designed to receive these data transmitted by the DCPs. When the satellite is passing over Brazil and the EDC is activated, it will receive the data from the DCPs and store them for later transmission to the ground segment.

Environmental data integrated system
------------------------------------


The Enviromental Data Integrated System (SINDA, *Sistema Integrado de Dados Ambientais* in portuguese) is the main data reception center of INPE. It is responsible for receiving the data transmitted by the satellite, processing it, and distributing it to end users. SINDA also plays an important role in monitoring the health and performance of the satellite.

When the satellite is passing over SINDA and the communication link is established, the data collected by the EDC will be transmitted to SINDA. Upon receipt, SINDA will process this data and make it available to end users.

Additionally, SINDA will regularly receive telemetry from the satellite, allowing the mission control team to monitor the health and performance of the satellite and make operational decisions based on this information.

Control and coordination
------------------------


The coordination and control of the ground segment will be carried out by the mission control team, which is responsible for ensuring that all parts of the ground segment are functioning correctly and for resolving any issues that may arise. They will also be responsible for determining when and where the EDC should be activated based on the TLEs and the orbit propagation of the satellite.

In summary, the ground segment is a vital part of the mission. It enables data collection and transmission, satellite monitoring and control, and facilitates the interaction between the satellite and the DCPs, ensuring the success of the mission.

Mission control
===============


Mission control will be carried out by the UFSC. UFSC has a pass involvement in satellite development, providing a wide range of skills and expertise to manage the satellite operation.

Mission control station
-----------------------


UFSC will establish a dedicated mission control station for this purpose. This station will be responsible for the continuous monitoring of the satellite's health and performance, as well as the execution of flight control commands, such as attitude maneuvers, software updates, and anomaly resolution.

Mission control team
--------------------


The mission control team will be composed of students and professors from UFSC who have been trained to operate the satellite system. The team will be responsible for monitoring the satellite's telemetry, identifying and resolving issues, and interfacing with other stakeholders, such as the teams responsible for the ground segment.

Mission planning
----------------


The UFSC mission control team will also be responsible for planning and executing mission activities. This includes preparing detailed mission plans that define the activities to be performed by the satellite, such as activating the EDC and collecting data from the DCPs. These mission plans will be based on the propagation of the satellite's orbit, which is calculated using the TLEs.

Coordination with external entities
-----------------------------------


As part of mission control, UFSC will also coordinate with other entities involved in the mission, such as INPE and the ground stations for data reception. This includes coordinating the upload of TLEs and the transmission of received data to INPE's SINDA for processing and distribution.

In summary, UFSC will have a central role in mission control, ensuring that the satellite operates efficiently and performs its tasks as planned. UFSC's extensive experience in mission operations will be a significant advantage for the success of this mission.

Schedule
========


.. _tab:conops-schedule:

.. list-table:: Steps of operation.
   :header-rows: 1
   :widths: 25 15 20 40

   * - **Experiment**
     - **Start**
     - **End**
     - **Observations**
   * - DCPs data reception
     - Day 2
     - End of lifespan
     - Continuous operation, subject to the availability of the DCPs.
   * - Data transmission
     - Day 2
     - End of lifespan
     - Data transmission will be performed as data is received from the DCPs.
   * - Radiation effects evaluation
     - Day 2
     - End of lifespan
     - This experiment takes place continuously during the mission, collecting and sending data periodically.
   * - Retransmission service
     - Day 7
     - End of lifespan
     - The relay service will be available to the amateur radio community, with restrictions to avoid interfering with the satellite's primary operation.
