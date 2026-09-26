# Integrated candidate: argument and remaining obligations

**Status: unverified, not an accepted reduction.** The command is
`algorithm.py`; its component implementations remain in rounds 022–040.
No solver is called by either command mode. This document separates the proved
graph step and conditional picture argument from the outstanding acceptance
obligations. It does not claim that finite gadget checks prove global correctness.

## Source to a graph of maximum degree three

For a variable with t occurrences, create an alternating cycle with 2t vertices,
one even/odd pair per occurrence. For t=1 use its single undirected edge; omit
variables with no occurrences. For each clause create a triangle, and connect
each of its vertices to the even occurrence vertex for a positive literal or the
odd occurrence vertex for a negative literal. Repetitions and tautologies need
no special treatment: each occurrence has its own pair. There are 9m vertices,
at most 27m/2 edges, and maximum degree three for m clauses. Use budget 5m.
The clause-by-clause renumbering in `rounds/040/graph.py` is an isomorphism.

Each variable cycle needs at least t vertices in a cover and each clause
triangle at least two, so any cover of size at most 5m meets every lower bound
exactly. A minimum cover of an even cycle consists of one parity class: its
complement is an independent set of half the cycle, and each cyclic gap must
then be exactly two. The single-edge case also has exactly the two parity
choices. Read true from selection of the even class. The unselected vertex of
each clause triangle has its attached occurrence vertex selected, so that
literal is true. This recovers a satisfying assignment from every graph cover
within budget. Unused variables may be set false.

Conversely, select the parity representing a satisfying assignment, and in
each triangle leave out one vertex corresponding to a true literal. This is a
cover of size 5m. Thus the graph equivalence and decoder are unconditional.
An independent SAT solver checked all 120 prepared sources and recovered 212
graph covers; this supports the implementation, not the general proof itself.

## Picture construction and local counts

`rounds/040/picture.py` gives exact integer coordinates through `graph_layout`,
then rank-compresses their rectangle union and materializes the binary matrix.
For q incidence tracks it uses pitch 100(q+1)^2+1. Sources occupy disjoint
horizontal intervals and successive row bands; all their outgoing beam columns
are separated by at least the pitch. Nonbeam columns are duplicated to obtain
this separation. The routing permutation groups each edge's two incidences in
adjacent parked positions. A right-wing translator on the left incidence
prepares its attachment to a terminal. The terminal's nonbeam middle column is
duplicated to span the remaining distance. Every module is in a new row band;
its input strips extend back to its producers. The empty graph gives an empty
matrix with budget zero for source instances.

The local bounds used are:

| Module | Exact local rectangle count |
|---|---|
| Degree-d source, 1≤d≤3 | 9d+8 plus one if any output is selected |
| Translator | 16 plus one for a selected output without supplied input |
| Swap | 46 plus the number of selected outputs without their corresponding inputs |
| Terminal | 5 plus one if neither input is supplied |

See [source](source-lemma.md), [terminal](terminal-lemma.md), and
[routing](routing-lemma.md) lemmas for templates, stretching arguments and
directly checkable upper/lower certificates. Let B be the sum of baselines and
set K=B+5m. [Rank compression](rank-compression.md) preserves exact cover counts.

## Conditional all-cover recovery

The remaining global premise is precise: every maximal rectangle in the whole
picture is internal to one module or is one designated beam meeting just its
producer and consumer. Its restrictions must equal the stipulated local output
rectangle and supplied input strip. All source and terminal attachments, and
arbitrarily many intervening idle strips, must satisfy that premise together.
The routing invariant addresses the routing interior. Three complete small
graph pictures satisfy the premise by exhaustive maximal-rectangle enumeration;
this is not a substitute for an audit of all attachment cases at arbitrary size.

Under that premise, [cut composition](cut-composition.md) proves the following.
Extend each cover rectangle to a maximal legal rectangle, and remove duplicates.
Charge every selected interface to its producer and every internal rectangle to
its module. Select a graph vertex for each activated source; select the known
origin of each routing channel that becomes selected without its incoming
signal; for each terminal with no input select one endpoint. Every edge is
covered: tracing any selected terminal input backwards reaches either an
activated source or a newly created signal of its own endpoint. The other
terminals receive an endpoint explicitly. Deduplication reduces the number of
selected vertices. The local lower bounds give at most |cover|−B≤5m selected
vertices. `recover_cover` implements exactly this procedure and checks the
resulting graph cover, then `recover_graph` recovers the assignment.

For the converse, activate all channels of a graph cover, propagate each through
its routing path, and use matching local upper covers. Every terminal has an
input. Extending each selected output through its interface gives a legal cover
of at most B plus the number of selected vertices. Consequently, under the
global premise, returning NO-SOLUTION unchanged is sound in both directions.
No preferred or minimum target cover is assumed by recovery.

## Encoding, cost, and current limits

There are O(m²) constant-complexity modules and O(m²) rectangle boundary
coordinates per axis. Their integer coordinates have polynomial magnitude in
m. The compressed matrix has O(m⁴) entries. Brute-force maximal-rectangle
enumeration, extension and membership checking are polynomial in this explicit
matrix size; reconstructing metadata from the source uses no hidden process
state. These bounds explain polynomial geometry size; they are not practical
runtime claims. Case 70 in the fixed corpus, with 16 clauses, produces a measured
169485×91539 matrix (15,514,487,415 entries). The bounded renumbering improvement
reduced the initial 134,247,719,259-entry layout, without making verification
feasible. No target-size restriction was added to the question or checker.

There is also a source-encoding qualification. The executable contract permits
a binary integer n with arbitrarily many unused variables, but requires an
explicit Boolean list of length n. This implementation allocates n occurrence
lists and returns n Boolean values even for an empty formula. Its source cost
is polynomial in n+m, not necessarily the bit length of that JSON. This is an
unresolved contract/bit-complexity obligation; the conventional explicit-variable
3SAT theorem does not by itself resolve it. No source domain or output format
has been silently changed, and no impossibility claim about classical rectangle
cover hardness is being made.

Acceptance still requires a complete attachment proof, a bit-length statement
consistent with the fixed source contract, successful prepared end-to-end tests
including nonempty formulas and NO-SOLUTION recovery, and independent review.
The known hardness result remains compatible with all failures in this campaign.
