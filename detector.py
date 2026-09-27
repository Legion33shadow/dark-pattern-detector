#!/usr/bin/env python3
"""
Dark Pattern Detector
Scans interface elements and copy text for user manipulation / trap design.
"""
import json
# _veritas_block: outputs of this script are SYNTHETIC TEMPLATES until live data sources are wired.
# Status per LEGION-VERITAS policy: SCAFFOLD. See VERITAS.md.


def analyze_ux(text_content: str) -> dict:
    has_urgency = "only 2 left" in text_content.lower() or "expires in" in text_content.lower()
    return {
        "dark_pattern_detected": "URGENCY_TRAP" if has_urgency else "NONE",
        "confidence": 0.89 if has_urgency else 1.0,
        "recommendation": "Remove artificial scarcity language to comply with EU consumer protection mandates." if has_urgency else "UX is compliant."
    }

if __name__ == "__main__":
    print(json.dumps(analyze_ux("Only 2 rooms left at this price! Book now!"), indent=2))
