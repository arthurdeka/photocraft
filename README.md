# PhotoCraft contribution evidence

UI captures for [#3982](https://github.com/storytold/photocraft/pull/3982) and [#3983](https://github.com/storytold/photocraft/pull/3983), rendered with PhotoCraft's existing offscreen `snapshot` example on synthetic documents.

- Before: upstream `5e0a6d404d3b02b811ea5ba066e9c9d6b661314d`.
- Gradient Map: `fix/2958-gradient-map-handles`, validated in [this run](https://github.com/arthurdeka/photocraft/actions/runs/38211263238).
- Zoom: `fix/3344-status-zoom-wrap`, validated in [this run](https://github.com/arthurdeka/photocraft/actions/runs/38209981717).

The zoom probe supplies a mouse drag at the left logical viewport edge, simulates acknowledgement of any native cursor-position command, and continues the same drag by another 100 points. The JSON files record the resulting percentages and command target. This is automated input evidence, not a physical Windows hardware test.

These captures and the capture instrumentation are hosted separately from the contribution branches. No capture image, snapshot exporter or validation workflow is part of either PR.

License: MIT OR Apache-2.0, like the captured project UI. See the license files.
