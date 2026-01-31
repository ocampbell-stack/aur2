# Hands-Off Development

## Vision
The user architects at a high level — writing 3-4 visions per day — and agents implement without monitoring. The user never reads code. This is the end-state that all other visions feed into.

## Pipeline
```
User writes vision (voice memo, text, github issue)
  → aura.scope decomposes into plan + sub-beads
  → aura.execute implements each sub-bead on a branch
  → commits accumulate, PR is created
  → user reviews PR summary (not code)
```

## What Must Be True First
1. Skills produce reliable output (scope gives good plans, execute gives working code)
2. Git workflow is baked into skills (branching, commits, PRs automatic)
3. Programmatic invocation works (`aura run` / `aura chain`)
4. Error handling exists (failures don't silently produce broken code)

## Sequence to Get There
1. **Now**: Test scope + execute interactively, fix skill prompts through repetition
2. **Next**: Add git instructions to skills, dogfood on real features
3. **Then**: Build `aura run` CLI command for programmatic invocation
4. **Finally**: Chain it all together, add triggers (cron, webhook, voice memo)

## Anti-Pattern to Avoid
Automating unreliable skills gives automated unreliable output at scale. Each layer must be proven before adding the next.
