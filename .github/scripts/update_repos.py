#!/usr/bin/env python3
"""Update the auto-managed sections of the profile README.

Rebuilds three marker-delimited blocks:
  * MOST_POPULAR     - top N public, non-fork repos by GitHub stars.
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
POPULAR_LIMIT = 10
RECENT_LIMIT = 10
README = Path(__file__).resolve().parents[2] / "README.md"

POPULAR_START = "<!-- MOST_POPULAR:START -->"
POPULAR_END = "<!-- MOST_POPULAR:END -->"
RECENT_START = "<!-- RECENTLY_UPDATED:START -->"
RECENT_END = "<!-- RECENTLY_UPDATED:END -->"
NEW_START = "<!-- NEW_REPOS:START -->"
NEW_END = "<!-- NEW_REPOS:END -->"

POPULAR_DISPLAY_NAMES = {
    "azure-dns-private-resolver": "Azure DNS Private Resolver",
    "azure-expressroute": "Azure ExpressRoute",
    "azure-gateway-lb": "Azure Gateway Load Balancer with OPNsense HA",
    "azure-virtualwan": "Azure Virtual WAN",
    "azure-vnet-encryption": "Azure Virtual Network Encryption",
    "azurevm-router": "Deploy Linux or Windows VM as Routers (IPv4/IPv6/NAT)",
    "lab": "Azure Networking Labs & Scripts",
    "network-desk": "Network Desk — Cloud Networking AI Agents",
    "opnazure": "OPNsense NVA Firewall in Azure",
    "privatelink": "Azure Private Link",
}

DISPLAY_WORDS = {
    "ai": "AI",
    "aws": "AWS",
    "azure": "Azure",
    "dns": "DNS",
    "gcp": "GCP",
    "ha": "HA",
    "ip": "IP",
    "ipv4": "IPv4",
    "ipv6": "IPv6",
    "nva": "NVA",
    "opnsense": "OPNsense",
    "vm": "VM",
    "vnet": "VNet",
    "vpn": "VPN",
    "wan": "WAN",
}


def fetch_repos():
    out = subprocess.run(
        [
            "gh", "repo", "list", OWNER,
            "--visibility", "public", "--no-archived",
            "--limit", "300",
            "--json", "name,description,url,pushedAt,isFork,repositoryTopics,stargazerCount",
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
                "stars": r.get("stargazerCount") or 0,
                "topics": topics,
            }
        )
    return cleaned


def badge(name):
    return (
        f"![updated](https://img.shields.io/github/last-commit/{OWNER}/{name}"
        f"?style=flat-square&label=updated&color=informational)"
    )


def stars_badge(name):
    return (
        f"![stars](https://img.shields.io/github/stars/{OWNER}/{name}"
        f"?style=flat-square&label=stars&color=yellow)"
    )


def friendly_name(name):
    override = POPULAR_DISPLAY_NAMES.get(name.lower())
    if override:
        return override

    words = re.split(r"[-_.]+", name)
    return " ".join(DISPLAY_WORDS.get(word.lower(), word.capitalize()) for word in words)


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


def render_popular(repo):
    parts = [f"- [{friendly_name(repo['name'])}]({repo['url']})"]
    if repo["desc"]:
        parts.append(f"— {repo['desc']}")
    parts.append(stars_badge(repo["name"]))
    return " ".join(parts)


def replace_block(text, start, end, body):
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    return pattern.sub(f"{start}\n{body}\n{end}", text)


def curated_repo_names(text):
    """Repo names linked in the README outside the auto-managed blocks."""
    stripped = replace_block(text, POPULAR_START, POPULAR_END, "")
    stripped = replace_block(stripped, RECENT_START, RECENT_END, "")
    stripped = replace_block(stripped, NEW_START, NEW_END, "")
    names = set()
    for m in re.finditer(r"github\.com/" + re.escape(OWNER) + r"/([A-Za-z0-9_.-]+)", stripped):
        names.add(m.group(1).lower())
    return names


def main():
    text = README.read_text(encoding="utf-8")
    repos = fetch_repos()
    by_pushed = sorted(repos, key=lambda r: r["pushed"], reverse=True)

    popular = sorted(
        (r for r in repos if r["stars"] > 0),
        key=lambda r: (-r["stars"], r["name"].lower()),
    )[:POPULAR_LIMIT]
    popular_body = "\n".join(render_popular(r) for r in popular) or "- _No starred repositories found._"

    recent = by_pushed[:RECENT_LIMIT]
    recent_body = "\n".join(render(r) for r in recent) or "- _No repositories found._"

    known = curated_repo_names(text)
    new = [r for r in by_pushed if r["name"].lower() not in known]
    new_body = "\n".join(render(r) for r in new) or "- _All public repos are already curated._"

    updated = replace_block(text, POPULAR_START, POPULAR_END, popular_body)
    updated = replace_block(updated, RECENT_START, RECENT_END, recent_body)
    updated = replace_block(updated, NEW_START, NEW_END, new_body)

    if updated == text:
        print("No changes.")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(
        f"Updated: {len(popular)} popular, {len(recent)} recent, "
        f"{len(new)} not-yet-curated."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
