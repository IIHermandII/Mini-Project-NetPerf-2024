#!/usr/bin/python

"CS144 In-class exercise: Buffer Bloat"

from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
import csv
from subprocess import Popen, PIPE

from time import sleep, time
from multiprocessing import Process
import sys

import os

class Barbell(Topo):
    def __init__(self, n=2, cpu=None, bw_host=10, bw_net=10, delay=5, maxq=None, loss = 0):
        super(Barbell, self).__init__()

        # Create switches
        r1 = self.addSwitch('r1', fail_mode='open')
        r2 = self.addSwitch('r2', fail_mode='open')

        # Add the bottleneck link between the routers
        self.addLink(r1, r2, bw=bw_net, delay='%s' % delay, max_queue_size=int(maxq), loss = loss)

        # Add source and destination hosts and links
        for i in range(n):
            s = self.addHost('s%d' % (i + 1), cpu=cpu)
            d = self.addHost('d%d' % (i + 1), cpu=cpu)
            self.addLink(s, r1, bw=bw_host, delay='%s' % delay, max_queue_size=int(maxq))
            self.addLink(d, r2, bw=bw_host, delay='%s' % delay, max_queue_size=int(maxq))

def monitor_cwnd(host, interval_sec=0.01, runtime_sec=60, filename='cwnd.csv', verbose=False):
    # Open the CSV file in binary write mode for Python 2.7 compatibility
    with open(filename, mode='wb') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'CWND', 'RTT'])  # Write header row
        start = time()
        while True:
            timestepped = time() - start
            output = host.cmd('ss -ti')
            for line in output.splitlines():
                if ('cwnd' in line and 'rtt' in line):
                    c1 = line.find('cwnd')
                    c2 = line.find(':', c1)
                    c3 = line.find(" ", c2)
                    r1 = line.find('rtt')
                    r2 = line.find(':', r1)
                    r3 = line.find("/", r2)
                    # Write timestamp and cwnd info to the CSV file
                    writer.writerow([timestepped, line[c2+1:c3], line[r2+1:r3]])
                    if verbose: print("%f - %s%s - %s%s" % (timestepped, line[c1:c2], line[c2:c3], line[r1:r2], line[r2:r3]))
            if time() - start > runtime_sec:
                break
            sleep(interval_sec)  # Monitor every specified interval

def bbnet(bw_host=10, bw_net=10, delay=5, dir='./', j=0, maxq=100, n=5, loss = 0, tcptype='reno', verbose=False):
    "Create network and run Buffer Bloat experiment"
    if verbose: print("starting mininet ....")
    # Seconds to run iperf; keep this very high
    seconds = 60
    # Reset to known state
    topo = Barbell(n=n, bw_host=bw_host,
                    delay='%sms' % delay,
                    bw_net=bw_net, maxq=maxq, loss = loss)
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink,
                  autoPinCpus=True)
    
    net.start()
    if verbose: dumpNodeConnections(net.hosts)
    if verbose: print("exec tc_cmd_miniperf.sh")
    os.system("bash tc_cmd_miniperf.sh %s %s" % (maxq, delay))

    if verbose: print("Starting iperfs...")
    for i in range(n):
            s = net.getNodeByName('s%d' % (i + 1))
            d = net.getNodeByName('d%d' % (i + 1))
            # Start iperf server on destination
            #d.cmd('iperf -s -p %d -i 1 > %s/iperf-recv-%d.txt &' % (5001 + i, dir, i))
            d.cmd('iperf -s -p %d -i 1 &' % (5001 + i))
            # Start iperf client on source
            #s.cmd('iperf -c %s -p %d -t %d -i 1 > %s/iperf-send-%d.txt &' % (d.IP(), 5001 + i, seconds, dir, i))
            s.cmd('iperf -c %s -p %d -t %d -i 1 &' % (d.IP(), 5001 + i, seconds))
    
    monitor_cwnd(net.getNodeByName('s1'), filename='%s/cwnd_%i_%s.csv' % (dir,n, tcptype), verbose=verbose)

    net.stop()
    Popen("killall -9 cat", shell=True).wait()

def cleanup():
    """Clean up processes after the experiment."""
    print("Cleaning up...")
    os.system("killall -9 iperf ping")
    os.system("mn -c > /dev/null 2>&1")
    print("Cleanup complete.")

if __name__ == '__main__':
    dir = './testdir'
    if not os.path.exists(dir):
        os.makedirs(dir)
    tcptypes = ['reno', 'cubic', 'vegas', 'bbr']
    ns = [5, 10, 35, 100]
    #tcptype = 'reno'
    for j, tcptype in enumerate(tcptypes):
        cleanup()
        for n in ns:
            print("Running experiment with %d flows" % n)
            print("Setting TCP congestion control to %s" %tcptype)
            os.system("sudo sysctl -w net.ipv4.tcp_congestion_control=%s" % tcptype)
            os.system("sudo sysctl -w net.ipv4.tcp_min_tso_segs=1")
            bbnet(bw_host=10, bw_net=10, delay=5, dir=dir, j=j, maxq=100, n=n, loss=1, tcptype=tcptype, verbose=False)
            cleanup()
