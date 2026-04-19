<think>
This document describes Claude Code's work adapter for task execution. The key points are:

1. Work adapter handles task claiming and execution flow
2. The bw task block command was removed - use verbal explanation instead
3. Task release now reverts in_progress to pending (not to ready)
4. Key steps: claim, read task file, read scope files, execute, verify ACs
5. 5 key rules for task execution

I need to produce a one-line summary (max 80 tokens) that captures the core topic and key insight.

Core topic: Claude Code work adapter for task execution
Key insight: The bw task block command was removed and replaced with verbal explanation; task release now goes to pending not ready