.. packets.rst

    Copyright The GOLDS-UFSC Contributors.

    GOLDS-UFSC Documentation

    This work is licensed under the Creative Commons Attribution-ShareAlike 4.0
    International License. To view a copy of this license,
    visit http://creativecommons.org/licenses/by-sa/4.0/.

.. _anx:packets:

*************************
Telecommunication Packets
*************************

This appendix lists all the packets used by the RF links of the satellite: Beacon, downlink, and uplink. The fields and length of each type of packet is also presented.

Beacon
======

The :numref:`tab:beacon-packets` presents the content of the beacon packets.

.. _tab:beacon-packets:

.. list-table:: Beacon packets.
   :header-rows: 1
   :widths: 20 10 55 15

   * - **Packet** 
     - **Position** 
     - **Content** 
     - **Length [bytes]** 
   * - EPS data
     - 0
     - Packet ID (00h)
     - 1
   * - EPS data
     - 1
     - Source callsign (“ PY0EFS”)
     - 7
   * - EPS data
     - 8
     - Timestamp in ms
     - 4
   * - EPS data
     - 12
     - Battery cell 1 voltage in mV
     - 2
   * - EPS data
     - 14
     - Battery cell 2 voltage in mV
     - 2
   * - EPS data
     - 16
     - Battery current in mA
     - 2
   * - EPS data
     - 18
     - Battery charge in mAh
     - 2
   * - EPS data
     - 20
     - Battery cell 1 temperature in K
     - 2
   * - EPS data
     - 22
     - Battery cell 2 temperature in K
     - 2
   * - EPS data
     - 24
     - Battery monitor temperature in K
     - 2
   * - EPS data
     - 26
     - Solar panel voltage in mV (-Y and +X)
     - 2
   * - EPS data
     - 28
     - Solar panel voltage in mV (-X and +Z)
     - 2
   * - EPS data
     - 30
     - Solar panel voltage in mV (-Z and +Y)
     - 2
   * - EPS data
     - 32
     - Solar panel current in mA (-Y)
     - 2
   * - EPS data
     - 34
     - Solar panel current in mA (+Y)
     - 2
   * - EPS data
     - 36
     - Solar panel current in mA (-X)
     - 2
   * - EPS data
     - 38
     - Solar panel current in mA (+X)
     - 2
   * - EPS data
     - 40
     - Solar panel current in mA (-Z)
     - 2
   * - EPS data
     - 42
     - Solar panel current in mA (+Z)
     - 2
   * - EPS data
     - 44
     - Temperature of the EPS µC in K
     - 2
   * - EPS data
     - 
     - Total length
     - 46
   * - TTC data
     - 0
     - Packet ID (01h)
     - 1
   * - TTC data
     - 1
     - Source callsign (“ PY0EFS”)
     - 7
   * - TTC data
     - 8
     - Timestamp in ms
     - 4
   * - TTC data
     - 12
     - Temperature of the TTC µC in K
     - 2
   * - TTC data
     - 14
     - Reset counter
     - 2
   * - TTC data
     - 16
     - Last reset cause
     - 1
   * - TTC data
     - 15
     - Temperature of the beacon radio in K
     - 2
   * - TTC data
     - 
     - Total length
     - 19

Downlink
========

In :numref:`tab:downlink-packets` the content of the downlink packets is available.

.. _tab:downlink-packets:

.. list-table:: Downlink packets.
   :header-rows: 1
   :widths: 20 10 55 15

   * - **Packet** 
     - **Position** 
     - **Content** 
     - **Length [bytes]** 
   * - General telemetry
     - 0
     - Packet ID (20h)
     - 1
   * - General telemetry
     - 1
     - Source callsign (“ PY0EFS”)
     - 7
   * - General telemetry
     - 8
     - Time counter in milliseconds
     - 4
   * - General telemetry
     - 12
     - Temperature of the OBDH µC in Kelvin
     - 2
   * - General telemetry
     - 14
     - Input current of the OBDH in mA
     - 2
   * - General telemetry
     - 16
     - Input voltage of the OBDH in mV
     - 2
   * - General telemetry
     - 18
     - Last reset cause of the OBDH
     - 1
   * - General telemetry
     - 19
     - Reset counter of the OBDH
     - 2
   * - General telemetry
     - 21
     - Last valid telecommand (uplink packet ID)
     - 1
   * - General telemetry
     - 22
     - Temperature of the radio in Kelvin
     - 2
   * - General telemetry
     - 24
     - RSSI of the last valid telecommand
     - 2
   * - General telemetry
     - 26
     - Temperature of the antenna in Kelvin
     - 2
   * - General telemetry
     - 28
     - Antenna status
     - 2
   * - General telemetry
     - 30
     - Payloads status
     - 1
   * - General telemetry
     - 31
     - Temperature of the EPS µC in K
     - 2
   * - General telemetry
     - 33
     - EPS circuitry and Beacon MCU current in mA
     - 2
   * - General telemetry
     - 35
     - Last reset cause of the EPS
     - 1
   * - General telemetry
     - 36
     - Reset counter (EPS)
     - 2
   * - General telemetry
     - 38
     - -Y and +X sides solar panel voltage in mV
     - 2
   * - General telemetry
     - 40
     - -X and +Z sides solar panel voltage in mV
     - 2
   * - General telemetry
     - 42
     - -Z and +Y sides solar panel voltage in mV
     - 2
   * - General telemetry
     - 44
     - -Y side solar panel current in mA
     - 2
   * - General telemetry
     - 46
     - +Y side solar panel current in mA
     - 2
   * - General telemetry
     - 48
     - -X side solar panel current in mA
     - 2
   * - General telemetry
     - 50
     - +X side solar panel current in mA
     - 2
   * - General telemetry
     - 52
     - -Z side solar panel current in mA
     - 2
   * - General telemetry
     - 54
     - +Z side solar panel current in mA
     - 2
   * - General telemetry
     - 55
     - MPPT 1 duty cycle in %
     - 1
   * - General telemetry
     - 56
     - MPPT 2 duty cycle in %
     - 1
   * - General telemetry
     - 57
     - MPPT 3 duty cycle in %
     - 1
   * - General telemetry
     - 59
     - Main power bus voltage in mV
     - 2
   * - General telemetry
     - 61
     - Batteries voltage in mV
     - 2
   * - General telemetry
     - 63
     - Batteries current in mA
     - 2
   * - General telemetry
     - 65
     - Batteries average current in mA
     - 2
   * - General telemetry
     - 67
     - Batteries accumulated current in mA
     - 2
   * - General telemetry
     - 69
     - Batteries charge in mAh
     - 2
   * - General telemetry
     - 71
     - Battery monitor IC temperature in K
     - 2
   * - General telemetry
     - 73
     - Battery heater 1 duty cycle in %
     - 1
   * - General telemetry
     - 74
     - Battery heater 2 duty cycle in %
     - 1
   * - General telemetry
     - 75
     - Payload EDC status (00h=none, 01h=EDC_1, 02h=EDC_2, 03h=Both)
     - 1
   * - General telemetry
     - 76
     - Radiation instrument status (00h=OFF,01h=ON)
     - 1
   * - General telemetry
     - 77
     - Radiation monitor status (00h=OFF,01h=ON)
     - 1
   * - General telemetry
     - 
     - Total length
     - 78
   * - Ping answer
     - 0
     - Packet ID (21h)
     - 1
   * - Ping answer
     - 1
     - Source callsign (“ PY0EFS”)
     - 7
   * - Ping answer
     - 8
     - Requester callsign
     - 7
   * - Ping answer
     - 
     - Total length
     - 15
   * - Data request answer
     - 0
     - Packet ID (22h)
     - 1
   * - Data request answer
     - 1
     - Source callsign (“ PY0EFS”)
     - 7
   * - Data request answer
     - 8
     - Requester callsign
     - 7
   * - Data request answer
     - 15
     - Data type ID
     - 1
   * - Data request answer
     - 16
     - Timestamp
     - 4
   * - Data request answer
     - 20
     - Data
     - Var.
   * - Data request answer
     - 
     - Total length
     - 20 (min.)
   * - Message broadcast
     - 0
     - Packet ID (23h)
     - 1
   * - Message broadcast
     - 1
     - Source callsign (“ PY0EFS”)
     - 7
   * - Message broadcast
     - 8
     - Requester callsign
     - 7
   * - Message broadcast
     - 15
     - Destination callsign
     - 7
   * - Message broadcast
     - 22
     - Message
     - up to 38
   * - Message broadcast
     - 
     - Total length
     - 22 to 60
   * - Payload data (EDC info)
     - 0
     - Packet ID (24h)
     - 1
   * - Payload data (EDC info)
     - 1
     - Source callsign (“ PY0EFS”)
     - 7
   * - Payload data (EDC info)
     - 8
     - Payload ID (01h or 02h)
     - 1
   * - Payload data (EDC info)
     - 9
     - PTT signal receiving time
     - 4
   * - Payload data (EDC info)
     - 13
     - Error code
     - 1
   * - Payload data (EDC info)
     - 14
     - Carrier frequency
     - 2
   * - Payload data (EDC info)
     - 16
     - Carrier amplitude at ADC interface output
     - 2
   * - Payload data (EDC info)
     - 18
     - User message length in bytes
     - 1
   * - Payload data (EDC info)
     - 19
     - ARGOS-2 PTT-A2 user message
     - 35
   * - Payload data (EDC info)
     - 54
     - Current time since J2000 epoch
     - 4
   * - Payload data (EDC info)
     - 58
     - Elapsed time since last reset
     - 4
   * - Payload data (EDC info)
     - 62
     - System current supply in mA
     - 2
   * - Payload data (EDC info)
     - 64
     - System voltage supply in mV
     - 2
   * - Payload data (EDC info)
     - 65
     - EDC board temperature
     - 1
   * - Payload data (EDC info)
     - 66
     - RF front end LO
     - 1
   * - Payload data (EDC info)
     - 67
     - RMS level at front-end output
     - 2
   * - Payload data (EDC info)
     - 69
     - Generated PTT packages since last initialization
     - 1
   * - Payload data (EDC info)
     - 70
     - Max
     - 1
   * - Payload data (EDC info)
     - 71
     - Memory error count
     - 1
   * - Payload data (EDC info)
     - 72
     - Current time
     - 4
   * - Payload data (EDC info)
     - 76
     - Number of PTT package available for reading
     - 1
   * - Payload data (EDC info)
     - 77
     - PTT decoder task status
     - 1
   * - Payload data (EDC info)
     - 78
     - ADC sampler state
     - 1
   * - Payload data (EDC info)
     - 
     - Total length
     - 79
   * - Payload data (EDC samples)
     - 0
     - Packet ID (24h)
     - 1
   * - Payload data (EDC samples)
     - 1
     - Source callsign (“ PY0EFS”)
     - 7
   * - Payload data (EDC samples)
     - 8
     - Payload ID (01h or 02h)
     - 1
   * - Payload data (EDC samples)
     - 9
     - Elapsed time since J2000 epoch
     - 4
   * - Payload data (EDC samples)
     - 13
     - ADC sample packet number
     - 1
   * - Payload data (EDC samples)
     - 14
     - First ADC I-sample
     - 2
   * - Payload data (EDC samples)
     - 16
     - First ADC Q-sample
     - 2
   * - Payload data (EDC samples)
     - ``...``
     - ``...``
     - ``...``
   * - Payload data (EDC samples)
     - 214
     - N ADC I-sample
     - 2
   * - Payload data (EDC samples)
     - 216
     - N ADC Q-sample
     - 2
   * - Payload data (EDC samples)
     - 
     - Total length
     - 218
   * - TC feedback
     - 0
     - Packet ID (25h)
     - 1
   * - TC feedback
     - 1
     - Source callsign (“ PY0EFS”)
     - 7
   * - TC feedback
     - 8
     - Requester callsign
     - 7
   * - TC feedback
     - 15
     - TC packet ID
     - 1
   * - TC feedback
     - 16
     - Timestamp
     - 4
   * - TC feedback
     - 
     - Total length
     - 20
   * - Parameter value
     - 0
     - Packet ID (26h)
     - 1
   * - Parameter value
     - 1
     - Source callsign (“ PY0EFS”)
     - 7
   * - Parameter value
     - 8
     - Requester callsign
     - 7
   * - Parameter value
     - 15
     - Subsystem ID
     - 1
   * - Parameter value
     - 16
     - Parameter ID
     - 1
   * - Parameter value
     - 17
     - Parameter value
     - 4
   * - Parameter value
     - 
     - Total length
     - 21

Uplink
======

As shown in :numref:`tab:packets-struct`, there are 14 supported telecommands. Below there is a description of each one.

* **Ping Request:**  It is a simple command to test the communication with the satellite. When the satellite receives a ping packet, it will respond with another ping packet (with another packet ID, as defined in the downlink packets list). There are no additional parameters in the ping packet, just the packet ID and the source callsign (or address). It is also a public telecommand, anyone can send a ping request telecommand to a satellite.
* **Data Request:**  It is a command to download data from the satellite. This command allows a ground station to get specific parameters from a given period (stored in the non-volatile memory of the onboard computer of the satellite). The list of possible parameters varies according to the satellite. The required fields of this telecommand are the parameter ID (1 byte), the start period in milliseconds (epoch, 4 bytes), and the end period in milliseconds (epoch, 4 bytes). This is a private telecommand, and a key is required to send it.
* **Bloadcast Message:**  The "broadcast message" is another public telecommand, no authentication or key is required to send this telecommand to a satellite. This command has the purpose of making a satellite transmit a custom message back to Earth. This can be useful for communication tasks, like a station sending data to another. There are two parameters in this telecommand: the destination callsign (or address), and the content of the message, which can be any sequence of ASCII characters or any byte value. There is a limit of 38 characters in the message field.
* **Enter Hibernation:**  This telecommand activates the hibernation mode in a satellite. During the hibernation mode, no transmissions are made by the satellite; it keeps just listening for new incoming packets (reception). The satellite will stay in hibernation mode for a custom period (1 to 65536 minutes), or until a "Leave Hibernation" mode is received. This is a private telecommand, a key is required to send it. Beyond the packet ID and the source callsign (or address), the number o minutes (2 bytes long) is also transmitted.
* **Leave Hibernation:**  This telecommand complements the "enter hibernation" telecommand by deactivating the hibernation mode in the satellite. When a satellite receives this telecommand, it enables the transmission again immediately. This is also a private telecommand; a specific key is required to send it. There is no additional content to this telecommand packet, just the packet ID and the source callsign (or address).
* **Activate Module:** It activates an internal module of the satellite. Each module has a unique ID that is passed as an argument of this telecommand's packet. The module Battery heater's ID is 1, Beacon's ID is 2 and Periodic telemetry has ID number 3.
* **Activate Payload:**  This one is similar to the telecommand "Activate Module", but in this case is used for activating payloads of the satellite. Each satellite will have a list of IDs of the set of payloads. This is also a private telecommand, and a key is required to transmit it.
* **Deactivate Payload:**  It is the same as the "Deactivate Module" telecommand, but for payloads.
* **Erase Memory:**  It erases all the content presented in the non-volatile memories of the onboard computer of a satellite. This is a private command, and a key is required to send it. No additional content is required in a erase memory telecommand packet, just the packet ID and the source callsign (or address).
* **Force Reset:**  It performs a general reset of the satellite. When received, the satellite reset all subsystems. This is a private telecommand, and a key is required to send this command to a satellite. There is no additional content in this packet, just the packet ID and the source callsign (or address).
* **Get Payload Data:**  It allows a ground station to download data from a specific payload of the satellite. The required fields are the payload ID, and optionally, arguments to be passed to the payload. The IDs and arguments vary according to the satellite. This is a private telecommand, and a key is required to send it.
* **Set Parameter:**  It allows the configuration of specific parameters of a given subsystem of the satellite. The required fields are the ID of the subsystem to set (1 byte), the ID of the parameter to set (1 byte), and the new value of the parameter (4 bytes long). The possible IDs (subsystem and parameter) vary according to the satellite. This is a private telecommand, and a key is required to send it.
* **Get Parameter:**  This telecommand complements the "Set Parameter" telecommand. It has the purpose of reading specific parameters of a given subsystem. The required fields are the subsystem's ID (1 byte) and the parameter ID (1 byte). The possible IDs (subsystem and parameter) vary according to the satellite. This is a private telecommand, and a key is required to send it.

The :numref:`tab:uplink-packets` presents the content of the uplink packets.

.. _tab:uplink-packets:

.. list-table:: Uplink packets.
   :header-rows: 1
   :widths: 20 10 55 15

   * - **Packet** 
     - **Position** 
     - **Content** 
     - **Length [bytes]** 
   * - Ping request
     - 0
     - Packet ID (40h)
     - 1
   * - Ping request
     - 1
     - Ground station callsign
     - 7
   * - Ping request
     - 
     - Total length
     - 8
   * - Data request
     - 0
     - Packet ID (41h)
     - 1
   * - Data request
     - 1
     - Ground station callsign
     - 7
   * - Data request
     - 8
     - Data type ID
     - 1
   * - Data request
     - 9
     - Start timestamp
     - 4
   * - Data request
     - 13
     - End timestamp
     - 4
   * - Data request
     - 17
     - HMAC hash
     - 20
   * - Data request
     - 
     - Total length
     - 37
   * - Broadcast message
     - 0
     - Packet ID (42h)
     - 1
   * - Broadcast message
     - 1
     - Ground station callsign
     - 7
   * - Broadcast message
     - 8
     - Destination callsign
     - 7
   * - Broadcast message
     - 15
     - Message
     - up to 38
   * - Broadcast message
     - 
     - Total length
     - up to 53
   * - Enter hibernation
     - 0
     - Packet ID (43h)
     - 1
   * - Enter hibernation
     - 1
     - Ground station callsign
     - 7
   * - Enter hibernation
     - 8
     - Hibernation in hours
     - 2
   * - Enter hibernation
     - 10
     - HMAC hash
     - 20
   * - Enter hibernation
     - 
     - Total length
     - 30
   * - Leave hibernation
     - 0
     - Packet ID (44h)
     - 1
   * - Leave hibernation
     - 1
     - Ground station callsign
     - 7
   * - Leave hibernation
     - 8
     - HMAC hash
     - 20
   * - Leave hibernation
     - 
     - Total length
     - 28
   * - Activate module
     - 0
     - Packet ID (45h)
     - 1
   * - Activate module
     - 1
     - Ground station callsign
     - 7
   * - Activate module
     - 8
     - Module ID
     - 1
   * - Activate module
     - 9
     - HMAC hash
     - 20
   * - Activate module
     - 
     - Total length
     - 29
   * - Deactivate module
     - 0
     - Packet ID (46h)
     - 1
   * - Deactivate module
     - 1
     - Ground station callsign
     - 7
   * - Deactivate module
     - 8
     - Module ID
     - 1
   * - Deactivate module
     - 9
     - HMAC hash
     - 20
   * - Deactivate module
     - 
     - Total length
     - 29
   * - Activate payload
     - 0
     - Packet ID (47h)
     - 1
   * - Activate payload
     - 1
     - Ground station callsign
     - 7
   * - Activate payload
     - 8
     - Payload ID
     - 1
   * - Activate payload
     - 9
     - HMAC hash
     - 20
   * - Activate payload
     - 
     - Total length
     - 29
   * - Deactivate payload
     - 0
     - Packet ID (48h)
     - 1
   * - Deactivate payload
     - 1
     - Ground station callsign
     - 7
   * - Deactivate payload
     - 8
     - Payload ID
     - 1
   * - Deactivate payload
     - 9
     - HMAC hash
     - 20
   * - Deactivate payload
     - 
     - Total length
     - 29
   * - Erase memory
     - 0
     - Packet ID (49h)
     - 1
   * - Erase memory
     - 1
     - Ground station callsign
     - 7
   * - Erase memory
     - 8
     - HMAC hash
     - 20
   * - Erase memory
     - 
     - Total length
     - 28
   * - Force reset
     - 0
     - Packet ID (4Ah)
     - 1
   * - Force reset
     - 1
     - Ground station callsign
     - 7
   * - Force reset
     - 8
     - HMAC hash
     - 20
   * - Force reset
     - 
     - Total length
     - 28
   * - Get payload data
     - 0
     - Packet ID (4Bh)
     - 1
   * - Get payload data
     - 1
     - Ground station callsign
     - 7
   * - Get payload data
     - 8
     - Payload ID
     - 1
   * - Get payload data
     - 9
     - Payload arguments
     - 12
   * - Get payload data
     - 21
     - HMAC hash
     - 20
   * - Get payload data
     - 
     - Total length
     - 41
   * - Set parameter
     - 0
     - Packet ID (4Ch)
     - 1
   * - Set parameter
     - 1
     - Ground station callsign
     - 7
   * - Set parameter
     - 8
     - Subsystem ID
     - 1
   * - Set parameter
     - 9
     - Parameter ID
     - 1
   * - Set parameter
     - 10
     - Parameter value
     - 4
   * - Set parameter
     - 14
     - HMAC hash
     - 20
   * - Set parameter
     - 
     - Total length
     - 34
   * - Get parameter
     - 0
     - Packet ID (4Dh)
     - 1
   * - Get parameter
     - 1
     - Ground station callsign
     - 7
   * - Get parameter
     - 8
     - Subsystem ID
     - 1
   * - Get parameter
     - 9
     - Parameter ID
     - 1
   * - Get parameter
     - 10
     - HMAC hash
     - 20
   * - Get parameter
     - 
     - Total length
     - 30
