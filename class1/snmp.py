import pysnmp
import sys
import date
import time 

from pysnmp.hlapi import *
errorIndication, errorStatus, errorIndex, varBinds = next(getCmd(SnmpEngine(snmpEngineID=OctetString(hexValue='8000000903000027E32F1766')),CommunityData('public', mpModel=0),UdpTransportTarget(('10.1.14.1', 161)),ContextData(),ObjectType(ObjectIdentity('IF-MIB', 'ifIndex', 1))))
for varBind in varBinds:
    print(' = '.join([x.prettyPrint() for x in varBind]))