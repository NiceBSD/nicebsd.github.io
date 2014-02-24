Technical Goals
###############
:date: 2014-02-23

Design requirements
===================

Full rebuild should take less than 10 minutes on modest hardware
----------------------------------------------------------------

Slow compilation leads to slow development. The tools necessary to do this
exist, but we aren’t using them yet. It’s much easier to test deep and
wide-ranging bugs when a system build takes the time to make a pot of coffee.

1 million LOC limit (excluding hardware drivers) for full system
----------------------------------------------------------------

It should be possible for a reasonably dedicated person to audit the entire
base system in under 2 years, assuming 2,000 LOC/day (500 days)

Code should allow for reuse outside of NiceBSD
----------------------------------------------

While NiceBSD should be a usable system, the aim is to "raise all ships" with
its codebase.

Loose Roadmap
=============

Start with FreeBSD codebase
---------------------------

We’ll want to start with a working codebase, so that off the bat the system is
usable. While NiceBSD aims to be a test bed for new approaches to systems
programming, it should be useful, able to bootstrap itself, "production-ready"

Port core userland code to Go
-----------------------------

In order to have the succinctness and compilation speed requirements, we have
to look beyond a world written in C code. Yes, C is a lingua franca, but the
cost for its speed is simply too high given the alternatives. Given the
increase in speed of processors since 1972, and the rise of multiprocessor
systems, this isn’t as ridiculous proposal as one may think

Replace GNU code with BSD alternatives (full BSD/MIT/Public Domain codebase)
----------------------------------------------------------------------------

In order to "raise all ships", the code should allow for simple inclusion in
other systems and projects. A BSD/MIT/PD license allows for this, with minimal
headaches downstream.
