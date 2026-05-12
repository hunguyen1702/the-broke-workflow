import json
import unittest
from pathlib import Path

from click.testing import CliRunner

from bw.cli import main


def _init_project(runner: CliRunner) -> None:
    result = runner.invoke(main, ["init"])
    if result.exit_code != 0:
        raise AssertionError(result.output)


def _write_milestones(slug: str) -> None:
    Path(f".bw/plans/{slug}/milestones.md").write_text(
        """---
slug: search-platform
status: draft
---

# Milestones: Search Platform

## Milestone 1: Search Index

**Goal:** Build the searchable index foundation.

## Milestone 2: Query API

**Goal:** Expose search through an API.
"""
    )


def _only_plan_dir(prefix: str) -> Path:
    matches = sorted(Path(".bw/plans").glob(f"{prefix}-*"))
    if len(matches) != 1:
        raise AssertionError(f"Expected one {prefix} plan dir, found: {matches}")
    return matches[0]


class EpicFlowCliTests(unittest.TestCase):
    def test_top_level_help_lists_epic_and_hides_legacy_command(self):
        runner = CliRunner()
        result = runner.invoke(main, ["--help"])

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn("epic", result.output)
        self.assertNotIn("pro" + "duct", result.output)

    def test_epic_help_exposes_lifecycle_subcommands(self):
        runner = CliRunner()
        result = runner.invoke(main, ["epic", "--help"])

        self.assertEqual(result.exit_code, 0, result.output)
        for command in ["init", "list", "docs", "read", "finalize", "plan", "status", "link", "remove"]:
            self.assertIn(command, result.output)

    def test_step_flow_accepts_epic_and_rejects_legacy_flow(self):
        runner = CliRunner()

        epic_result = runner.invoke(main, ["step", "list", "--flow", "epic"])
        self.assertEqual(epic_result.exit_code, 0, epic_result.output)
        self.assertEqual(epic_result.output.strip(), "requirements summary milestones review present")

        legacy_result = runner.invoke(main, ["step", "list", "--flow", "pro" + "duct"])
        self.assertNotEqual(legacy_result.exit_code, 0)
        self.assertIn("Invalid value", legacy_result.output)

    def test_epic_init_creates_epic_and_milestones_docs(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            _init_project(runner)

            result = runner.invoke(main, ["epic", "init", "Search Platform"])

            self.assertEqual(result.exit_code, 0, result.output)
            epic_dir = _only_plan_dir("search-platform")
            self.assertTrue((epic_dir / "epic.md").exists())
            self.assertTrue((epic_dir / "milestones.md").exists())

    def test_epic_plan_links_implementation_plan_with_epic_frontmatter(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            _init_project(runner)
            self.assertEqual(runner.invoke(main, ["epic", "init", "Search Platform"]).exit_code, 0)
            epic_slug = _only_plan_dir("search-platform").name
            _write_milestones(epic_slug)

            result = runner.invoke(main, ["epic", "plan", epic_slug, "1"])

            self.assertEqual(result.exit_code, 0, result.output)
            plan = (_only_plan_dir("search-index") / "plan.md").read_text()
            self.assertIn(f"epic: {epic_slug}", plan)
            self.assertIn("milestone: 1", plan)
            self.assertNotIn("pro" + "duct:", plan)

    def test_epic_status_json_rolls_up_linked_milestone_plans(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            _init_project(runner)
            self.assertEqual(runner.invoke(main, ["epic", "init", "Search Platform"]).exit_code, 0)
            epic_slug = _only_plan_dir("search-platform").name
            _write_milestones(epic_slug)
            self.assertEqual(runner.invoke(main, ["epic", "plan", epic_slug, "1"]).exit_code, 0)
            plan_slug = _only_plan_dir("search-index").name

            task_dir = Path(".bw/tasks") / plan_slug
            task_dir.mkdir(parents=True)
            (task_dir / "001-build-index.md").write_text(
                f"""---
id: {plan_slug}/001-build-index
title: Build index
status: done
---
"""
            )

            result = runner.invoke(main, ["epic", "status", epic_slug, "--json"])

            self.assertEqual(result.exit_code, 0, result.output)
            data = json.loads(result.output)
            self.assertEqual(data["slug"], epic_slug)
            self.assertEqual(data["totals"]["tasks"], 1)
            self.assertEqual(data["totals"]["done"], 1)
            self.assertEqual(data["milestones"][0]["plans"][0]["slug"], plan_slug)

    def test_plan_status_json_uses_epic_key_not_legacy_key(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            _init_project(runner)
            self.assertEqual(runner.invoke(main, ["epic", "init", "Search Platform"]).exit_code, 0)
            epic_slug = _only_plan_dir("search-platform").name
            _write_milestones(epic_slug)
            self.assertEqual(runner.invoke(main, ["epic", "plan", epic_slug, "1"]).exit_code, 0)
            plan_slug = _only_plan_dir("search-index").name

            result = runner.invoke(main, ["plan", "status", plan_slug, "--json"])

            self.assertEqual(result.exit_code, 0, result.output)
            data = json.loads(result.output)
            self.assertEqual(data["epic"], epic_slug)
            self.assertNotIn("pro" + "duct", data)


if __name__ == "__main__":
    unittest.main()
