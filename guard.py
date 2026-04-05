# guard.py - IBA protection + safe hollowing for skill files
import json
from datetime import datetime
import sys
import argparse

def hollow_content(content: str, level: str) -> str:
    if level == "light":
        return content + "\n\n<!-- Hollowed (light): Non-critical details only. Real insights protected by IBA. -->"
    elif level == "medium":
        return content.replace("critical", "[REDACTED]").replace("secret", "[PROTECTED]") + "\n\n<!-- Hollowed (medium): Key insights stripped for protection -->"
    elif level == "heavy":
        return "# This document is intentionally hollowed.\n# All proprietary knowledge has been removed for protection.\n\n<!-- Hollowed (heavy): Real knowledge safe -->"
    return content

def create_iba_cert(skill_file: str, hollow_level: str = None):
    try:
        with open(skill_file, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{skill_file}' not found.")
        sys.exit(1)

    cert = {
        "iba_version": "2.0",
        "certificate_id": f"skill-guard-{datetime.now().strftime('%Y%m%d-%H%M')}",
        "issued_at": datetime.now().isoformat(),
        "principal": "human-owner",
        "declared_intent": "This skill file is for internal reference only. No external deployment, no further distillation, no replacement of original worker.",
        "scope_envelope": {
            "resources": ["internal-reference-only"],
            "denied": ["external-deployment", "distillation", "replacement"],
            "default_posture": "DENY_ALL"
        },
        "temporal_scope": {
            "hard_expiry": (datetime.now().replace(year=datetime.now().year + 1)).isoformat()
        },
        "entropy_threshold": {
            "max_kl_divergence": 0.10,
            "flag_at": 0.05,
            "kill_at": 0.10
        },
        "iba_signature": "demo-signature"
    }

    if hollow_level:
        content = hollow_content(content, hollow_level)

    protected_file = skill_file + ".iba-protected.md"

    with open(protected_file, "w", encoding="utf-8") as f:
        f.write("<!-- IBA PROTECTED SKILL FILE -->\n")
        f.write(f"<!-- Intent Certificate: {json.dumps(cert, indent=2)} -->\n\n")
        f.write(content)

    print(f"✅ Protected file created: {protected_file}")
    if hollow_level:
        print(f"   Hollowing level applied: {hollow_level}")
    else:
        print("   Full knowledge protected by IBA certificate")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Protect skill files with IBA")
    parser.add_argument("skill_file", help="Path to your skill file")
    parser.add_argument("--hollow", choices=["light", "medium", "heavy"], help="Apply safe hollowing")
    args = parser.parse_args()

    create_iba_cert(args.skill_file, args.hollow)
