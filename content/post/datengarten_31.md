---
title: "Datengarten 31"
subtitle: "Dem Compiler beim Optimieren zuschauen"
date: 2009-06-25T00:00:00+02:00
event_date: 2009-06-25T20:00:00+02:00
location: CCCB
speaker: hannes
language: Deutsch
streaming: false
---
{{< datengarten-infobox >}}

**A tool for debugging compiler optimizations and type inference** (in
deutscher Sprache)

Abstract
--------

The focus of this talk will be type theory (type system and type
inference), applied to a dynamic language (Slides of a previous talk are
\[6\]). A side-effect during working on this topic was the development
of a visualization tool:

This tool is a Java application which visualizes the control and data
flow graph of the intermediate representation of Open Dylan \[1\]
(former DylanWorks, Harlequin Dylan, Functional Developer) and animates
optimizations. The Open Dylan compiler was extended with hooks to send
control flow and data flow changes via TCP/IP to the Java application.
The justification why the visualization is in Java is because I couldn't
find a decent graph layouting and animation library with an API. The
graph library used is yFiles \[2\]. The Java code \[3\] consists of 2000
lines of code, the compiler hooks were about 250 lines of code.
Interactive application can be viewed at \[5\]. The communication
protocol in use are S-expressions, in the same marshalling format as
swank (the slime backend protocol).

An example for this work is a visualized map(method(x) x end, \#(1)),
available at \[4\] (data flow nodes and edges are pink).

Links
-----

1. <http://www.opendylan.org/>
2. <http://www.yworks.com/en/products_yfiles_about.html>
3. <http://www.opendylan.org/cgi-bin/viewvc.cgi/branches/opendylan-visualization/FlowGraphVisualization/src/>
4. <http://www.opendylan.org/~hannes/yworks/test4.avi>
5. <http://visualization.dylan-user.org/>
6. <http://www.opendylan.org/~hannes/ph-neutral.pdf>

