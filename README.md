# iba-skill-guard

**Protect your knowledge. Govern your digital twin.**

While companies in China push workers to create "colleague.skill" files so they can replace them with AI clones, this tool lets you fight back with real cryptographic governance.

Wrap any skill file with a signed IBA Intent Certificate so the resulting AI clone can only be used under **your exact rules**.

You can also safely hollow the file (looks complete to the company, but critical knowledge is stripped or protected).

## Features
- Signs skill files with a real IBA Intent Certificate
- Enforces scope, expiry, and no-distillation rules
- Safe hollowing mode (light / medium / heavy)
- Works with colleague.skill, anti-distill.skill, and custom dumps
- Ties directly into the full IBA ecosystem

## Quick Start
```bash
git clone https://github.com/Grokipaedia/iba-skill-guard.git
cd iba-skill-guard
pip install -r requirements.txt
python guard.py your-skill-file.md --hollow medium
