#!/usr/local/bin/python
import datetime
import time
import sys
import dpkt
import socket

def print_packet_info(ts, src_ip, src_port, dst_ip, dst_port, protocol, pkt_len, ttl):
    
    # get UTC timestamp, source/destination IP/port
    utc_timestamp = str(datetime.datetime.utcfromtimestamp(ts))
    
    # create log line
    log_line = '[%s] - %s:%s -> %s:%s (%s, len=%d, ttl=%d)' % \
      (utc_timestamp, src_ip, src_port, dst_ip, dst_port, protocol, pkt_len, ttl)
    
    print(log_line)

def print_summary(total_packet_count, total_bytes_count, average_pkt_size):

    print ('\n------------------- SUMMARY -------------------\n')
    print ('Total packets: %i' % (total_packet_count))
    print ('Total bytes (bytes): %i' % (total_bytes_count))
    print ('Average packet size (bytes): %i' % (average_pkt_size))
    print ('\n-----------------------------------------------')

def run_example():
 
    global total_packet_count, total_bytes_count
    
    try:
        sys.argv[1]
        dmp_file = sys.argv[1]
        fp_dmp_file = open(dmp_file)
    except Exception as e:
        print ('Error: please supply pcap filename!\n')
    return

f = open('test1.pcap') 
try: 
    sys.argv[1] 
    dmp_file = sys.argv[1] 
    file = open(dmp_file)
except Exception as e:
    print ('Error: please supply pcap filename!\n')
    pcap = dpkt.pcap.Reader(file)
    

for ts, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data
    src_ip = socket.inet_ntoa(ip.src)
    src_port = str(ip.data.sport)
    dst_ip = socket.inet_ntoa(ip.dst)
    dst_port = str(ip.data.dport)

if type(ip.data) == dpkt.tcp.TCP:
    protocol = 'tcp'
    
elif type(ip.data) == dpkt.udp.UDP:    
    protocol = 'udp'

print_packet_info(ts, src_ip, src_port, dst_ip, dst_port, protocol, ip.len, ip.ttl)

## write print_summary to be related to pcap file
for buf, print_summary in pcap:

    total_packet_count <=17;  
    total_bytes_count <=1500;  
    average_pkt_size <=1000;  

##print (total_packet_count, total_bytes_count, average_pkt_size)
print_summary(total_packet_count, total_bytes_count, average_pkt_size)

fp_dmp_file.close()

if name == 'main': 
  run_example()
