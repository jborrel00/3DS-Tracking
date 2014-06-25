3DS-Tracking
============

programs to power collateral-tracking hardware for 3DS events

Process
-------
-when a new item comes in, place an NDEF-formatted* tag on it

-write an item id onto the tag using tag_writer.pde (edit line 43 to create unique item ids)

-the tag an now be read by an NFC-enabled arduino running tag_reader.pde

-connect an NFC-reading arduino to the raspberry pi hub

-to act as a hub, the raspberry pi must have 3dinventory_script.py in the directory /home/pi/3ds_tracking

-operating a fully assembled tag reader from boot:
>cd 3ds_tracking

>sudo python 3dinventory_script.py

-follow the onscreen instructions

-once completed mysql table 3ds_tracking will be updated in database 3dsystems


*use arduino example code to convert mifare cards to ndef formatting
