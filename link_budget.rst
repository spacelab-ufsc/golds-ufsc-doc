.. link_budget.rst

    Copyright The GOLDS-UFSC Contributors.

    GOLDS-UFSC Documentation

    This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
    International License. To view a copy of this license,
    visit http://creativecommons.org/licenses/by-sa/4.0/.

.. _anx:link-budget:

***********************
Link Budget Calculation
***********************

This appendix shows the link budget calculation of all the satellite links (including the radio links of the payloads). The method used was taken from :cite:`larson2005` (section 13.3).

Distance to Satellite at Horizon
================================

The distance to the satellite at the horizon (the maximum theoretical distance between the satellite and a ground station) can be calculated using :eq:`eq:horizon-distance`.

.. math::
   :label: eq:horizon-distance

   d = \sqrt{2\cdot R_{e}\cdot h + h^{2}}

Where:

* :math:`R_{e}` = Earth radius = 6378 km
* :math:`h` = Satellite altitude = 550 km
* :math:`d` = Distance to the satellite at the horizon

So, the distance to the satellite at the horizon is:

.. math::
   :label: eq:horizon-distance-result

   d = \sqrt{2\cdot 6378\cdot 550 + 550^{2}} = \mathbf{2705\ km}

Free-Space Path Loss
====================

The free-space path loss (:math:`FSPL`) can be calculated using :eq:`eq:fspl`.

.. math::
   :label: eq:fspl

   FSPL = \left( \frac{4\pi d f}{c} \right)^{2}

Where:

* :math:`d` = Distance between the satellite and the ground station
* :math:`f` = Radiofrequency
* :math:`c` = Speed of light

The FSPL value in decibels can be calculated with :eq:`eq:fsbl-db`.

.. math::
   :label: eq:fsbl-db

   \begin{split}
   FSPL^{dB} & = 20\log\left(\frac{4\pi}{c}\right) + 20\log\left(d\right) + 20\log\left(f\right) \\
   & = 32,45 + 20\log\left(\frac{d}{1\ km}\right) + 20\log\left(\frac{f}{1\ MHz}\right) \\
   \end{split}

The minimum distance between the satellite and a ground station is the satellite altitude, in this case: 600 km. The maximum distance is the distance at the horizon, defined by :eq:`eq:horizon-distance-result`.

Beacon
------

Considering the frequency of the beacon as 437 MHz, the minimum and maximum FSBL is:

.. math::

   FSPL^{dB}_{min} = 32,45 + 20\log\left(\frac{550}{1\ km}\right) + 20\log\left(\frac{146}{1\ MHz}\right) = \mathbf{130,5\ dB}

.. math::

   FSPL^{dB}_{max} = 32,45 + 20\log\left(\frac{2705}{1\ km}\right) + 20\log\left(\frac{146}{1\ MHz}\right) = \mathbf{144,4\ dB}

.. math::

   \mathbf{130,5 \leq FSPL^{dB} \leq 144,4\ dB}

Downlink/Uplink
---------------

Considering the frequency of the downlink/uplink as 462,5 MHz, the minimum and maximum FSBL is:

.. math::

   FSPL^{dB}_{min} = 32,45 + 20\log\left(\frac{550}{1\ km}\right) + 20\log\left(\frac{450}{1\ MHz}\right) = \mathbf{140,3\ dB}

.. math::

   FSPL^{dB}_{max} = 32,45 + 20\log\left(\frac{2705}{1\ km}\right) + 20\log\left(\frac{450}{1\ MHz}\right) = \mathbf{154,2\ dB}

.. math::

   \mathbf{140,3 \leq FSPL^{dB} \leq 154,2\ dB}

Uplink (Payload)
----------------

Considering the frequency of the payload's uplink is 401,635 MHz, the minimum and maximum FSBL is:

.. math::

   FSPL^{dB}_{min} = 32,45 + 20\log\left(\frac{550}{1\ km}\right) + 20\log\left(\frac{401,635}{1\ MHz}\right) = \mathbf{139,3\ dB}

.. math::

   FSPL^{dB}_{max} = 32,45 + 20\log\left(\frac{2705}{1\ km}\right) + 20\log\left(\frac{401,635}{1\ MHz}\right) = \mathbf{153,2\ dB}

.. math::

   \mathbf{139,3 \leq FSPL^{dB} \leq 153,2\ dB}

Power at Receiver
=================

The power of the signal at the receiver can be estimated using :eq:`eq:power-at-receiver`.

.. math::
   :label: eq:power-at-receiver

   P_{r} = P_{t} + G_{t} + G_{r} - L_{p} - L_{s}

Where:

* :math:`P_{r}` = Power at the receiver
* :math:`P_{t}` = Transmitter power
* :math:`G_{t}` = Antenna gain of the transmitter
* :math:`G_{r}` = Antenna gain of the receiver
* :math:`L_{p}` = FSPL (Free-Space Path Loss)
* :math:`L_{s}` = Other losses in the system

Considering the worst scenario with the maximum possible distance between the satellite and a ground station, the power at the receiver for each link is calculated below.

Beacon
------

.. math::

   P_{r} = 30 + 0 + 12 - 144,4 - 5 = -107,4\ dBm

.. math::

   \mathbf{P_{r} \geq -107,4\ dBm}

Downlink (UHF)
--------------

.. math::

   P_{r} = 30 + 0 + 12 - 154,2 - 5 = -117,2\ dBm

.. math::

   \mathbf{P_{r} \geq -117,2\ dBm}

Uplink (UHF)
------------

.. math::

   P_{r} = 44 + 12 + 0 - 154,2 - 5 = -103,2\ dBm

.. math::

   \mathbf{P_{r} \geq -103,2\ dBm}

Uplink (Payload)
----------------

.. math::

   P_{r} = 30 + 3 + 0 - 153,2 - 5 = -125,2\ dBm

.. math::

   \mathbf{P_{r} \geq -125,2\ dBm}

Signal-to-Noise-Ratio
=====================

The Signal-to-Noise-Ratio (SNR, Signal To Noise Ratio) of a transmitted signal at the receiver can be expressed using :eq:`eq:snr`:

.. math::
   :label: eq:snr

   SNR = \frac{E_{b}}{N_{0}} = \frac{P_{t}G_{t}G_{r}}{kT_{s}RL_{p}}

Where:

* :math:`P_{t}` = Transmitter power
* :math:`G_{t}` = Antenna gain of the transmitter
* :math:`G_{r}` = Receiver gain
* :math:`k` = Boltzmann's constant (:math:`\cong 1,3806 \times 10^{-23}\ J/K`)
* :math:`T_{s}` = System noise temperature
* :math:`R` = Data rate in bits per second (bps)
* :math:`L_{p}` = Free-Space Path Loss (FSPL)

The system noise temperature (:math:`T_{s}`) can be defined using :eq:`eq:system-noise-temperature`.

.. math::
   :label: eq:system-noise-temperature

   T_{s} = T_{ant} + T_{r}

with:

.. math::
   :label: eq:noise-temperature-receiver

   T_{r} = \frac{T_{0}}{L_{r}} (F - L_{r})

and:

.. math::
   :label: eq:noise-figure

   F = 1 + \frac{T_{r}}{T_{0}}

Combining Equations :eq:`eq:system-noise-temperature`, :eq:`eq:noise-temperature-receiver` and :eq:`eq:noise-figure`:

.. math::
   :label: eq:system-noise-temp-expanded

   T_{s} = T_{ant} + \left( \frac{T_{0}(1 - L_{r})}{L_{r}} \right) + \left( \frac{T_{0} (F - 1)}{L_{r}} \right)

Where:

* :math:`T_{ant}` = Antenna noise temperature
* :math:`T_{0}` = Reference temperature (usually 290 K)
* :math:`L_{r}` = Line loss between the antenna and the receiver
* :math:`F` = Noise figure of the receiver
* :math:`T_{r}` = Noise temperature of the receiver

The SNR value in decibels can be calculated using the :eq:`eq:snr-db`:

.. math::
   :label: eq:snr-db

   \begin{split}
   SNR^{dB} & = 10\log_{10}\left( \frac{E_{b}}{N_{0}} \right) = 10\log_{10} \left( \frac{P_{t}G_{t}G_{r}}{kT_{s}RL_{p}} \right) \\
   & = P_{t}^{dBm} - 30 + G_{t}^{dB} + G_{r}^{dB} - L_{p}^{dB} - 10\log k - 10\log T_{s} - 10\log R
   \end{split}

Considering other losses in the system (:math:`L_{s}`) (cable and connection losses as an example), the :eq:`eq:snr-db` can be corrected as presented in :eq:`eq:snr-db-with-losses`.

.. math::
   :label: eq:snr-db-with-losses

   SNR^{dB} = P_{t}^{dBm} - 30 + G_{t}^{dB} + G_{r}^{dB} - L_{p}^{dB} - L_{s}^{dB} - 10\log k - 10\log T_{s} - 10\log R

Beacon
------

Using Equations :eq:`eq:snr-db-with-losses` and :eq:`eq:system-noise-temperature`, with:

* :math:`P_{t} = 30\ dBm`
* :math:`G_{t} = 0\ dBi`
* :math:`G_{r} = 12\ dBi`
* :math:`L_{p} = 144,4\ dB`
* :math:`L_{s} = 5\ dB`
* :math:`R = 1200\ bps`
* :math:`T_{0} = 290\ K`
* :math:`T_{r} = 290\ K`
* :math:`T_{ant} = 300\ K`
* :math:`F = 2\ dB`
* :math:`L_{r} = 0,89\ (0,5\ dB)`

.. math::

   T_{s} = 300 + \left( \frac{290 (1 - 0,89)}{0,89} \right) + \left( \frac{290 (2 - 1)}{0,89} \right) = 661,7\ K

.. math::

   SNR^{dB} = 30 - 30 + 0 + 12 - 144,4 - 5 + 228,6 - 28,21 - 30,79 = 32,22\ dB

.. math::

   \mathbf{SNR^{dB} \geq 32,22\ dB}

Downlink
--------

Using Equations :eq:`eq:snr-db-with-losses` and :eq:`eq:system-noise-temperature`, with:

* :math:`P_{t} = 30\ dBm`
* :math:`G_{t} = 0\ dBi`
* :math:`G_{r} = 12\ dBi`
* :math:`L_{p} = 154,2\ dB`
* :math:`L_{s} = 5\ dB`
* :math:`R = 9600\ bps`
* :math:`T_{0} = 290\ K`
* :math:`T_{r} = 290\ K`
* :math:`T_{ant} = 300\ K`
* :math:`F = 2\ dB`
* :math:`L_{r} = 0,89\ (0,5\ dB)`

.. math::

   SNR^{dB} = 30 - 30 + 0 + 12 - 154,2 - 5 + 228,6 - 28,21 - 39,82 = 13,41\ dB

.. math::

   \mathbf{SNR^{dB} \geq 13,41\ dB}

Uplink
------

Using Equations :eq:`eq:snr-db-with-losses` and :eq:`eq:system-noise-temperature`, with:

* :math:`P_{t} = 44\ dBm`
* :math:`G_{t} = 12\ dBi`
* :math:`G_{r} = 0\ dBi`
* :math:`L_{p} = 154,2\ dB`
* :math:`L_{s} = 5\ dB`
* :math:`R = 9600\ bps`
* :math:`T_{0} = 290\ K`
* :math:`T_{r} = 290\ K`
* :math:`T_{ant} = 300\ K`
* :math:`F = 2\ dB`
* :math:`L_{r} = 0,89\ (0,5\ dB)`

.. math::

   SNR^{dB} = 44 - 30 + 12 + 0 - 154,2 - 5 + 228,6 - 28,21 - 39,82 = 27,41\ dB

.. math::

   \mathbf{SNR^{dB} \geq 27,41\ dB}

Uplink (Payload)
----------------

Using Equations :eq:`eq:snr-db-with-losses` and :eq:`eq:system-noise-temperature`, with:

* :math:`P_{t} = 30\ dBm`
* :math:`G_{t} = 3\ dBi`
* :math:`G_{r} = 0\ dBi`
* :math:`L_{p} = 153,2\ dB`
* :math:`L_{s} = 5\ dB`
* :math:`R = 400\ bps`
* :math:`T_{0} = 290\ K`
* :math:`T_{r} = 290\ K`
* :math:`T_{ant} = 300\ K`
* :math:`F = 2\ dB`
* :math:`L_{r} = 0,89\ (0,5\ dB)`

.. math::

   SNR^{dB} = 30 - 30 + 3 + 0 - 153,2 - 5 + 228,6 - 28,21 - 26,02 = 19,17\ dB

.. math::

   \mathbf{SNR^{dB} \geq 19,17\ dB}

Link Margin
===========

From :cite:`larson2005`, the minimum SNR value at the received considering a :math:`10^{-5}` bit error rate is:

* Beacon: :math:`SNR^{dB} \geq 9,6\ dB`
* Downlink/Uplink: :math:`SNR^{dB} \geq 9,6\ dB`
* Uplink (payload): :math:`SNR^{dB} \geq 9,6\ dB`

And considering the link margin as the SNR of the link minus the SNR threshold for a given bit error, the link margin of the radio links of the satellite are:

* Beacon: :math:`32,22 - 9,6 = \mathbf{22,62\ dB}`
* Downlink: :math:`13,41 - 9,6 = \mathbf{3,812\ dB}`
* Uplink: :math:`27,41 - 9,6 = \mathbf{17,81\ dB}`
* Uplink (payload): :math:`19,17 - 9,6 = \mathbf{9,57\ dB}`
