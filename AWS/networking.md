
### public ip addressing for ec2 inst 
- public IP auto assigned 
- inbound connection initiated via internet -> implies public 
- Elastic IP addr (EIP) 
	- static + public ipv4 addr for your ec2 instances -> can be remapped 
- public ip mapped to private ip through [NAT](https://en.wikipedia.org/wiki/Network_address_translation)

### traffic out of sub net
- use route table
	- directs traffic out of your destinations 

### connect vpc to internet 
- use the igw -> performs **stateless** 1:1 NAT translation b/w public/private IPs.

### exposing internal services to other internal services
- use aws private link
- use vpc peering
- see [here](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html) for overview - aws private link is more specific; vpc peering allows range of IP

- we can use [transit gateway](https://aws.amazon.com/transit-gateway/) to simplify vpc mesh connections -> route sharing, so fully connected network topologies are easier 
- we must think about cidr blocks -> big cidr blocks might overlap, causing conflicts

### cidr blocks
0.0.0.0/8 -> first 8 bits are reserved; we do a bitwise AND with the actual IP to calculate range