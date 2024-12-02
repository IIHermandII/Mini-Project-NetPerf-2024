#!/bin/bash

qlen=$1
dlay=$2
rate=10Mbit
rate2=10Mbit

function add_qdisc {
    dev=$1
    tc qdisc del dev $dev root
    echo qdisc removed

    tc qdisc add dev $dev root handle 1:0 htb default 1
    echo qdisc added

    tc class add dev $dev parent 1:0 classid 1:1 htb rate $rate ceil $rate
    echo classes created

    tc qdisc add dev $dev parent 1:1 handle 10: netem delay $dlay limit $qlen

    echo delay added
}

add_qdisc r1-eth1
add_qdisc r2-eth2