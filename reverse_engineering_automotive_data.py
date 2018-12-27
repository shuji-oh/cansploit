import sys
import math
from statistics import mean, median,variance,stdev

#classifer LABELs
COUNTER = "Counter"
CRC = "CRC"
PHYS = "Physical_Value"
CONSTANT = "Constant"

def matchCounter(bitFlip):
	if bitFlip == []:
		return False
	elif bitFlip[len(bitFlip)-1]==1 :
		return True
	else :
		return False

def PreProcessing(messageList, DLC):
	payloadLen = len(messageList)
	bitFlip = [0 for i in range(DLC)]
	magnitude = [0 for i in range(DLC)]
	previous = messageList[0]

	for item in messageList:
		DLC = len(item)
		for ix in range(0, DLC):
			if item[ix] != previous[ix]:
				bitFlip[ix] += 1

	for ix in range(0, DLC):
		bitFlip[ix] = bitFlip[ix]/payloadLen
		# eliminate log10(0.0)
		if bitFlip[ix] != 0.0 :
			magnitude[ix] = math.ceil(math.log10(bitFlip[ix]))
		else:
			magnitude[ix] = -100

	return bitFlip,magnitude

def Phase1(magnitude, DLC):
	ref = list()
	prevMagnitude = magnitude[0]
	ixS = 0
	for ix in range(1, DLC):
		if magnitude[ix] < prevMagnitude :
			ref.append((ixS, ix-1))
			ixS = ix
		prevMagnitude = magnitude[ix]
	ref.append((ixS, DLC-1))
	return ref

def Phase2(ref, bitFlip, magnitude):
	rRef = list()
	for sign in ref :
		ixS,ixE = sign
		if (ixE - ixS) > 1 :
			mu = mean(bitFlip[ixS:ixE])
			std = stdev(bitFlip[ixS:ixE])
		else  :
			mu = 0
			std = 0
		if magnitude[ixE] == 0 and matchCounter(bitFlip[ixS:ixE]):
			rRef.append((ixS, ixE, COUNTER))
		elif all(x == 0 for x in magnitude[ixS:ixE]) and 0.5-std <= mu <= 0.5+std:
			rRef.append((ixS, ixE, CRC))
		elif all(x == -100 for x in magnitude[ixS:ixE]):
			rRef.append((ixS, ixE, CONSTANT))
		else :
			rRef.append((ixS, ixE, PHYS))
	return rRef

if __name__=='__main__':
	argvs = sys.argv
	argc = len(argvs)

	if argc < 2:
		print('Usage: python3 %s filename' % argvs[0])
		print('[filename format]\n\t[CAN ID]#[PAYLOAD]\nex)\t000#00000000')
		quit()

	CANtraffic_log = argvs[1]

	canids = list()
	messageLists = [list() for i in range(2048)]

	# create list of canid, list of binary payload 
	with open(CANtraffic_log) as log_file:
		for log in log_file:
			canpacket = log.split("#")
			format_len = '0'+str((len(canpacket[1])-1)*4)+'b'
			payload = format(int(canpacket[1],16), format_len)
			#print(canpacket[0], payload)
			messageLists[int(canpacket[0], 16)].append(payload)
			if int(canpacket[0], 16) not in canids :
				canids.append(int(canpacket[0], 16))
	canids.sort()

	# perform Reverse Engineering of Automotive Data frames
	for canid in canids:
		DLC = len(messageLists[canid][0])
		bitFlip, magnitude = PreProcessing(messageLists[canid], DLC)
		#print(hex(canid), bitFlip, magnitude)
		ref = Phase1(magnitude, DLC)
		#print(hex(canid), ref)
		rRef = Phase2(ref, bitFlip, magnitude)
		print(hex(canid), rRef)