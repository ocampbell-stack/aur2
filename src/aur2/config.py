DOT_AUR2_CFG = {
    "blacklist": [
        "visions",  # visions/queue, visions/processed, visions/failed are created empty
        "plans",  # plans/queue, plans/processed are created empty
    ],
    "copy_env": True,
}

# Folders to create (with .gitkeep)
DOT_AUR2_FOLDERS = [
    "visions/queue",
    "visions/processed",
    "visions/failed",
    "plans/queue",
    "plans/processed",
]

DOT_CLAUDE_CFG = {}
