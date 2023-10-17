# Physics-Simulations
This repository is based on how you can develop physics simulations using pygame and pymunk library

* Pygame is typically used for developing 2D games using Python programming language basically used for visualization.
* Pymunk is used for 2D physics simulation using Python programming language this is used for calculating the physics. 

### Pymunk

* Initially this requires a <B><I>space</I></B> where to calculate all the physics calculation happens this is like our own universe with our own physical laws.
  
  * In this space we have a physical law which is gravity and also we need to keep in mind that we should be continuously keep on updating the simulations.

* Then we create a physical object where the physical simulations are applied to it named as <B><I>body</I></B>. There are two different types of physical body.

  * Static Body : A body that doesn't move but other bodies can collide with it.
  * Dynamic Body : A body that can be moved by physics simulations.
  * Kinematic Body: A body that can be moved by the player (or other non-physical code).

* Dynamic body we need three different arguments <B>Mass</B> (weight), <B>Inertia</B> (To resist change in its state of motion), <B>body_type</B> (what body type we want).

