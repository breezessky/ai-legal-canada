# Skill: /legal compare

## Purpose
Side-by-side comparison of two contract versions. Flags additions, removals, and dangerous changes under Canadian law.

## Trigger
`/legal compare <file1> <file2>`

## Process
1. Parse both documents
2. Align clauses by section heading and content similarity
3. Identify: Added clauses, Removed clauses, Modified clauses
4. For each change, assess: Did this improve or worsen your position under Canadian law?

## Output Format

```
═══════════════════════════════════════════════════
  CONTRACT COMPARISON REPORT
  Version A vs Version B | Jurisdiction: [Province]
═══════════════════════════════════════════════════

SUMMARY OF CHANGES
  ✅ Improvements:  [n] clauses improved in your favour
  ⚠️  Neutral:      [n] clauses unchanged or minor edits
  🔴 Regressions:  [n] clauses worsened — review urgently

─────────────────────────────────────────────────
CLAUSE CHANGES
─────────────────────────────────────────────────

[CLAUSE NAME]
  Change Type: 🆕 ADDED / ❌ REMOVED / ✏️ MODIFIED
  Impact:      🔴 WORSE / 🟡 NEUTRAL / ✅ BETTER
  Version A:   [Original text summary]
  Version B:   [New text summary]
  Canadian Law Note: [How this affects you under Canadian law]
  Action Required:   [What to do about it]

─────────────────────────────────────────────────
CRITICAL REGRESSIONS — ACT IMMEDIATELY
─────────────────────────────────────────────────
[List only the highest-risk changes that need immediate attention]

─────────────────────────────────────────────────
DISCLAIMER
─────────────────────────────────────────────────
This comparison is for informational purposes only.
Consult a licensed Canadian lawyer before signing.
═══════════════════════════════════════════════════
```
