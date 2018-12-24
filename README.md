# cansploit

<img width="500" alt="logo" src="https://user-images.githubusercontent.com/27995559/50401141-a2a72b00-07cf-11e9-8ba1-aa2f416a797b.png">

cansploit
====

## Overview

cansploit is penetration test tool for in-vehicle network (CAN). cansploit provide pentesters of CAN with State-of-the-art format specification analysis method, DoS (Denial of Servide) attack method with arbitrary entropy.

## Description

cansploit is penetration test tool for Controller Area Network. Car pentesters can test general vulnerability on CAN (e.g., No encryption/authentication, Low speed bus topology network, ...).

## Directory Structure

cansploit  
┣━ main  
┃	┣━ main.py  
┃	┣━ sniffing.py  
┃	┣━ specification_analysis.py (READ algorithm)  
┃	┣━ DoS_attack.py (Traditional, Random, Targeted DoS attack)  
┃   ┣━ spoofing_attack.py  
┃	┗━ replay_attack.py  
┣━ sample-IDS  
┃	┣━ cycle-IDS.py  
┃	┣━ entropy-IDS.py  
┃	┗━ id-sequence.py  
┣━ .cansploitrc  
┗━ README.md  

## Requirement

can interface, virtual can interface

## Usage

$ git clone https://github.com/ohirangosta/cansploit  
$ cd cansploit  
$ ./cansploit can0  

## Attack Description

### Message sniffing

### Format specification analysis

### Denial of Service attack

### Spoofing attack

### Replay attack

## Contribution

## Author

[rangosta](https://github.com/ohirangosta)
