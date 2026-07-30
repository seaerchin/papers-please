# allowed lifecycle events

when a cloudfront distribution is associated with a lambda, we can execute the lambda on the following lifecycle events of cloudfront:
1. viewer request (when the viewer requests a page from cloudfront)
2. origin request (cloudfront cache miss -> we need to fetch from origin)
3. origin response (origin responds to cloudfront's request for that key)
4. viewer response (cloudfront back to user)

WAF executes **before** lambda@edge!
# event structure

contains [information](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-event-structure.html#lambda-event-structure-response) about the origin etc. this can be used to identify the origin that the request will be forwarded to. 

additionally, this allows us to do dynamic origin selection also - we can update the `origin` key to another value for cloudfront to route the request to that new origin