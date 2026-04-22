# iba-skill-guard

> **Protect your knowledge. Govern your digital twin.**

---

## The Problem

Companies are forcing workers to create **colleague.skill** files so they can replace them with AI clones. The worker does the work. The company owns the output. The AI agent trained on it has no declared boundary on what it can do with your expertise.

iba-skill-guard lets you fight back with real cryptographic governance.

Wrap any skill file with a signed **IBA Intent Certificate** so the resulting AI clone can only be used under **your exact rules** — declared scope, expiry, no-distillation clauses, and safe hollowing that makes the file look complete while protecting critical knowledge.

---

## Features

- Signs skill files with a proper IBA Intent Certificate
- Enforces scope, expiry, and no-distillation rules
- Safe hollowing — light / medium / deep
- Works with colleague.skill, anti-distill.skill, and any custom knowledge dump
- DENY_ALL default — the clone cannot act outside what you declared
- Immutable audit chain — every use logged

---

## Quick Start

```bash
git clone https://github.com/Grokipaedia/iba-skill-guard.git
cd iba-skill-guard
pip install -r requirements.txt
python guard.py your-skill-file.md --hollow medium
```

---

## Gate Logic

```
Valid human cert?                 → PROCEED
Action within declared scope?    → PROCEED
No-distillation clause active?   → BLOCK model training use
Cert expired?                    → BLOCK
Outside declared scope?          → BLOCK (DENY_ALL)
Distillation attempt detected?   → TERMINATE + LOG
No cert present?                 → BLOCK
```

**No cert = No clone action.**

---

## Safe Hollowing

```bash
# Light — redact specific proprietary methods only
python guard.py your-skill.md --hollow light

# Medium — redact methods + client-specific knowledge
python guard.py your-skill.md --hollow medium

# Deep — redact all proprietary knowledge, keep structure only
python guard.py your-skill.md --hollow deep
```

The file looks complete and professional to the company. The critical knowledge is yours.

---

## Related Repos

| Repo | Track |
|------|-------|
| [iba-governor](https://github.com/Grokipaedia/iba-governor) | Core gate · any agent |
| [iba-twin-guard](https://github.com/Grokipaedia/iba-twin-guard) | Digital twin identity governance |
| [iba-digital-worker-guard](https://github.com/Grokipaedia/iba-digital-worker-guard) | 19 AI models · parallel routing |

---

## Patent & Standards Record

```
Patent:   GB2603013.0 (Pending) · UK IPO · Filed February 10, 2026
Conception: February 5, 2026 · OTS timestamp + witness email
WIPO DAS: Confirmed April 15, 2026 · Access Code C9A6
PCT:      150+ countries · Protected until August 2028
IETF:     draft-williams-intent-token-00 · CONFIRMED LIVE
          datatracker.ietf.org/doc/draft-williams-intent-token/
NIST:     13 filings · NIST-2025-0035
NCCoE:    10 filings · AI Agent Identity & Authorization
```

---

## Acquisition Enquiries

IBA Intent Bound Authorization is available for acquisition.

**Jeffrey Williams**
IBA@intentbound.com
IntentBound.com · AgentialOnChain.com
Patent GB2603013.0 Pending · WIPO DAS C9A6 · IETF draft-williams-intent-token-00
