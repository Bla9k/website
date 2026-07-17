# GIVEN

GIVEN is a Ren'Py visual novel project.

## Project metadata

- **Game title:** GIVEN
- **Package/build name:** `given`
- **Engine:** Ren'Py
- **Primary script directory:** `game/`

## Repository layout

```text
.
├── game/              # Ren'Py game scripts and assets
│   ├── script.rpy     # Entry point for the visual novel
│   ├── options.rpy    # Project metadata and build configuration
│   ├── gui.rpy        # GUI defaults for the project
│   ├── images/        # Character sprites, backgrounds, CGs
│   ├── audio/         # Music and sound effects
│   └── gui/           # GUI image assets
├── docs/              # Design notes and production documentation
├── builds/            # Local Ren'Py build output (ignored by Git)
├── exports/           # Distribution/export staging (ignored by Git)
└── saves/             # Local save data (ignored by Git)
```

## Development

1. Install Ren'Py from <https://www.renpy.org/>.
2. Open this repository from the Ren'Py launcher.
3. Launch the project named **GIVEN**.
4. Edit files in `game/` to implement scenes, characters, UI, and assets.

## Building

Use the Ren'Py launcher to create distributions. Generated packages should be written to `builds/` or `exports/`; those directories are intentionally ignored so release artifacts do not enter source control.
