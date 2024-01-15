## What to do
Before the code is run: please do the below.
Set up the project code and directories as is.

## AWS CONSOLE
Navigate to AWS console and start it
Copy the aws_access_key_id, aws_secret_access_key, aws_session_token

Replace the parameters in the auth/auth.json file with these respectively.
Next navigate to the security group of the Master and add two Inbound/Ingress rules

Allow SSH traffic on port 22, choose Either My Ip or Custom.

For Custom, input the subnet mask for all IPs from which traffic is expected.
For My Ip, your IP will be in put automatically.
Allow All TCP traffic from the either presto port usually (8889) and set up as specified above.

If you are unsure about the port, simply choose the entire port range (0 - 63555).
FOR THIS IT IS CRUCIAL THAT YOU LIMIT THE TRAFFIC TO COME FROM EITHER YOUR IP ONLY OR THE CUSTOM SUBNET MASK.
IF YOU DONT, IT ALLOWS ALL PUBLIC TRAFFIC AND PUBLIC TRAFFIC IS VERY SUSCEPTIBLE TO HACKS.
After the above the code should run fine.

## CODE EXECUTION
Make the changes in the auth/auth.json
Run the Main_File.py
An analysis is done on the data in the bigdata-project-analysis.ipynb
These are the only two files that need to be run

Feel free to reach out for clarity.
