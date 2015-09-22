CHANGE LOG
----------
*v1.1*
***
_Broken pipe and tcp client faliure fixed. Serial is implemented next._
* Fixed broken pipe error on tcp. 
* Fixed client is not listening (removed `socket.listen()`). (Client doesn't write to Serial yet.)
* Rewritten Tcp server and client.
* All Python software not is for version **2.7** and not **3**. See "System Requirements" in the wiki.
* Serial support with `pyserial`.
