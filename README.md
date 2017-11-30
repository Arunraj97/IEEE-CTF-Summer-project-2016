# Jellyfish-Topology-Helper

Implementation of Jellyfish Topology in ns-3

## Introduction

Jellyfish, a high-capacity network interconnect which, by adopting a random graph topology, yields itself
naturally to incremental expansion. In this project we develop a topology helper for Jellyfish (like Dumbbell topology helper) in ns-3 


## Running the code

The helper file is at ``` src/point-to-point-layout/model/jellyfish_topology_helper.cc  ```

The example file is at ``` scratch/jellyfish-animation.cc ```

To run the code type the following in the terminal 

```
./waf --run "scratch/jellyfish-animation --N=<value> --K=<vlaue> --R=<value>"
```

## References

* [Paper](https://people.inf.ethz.ch/asingla/papers/jellyfish-nsdi12.pdf) 
* [Dumbbell Helper](https://www.nsnam.org/doxygen/classns3_1_1_point_to_point_dumbbell_helper.html)


