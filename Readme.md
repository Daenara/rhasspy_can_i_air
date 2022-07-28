This is just a small rhasspy skill that answers the question if I can open the window based on the difference of the 
outside temperature and the one in the room asked. The temperatures are provided via mqtt and the room names send by rhasspy 
match the ones used for the temperatures.

It can be used by others, but to do so, you have to edit the code directly, and with how simple this is, you might be 
faster just writing it yourself.

Rhasspy sentences:
```
[CanIAir]
Kann ich das [$rooms {room}]Fenster (öffnen | auf machen)
Kann ich [im | bei | das | den] $rooms {room} (lüften | das Fenster öffnen)
```
The sentences use a slot file named rooms that you have to create also, if you want to use this. 