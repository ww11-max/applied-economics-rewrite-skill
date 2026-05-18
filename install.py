#!/usr/bin/env python3
"""Install the Applied Economics Rewrite Skill for Claude Code.

Usage:
    python install.py

This script:
  1. Installs required Python packages
  2. Copies the skill file to ~/.claude/skills/applied-economics-rewrite/
  3. Replaces {{REPO_ROOT}} with the absolute path to this repository
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


def main():
    repo_root = Path(__file__).resolve().parent
    print(f"[install] Repository root: {repo_root}")

    # 1. Install Python dependencies
    print("[install] Installing Python dependencies...")
    req_file = repo_root / "requirements.txt"
    if req_file.exists():
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install",
                               "sentence-transformers", "faiss-cpu", "numpy"])

    # 2. Read skill template and replace placeholder
    skill_template = repo_root / "skill" / "SKILL.md"
    if not skill_template.exists():
        print(f"[install] ERROR: Skill template not found at {skill_template}")
        sys.exit(1)

    skill_content = skill_template.read_text(encoding="utf-8")
    skill_content = skill_content.replace("{{REPO_ROOT}}", str(repo_root))

    # 3. Write to Claude Code skills directory
    skills_dir = Path.home() / ".claude" / "skills" / "applied-economics-rewrite"
    skills_dir.mkdir(parents=True, exist_ok=True)

    skill_file = skills_dir / "SKILL.md"
    skill_file.write_text(skill_content, encoding="utf-8")
    print(f"[install] Skill installed to: {skill_file}")

    # 4. Verify
    print("[install] Verifying installation...")
    data_dir = repo_root / "data"
    required_files = [
        data_dir / "economics_papers_vectors.jsonl",
        data_dir / "economics_papers.index",
        data_dir / "economics_papers_meta.json",
    ]
    for f in required_files:
        if f.exists():
            size_mb = f.stat().st_size / (1024 * 1024)
            print(f"  [OK] {f.name} ({size_mb:.1f} MB)")
        else:
            print(f"  [MISSING] {f.name} — RAG retrieval will not work")

    print("\n[install] Done! Restart Claude Code and use /applied-economics-rewrite")
    print(f"[install] Repo path recorded as: {repo_root}")


if __name__ == "__main__":
    main()
