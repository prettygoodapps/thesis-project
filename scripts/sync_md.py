import os
import re
import time
import sys
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
CLAUDE_FILE = PROJECT_ROOT / "CLAUDE.md"
GEMINI_FILE = PROJECT_ROOT / "GEMINI.md"

# Sections to sync (must exist with ## heading)
SYNC_SECTIONS = [
    "Project Overview",
    "AI Document Conventions",
    "Commit Convention",
    "Technical Conventions",
    "Usage"
]

def transform_content(content, to_model="gemini"):
    """
    Transforms content from one model context to another.
    """
    if to_model == "gemini":
        # Claude -> Gemini
        content = content.replace("claude", "gemini")
        content = content.replace("Claude", "Gemini")
        content = content.replace("Anthropic", "Google")
        content = content.replace("Claude Code", "Gemini CLI")
    else:
        # Gemini -> Claude
        content = content.replace("gemini", "claude")
        content = content.replace("Gemini", "Claude")
        content = content.replace("Google", "Anthropic")
        content = content.replace("Gemini CLI", "Claude Code")
    return content

def extract_sections(text):
    """
    Extracts sections starting with ## into a dictionary.
    """
    sections = {}
    current_section = None
    lines = []
    
    for line in text.splitlines():
        match = re.match(r"^##\s+(.*)", line)
        if match:
            if current_section:
                sections[current_section] = "\n".join(lines).strip()
            current_section = match.group(1).strip()
            lines = []
        elif current_section:
            lines.append(line)
            
    if current_section:
        sections[current_section] = "\n".join(lines).strip()
        
    return sections

def update_file(source_file, target_file, target_model):
    """
    Syncs SYNC_SECTIONS from source to target.
    """
    if not source_file.exists() or not target_file.exists():
        return

    print(f"Syncing changes from {source_file.name} to {target_file.name}...")
    
    with open(source_file, 'r') as f:
        source_text = f.read()
    
    with open(target_file, 'r') as f:
        target_text = f.read()

    source_sections = extract_sections(source_text)
    target_sections = extract_sections(target_text)
    
    # 1. Update existing sections in target
    lines = []
    current_section = None
    skip_mode = False
    processed_sync_sections = set()
    
    # Header check (preserve everything before the first ##)
    header_found = False
    for line in target_text.splitlines():
        match = re.match(r"^##\s+(.*)", line)
        if match:
            header_found = True
            break
        if not header_found:
            lines.append(line)

    # Re-iterate and process
    for line in target_text.splitlines():
        if not header_found: # Already handled
            continue
            
        match = re.match(r"^##\s+(.*)", line)
        if match:
            if current_section and skip_mode:
                skip_mode = False
            
            section_name = match.group(1).strip()
            sync_match = next((s for s in SYNC_SECTIONS if s in section_name or section_name in s), None)
            
            if sync_match and sync_match in source_sections:
                lines.append(f"## {section_name}")
                transformed = transform_content(source_sections[sync_match], to_model=target_model)
                lines.append(transformed)
                skip_mode = True
                processed_sync_sections.add(sync_match)
                current_section = section_name
            else:
                lines.append(line)
                skip_mode = False
                current_section = section_name
        else:
            if header_found and not skip_mode:
                lines.append(line)
            elif not header_found:
                # This should not be reachable if logic is correct
                pass

    # 2. Append missing sync sections
    for sync_section in SYNC_SECTIONS:
        if sync_section not in processed_sync_sections and sync_section in source_sections:
            print(f"Adding missing section: {sync_section}")
            lines.append(f"\n## {sync_section}")
            transformed = transform_content(source_sections[sync_section], to_model=target_model)
            lines.append(transformed)

    new_text = "\n".join(lines).strip() + "\n"
    
    if new_text.strip() != target_text.strip():
        with open(target_file, 'w') as f:
            f.write(new_text)
        print(f"Successfully updated {target_file.name}")
    else:
        print(f"No changes needed for {target_file.name}")

class SyncHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_sync = 0

    def on_modified(self, event):
        # Debounce
        if time.time() - self.last_sync < 1:
            return
            
        src_path = Path(event.src_path).resolve()
        if src_path == CLAUDE_FILE.resolve():
            update_file(CLAUDE_FILE, GEMINI_FILE, "gemini")
            self.last_sync = time.time()
        elif src_path == GEMINI_FILE.resolve():
            update_file(GEMINI_FILE, CLAUDE_FILE, "claude")
            self.last_sync = time.time()

if __name__ == "__main__":
    print(f"Starting MD Sync Agent for {PROJECT_ROOT.name}...")
    print(f"Watching: {CLAUDE_FILE.name} and {GEMINI_FILE.name}")
    
    # Run initial sync
    update_file(GEMINI_FILE, CLAUDE_FILE, "claude")
    update_file(CLAUDE_FILE, GEMINI_FILE, "gemini")
    
    event_handler = SyncHandler()
    observer = Observer()
    observer.schedule(event_handler, path=str(PROJECT_ROOT), recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
