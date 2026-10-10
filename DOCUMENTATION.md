# PhotoCraft — Living Documentation

> This document describes the current state of the project. It is maintained
> by the `docs-sync` skill and contains no history.

## Overview

PhotoCraft is a native layered image editor implemented in Rust. The desktop application uses
egui/eframe and wgpu; the web application compiles the same Rust UI and engine to WebAssembly.
Documents contain raster, text, shape, adjustment, fill and smart-object layers.

## Business Rules

1. Document actions use registered engine commands with stable identifiers. The UI, CLI,
   control channel and MCP dispatch those commands; view and window state belongs to the UI shell.
2. Pixel depth, colour model and ICC profiles are document data. Colour conversions use the
   colour-management crate, and the native format preserves the document model.
3. Commands validate their inputs and return errors. Editing operations record undo history;
   temporary UI previews do not commit document edits.
4. Contributor display names are opt-in entries in `contributors/people.toml`. Generated
   contributor statistics are compiled into the application.

## Architecture

### Components

The workspace separates geometry, colour management, pixel storage and standalone codecs from
the document model. Operations, painting, imaging, text and vector crates implement editing;
CPU/GPU composition and native-format storage consume the model. I/O and sandboxed WebAssembly
plug-ins feed the engine. Native, web and automation clients sit above the engine.

### Data Flow

Import creates a document in an engine session. Commands update its model and history; the
compositor renders that state for the UI or export. UI preferences and serializable view state
control themes, panels, tools and workspaces independently of image pixels.

### Integrations

The desktop application exposes a JSON control channel; the automation crate exposes MCP.
Optional `CRAFT_FONTS_DIR` supplies font assets during native builds. The application imports and
exports PSD and flat image formats and saves its complete model in `.pcraft` files.

## Gotchas & Pitfalls

Menu identifiers and paths are distinct from translated display labels. UI controls dispatch
commands rather than duplicating document-editing algorithms. Raster work must account for
runtime depth and colour model, active selections, masks and layer locks.

See [architecture](docs/architecture.md), [UI design](docs/ui-design.md),
[development](docs/development.md) and [control protocol](docs/control-protocol.md) for the
component contracts and verification workflows.
