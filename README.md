# iba-skill-guard

**Protect your knowledge. Govern your digital twin.**

While companies force workers to create **colleague.skill** files so they can replace them with AI clones, this tool lets you fight back with real cryptographic governance.

Wrap any skill file with a signed **IBA Intent Certificate** so the resulting AI clone can only be used under **your exact rules**.

You can also safely hollow the file — it looks complete to the company, but critical knowledge is protected.

## Live Demo
Try it here: [https://governinglayer.com/skillguard-html/](https://governinglayer.com/skillguard-html/)

## Features
- Signs skill files with a proper IBA Intent Certificate
- Enforces scope, expiry, and no-distillation rules
- Safe hollowing (light / medium / heavy)
- Works with colleague.skill, anti-distill.skill, and any custom dump

## Quick Start
```bash
git clone https://github.com/Grokipaedia/iba-skill-guard.git
cd iba-skill-guard
pip install -r requirements.txt
python guard.py your-skill-file.md --hollow medium
