#!/bin/bash

# Configuration
SESSION="deliberation"
WORKSPACE="/home/pas/projects/thesis-project"

# Check if the session already exists
tmux has-session -t "$SESSION" 2>/dev/null

if [ $? != 0 ]; then
  # Start a new session in the workspace directory
  tmux new-session -d -s "$SESSION" -c "$WORKSPACE"

  # Rename the first window
  tmux rename-window -t "$SESSION:0" 'Main Deliberation'

  # Split into a layout: Main pane (Gemini), Side panes (Claude, Multi)
  tmux split-window -h -p 35 -c "$WORKSPACE"
  tmux split-window -v -p 50 -c "$WORKSPACE"

  # Select the main pane
  tmux select-pane -t 0
  tmux send-keys "echo 'Main Agent (Gemini) ready...'; ls" C-m

  # Setup the secondary panes
  tmux select-pane -t 1
  tmux send-keys "echo 'Secondary Agent (Claude) ready...'; ls" C-m

  tmux select-pane -t 2
  tmux send-keys "echo 'Orchestration / Logs ready...'; ls" C-m

  # Return focus to the main pane
  tmux select-pane -t 0
fi

# Attach to the session
echo "Attaching to tmux session: $SESSION"
echo "Controls:"
echo "  - Ctrl+a | (vertical split)"
echo "  - Ctrl+a - (horizontal split)"
echo "  - Alt + Arrow Keys (move between panes)"
echo "  - Mouse support is ON (click to select, drag to resize, scroll for history)"
tmux attach-session -t "$SESSION"
