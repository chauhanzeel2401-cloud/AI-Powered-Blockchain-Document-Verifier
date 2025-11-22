#!/usr/bin/env python3
"""
run_demo.py
Simple end-to-end demo for:
 - extracting text from a PDF
 - running lightweight 'AI' checks (heuristics)
 - generating SHA-256 file fingerprint
 - printing the bytes32 hash (0x... ; ready for Remix)
Outputs JSON-like result you can paste to Remix or include in your Kaggle notebook.

Usage:
  python3 run_demo.py /path/to/your/sample_document.pdf

If you run without argument the script will try to auto-find a PDF in the current folder.
"""
import sys
import os
import hashlib
import json
from pathlib import Path

# Optional: import PDF reader
try:
    from PyPDF2 import PdfReader
except Exception:
    PdfReader = None

def generate_file_hash(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def extract_text(file_path):
    p = Path(file_path)
    if p.suffix.lower() == ".pdf":
        if PdfReader is None:
            return ""  # safe fallback; still produce hash even if no text extracted
        reader = PdfReader(str(file_path))
        parts = []
        for page in reader.pages:
            parts.append(page.extract_text() or "")
        return "\n".join(parts)
    else:
        # other text file types
        return p.read_text(encoding='utf-8', errors='ignore')

def simple_ai_checks(text):
    """
    Student-level heuristic checks:
    returns (verdict, issues[], confidence:int)
    """
    issues = []
    lower = (text or "").lower()
    if not text or len(text.strip()) < 50:
        issues.append("Document text is very short or empty.")
    # suspicious placeholders
    if "lorem ipsum" in lower or "sample text" in lower:
        issues.append("Contains placeholder text (lorem ipsum/sample).")
    # certificate-like tokens (informational)
    cert_tokens = ["certificate", "certify", "issued to", "transcript", "degree"]
    if any(tok in lower for tok in cert_tokens):
        # we mark as info but not issue
        pass
    # numeric garbage check
    import re
    if re.search(r"\d{9,}", lower):
        issues.append("Long numeric sequence found; check for embedded data.")
    # confidence heuristic
    confidence = 90 if not issues else max(30, 100 - 20*len(issues))
    verdict = "VALID" if not issues else "SUSPICIOUS"
    return verdict, issues, confidence

def auto_find_pdf():
    # search current folder for pdfs
    cwd = Path.cwd()
    pdfs = list(cwd.glob("*.pdf"))
    if pdfs:
        return str(pdfs[0])
    return None

def main():
    # 1) get file path (argument or auto-detect)
    if len(sys.argv) >= 2:
        file_path = sys.argv[1]
    else:
        file_path = auto_find_pdf()
        if not file_path:
            print("No file provided and no PDF found in current folder.")
            print("Usage: python3 run_demo.py /path/to/sample.pdf")
            sys.exit(1)

    # 2) confirm file exists
    if not os.path.exists(file_path):
        print(f"ERROR: file not found → {file_path}")
        sys.exit(1)

    print("Running AI + Hash demo on:", file_path)

    # 3) extract text (optional)
    text = extract_text(file_path)
    # 4) run simple AI heuristics
    verdict, issues, confidence = simple_ai_checks(text)

    # 5) generate SHA-256 hash
    hex_hash = generate_file_hash(file_path)
    bytes32 = "0x" + hex_hash  # ready to paste into Remix

    # 6) build final result
    result = {
        "file_path": file_path,
        "hash_hex": hex_hash,
        "hash_bytes32": bytes32,
        "ai_verdict": verdict,
        "ai_issues": issues,
        "ai_confidence": confidence,
        "excerpt": (text or "")[:800]
    }

    # print JSON result (human + machine readable)
    print("\n--- DEMO RESULT ---\n")
    print(json.dumps(result, indent=2))
    print("\n--- HOW TO USE THIS OUTPUT ---")
    print("1) To register on chain (Remix): use function registerDocument and paste the 'hash_bytes32' value.")
    print("2) To verify later: call verifyDocument(hash_bytes32); contract returns true/false.")
    print("\nExample bytes32 to copy:\n", bytes32)
    print("\nDemo complete.\n")

if __name__ == "__main__":
    main()
