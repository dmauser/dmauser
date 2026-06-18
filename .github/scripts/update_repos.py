#!/usr/bin/env python3
"""Update the auto-managed sections of the profile README.

Rebuilds two marker-delimited blocks:
  * RECENTLY_UPDATED - top N public, non-fork repos by push date.
  * NEW_REPOS        - public, non-fork repos not already linked in the
                       hand-curated portion of the README.

Data comes from the `gh` CLI (uses GH_TOKEN in CI). No third-party deps.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

OWNER = "dmauser"
SELF_REPO = "dmauser"  # the profile repo itself, always excluded
RECENT_LIMIT = 10
README = Path(__file__).resolve().parents[2] / "README.md"

RECENT_START = "<!-- RECENTLY_UPDATED:START -->"
RECENT_END = "<!-- RECENTLY_UPDATED:END -->"
NEW_START = "<!-- NEW_REPOS:START -->"
NEW_END = "<!-- NEW_REPOS:END -->"


def fetch_repos():
    out = subprocess.run(
        [
            "gh", "repo", "list", OWNER,
            "--visibility", "public", "--no-archived",
            "--limit", "300",
            "--json", "name,description,url,pushedAt,isFork,repositoryTopics",
        ],
        capture_output=True, text=True, encoding="utf-8", check=True,
    ).stdout
    repos = json.loads(out)
    cleaned = []
    for r in repos:
        if r.get("isFork"):
            continue
        if r["name"].lower() == SELF_REPO.lower():
            continue
        topics = [t["name"] for t in (r.get("repositoryTopics") or [])]
        cleaned.append(
            {
                "name": r["name"],
                "url": r["url"],
                "desc": (r.get("description") or "").strip(),
                "pushed": r.get("pushedAt") or "",
                "topics": topics,
            }
        )
    return cleaned


def badge(name):
    return (
        f"![updated](https://img.shields.io/github/last-commit/{OWNER}/{name}"
        f"?style=flat-square&label=updated&color=informational)"
    )


def render(repo):
    parts = [f"- [{repo['name']}]({repo['url']})"]
    if repo["desc"]:
        parts.append(f"— {repo['desc']}")
    parts.append(badge(repo["name"]))
    line = " ".join(parts)
    if repo["topics"]:
        tags = " · ".join(f"`{t}`" for t in repo["topics"][:6])
        line += f"<br>  <sub>{tags}</sub>"
    return line


def replace_block(text, start, end, body):
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    return pattern.sub(f"{start}\n{body}\n{end}", text)


def curated_repo_names(text):
    """Repo names linked in the README outside the auto-managed blocks."""
    stripped = replace_block(text, RECENT_START, RECENT_END, "")
    stripped = replace_block(stripped, NEW_START, NEW_END, "")
    names = set()
    for m in re.finditer(r"github\.com/" + re.escape(OWNER) + r"/([A-Za-z0-9_.-]+)", stripped):
        names.add(m.group(1).lower())
    return names


def main():
    text = README.read_text(encoding="utf-8")
    repos = fetch_repos()
    by_pushed = sorted(repos, key=lambda r: r["pushed"], reverse=True)

    recent = by_pushed[:RECENT_LIMIT]
    recent_body = "\n".join(render(r) for r in recent) or "- _No repositories found._"

    known = curated_repo_names(text)
    new = [r for r in by_pushed if r["name"].lower() not in known]
    new_body = "\n".join(render(r) for r in new) or "- _All public repos are already curated._"

    updated = replace_block(text, RECENT_START, RECENT_END, recent_body)
    updated = replace_block(updated, NEW_START, NEW_END, new_body)

    if updated == text:
        print("No changes.")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"Updated: {len(recent)} recent, {len(new)} not-yet-curated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
