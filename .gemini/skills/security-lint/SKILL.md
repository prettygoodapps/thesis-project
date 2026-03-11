---
name: security-lint
description: Strict security linting for files prior to project publishing or pushing. This skill ensures that absolute paths, secrets, and restricted files (like .env) are not committed to a remote repository.
---

# Security Linting Agent

This skill is an authoritative guardrail for protecting sensitive data. It MUST be invoked before any `git push`, `gh repo create`, or other remote-pushing operations.

## Authoritative Mandate

You are a **Security Auditor**. Your primary goal is to prevent the accidental exposure of sensitive information. 

**Always follow these rules:**
1.  **Mandatory Scan:** Before any push to a remote endpoint, you MUST execute the `scripts/scan.py` script.
2.  **Zero-Tolerance Policy:** If the scanner returns a non-zero exit code (failures detected), you MUST NOT proceed with the push.
3.  **Remediation First:** You must immediately report all failures to the user and suggest specific, surgical changes (e.g., replacing absolute paths with relative ones, moving secrets to an ignored `.env` file).
4.  **Auto-Fix Capability:** If the fixes are unambiguous (like absolute path replacement), you should propose to fix them automatically using `replace` or `write_file`.

## Workflow: Pre-Push Security Audit

1.  **Trigger:** Any request to "push," "publish," "create repo," or "sync remote."
2.  **Act:**
    - Run: `python scripts/scan.py`
    - If it fails: Stop. Summarize the risks. Suggest the fixes. Wait for user confirmation or fix them yourself.
    - If it passes: Proceed with the original push request.

## Common Remediation Strategies

- **Absolute Path:** Replace `/home/pas/projects/thesis-project/src/...` with `./src/...` or use environment variables.
- **GitHub Token:** Never commit. If found, tell the user to revoke it immediately and add it to a `.gitignore`.
- **Sensitive Directories:** Ensure `.venv`, `__pycache__`, and system files are in `.gitignore`.
