# Executable contract

Source JSON is `{ "n": nonnegative integer, "clauses": [[signed integer, signed integer, signed integer], ...] }`. Literals have nonzero absolute value at most `n`; repeated literals and tautological clauses are legal. An empty clause list is legal. A source output is a Boolean list of length `n`, or the JSON string `"NO-SOLUTION"` exactly when the formula has no satisfying assignment. The list is ordered by variable number.

Target JSON is `{ "matrix": [[0 or 1, ...], ...], "K": nonnegative integer }`. Rows must have equal width; the empty matrix has width zero. A target output is a list of rectangles `[first_row, last_row, first_column, last_column]` with inclusive zero-based endpoints, or `"NO-SOLUTION"` exactly when no cover of at most `K` rectangles exists. Empty rectangle lists cover all-zero matrices. Every rectangle must be nonempty, in bounds, and contain only ones. Their union must be exactly the one entries.

`algorithm.py` reads one source JSON on standard input and writes one target JSON on standard output. `algorithm.py --extract` reads `{ "source": source, "target_solution": target_output }` and writes a source output. Both invocations are independent processes. Diagnostics go to standard error; execution errors exit nonzero. The independent checker validates each output against the definitions above.
