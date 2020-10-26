This project is used to integrate Reveal(x) with AT&T Cyber Security's Open Threat Exchange (OTX) API.  
The Notebook will connect to a specific OTX Pulse and import the Observables into the ExtraHop Memcached.  From there transactions that are relevant to the observables (Domains, URLs, IP Addresses) can be used to check against future transactions to see if there are any matches. 

The trigger included highlights the events that you need to select to make the trigger work.  

Also note, as this is using the Session table (Memcached) it is volitile so a capture restart or firmware patching as well as regular FIFO priorities are in play.  You have a little over 30,000 entries you can use in the Session table (this CAN be increased but isn't supported) so if you have something with over 10's of thousands of observables, use the STIX feature.  
