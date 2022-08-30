### IAM permissions
- supposed to use aws session manager
	- finicky -> doesn't seem to work even w/ identical perms
- if you use `http` , other traffic won't work

### Cloudformation
- manage your resources for you (IaC)

### Amplify
- dump static resources into amplify 
- point cloudformation to s3 bucket link 
- dns automatic through cloudformation

### ec2
- launch templates - easy way to templatize launch requests (ie, seems to be iac platform?)