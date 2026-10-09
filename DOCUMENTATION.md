# PhotoCraft — Living Documentation

> This document describes the current state of the project. It is maintained
> by the `docs-sync` skill and contains no history.

## Overview

PhotoCraft is a Rust image editor with a native desktop interface, a WebAssembly
frontend and a headless CLI. Its document model represents layers, masks,
adjustments, text, shapes and smart objects, with PSD import/export and a native
`.pcraft` format.

## Business Rules

1. Editing actions dispatch engine commands shared by the UI, CLI and automation
   interfaces. Pure view and window state belongs to the UI shell.
2. Pixel depth and colour model are document data; colour conversions use the
   colour-management layer.
3. Closing, reverting or quitting with unsaved documents requires confirmation.
   Pending confirmations track document ids rather than tab positions.
4. The macOS unsaved-changes prompt displays Save, Don't Save and Cancel without
   visible letter mnemonics. S and Return save, D discards, and C or Escape cancel.
   Tab focuses buttons, and Return activates a focused button. Windows and Linux
   use Yes, No and Cancel with visible Y/N mnemonics.
5. A cancelled or failed save leaves the unsaved-changes prompt pending. Layered
   TIFF saves wait for TIFF Options and a successful document save.

## Architecture

### Components

The Cargo workspace separates geometry, colour management and tiled raster
storage from the document model, editing algorithms, history, compositors and
file handling. `photocraft-engine` exposes sessions and a command registry;
`photocraft-ui-egui` provides the egui shell. The desktop app uses eframe/wgpu,
and the browser app compiles Rust to WebAssembly. See [architecture](docs/architecture.md).

### Data Flow

Frontends dispatch commands through the engine session. Document snapshots share
copy-on-write tiles, editing operations record history, and compositors produce
the image. I/O translates documents to supported external formats or the native
bundle. The UI parks destructive close actions while save confirmations run.

### Integrations

The headless MCP server and authenticated desktop control channel expose editing
and inspection to agents. Platform services supply file dialogs and file writes
to the UI. Contributor statistics and opt-in profile names are compiled into the
About window from `contributors/contributors.json` and `contributors/people.toml`.

## Gotchas & Pitfalls

- Menu wiring coverage does not establish behavioural or file-format fidelity;
  the [scorecard](docs/scorecard.md) tracks separate measurements.
- Pending save confirmations can outlive tab reordering or asynchronous file
  dialogs, so they identify their target by document id.
- Displayed shortcut mnemonics and keyboard handling are separate concerns:
  macOS save buttons have plain labels while retaining their letter shortcuts.
