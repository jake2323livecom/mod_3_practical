# Practical Exam

## Red Router

```
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname PRAC-RED-RTR
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
ethernet lmi ce
!
!
!
mmi polling-interval 60
no mmi auto-configure
no mmi pvc
mmi snmp-timeout 180
!
!
!
!
!
!
!
!
!
!
!
no ip domain lookup
ip domain name orko.local
no ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
archive
 log config
  logging enable
  logging persistent auto
  logging size 500
  hidekeys
file prompt quiet
username orko privilege 15 secret 5 $1$hzf.$3xSuThkYUYM47JTVNEq1w/
!
redundancy
!
!
! 
!
!
!
!
!
!
!
!
!
!
!
!
interface GigabitEthernet0/0
 no shutdown
 ip address 10.59.99.1 255.255.0.0
 duplex full
 speed auto
 media-type rj45
!
interface GigabitEthernet0/1
 no shutdown
 no ip address
 shutdown
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/2
 no shutdown
 no ip address
 shutdown
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/3
 no shutdown
 no ip address
 shutdown
 duplex auto
 speed auto
 media-type rj45
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip ssh version 2
!
!
!
!
control-plane
!
banner exec ^C

This is a practical exam device.



^C
banner incoming ^C

This is a practical exam device.



^C
banner login ^C

This is a practical exam device.



^C
!
line con 0
line aux 0
line vty 0 4
 login local
 transport input ssh
 transport output ssh
!
no scheduler allocate
event manager applet crypto_key
 event timer cron cron-entry "@reboot"
 action 1.0 cli command "enable"
 action 1.1 cli command "config t"
 action 1.2 cli command "file prompt quiet"
 action 1.3 cli command "crypto key generate rsa modulus 2048"
 action 1.4 cli command "end"
 action 1.5 cli command "write mem" pattern "confirm|#"
!
end
```

## Yellow Router

```
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname PRAC-YELLOW-RTR
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
ethernet lmi ce
!
!
!
mmi polling-interval 60
no mmi auto-configure
no mmi pvc
mmi snmp-timeout 180
!
!
!
!
!
!
!
!
!
!
!
no ip domain lookup
ip domain name orko.local
no ip cef
no ipv6 cef
!
multilink bundle-name authenticated
!
!
!
!
archive
 log config
  logging enable
  logging persistent auto
  logging size 500
  hidekeys
file prompt quiet
username orko privilege 15 secret 5 $1$JkE8$4dTIo0KXTnvqMNk424dOU/
!
redundancy
!
!
! 
!
!
!
!
!
!
!
!
!
!
!
!
interface GigabitEthernet0/0
 no shutdown
 ip address 10.59.99.3 255.255.0.0
 duplex full
 speed auto
 media-type rj45
!
interface GigabitEthernet0/1
 no shutdown
 no ip address
 shutdown
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/2
 no shutdown
 no ip address
 shutdown
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/3
 no shutdown
 no ip address
 shutdown
 duplex auto
 speed auto
 media-type rj45
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip ssh version 2
!
!
!
!
control-plane
!
banner exec ^C

This is a practical exam device.



^C
banner incoming ^C

This is a practical exam device.



^C
banner login ^C

This is a practical exam device.



^C
!
line con 0
line aux 0
line vty 0 4
 login local
 transport input ssh
 transport output ssh
!
no scheduler allocate
event manager applet crypto_key
 event timer cron cron-entry "@reboot"
 action 1.0 cli command "enable"
 action 1.1 cli command "config t"
 action 1.2 cli command "file prompt quiet"
 action 1.3 cli command "crypto key generate rsa modulus 2048"
 action 1.4 cli command "end"
 action 1.5 cli command "write mem" pattern "confirm|#"
!
end
```

## Red Switch

```
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname PRAC-RED-SW
!
boot-start-marker
boot-end-marker
!
!
!
username orko privilege 15 secret 5 $1$WMRK$s6AQiP8NHPsrqn88MYGZS/
no aaa new-model
!
!
!
!
!
vtp mode transparent
!
!
!
no ip domain-lookup
ip domain-name orko.local
no ip cef
no ipv6 cef
!
!
file prompt quiet
archive
 log config
  logging enable
  logging persistent auto
  logging size 500
  hidekeys
!
spanning-tree mode pvst
spanning-tree extend system-id
!
vlan internal allocation policy ascending
!
vlan 59
 name ORKO_LABS
!
! 
!
!
!
!
!
!
!
!
!
!
!
!
interface GigabitEthernet0/0
 no shutdown
 switchport access vlan 59
 switchport mode access
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/1
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/2
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/3
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/0
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/1
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/2
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/3
 no shutdown
 media-type rj45
 negotiation auto
!
interface Vlan59
 no shutdown
 ip address 10.59.99.2 255.255.0.0
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
ip ssh version 2
!
!
!
!
!
control-plane
!
banner exec ^C

This is a practical exam device.



^C
banner incoming ^C

This is a practical exam device.



^C
banner login ^C

This is a practical exam device.



^C
!
line con 0
line aux 0
line vty 0 4
 login local
 transport input ssh
 transport output ssh
!
no scheduler allocate
event manager applet crypto_key
 event timer cron cron-entry "@reboot"
 action 1.0 cli command "enable"
 action 1.1 cli command "config t"
 action 1.2 cli command "file prompt quiet"
 action 1.3 cli command "crypto key generate rsa modulus 2048"
 action 1.4 cli command "end"
 action 1.5 cli command "write mem" pattern "confirm|#"
!
end
```

## Yellow Switch

```
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname PRAC-YELLOW-SW
!
boot-start-marker
boot-end-marker
!
!
!
username orko privilege 15 secret 5 $1$Ksc/$li9DnhkutpfEB2cHCBMMa0
no aaa new-model
!
!
!
!
!
vtp mode transparent
!
!
!
no ip domain-lookup
ip domain-name orko.local
no ip cef
no ipv6 cef
!
!
file prompt quiet
archive
 log config
  logging enable
  logging persistent auto
  logging size 500
  hidekeys
!
spanning-tree mode pvst
spanning-tree extend system-id
!
vlan internal allocation policy ascending
!
vlan 59
 name ORKO_LABS
!
! 
!
!
!
!
!
!
!
!
!
!
!
!
interface GigabitEthernet0/0
 no shutdown
 switchport access vlan 59
 switchport mode access
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/1
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/2
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/3
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/0
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/1
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/2
 no shutdown
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/3
 no shutdown
 media-type rj45
 negotiation auto
!
interface Vlan59
 no shutdown
 ip address 10.59.99.4 255.255.0.0
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
ip ssh version 2
!
!
!
!
!
control-plane
!
banner exec ^C

This is a practical exam device.



^C
banner incoming ^C

This is a practical exam device.



^C
banner login ^C

This is a practical exam device.



^C
!
line con 0
line aux 0
line vty 0 4
 login local
 transport input ssh
 transport output ssh
!
no scheduler allocate
event manager applet crypto_key
 event timer cron cron-entry "@reboot"
 action 1.0 cli command "enable"
 action 1.1 cli command "config t"
 action 1.2 cli command "file prompt quiet"
 action 1.3 cli command "crypto key generate rsa modulus 2048"
 action 1.4 cli command "end"
 action 1.5 cli command "write mem" pattern "confirm|#"
!
end
```