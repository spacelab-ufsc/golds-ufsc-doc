.. management.rst

    Copyright The GOLDS-UFSC Contributors.

    GOLDS-UFSC Documentation

    This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
    International License. To view a copy of this license,
    visit http://creativecommons.org/licenses/by-sa/4.0/.

.. _ch:management:

******************
Mission Management
******************

This chapter presents the main aspects of the general management of the project, like the mission schedule, product tree, and so on.

Schedule
========

The current schedule of the project is available in :numref:`tab:mission-schedule`.

.. _tab:mission-schedule:

.. list-table:: Mission schedule (updated on 2022/10/24).
   :header-rows: 1

   * - **Activity**
     - Nov 2022
     - Dez 2022
     - Jan 2023
     - Feb 2023
     - Mar 2023
     - Apr 2023
     - May 2023
     - Jun 2023
   * - 1
     - X
     - X
     - 
     - 
     - 
     - 
     - 
     - 
   * - 2
     - X
     - X
     - X
     - X
     - 
     - 
     - 
     - 
   * - 3
     - X
     - X
     - X
     - 
     - 
     - 
     - 
     - 
   * - 4
     - 
     - 
     - 
     - X
     - X
     - 
     - 
     - 
   * - 5
     - 
     - 
     - 
     - 
     - X
     - 
     - 
     - 
   * - 6
     - 
     - 
     - X
     - X
     - 
     - 
     - 
     - 
   * - 7
     - 
     - 
     - 
     - 
     - X
     - 
     - 
     - 
   * - 8
     - 
     - 
     - 
     - 
     - X
     - X
     - 
     - 
   * - 9
     - 
     - 
     - 
     - 
     - 
     - X
     - X
     - 
   * - 10
     - 
     - 
     - 
     - 
     - 
     - 
     - X
     - X
   * - 11
     - 
     - X
     - 
     - 
     - 
     - 
     - 
     - 
   * - 12
     - 
     - 
     - X
     - 
     - 
     - 
     - 
     - 

X indicates a scheduled activity.

Each activity of :numref:`tab:mission-schedule` is described below:

#. Integration of the engineering model in SpaceLab UFSC.
#. Preparation and suitability of the ground segment.
#. Verification and validation of the engineering model.
#. Integration and verification with data collection platforms.
#. Verification and validation tests of Engineering Model compatibility with EMMN in the INPE / CRN in Natal.
#. Verification and validation of the flight model.
#. Environmental tests at the Integration and Testing Laboratory (LIT/INPE).
#. Flight model acceptance and ground segment review.
#. Ground segment delivery.
#. Flight model delivery.
#. Purchase (flight model).
#. Delivery of purchased items (flight model).

Product Tree
============

The product tree of the GOLDS-UFSC mission is the project breakdown into successive levels of hardware and software products (or elements). The product tree of the project can be seen in the diagram of :numref:`fig:product-tree`. As shown, the satellite was divided into eight segments.

.. _fig:product-tree:

.. figure:: figures/product-tree.*
   :width: 100%
   :align: center
   :alt: Product tree of the satellite.

   Product tree of the satellite.

The responsibility of each segment of the product tree is described next:

* **Structure**: UFSC (COTS (Commercial Off-The-Shelf)).
* **EPS**: UFSC (developed in-house, with COTS solar panels).
* **OBDH**: UFSC (developed in-house).
* **TTC**: UFSC (developed in-house).
* **ACS**: UFSC (developed in-house).
* **Payload EDC**: INPE
* **Radiation instrument**: UFSC (developed in-house).
* **Interfaces**: UFSC (developed in-house).
* **Ground segment**:

   * **EMMN ground station**: INPE
   * **DCPs**: INPE/SINDA and other institutions
   * **UFSC ground station**: UFSC

Work Breakdown Structure
------------------------

The Work Breakdown Structure (WBS (Work Breakdown Structure)) is presented as a diagram in :numref:`fig:wbs`. The WBS is divided into work packages (WP (Work Package)) as can be seen in the diagram. The description of each WP is detailed below.

.. _fig:wbs:

.. figure:: figures/wbs.*
   :width: 100%
   :align: center
   :alt: WBS diagram.

   WBS diagram.

* **WP0**: Management and preparation.
* **WP1**: Architecture study and specification.

   * **WP1.0**: Operation scenario definition.
   * **WP1.1**: Architecture definition.
   * **WP1.2**: Requirements definition.

* **WP2**: Engineering and flight models definition

   * **WP2.0**: Application design.
   * **WP2.1**: Platform design.
   * **WP2.2**: Application implementation.
   * **WP2.3**: Platform implementation.
   * **WP2.4**: Decoder implementation (EGSE).

* **WP3**: Engineering model integration.

   * **WP3.0**: Subsystems integration and tests.
   * **WP3.1**: Engineering model satellite integration.
   * **WP3.2**: Integration and tests with decoder.

* **WP4**: Engineering model validation.

   * **WP4.0**: Validation scenarios specification.
   * **WP4.1**: Project validation.

* **WP5**: Fligth model integration.

   * **WP5.0**: Subsystems integration and tests.
   * **WP5.1**: Fligth model satellite integration.

* **WP6**: Fligth model validation.

   * **WP6.0**: Validation scenarios specification.
   * **WP6.1**: Project validation.

* **WP7**: Evaluation and dissemination.

Risk Management
===============

A risk is an event that threatens the project's success, even if partially. Therefore, this plan aims to help identifying adverse events at an early stage, handle them, and mitigate.

The development of this project will be based on a qualitative risk analysis standard. This depends on crossing two metrics: the probability of risk occurrence and the impact of risk occurrence. :numref:`likelihood` shows definitions of the probability of occurrence categorization.

.. _likelihood:

.. list-table:: Likelihood categorization.
   :header-rows: 1

   * - **Likelihood**
     - **Likelihood of occurrence**
   * - Expected
     - Almost certain occurrence. Very likely event to occur.
   * - Probable
     - Occurs frequently, relatively recurrent observations.   Event with considerable chances of occurring.
   * - Improbable
     - Occurs occasionally, it is not a rare event. Event with   a significant but small chance of occurring.
   * - Rare
     - Occurs rarely, rare observations. Very unlikely   event to occur.
   * - Very rare
     - It almost never occurs, very rare occurrences, or   never occurred. An almost impossible event to occur.

Five levels of impact define the occurrence impact metric:

* **5 (Catastrophic):** In general, these are risks that, if materialized, make the Subject or Activity unfeasible or end. Some examples of the description by feature:

   * *Financial Resources:* Significant increase in expenses that makes the continuation of the project or activity unfeasible or causes its termination;
   * *Material Resources:* loss of materials that makes the continuation of the project or activity unfeasible or causes its termination;
   * *Temporal Resources:* delay that makes the continuation of the project or activity unfeasible or causes its termination;
   * *Human Resources:* Death of one or more people. Evasion of more than 95% of those involved; and
   * *Organizational Image Resources:* Loss of total institutional credibility.

* **4 (Critical):** Overall, these are risks that, if materialized, make it very difficult to complete or progress the Subject/Activity and may raise considerations of finishing the Subject or Activity. Some examples of the description by resource:

   * *Financial Resources:* Increase of over 50% in expenses;
   * *Material Resources:* Material loss that cannot be replaced in a timely manner and that causes a significant loss of permanent performance of the system;
   * *Temporal Resources:* delay of more than 80% in the estimated time in the conclusion of the Subject/Activity;
   * *Human Resources:* Permanent disability of one or more people. Evasion between 70% and 95% of those involved; and
   * *Organizational Image Resources:* Very strong loss of institutional credibility.

* **3 (Major):** Overall, these are risks that, if materialized, make it difficult to complete or progress the Subject/Activity but do not usually raise considerations about ending the Subject or Activity. Some examples of the description by resource:

   * *Financial Resources:* Increase in subject/activity expenses between 15% and 50%;
   * *Material Resources:* Material loss capable of being replaced in a timely manner, but causing significant temporary system loss;
   * *Temporal Resources:* delay between 40% and 80% in the estimated time in the conclusion of the Subject/Activity;
   * *Human Resources:* Temporary disability of one or more people. Evasion between 40% and 70% of those involved; and
   * *Organizational Image Resources:* Loss of significant institutional credibility.

* **2 (Minor):** Overall, these are risks that, if materialized, significantly hamper the completion or progress of the Subject/Activity, but definitely do not raise the consideration of termination. Some examples of the description by feature:

   * *Financial Resources:* Increase in subject/activity expenses between 5% and 15%;
   * *Material Resources:* Material loss capable of being replaced in a timely manner and causing a temporary loss of system performance;
   * *Temporal Resources:* delay between 10% and 20% in the estimated time for completion of the Subject/Activity;
   * *Human Resources:* Minor injuries to one or more people. Evasion between 25% and 40% of those involved; and
   * *Organizational Image Resources:* Some loss of institutional credibility.

* **1 (Insignificant):** Overall, these are risks that, if materialized, make it a little difficult to complete or progress the Subject/Activity. Some examples of the description by resource:

   * *Financial Resources:* Increase in subject/activity expenses by up to 5%;
   * *Material Resources:* Loss of material that does not cause temporary loss of performance;
   * *Temporal Resources:* delay of up to 10% in the estimated time in the conclusion of the Subject/Activity;
   * *Human Resources:* Minor injuries to one or more people. Evasion of less than 25% of those involved; and
   * *Organizational Image Resources:* Little loss of institutional credibility.

Risks identification
--------------------

The identified risks are displayed in :numref:`risk_ID`, classified by context (mission or system), likelihood (Very Rare-Expected), and by level of impact (1-5).

.. _risk_ID:

.. list-table:: Mission and space systems risks.
   :header-rows: 1

   * - **ID**
     - **Risk**
     - **Context**
     - **Likelihood**
     - **Impact**
   * - RSK-1
     - Unable to obtain additional financial resources to complete the mission
     - Mission
     - Improbable
     - 5
   * - RSK-2
     - Lack of components on the market
     - Mission
     - Probable
     - 2
   * - RSK-3
     - High turnover of the development team
     - Mission
     - Improbable
     - 2
   * - RSK-4
     - Significant rise in the dollar (may not have enough resources to acquire systems)
     - Mission
     - Probable
     - 3
   * - RSK-5
     - Satellite commissioning failure
     - Mission
     - Improbable
     - 5
   * - RSK-6
     - Satellite does not survive launch
     - Mission
     - Rare
     - 5
   * - RSK-7
     - Ground Station failure
     - Mission
     - Improbable
     - 5
   * - RSK-8
     - LIT not available for satellite qualification tests
     - Mission
     - Improbable
     - 2
   * - RSK-9
     - Operational licensing not available on launch time
     - Mission
     - Improbable
     - 3
   * - RSK-10
     - EPS Software operation failure
     - System
     - Improbable
     - 5
   * - RSK-11
     - OBDH software operation failure
     - System
     - Improbable
     - 5
   * - RSK-12
     - Radiation instrument operation failure
     - System
     - Improbable
     - 1
   * - RSK-13
     - GSE software operation failure
     - System
     - Improbable
     - 4
   * - RSK-14
     - EDC does not comply with requirements
     - System
     - Rare
     - 4
   * - RSK-15
     - Materials resources not sufficient for preliminary tests
     - System
     - Probable
     - 2
   * - RSK-16
     - Fail on vibration tests impacting on delays
     - System
     - Rare
     - 3
   * - RSK-17
     - Non compliant metrological requirements impacting on delays
     - System
     - Probable
     - 2
   * - RSK-18
     - Kill switch mechanism fail, and satellite does not power on
     - System
     - Very rare
     - 5
   * - RSK-19
     - COTS systems not available in market
     - System
     - Rare
     - 3
