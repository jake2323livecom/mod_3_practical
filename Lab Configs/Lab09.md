# Lab 9

## Red Router

```
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname LAB09-RED-RTR
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
username orko privilege 15 secret 5 $1$nfpG$WaddQf3kvg0uDfj2Fst7w/
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
 ip address 10.59.9.1 255.255.0.0
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
banner exec z

This is an Ansible Lab 09 device.



z
banner incoming z

This is an Ansible Lab 09 device.



z
banner login z

This is an Ansible Lab 09 device.



z
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
hostname LAB09-YELLOW-RTR
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
username orko privilege 15 secret 5 $1$sfbv$s1zcaFOMX78SqYitZRJNm0
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
 ip address 10.59.9.2 255.255.0.0
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
banner exec z

This is an Ansible Lab 09 device.



z
banner incoming z

This is an Ansible Lab 09 device.



z
banner login z

This is an Ansible Lab 09 device.



z
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
