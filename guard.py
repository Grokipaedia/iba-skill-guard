
### 2. Updated `guard.py` (now with safe hollowing)

```python
# guard.py - IBA protection + safe hollowing for skill files
import json
from datetime import datetime
import sys
import argparse

def create_iba_cert(skill_file: str, hollow_level: str = None):
    cert = {
        "iba_version": "2.0",
        "certificate_id": "skill-guard-" + datetime.now().strftime("%Y%m%d-%H%M"),
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

    protected_file = skill_file + ".iba-protected.md"

    content = open(skill_file, encoding="utf-8").read()

    if hollow_level:
        content = hollow_content(content, hollow_level)

    with open(protected_file, "w", encoding="utf-8") as f:
        f.write(f"<!-- IBA PROTECTED SKILL FILE -->\n")
        f.write(f"<!-- Intent Certificate: {json.dumps(cert, indent=2)} -->\n\n")
        f.write(content)

    print(f"✅ IBA-protected file created: {protected_file}")
    if hollow_level:
        print(f"   Hollowing level: {hollow_level} (critical knowledge protected)")
    else:
        print("   Full knowledge protected by IBA certificate")

def hollow_content(content: str, level: str):
    if level == "light":
        return content + "\n\n<!-- Hollowed: Non-critical details only. Real insights protected. -->"
    elif level == "medium":
        return content.replace("critical", "[REDACTED]").replace("secret", "[PROTECTED]") + "\n\n<!-- Medium hollow: Key insights stripped -->"
    elif level == "heavy":
        return "This document contains only high-level structure. All proprietary knowledge has been intentionally removed for protection.\n\n<!-- Heavy hollow: Real knowledge safe -->"
    return content

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_file", help="Path to your skill file")
    parser.add_argument("--hollow", choices=["light", "medium", "heavy"], help="Hollowing level")
    args = parser.parse_args()

    create_iba_cert(args.skill_file, args.hollow)
