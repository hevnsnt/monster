# Monster in a Box 
###### OpenSource Scares by hevnsnt


<pre>
          Controlling a
           _   .-')                     .-') _   .-')    .-') _     ('-.  _  .-')   
          ( '.( OO )_       v1.0      ( OO ) ) ( OO ). (  OO) )  _(  OO)( \( -O )  
           ,--.   ,--.).-'),-----. ,--./ ,--,' (_)---\_)/     '._(,------.,------.  
           |   `.'   |( OO'  .-.  '|   \ |  |\ /    _ | |'--...__)|  .---'|   /`. ' 
           |         |/   |  | |  ||    \|  | )\  :` `. '--.  .--'|  |    |  /  | | 
           |  |'.'|  |\_) |  |\|  ||  .     |/  '..`''.)   |  |  (|  '--. |  |_.' | 
           |  |   |  |  \ |  | |  ||  |\    |  .-._)   \   |  |   |  .--' |  .  '.' 
           |  |   |  |   `'  '-'  '|  | \   |  \       /   |  |   |  `---.|  |\  \  
           `--'   `--'     `-----' `--'  `--'   `-----'    `--'   `------'`--' '--' 
                                                                           IN A BOX          
</pre>


A RaspberryPi based Halloween prop that is guaranteed to scare the costumes off Trick or Treaters and make your house the favorite haunt of the neighborhood

This fully open-source project creates a "Monster in a Box" Halloween prop, a fully animated box that appears to be jailing a monster which is on the verge of escaping.

In order to replicate the MVP (v0.0.1) you will need to have prior experience with RaspberryPi, Python, 3d Printing, and some basic electronic component knowledge. However I am expecting to continue with this project and release a more complete project for the general public by Halloween 2019.


## Parts List:
<pre>
* RaspberryPi 3 B+       : http://a.co/d/8gMNQvR  ($34.99) 
* 32Gb SD Card           : http://a.co/d/ikK2kIr  ($8.99)
* 4 Chan 5V Relay Module : http://a.co/d/eE9fITI  ($7.86)
* 2x Door Lock Actuators : http://a.co/d/ic8SmtQ  ($9.57)
* Powered Speakers       : http://a.co/d/2sLVZjJ  ($10.99) --  Not required, but you should!
* Fog Machine            : http://a.co/d/7cQjDfj  ($35.99) --  Not required, makes it seriously awesome!
* Pallet Box (DIY)       : https://bit.ly/2C0RcVe
</pre>

*Note: Previous versions of RaspberryPis will likely work fine, but please check for GPIO changes!*

## Release History:

* 0.0.1
    * MVP -- 2018 Halloween. RaspberryPi based; mainly because that is what I have on hand. Future verisons will likely be ESP32 based in order to reduce cost and fit within the Hallowuino framework.

## To Do:
* Everything! Literally nothing is done!
	* Relay 1: Lid Lifter
	* Relay 2: Box Lifter
	* Relay 3: Smoke Machine
	* Relay 4: --

## Schematics:


## Meta:
Created by: Bill Swearingen – [@hevnsnt](https://twitter.com/hevnsnt) – bill@seckc.org

Distributed under the GNU General Public License v3.0. See ``LICENSE`` for more information.

For my other projects, please see [https://github.com/hevnsnt/](https://github.com/hevnsnt/)

## Contributing:
I love contributors! Please help out this project by replacing my crappy code with good code!

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Inspiration & Stolen Code:
* craig jameson
	* https://create.arduino.cc/projecthub/craig-jameson/monster-in-a-box-41cc38
* skiwithpete
	* https://github.com/skiwithpete/relaypi
    * https://www.youtube.com/watch?v=OQyntQLazMU
* jarame
	* https://www.instructables.com/id/Monster-In-A-Box-Halloween-Prop-Part-1-The-Box-or-/
    * https://www.instructables.com/id/Monster-In-A-Box-Halloween-Prop-Part-2-The-Guts/
* Fritzing
	* http://fritzing.org/home/
* Fritzing Relay Parts
	* https://timgolisch.wordpress.com/2015/09/12/fritzing-4-channel-relay-part/
    * https://timgolisch.wordpress.com/2015/02/22/fritzing-2-channel-relay-part/
