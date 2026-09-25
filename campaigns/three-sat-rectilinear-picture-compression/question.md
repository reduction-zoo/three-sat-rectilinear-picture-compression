# Fixed question

```json
{
  "source": "3-SAT",
  "target": "Rectilinear picture compression",
  "category": "Construction open",
  "summary": "The task reconstructs a usable hardness rule for lossless rectangle-based representation of binary images.",
  "source_definition": "A Boolean CNF formula with three literals per clause is given explicitly. Return a satisfying truth assignment. Return NO-SOLUTION exactly when no such witness exists. Graphs, families and strings are explicit; numerical parameters use binary encodings.",
  "target_definition": "Given a binary matrix and K, return at most K axis-aligned rectangles with integer row and column endpoints whose union is exactly the matrix's one entries. A valid output is a witness satisfying these conditions, or NO-SOLUTION exactly when none exists.",
  "required_result": "Construct deterministic polynomial-time maps F and G. F must produce a legal target instance, and G(x,y) must return a valid source output for every valid target output y, including NO-SOLUTION. A complete rule may reconstruct a published construction or give a new one; it must specify every gadget, numerical parameter and decoding step.",
  "acceptance": "Deliver executable instance construction and output recovery, a general proof covering all legal inputs and target outputs, and worst-case polynomial time and encoding-size bounds. Cite the actual proof used, or identify a newly derived argument. Check small positive and negative instances with independent solvers; finite tests alone do not establish correctness.",
  "importance": "The task reconstructs a usable hardness rule for lossless rectangle-based representation of binary images.",
  "difficulty": "Difficulty is not yet established by a construction attempt. Every gadget needs a concrete binary pattern. Unintended rectangles crossing gadget boundaries must be excluded, and the exact rectangle budget proved.",
  "openness": "This is a rule-completion task from the imported catalog. The requested contribution is a complete, reproducible construction, proof and implementation; the existing hardness attribution is not presented as an unsolved complexity classification. The references are leads to check, not a verified solution.",
  "literature_checked": "2026-09-18",
  "coverage": "Import inventory review of the cited sources. Primary proofs have not been independently re-audited; availability of a complete reconstruction elsewhere remains unassessed.",
  "references": [
    {
      "title": "Problem-Reductions: 3-SAT \u2192 Rectilinear picture compression",
      "url": "https://github.com/CodingThrust/problem-reductions/issues/458",
      "note": "Upstream task and discussion checked on 2026-09-18. Reported reference: Garey & Johnson, *Computers and Intractability*, Appendix A4.2, p.232"
    }
  ],
  "solutions": [],
  "equation": ""
}
```
