# Computer Architecture Final Project: GPU Design and Research
### By Daniel Connolly and Qingmu "Josh" Deng

## Proposal
### Project Overview
In our final project for our computer architecture course, we intend to design and implement in a high level programming language a simulation of the graphics pipeline that is happening on the software side of the Graphics Processing Unit (GPU) of a computer and to explore, on a more broad scale, the operations of GPUs. Our hope is that by creating a simulation of the pipeline in software, we will gain a better understanding of why GPUs are organized as they are and why the GPU schedules operations in the way it does, as this is our main confusion after conducting our initial research as of 11/28/18. We anticipate this will lead us to a deeper understanding of GPUs and how they interact with other elements of a computer.

### References
Our project would take the approach introduced in [Lab 0 of CSE 467: Advanced Digital Design](https://courses.cs.washington.edu/courses/cse467/15wi/docs/prj0.pdf).

In order to develop an understanding of graphics processing units, we will investigate the following resources as well:
- [How a GPU Works from CMU](https://www.cs.cmu.edu/afs/cs/academic/class/15462-f11/www/lec_slides/lec19.pdf)
- [Nvidia Geforce 200 Architecture](https://www.nvidia.com/docs/IO/55506/GeForce_GTX_200_GPU_Technical_Brief.pdf)
- [Data-Level Parallelism in Vector, SIMD, and GPU Architectures](https://app.knovel.com/web/view/khtml/show.v/rcid:kpCAAQAE11/cid:kt00B7Z297/viewerType:khtml//root_slug:41-introduction/url_slug:data-level-introduction?b-toc-cid=kpCAAQAE11&b-toc-root-slug=&b-toc-url-slug=data-level-introduction&b-toc-title=Computer%20Architecture%20-%20A%20Quantitative%20Approach%20(5th%20Edition)&page=2&view=collapsed&zoom=1)
 - [MIAOW GPGPU](https://github.com/VerticalResearchGroup/miaow/wiki/Architecture)
 - [Introduction to Graphics Processing Units](https://app.knovel.com/web/view/khtml/show.v/rcid:kpCODTHS0F/cid:kt010Y88K6/viewerType:khtml//root_slug:computer-organization/url_slug:introduction-graphics?b-q=graphics%20processing%20unit&sort_on=default&b-subscription=true&b-group-by=true&page=26&b-sort-on=default&b-content-type=all_references&b-sort-on=default&b-content-type=all_references&view=collapsed&zoom=1&q=graphics%20processing%20unit)
 - [Nvidia Turing Architecture Whitepaper](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/technologies/turing-architecture/NVIDIA-Turing-Architecture-Whitepaper.pdf)
 - [Introduction to NVIDIA RTX and DirectX Ray Tracing](https://devblogs.nvidia.com/introduction-nvidia-rtx-directx-ray-tracing/)
 - [NVIDIA RTX](https://developer.nvidia.com/rtx)

### Deliverables
In terms of deliverables, we will produce a report demonstrating our level of GPU operation understanding and explaining the purpose and functionality of the graphics pipeline. Additionally, we will produce a codebase that demonstrates the process by which the graphics pipeline renders graphics and the GPU performs calculations in order to render those graphics. We will describe our software simulation in the report as well.
##### Minimum
Our minimum deliverable will be a report detailing the algorithms we would employ over the graphics pipeline to convert vertices to pixels on a screen and what we have learned from the process.
##### Planned
We hope to create a software simulation of the graphics pipeline that demonstrates in real time the edits and transformations that are happening. The report will include a section on how modern GPU architecture utilize such operations on a high level as well as providing more detail about individual parts of the whole GPU and how they interact.
##### Stretch
As a stretch goal, we may try to design and implement a simplified version of some components of or an entire GPU in Verilog that can handle and render files as our simulation does.

### Work Plan
11/29/18 - Finish initial research and begin to work on pipeline simulation

12/2/18 - Continue more in-depth research, begin writing report, and continue work on pipeline simulation

12/5/18 - Finish first draft of report, finish first pass at simulation, work on documentation

12/8/18 - Complete simulation implementation

12/9/18 - Finish documentation

12/10/18 - Finish report, work on poster or demo

12/11/18 - Finish poster/demo
