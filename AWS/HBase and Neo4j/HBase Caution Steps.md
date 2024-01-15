Hbase

1.create Hbase cluster : 
link:https://youtu.be/jylp2atrZjc

in aws, create HBase cluster use “EMR”, click “HBase” 
when create the cluster, remember choose use Key Pair
Add inbound rule in cluster:
EC2 security groups (firewall)
add type:SSH source:My IP


2.Connect to the master node using SSH:
download the Key pairs
use Puttygen transform ppk to ppm 
click DNS, copy the code and modify and run:
e.g.  ssh -i ~/mykeypair.pem hadoop @ ec2-54-204-249-123.compute-1.amazonaws.com
	
3.launch HBase shell and use command
link:Using the HBase shell - Amazon EMR


4.Some other tips:
Transform the ppk to key file and give it permit
upload the openssh.key to cloudshell 
chrome the the file (permit access)
chmod 400 ~/NAOMI_openssh.key
