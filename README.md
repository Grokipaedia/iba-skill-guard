# iba-skill-guard

**Protect your knowledge. Govern your digital twin.**

While companies push "colleague.skill" files to clone workers into AI, this tool lets you fight back with real cryptographic governance.

Wrap any skill file with an IBA Intent Certificate so the resulting AI clone can only be used under your exact approved terms.

## Features
- Signs skill files with a real IBA Intent Certificate
- Enforces scope, expiry, and entropy limits
- Optional safe hollowing (looks complete but critical knowledge is protected)
- Works with colleague.skill, anti-distill.skill, and custom dumps
- Ties directly into the full IBA ecosystem

## Quick Start
```bash
git clone https://github.com/Grokipaedia/iba-skill-guard.git
cd iba-skill-guard
pip install -r requirements.txt
python guard.py your-skill-file.md
