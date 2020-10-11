Azure DevOps CI
===============
AWS agent pool configuration for Azure DevOps CI self hosted agent. Tutorial on YouTube_.

First step is create a new personal access token on Azure.

Click ``Show All Scopes``, select ``Agent Pools`` ``Read & Manage`` options, choose ``Deployment Groups`` ``Read & Manage`` option and finnaly click ``Create``.  

Next step go in to Azure setting and ``Get agent``. On this step everything is explained in documentation on this page. 

Run instance on AWS with Windows or Linux. If you need GPU compute power, select Elastic GPU in the instance setting. 
Open terminal and put the command you saw earlier in the documentation ``Get agent`` pages. Tested on ``t2.xlarge`` instance with GPU. 

Everything is explained in the video tutorial above. Check it out if you have any problems.

You can also use your computer as an agent, then you don't need to run the machine on AWS or any other cloud computing provider. Just install the agent and it's ready.

Continuous Integration CI also available in `GITHUB ACTION`_.

.. _YouTube: https://www.youtube.com/watch?v=a1tWj3ytVSQ
.. _GITHUB ACTION: https://github.com/mdsanima/mdsanima/actions