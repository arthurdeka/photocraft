# Issue-fix visual evidence

The `before/` and `after/` PNGs are unmodified offscreen WGPU renders from the regression
fixtures in the corresponding PhotoCraft pull requests. The baseline keeps the fixture
and removes only the production correction; the corrected render restores it.

The fixtures use synthetic documents or an empty session and no external image inputs.
Comparison PNGs are labelled crops of the original renders, enlarged for readability.
These files are held only on this fork's evidence branch, outside the upstream PR diffs.

| Issue | Pull request | Source revision | Validation job |
| --- | --- | --- | --- |
| #2479 | [#2616](https://github.com/storytold/photocraft/pull/2616) | `060b65ba8804777f6b828b8f8a206ebfb397bac1` | [Palette validation](https://github.com/arthurdeka/photocraft/actions/runs/38063826511/job/114247332001) |
| #2600 | [#2617](https://github.com/storytold/photocraft/pull/2617) | `1d223a98cddcaae5a903b369116ee52c37bf4ea1` | [Ruler validation](https://github.com/arthurdeka/photocraft/actions/runs/38063043684/job/114245019422) |
| #2602 | [#2618](https://github.com/storytold/photocraft/pull/2618) | `c1aee34cd7ca6705544b7f456a377ef3e5f886ba` | [Status validation](https://github.com/arthurdeka/photocraft/actions/runs/38063826511/job/114247331833) |
| #2392 | [#2620](https://github.com/storytold/photocraft/pull/2620) | `955e654b3b1d72e008efc62616643492c65c9504` | [Workspace validation](https://github.com/arthurdeka/photocraft/actions/runs/38063826511/job/114247332033) |

The original UI assets retain their existing attribution and licence terms. The
generated renders and comparison layouts are provided under the repository's
MIT / Apache-2.0 terms; copies of those licences are included here.
