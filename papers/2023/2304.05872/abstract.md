---
title: Learning to Communicate and Collaborate in a Competitive Multi-Agent Setup to Clean the Ocean from Macroplastics
arXiv: 2304.05872
authors:
- Philipp D. Siedler
year: 2023
source: arXiv
venue: ICLR Workshop
difficulty: ★★★☆☆
importance: ★★★☆☆
read_status: deep_read
method_tags:
- Multi-Agent_RL
- Graph_Neural_Network
- Communication
- PPO
- MARL
application_tags:
- Ocean_Plastic
- Marine_Litter
- Multi-Agent_Systems
- Autonomous_Cleaning
- Environmental_AI
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Learning to Communicate and Collaborate in a Competitive Multi-Agent Setup to Clean the Ocean from Macroplastics

## TL;DR
MARL with GNN communication layer enables ocean plastic cleanup vessels to develop emergent communication protocol achieving 34% higher rewards.

## Research Question
How can multi-agent reinforcement learning with communication enable autonomous vessels to collaborate effectively for ocean macroplastic cleanup?

## Main Contributions
1. Proposes GNN-based dynamic communication layer enabling agents to develop emergent communication protocol via binary signals
2. Rewards weakest link in agent collective (global reward = worst performer * 0.01) to incentivize collaboration
3. Demonstrates 34% cumulative reward improvement and 41% global reward improvement through learned communication

## Method
MARL with PPO (Proximal Policy Optimization) algorithm. 3 vessels in Unity physics-based environment (200m x 200m). GNN message passing on dynamic network (100m connectivity threshold). Observation space: visual (25x25 satellite-like grid) + vector (position, velocity, neighbor position, signal). Continuous actions (thrust, rotation) + discrete signal action (binary). 2D Perlin noise for garbage distribution.

## Datasets
- Custom Unity simulation mimicking Great Pacific Garbage Patch
- 50m x 50m visual observation grid (2m cells) per agent
- 5000 steps per episode
- Training: seeds 0-99, Testing: seeds 0-9 with y-shift 200
- 20M total training steps

## Core Results
- MAC (with communication): 606.27 cumulative reward vs MA (no communication): 400.67
- 34% improvement in cumulative reward with communication
- 24% local reward improvement, 41% global reward improvement
- Agents developed follow (signal 0) and move-away (signal 1) communication protocol
- Episode length increased from 114 to 209 steps (longer survival with coordination)

## Limitations
- Small environment (200m x 200m) vs GPGP (1.6 million sq km)
- Only 3 agents vs fleet-scale operations needed for real ocean
- Synthetic garbage distribution (Perlin noise) vs real satellite data
- Fixed 100m communication range
- Single garbage type (buoyant plastic pebbles)

## Research Gaps
- Scaling to larger environments and more agents
- Integration with real satellite data for garbage mapping
- Real-world autonomous vessel communication systems
- Multi-type debris (sinking, entangled, microplastics)
- Weather and current adaptation
- Real ocean current modeling for realistic plastic drift
