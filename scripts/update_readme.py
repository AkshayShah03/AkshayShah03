"""Regenerate README.md from README.template.md using live GitHub search data.

Only public repositories are counted. Merged PRs include ones GitHub marks as
merged and ones closed with a `merged` label (Google repos land PRs through
Copybara, so GitHub shows them as closed).
"""

import datetime
import json
import os
import re
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "scripts" / "config.json").read_text())
USER = CONFIG["user"]
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def api(url):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-readme-updater"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as err:
            if err.code in (403, 429) and attempt < 2:
                time.sleep(30)
                continue
            raise


def search(qualifiers):
    excluded = " ".join(f"-org:{org}" for org in CONFIG["exclude_orgs"])
    query = f"author:{USER} is:public {excluded} {qualifiers}"
    items, page = [], 1
    while True:
        params = urllib.parse.urlencode({"q": query, "per_page": 100, "page": page})
        data = api(f"https://api.github.com/search/issues?{params}")
        items.extend(data["items"])
        if len(items) >= data["total_count"] or not data["items"]:
            return items
        page += 1
        time.sleep(2)


def repo_of(item):
    return item["repository_url"].split("/repos/", 1)[1]


def project_of(repo):
    owner = repo.split("/")[0]
    for project in CONFIG["projects"]:
        if repo in project.get("repos", []) or owner in project.get("orgs", []):
            return project["name"]
    return repo


PROJECT_ORDER = [p["name"] for p in CONFIG["projects"]]


def order_key(name):
    return PROJECT_ORDER.index(name) if name in PROJECT_ORDER else len(PROJECT_ORDER)


def copybara_commit(item):
    comments = api(item["comments_url"] + "?per_page=100")
    for comment in comments:
        match = re.search(r"merged via Copybara in commit ([0-9a-f]{7,40})", comment["body"])
        if match:
            return match.group(1)[:7]
    return None


def merged_rows(merged):
    by_project = defaultdict(list)
    for item in merged:
        by_project[project_of(repo_of(item))].append(item)

    lines = ["| Project | PR | What it fixed |", "|---|---|---|"]
    for name in sorted(by_project, key=order_key):
        items = sorted(by_project[name], key=lambda i: i["closed_at"], reverse=True)
        for index, item in enumerate(items):
            repo = repo_of(item)
            key = f"{repo}#{item['number']}"
            link = f"[#{item['number']}]({item['html_url']})"
            if not item["pull_request"].get("merged_at"):
                commit = copybara_commit(item)
                if commit:
                    link += f" ([{commit}](https://github.com/{repo}/commit/{commit}))"
            description = CONFIG["descriptions"].get(key, item["title"])
            project_cell = f"**{name}**" if index == 0 else ""
            lines.append(f"| {project_cell} | {link} | {description} |")
    return "\n".join(lines)


def search_url(qualifiers, kind):
    query = f"{qualifiers} author:{USER}"
    return "https://github.com/search?" + urllib.parse.urlencode({"q": query, "type": kind})


def scope(name, repos):
    project = next((p for p in CONFIG["projects"] if p["name"] == name), None)
    if project and project.get("orgs"):
        return " ".join(f"org:{org}" for org in project["orgs"])
    return " ".join(f"repo:{repo}" for repo in sorted(repos))


def open_rows(open_prs):
    by_project = defaultdict(set)
    counts = defaultdict(int)
    for item in open_prs:
        name = project_of(repo_of(item))
        by_project[name].add(repo_of(item))
        counts[name] += 1

    lines = ["| Project | PRs | Highlights |", "|---|---|---|"]
    for name in sorted(counts, key=lambda n: (-counts[n], order_key(n))):
        url = search_url(f"is:pr is:open {scope(name, by_project[name])}", "pullrequests")
        highlight = CONFIG["highlights"].get(name, "")
        lines.append(f"| **{name}** | [{counts[name]}]({url}) | {highlight} |")
    return "\n".join(lines)


def issues_line(issues):
    by_project = defaultdict(set)
    counts = defaultdict(int)
    for item in issues:
        name = project_of(repo_of(item))
        by_project[name].add(repo_of(item))
        counts[name] += 1

    parts = []
    for name in sorted(counts, key=lambda n: (-counts[n], order_key(n))):
        url = search_url(f"is:issue {scope(name, by_project[name])}", "issues")
        parts.append(f"[{name}]({url}) ({counts[name]})")
    return f"- Filed {len(issues)} issues (bug reports with reproductions, and proposals): " + ", ".join(parts) + "."


def main():
    merged = search("is:pr is:merged") + search("is:pr is:closed -is:merged label:merged")
    open_prs = search("is:pr is:open")
    issues = search("is:issue")

    projects = {project_of(repo_of(item)) for item in merged + open_prs}
    stats = (
        f"**{len(merged)} merged PRs** · **{len(open_prs)} under review** · "
        f"**{len(issues)} issues filed**, across {len(projects)} open-source projects from "
        f"{CONFIG['orgs_line']}."
    )

    readme = (ROOT / "README.template.md").read_text()
    readme = (
        readme.replace("{{STATS}}", stats)
        .replace("{{MERGED}}", merged_rows(merged))
        .replace("{{OPEN}}", open_rows(open_prs))
        .replace("{{ISSUES}}", issues_line(issues))
        .replace("{{DATE}}", datetime.date.today().strftime("%B %-d, %Y"))
    )
    (ROOT / "README.md").write_text(readme)


if __name__ == "__main__":
    main()
