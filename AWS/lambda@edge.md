# allowed lifecycle events

when a cloudfront distribution is associated with a lambda, we can execute the lambda on the following lifecycle events of cloudfront:
1. viewer request (when the viewer requests a page from cloudfront)
2. origin request (cloudfront cache miss -> we need to fetch from origin)
3. origin response (origin responds to cloudfront's request for that key)
4. viewer response (cloudfront back to user)

WAF executes **before** lambda@edge!
# event structure
