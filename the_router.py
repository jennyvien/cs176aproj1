from cs176.api import *
from cs176.basics import *

'''
Create your distance vector router in this file.
'''
class DVRouter (Entity):
    def __init__(self):
		self.forwardingTable = {} # dest and port
		self.routingTable = {}
		
		pass

    def handle_rx (self, packet, port):
        # Add your code here!
		if type(packet) is DiscoverPackets :
			if (packet.is_link_up == True) and (self.forwardingTable.get(packet.src) == None) :
				self.forwardingTable[packet.src] = port
		elif type(packet) is UpdateRouting :
			pass
		else : 
			self.send(packet, self.forwardingTable[packet.dst], flood=False)
			pass
		#raise NotImplementedError
