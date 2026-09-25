# Staircase endpoint coupling does not transmit a phase

## Claim and applicability

Tags: variable gadget, rectangle cover, staircase wire, phase propagation. A five-cell diagonal staircase has two minimum covers after maximalizing rectangles, but joining two copies at one endpoint creates a nine-cell staircase with four minimum maximal covers at the tight budget. This rules out the specific endpoint-sharing join as a binary equality wire. It says nothing about other joins or auxiliary cells.

## Evidence and status

Finite exhaustive maximal-rectangle enumeration and independent target-oracle checks: [round 005](../../campaigns/three-sat-rectilinear-picture-compression/rounds/005/round.md), `composition_probe.py`. The local tile also permits a singleton center rectangle in an arbitrary legal witness. Not independently reviewed.

## Consequence for search

Do not infer global assignment consistency from a local two-cover tile. Count all legal target covers and test propagation before scaling.

## Use history

Created 2026-09-25 in round 005. [Round 006](../../campaigns/three-sat-rectilinear-picture-compression/rounds/006/round.md) used the warning to require two phases differing in more than one rectangle; the 4×4 family had no such tile. Intended board promotion is pending; the board was not edited.
