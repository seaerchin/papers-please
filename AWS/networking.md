
```
export AWS_DEFAULT_REGION=ap-southeast-1
export AWS_ACCESS_KEY_ID=ASIARY7MWQIQDL523MHZ
export AWS_SECRET_ACCESS_KEY=f9w4URJjzoVNJYUZPdjlJA+ytAOUGFA3/gQD+JpY
export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEFsaCXVzLWVhc3QtMSJIMEYCIQDk3JKLmOm2v0aFknCieTKXOZ3TXvBv6mzgQy28ncr+/QIhAOALqPZ6FT/d4F9dX/8s/tGYBJdf66s5rP7cIQoa25rMKqACCOT//////////wEQABoMMTIyMzY2MTAwMDAwIgwUaAykoIdD+XpJ+C8q9AGFMyLgpeubIgxS4bZIs3mjhr9936gd6PxyGCnPG5gVE6EJOFeglBP0zZcd9wAVxetTGZGtvWlCh6n2i3H9KKo2iujoqpZUZhkf//jUpOQnO34r4PX44YyBrnTlIZ5hs+fYj8mgapuRpGfvewmH+jPWDQx5qRxUoXtGEuGXoETPPKo+p3nBzmcuin5eYDTwI0Lr5w5POolsA0Hd1rTvC0d51KmLHxZ7yqn/3bjRQCjB/hPSgjzOvRnz2QDHlbj4mNsdG8DAY8cCsu6VRov0Xr4zjlOcXAR7aChdu2Mr805965zUl92QS4aOXzUVMuuTKpMk01XwMKnh2pgGOpwBQSwbZ33E9OQ7oX7uPChae1d+0NwFWpMrmShoVtinqyEPfWSHdAyiR3FpVeGKcHdiM2zfvdqYVyv9ECvzsswNP+Fjr7kzo0ihVDy1Xd2UxlqddQSDzVo7TfHg84dt1kwkD5qWqNVuSX98ssi0ByZEuVtqzAtTShLCW7dHPD1BuIlq1VOlIkX7KQMcogbJoiOBBhlG+bfbLkXbTOYd
```

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