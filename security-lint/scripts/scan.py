import os
import re
import sys

# Define sensitive patterns to look for
SENSITIVE_PATTERNS = {
    "absolute_path": r"/(?:home|Users|Users|var|etc|root|tmp)/[\w\-\./]+",
    "github_token": r"gh[opus]_[a-zA-Z0-9]{36,255}",
    "generic_api_key": r"(?:api_key|secret|token|password|auth_token)\s*[:=]\s*['\"][\w\-\.]{10,}['\"]",
    "private_key": r"-----BEGIN (?:RSA|OPENSSH|PRIVATE) KEY-----",
    "env_file": r"\.env(?:\.local|\.production)?",
}

# Define files to always skip
IGNORE_FILES = {".git", ".venv", "__pycache__", ".github", "node_modules", ".skill", ".skill-package", ".gemini"}
# Files where certain patterns are allowed (e.g., .env in .gitignore)
ALLOW_LIST = {
    ".gitignore": ["env_file"],
    "scan.py": ["absolute_path", "env_file", "github_token", "generic_api_key", "private_key"],
    "SKILL.md": ["env_file", "absolute_path"],
    "GEMINI.md": ["env_file"],
}

def scan_file(file_path):
    issues = []
    file_name = os.path.basename(file_path)
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            for name, pattern in SENSITIVE_PATTERNS.items():
                # Check allow list
                if file_name in ALLOW_LIST and name in ALLOW_LIST[file_name]:
                    continue
                
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    # Skip matches that are just the project root (relative is fine)
                    # But if it's an absolute path to the parent or system, flag it.
                    match_str = match.group(0)
                    
                    line_no = content.count('\n', 0, match.start()) + 1
                    issues.append({
                        "file": file_path,
                        "line": line_no,
                        "type": name,
                        "match": match_str
                    })
    except Exception as e:
        return [{"file": file_path, "type": "error", "match": str(e)}]
    return issues

def main():
    root_dir = os.getcwd()
    all_issues = []
    
    for root, dirs, files in os.walk(root_dir):
        # Prune ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_FILES]
        
        for file in files:
            if file in IGNORE_FILES:
                continue
                
            file_path = os.path.join(root, file)
            issues = scan_file(file_path)
            all_issues.extend(issues)

    if all_issues:
        print("🚨 SECURITY LINTING FAILURES DETECTED")
        print("=" * 40)
        for issue in all_issues:
            print(f"File: {issue['file']}")
            if "line" in issue:
                print(f"Line {issue['line']}: [{issue['type']}] -> {issue['match']}")
            else:
                print(f"Error: {issue['match']}")
            print("-" * 20)
        print("=" * 40)
        print("ACTION REQUIRED: Remove sensitive data before pushing.")
        sys.exit(1)
    else:
        print("✅ SECURITY LINTING PASSED: No sensitive data detected.")
        sys.exit(0)

if __name__ == "__main__":
    main()
