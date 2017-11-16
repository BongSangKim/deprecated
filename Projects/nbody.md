# Requirements for N Body Simulation

## Note

This document is a *draft* version and will be updated. Please visit this page often to see if there is any update.

For those who are working on N body simulator, refer this document as a base of requirements of your N body simulator.

For those who are woking on the project of their own choice, please refer this document to see the scope/complexity/interfaces of the expected projects.

## Overview

This requirement shows what features should be implemented for N body simulation and how the simulator interact with users. The simulator takes text inputs from user and executes them.

## Commands

All commands are composed of two letters; the first letter indicates an action, and the second the kinds/types of objects.

The action letters include
- `p`: print
- `a`: add
- `d`: delete
- `c`: configure
- `r`: run
- `q`: quit

The second letters include
- `a`: all
- `p`: particle
- `s`: set
- `m`: memory
- `f`: force


### Print commands

- `pa`: print information about all the particles
- `pp <particle>`: print information of particle `<particle>`
- `ps <set>`: print information of set `<set>`
- `pf`: print information of forces
- `pt`: print the current time (in seconds)
- `pm`: print memory usage, i.e., the number of particles, sets and forces
- `pg`: print whether gravity is enabled

### Add commands

- `ap <particle> <mass> <x> <y> <v_x> <v_y>`: Add a particle `<particle>` with given mass and initial x, y location and x, y speed, i.e., initial location is given as a vector `(<x>, <y>)` and initial velocity is given as a vector `(<v_x>, <v_y>)`
- `as <set>`: add a set `<set>`
- `ae <set> <particle>`: add a particle `<particle>` to a set `<set>`
- `af <force> <set> <x> <y>`: add a force `<force>`, which is imposed on the particles in set `<set>` whose size is given as a vector `(<x>, <y>)`

### Delete commands

- `dp <particle>`: delete particle `<particle>`
- `de <set> <particle>`: delete particle `<particle>` from set `<set>`. Note that this does not delete particle, but remove a particle from a set
- `df <force>`: delete force `<force>`
- `da`: delete all particles, sets and forces

### Configure commands

- `ct <tick>`: change timetick (in seconds)
- `cg <bool>`: enable gravity if `<bool>` is "true", and disable gravity if `<bool>` is "false"
- `cp <particle> <bool>`: fix or unfix the location of particle `<particle>`, depending on `<bool>`

### Run commands

- `ru <duration>`: run the simulation for `<duration>` seconds
- `rv <duration>`: run the simulation for `<duration>` seconds and print out the location of each particle (x and y coordinates) at each tick

### Quit commands

- `qq`
  - stop the simulation
  - delete all the particles, sets and forces
  - print memory

### Run commands

### Quit commands




## Examples

### Proper input (w/o errors)

```
Enter a command: pa
No particles

Enter a command: pg
Gravity is active now

Enter a command: pm
Particles: 0
Sets: 0
Forces: 0

Enter a command: pt
Current time is 0

Enter a command: ap 0 1.9890e+30 0 0 0 0
Particle 0 added

Enter a command: ap 1 5.9740e+24 1.4960e+11 0.0000e+00 0.0000e+00 2.9800e+04
Particle 1 added

Enter a command: pp 0
Particle: 0
  Location: (0,0)
  Velocity: (0,0)

Enter a command: pp 1
Particle: 1
  Location: (1.496e+11,0)
  Velocity: (0,29800)

Enter a command: pa
Particle: 0
  Location: (0,0)
  Velocity: (0,0)
Particle: 1
  Location: (1.496e+11,0)
  Velocity: (0,29800)

Enter a command: as 1
Set 1 added

Enter a command: ae 1 0
Particle 0 added to set 1

Enter a command: ae 1 1
Particle 1 added to set 1

Enter a command: ps 1
--- Set 1 ---
Particle: 0
  Location: (0,0)
  Velocity: (0,0)
Particle: 1
  Location: (1.496e+11,0)
  Velocity: (0,29800)

Enter a command: pm
Particles: 2
Sets: 1
Forces: 0

Enter a command: af 1 1 1.5 2.5
Force 1 added

Enter a command: pf 1
Force 1 applied to set 1: (1.5,2.5)

Enter a command: ct 3600

Enter a command: cg false
Gravity disabled

Enter a command: cg true
Gravity enabled

Enter a command: cp 0 true
Particle 0 is set to fixed

Enter a command: cp 1 false
Particle is set to movable

Enter a command: de 1 1
Particle 1 deleted from set 1

Enter a command: ps 1
--- Set 1 ---
Particle: 0
  Location: (0,0)
  Velocity: (0,0)

Enter a command: dp 1
Particle 1 deleted

Enter a command: df 1
Force 1 deleted

Enter a command: pa
Particle: 0
  Location: (0,0)
  Velocity: (0,0)
Particle: 1
  Location: (1.496e+11,0)
  Velocity: (0,29800)

Enter a command: da
All force deleted
All sets deleted
All particles deleted

Enter a command: pa
No particles

Enter a command: qq
All force deleted
All sets deleted
All particles deleted
Particles: 0
Sets: 0
Forces: 0
Done
```

### Error input

*to be added*

```

```
