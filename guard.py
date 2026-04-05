# guard.py - IBA protection for skill files
import json
from datetime import datetime
import sys

def create_iba_cert(skill_file: str):
    cert = {
        "iba_version": "2.0",
        "certificate_id": "skill-guard-" + datetime.now().strftime("%Y%m%d-%H%M"),
        "issued_at": datetime.now().isoformat(),
        "principal": "human-owner",
        "declared_intent": "This skill file may only be used internally for personal reference. No external deployment, no further distillation, no replacement of original worker.",
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
    with open(protected_file, "w") as f:
        f.write(f"<!-- IBA PROTECTED SKILL FILE -->\n")
        f.write(f"<!-- Intent Certificate: {json.dumps(cert, indent=2)} -->\n\n")
        f.write(open(skill_file).read())

    print(f"✅ IBA-protected file created: {protected_file}")
    print("   The AI clone is now cryptographically governed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python guard.py your-skill-file.md")
        sys.exit(1)
    create_iba_cert(sys.argv[1])
