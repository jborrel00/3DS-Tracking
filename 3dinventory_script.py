"""
3DS Inventory Database
This python script will keep track of all 3D Systems inventory associated with Marketing events launched out of or channeled through the New York office at 868 Broadway, New York, NY, 10003
The script will read serial output from an arduino with NFC capabilities and store that output in a MySQL Database
The database will contain information pertaining to the item itself, where it was sent, when it was sent, and who/what it was sent to

this script is based largely on foosball_game.py, built in the affinitive skunkworks
"""
#opening serial connection between pi and arduino
import serial
import MySQLdb as mdb 
from time import sleep
import glob

if '/dev/ttyACM1' in glob.glob('/dev/tty*'):
	ser = serial.Serial('/dev/ttyACM1',115200)
else:
	ser = serial.Serial('/dev/ttyACM0',115200)

#read serial data sent from arduino - item_id on NFC tag
print "reading..."
r = ser.readline()
print r #debugging

#gathering checkout/checkin-specific data
item = str(raw_input('what kind of item is this? (i.e. - 3d printer, scanner, cartridge, ...'))
item_id = str(r)
#item_id = raw_input('what is the item id?') #this comes from the NFC tag
event = str(raw_input('what event is the item going to? (i.e. - CES, ComicCon, SU, ...)'))
in_out = str(raw_input('checking item in or out? (in/out)'))
#time = raw_input('when did this item get checked out?') #this will be automatically entered by mysql
location = str(raw_input('what geographic location is this item going to?'))
contact = str(raw_input('who is the contact person for this item while it is checked out?'))

#populating the database
con = mdb.connect('localhost','root','123dprint','3dsystems')
with con:
	cur = con.cursor()
	cur.execute("insert into 3ds_tracking (item,item_id,event,in_out,time,location,contact) values ("+item+","+item_id+","+event+","+in_out+",current_date(),"+location+","+contact+")")
