# VisualBI

Q2- 

Part 1 - Explain the Architecture model of this and the Benefit

The architecture employs cloud delivery network and load balancers for a host of servers. These servers are accessed 
via a website called foo.com.As per the model, the users are distributed across 5 geographic regions i.e Asia-Pacific, 
Europe, United States, Canada and Middle East. The model allows for a high available and scalable network. It helps to 
maximize application or data uptime. It also makes it possible to distribute data across a network of servers.

Part 2 - How do you roll out an update to the service without any downtime impact to the app foo.com

Let's assumes that the load balancer 1 is taking care of 6 servers/instances. If an update has to be rolled out then update 
can be rolled to 3 of the servers and while the other 3 will work as usual. This methodology will maintian uptime for users 
and won't result in any business loss. Once the update is carried for the before said servers it can be repeated for the 
remaining 3. Furthermore, the update process should be done in non-business hours to avoid any unforseen server congestion.

Part 3 - If you have to deploy this App to the Cloud what services would you use and explain the Architecture. 
		 You can mention for Cloud of your choice (AWS / Amazon / Google Cloud (GCP) / Oracle / Alibaba Cloud)
		 
AWS can be used to deploy this app. In AWS, we can use CloudFront for CDN purpose. There is also a provision for a 
service called Elastic Load Balancing(ELB). These ELB can be used as a Application Load Balancer in our case since 
users would be using HTTP/HTTPS to access foo.com. The instances/servers can be hosted on EC2 instances. Lastly, the 
data can be stored in S3 buckets. 

Using CloudFront with EC2 will also make sure that AWS doesn't charge for any data transfer between these services. Also, 
CloudFront works with AWS Shield which can be employed to avoid any DDoS via external IPs.
