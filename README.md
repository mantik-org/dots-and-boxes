# Dots And Boxes
[![Build Status](https://travis-ci.com/ai-namp/dots-and-boxes.svg?branch=main)](https://travis-ci.com/ai-namp/dots-and-boxes)
[![License: GPL](https://img.shields.io/badge/License-GPL-blue.svg)](/LICENSE) 

:game_die: **Online demo**: [HERE](https://dots-and-boxes-ai-namp.herokuapp.com/)  

Pencil-and-paper game for two players.  

## Description
The game starts with an empty grid of dots. Usually two players take turns adding a single horizontal or vertical line between two unjoined adjacent dots. A player who completes the fourth side of a 1×1 box earns one point and takes another turn. (A point is typically recorded by placing a mark that identifies the player in the box, such as an initial.) The game ends when no more lines can be placed. The winner is the player with the most points. The board may be of any size grid. When short on time, or to learn the game, a 2×2 board (3×3 dots) is suitable. A 5×5 board, on the other hand, is good for experts.

![Screenshot](/docs/images/screen01.png)

## Sources
In this project, artificial intelligence was supported by [DLV](https://dlv.demacs.unical.it/).  
DLV is an Answer Set Programming system, based on disjunctive logic programming, which offers front-ends to several advanced KR formalisms. The system supports a language based on a logical formalisms with a very high expressive power so that programs are able to represent relevant practical problems in presence of incomplete or contradictory knowledge.  

Notable sources are:
- **Player Agent**, [asp/player.asp](https://github.com/ai-namp/dots-and-boxes/blob/main/src/asp/player.asp) AI for calculate next move to get best score.
- **Phase Detector**, [asp/phase.asp](https://github.com/ai-namp/dots-and-boxes/blob/main/src/asp/phase.asp) detect and store status about current phase game.
- **Chains/Cycles Detector**, [asp/chain.asp](https://github.com/ai-namp/dots-and-boxes/blob/main/src/asp/chain.asp) detect all chains and cycle inside the current board state.


## Build

To run Dots And Boxes, execute the following command:
```shell script
make init
make run-server &
make run
```
**NOTE:** Building and running require [Python 3.x.x](https://www.python.org/) or greater.

## Run
Open your web browser on http://localhost:8080 after successful build.


## Third-Party Software
Dots And Boxes uses and depends on third-party open-source tools and libraries which are outside of this repository.
## License

Copyright (c) AI Namp. All rights reserved.

Licensed under the [GPL](/LICENSE) license.

