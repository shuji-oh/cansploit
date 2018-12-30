from setuptools import setup
import can
import attacks.DoS_attack
import attacks.Spoofing_attack
import attacks.Replay_attack
import attacks.FSA ### FSA = Format Specification Analysis ###

def print_logo():
	logo = "\n \
           .                                         .\n \
   .\n \
  \n \
            dBBBBBBb dBBBBB     dB      Bb     .               o\n \
           dB    Bb      BBP   dB dB   Bb\n \
          dB         dBP BB   dB  BBB Bb\n \
         dB    Bb   dBP  BB  dB    Bb'B\n \
        dBBBBBBb   dBBBBBBB dB      Bb\n \
  \n \
                                         dBBBBBP  dBBBBBb  dBP    dBBBBP dBP dBBBBBBP\n \
            .                      .                  dB' dBP    dB'.BP\n \
                                   |       dBP    dBBBB' dBP    dB'.BP dBP    dBP\n \
                                 --o--    dBP    dBP    dBP    dB'.BP dBP    dBP\n \
                                   |     dBBBBP dBP    dBBBBP dBBBBP dBP    dBP\n \
  \n \
                                                                      .\n \
                  .\n \
          o\n \
                             To boldly shell were no\n \
                              shell has gone before "
	print(logo)

def print_usage_cansploit():
	print("[usage]\n1:Sniffing\n2:Dump and Format Specification Analysis\n3:DoS\n4:Spoofing\n5:Replay\nh:help\n")

def print_usage_Sniffing():
	print("[usage]\nSelect can id [0x000~0x7FF]\n(negative value is all message sniffing)\n")

def print_usage_Dump_and_FSA(args):
	print("[usage]\n1:READ algorithm\n2:FBCA algorithm\n")

def print_usage_DoS():
	print("[usage]\n1:Traditional DoS attack\n2:Random DoS attack\n3:Targeted DoS attack\n")

def print_usage_Spoofing():
	print("[usage]\nSelect can id [0x000~0x7FF]\n")

def print_usage_Replay():
	print("[usage]\n[Dumping...] (if you want to stop dumping, please click Enter)\n[Fortmat Specification Analysis...] (Please wait)\nh:help\n")

def run_cansploit_Dump_and_FSA():
	READ_MODE = '1'
	FBCA_MODE = '2'

	# print usage
	print_usage_Dump_and_FSA()

	# start dump		
	dump_file = run_dump()

	while True:
		args = input("cansploit(Dump_and_FSA)>")
		if args == READ_MODE:
			FSA_algorithm = READ()
			FSA_algorithm.run(dump_file)
			FSA_algorithm.write(written_file)
		elif args == FBCA_MODE:
			FSA_algorithm = FBCA()
			FSA_algorithm.run(dump_file)
			FSA_algorithm.write(written_file)
		elif args == 'd':
			# start dump		
			dump_file = run_dump()
		elif args == 'e':
			break
		elif args == 'h':
			print_usage_Dump_and_FSA()
		else:
			print("invalid argument value")

def run_cansploit_Sniffing():
	# print usage
	print_usage_Sniffing()	
	
	while True:
		args = input("cansploit(Sniffing)>")
		if is_can_id(args):
			dump_file = run_dump()
		elif args == 'e':
			break
		elif args == 'h':
			print_usage_Sniffing()
		else:
			print("invalid argument value")

def run_cansploit_DoS():
	TRADITIONAL_MODE = '1'
	RANDOM_MODE = '2'
	TARGETED_MODE = '3'

	# print usage
	print_usage_DoS()

	while True:
		args = input("cansploit(DoS)>")
		if args == TRADITIONAL_MODE:
			execve('./TraditionalDoS', interface)
		elif args == RANDOM_MODE:
			execve('./RandomDoS', interface, range_low, range_high)
		elif args == TARGETED_MODE:
			execve('./TargetedDoS', interface, attack_id)
		elif args == 'e':
			break
		elif args == 'h':
			print_usage_DoS()
		else:
			print("invalid argument value")

def run_cansploit_Spoofing():
	# print usage
	print_usage_Spoofing()

	while True:
		args = input("cansploit(Spoofing)>")
		if is_can_id(args):
			Spoofing_attack(args)
		elif args == 'e':
			break
		elif args == 'h':
			print_usage_Spoofing()
		else:
			print("invalid argument value")

def run_cansploit_Replay():
	# print usage
	print_usage_Replay()

	# start dump		
	dump_file = run_dump()

	while True:
		args = input("cansploit(Replay)>")
		if args == 'r':
			Replay_attack(dump)
		elif args == 'd':
			# start dump		
			dump_file = run_dump()
		elif args == 'e':
			break
		elif args == 'h':
			print_usage_Replay()
		else:
			print("invalid argument value")

def run_cansploit():
	SNIFFING_MODE = '1'
	DUMP_FSA_MODE = '2'
	DoS_MODE = '3'
	SPOOFING_MODE = '4'
	REPLAY_MODE = '5'

	# print usage
	print_usage_cansploit()

	###########################
	### cansploit main loop ###
	###########################
	while True:
		cansploit_args = input("cansploit>")
		if cansploit_args == SNIFFING_MODE:
			run_cansploit_Sniffing()
		elif cansploit_args == DUMP_FSA_MODE:
			run_cansploit_Dump_and_FSA()
		elif cansploit_args == DoS_MODE:
			run_cansploit_DoS()
		elif cansploit_args == SPOOFING_MODE:
			run_cansploit_Spoofing()
		elif cansploit_args == REPLAY_MODE:
			run_cansploit_Replay()
		elif cansploit_args == 'h':
			print_usage_cansploit()
		else:
			print("invalid argument value")

if __name__ == '__main__':
	print_logo()
	run_cansploit()