# Live Bead Treadmill

## Vision
A continuously running bead graph where high-level beads automatically refine into implementable sub-beads as they approach the "now" window. Like a planning horizon that sharpens over time.

## Key Ideas
- Beads start as fuzzy visions (P4, one-line title, no plan)
- As priority increases or time approaches, auto-run `aura.scope` to decompose into sub-beads
- Sub-beads get dependencies via `bd dep add`
- `aura.execute` picks up ready sub-beads and implements them
- The treadmill is just a cron/loop: find highest-priority unscoped bead, scope it, repeat

## Reality Check
- This is optimization on top of a workflow that hasn't been validated manually yet
- The "refine a bead" step IS `aura.scope` — if that skill isn't reliable, automation just produces bad decompositions at scale
- Do the manual version first: create high-level beads, scope them by hand, execute them, then automate

## Depends On
- Reliable scope skill (proven over 5-10 real runs)
- Reliable execute skill
- Programmatic agent invocation (`aura run`)
