from setuptools import setup
import can

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
  print("[usage]\n1:Sniffing\n2:Dump and Format Specification Analysis\n3:DoS\n4:Spoofing\n5:Replay\n")

def print_usage_Sniffing():
  print("[usage]\nSelect can id [0x000~0x7FF]\n(negative value is all message sniffing)\n")

def print_usage_Dump_and_FSA(args):
  print("[usage]\n1:READ algorithm\n2:FBCA algorithm\n")
  dump_file = run_dump()
  Reverse_Engineering_Automotive_Data(dump_file)

def print_usage_DoS():
  print("[usage]\n1:Traditional DoS attack\n2:Random DoS attack\n3:Targeted DoS attack\n")

def print_usage_Spoofing():
  print("[usage]\nSelect can id [0x000~0x7FF]\n")

def print_usage_Replay():
  print("[usage]\n[Dumping...]\n")
'''
def run_cansploit_Sniffing():


def run_cansploit_Dump_and_FSA():
  READ_MODE = '1'
  FBCA_MODE = '2'


def run_cansploit_DoS():


def run_cansploit_Spoofing():


def run_cansploit_Replay():
'''


def run_cansploit():
  SNIFFING_MODE = '1'
  DUMP_FSA_MODE = '2'
  DoS_MODE = '3'
  SPOOFING_MODE = '4'
  REPLAY_MODE = '5'

  # cansploit main loop
  while True:
    cansploit_args = input("cansploit>")
    if cansploit_args == SNIFFING_MODE:
      input("cansploit(Sniffing)>")
      print_usage_Sniffing()
      run_cansploit_Sniffing()

    elif cansploit_args == DUMP_FSA_MODE:
      input("cansploit(Dump_and_FSA)>")
      print_usage_Dump_and_FSA()
      run_cansploit_Dump_and_FSA()

    elif cansploit_args == DoS_MODE:
      input("cansploit(DoS)>")
      print_usage_DoS()
      run_cansploit_DoS()

    elif cansploit_args == SPOOFING_MODE:
      input("cansploit(Spoofing)>")
      print_usage_Spoofing()
      run_cansploit_Spoofing()

    elif cansploit_args == REPLAY_MODE:
      input("cansploit(Replay)>")
      print_usage_Replay()
      run_cansploit_Replay()

    elif cansploit_args == 'h':
      print_usage_cansploit()

    else:
      print("invalid argument value")

if __name__ == '__main__':
  print_logo()
  '''
  input("cansploit(Sniffing)>")
  input("cansploit(Dump_and_FSA)>")
  input("cansploit(DoS)>")
  input("cansploit(Spoofing)>")
  input("cansploit(Replay)>")
  '''
  run_cansploit()