### host categories
1. no access to hosts in other enterprises/internet at large - such hosts may use *enterprise level* unambiguous IP addresses.  **but** their ip might conflict with hosts in other enterprises; in reality such hosts have their access to the internet guarded through their igw/router.
2. hosts that require access to **limited** set of external services 
3. hosts that require **network layer access** outside organization - routers?
jjjffff   



### private address space
- 3 blocks of IP addr reserved for private nets 
	- 10.0.0.0 - 10.255.255.255 (10/8) 
	- 172.16.0.0 - 172.31.255.255  (172.16/12 prefix)
	- 192.168.0.0 - 192.168.255.255 (192.168/16 prefix)

this reads as prefix/# bits for prefix; # bits = 32 - # bits for prefix

### migration to/from private -> public
>Moving a host from private to public or vice versa involves a change
   of IP address, changes to the appropriate DNS entries, and changes to
   configuration files on other hosts that reference the host by IP
   address.

- ip packets get routed to the next node specified by the route table 
- internal ip addresses are meaningless outside of their network
- when we shift from private -> public, the (meaningless) internal ip addresses need to be shifted to a **globally unique + addressable** addresses

### pros/cons of cidr addresses 

**pros**
- enterprises are free to allocate addresses as they see fit

**cons**
>Once one commits to using a private address, one is committing to
   renumber part or all of an enterprise, should one decide to provide
   IP connectivity between that part (or all of the enterprise) and the
   Internet.
- ^ we have to provide translation of network addresses if, for some reason, the internal nodes require access to the wider network
- we also need to provide renumbering when companies merge.

### ops concern
we need **2** authoritative name servers for the private network 
  - 1 for private addresses
  - 1 for public addresses (but this still gets mapped to an internal IP)