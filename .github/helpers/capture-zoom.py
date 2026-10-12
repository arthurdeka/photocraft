"""Fork-only capture instrumentation; never included in a contribution branch."""
from pathlib import Path
import sys

path = Path(sys.argv[1])
source = path.read_text()
source = source.replace("use serde_json::Value;", "use serde_json::Value;\nuse egui_kittest::kittest::Queryable;")
probe = r'''
    if args.iter().any(|a| a == "--zoom-wrap-probe") {
        harness.input_mut().viewports.entry(egui::ViewportId::ROOT).or_default().fullscreen = Some(true);
        harness.state_mut().ui.views[0].zoom = 10.0;
        harness.state_mut().ui.views[0].fit_pending = false;
        harness.run_steps(4);
        let start = harness.query_all_by_role(egui::accesskit::Role::SpinButton)
            .find(|n| n.rect().center().y > h - 40.0 && n.rect().center().x < 150.0)
            .expect("status zoom field").rect().center();
        harness.hover_at(start);
        harness.run_steps(1);
        harness.drag_at(start);
        harness.run_steps(1);
        let edge = egui::pos2(0.5, start.y);
        harness.hover_at(edge);
        harness.run_steps(1);
        let at_edge = harness.state().ui.views[0].zoom * 100.0;
        let warp = harness.output().viewport_output.values().flat_map(|v| &v.commands)
            .find_map(|c| match c { egui::ViewportCommand::CursorPosition(p) => Some(*p), _ => None });
        let mut after_warp = at_edge;
        if let Some(to) = warp {
            harness.hover_at(to);
            harness.run_steps(1);
            after_warp = harness.state().ui.views[0].zoom * 100.0;
            harness.hover_at(to - egui::vec2(100.0, 0.0));
            harness.run_steps(1);
        } else {
            harness.hover_at(edge);
            harness.run_steps(1);
        }
        let continued = harness.state().ui.views[0].zoom * 100.0;
        let metrics = serde_json::json!({
            "start": [start.x, start.y], "edge_percent": at_edge,
            "warp": warp.map(|p| [p.x, p.y]),
            "after_warp_percent": after_warp, "continued_percent": continued
        });
        println!("zoom-wrap-probe: {metrics}");
        std::fs::write(format!("{out}.json"), format!("{metrics}\n")).expect("probe metrics");
    }
'''
needle = "    let t_settle = std::time::Instant::now();"
assert source.count(needle) == 1
path.write_text(source.replace(needle, probe + "\n" + needle))
