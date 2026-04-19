<think>
The document describes a model configuration system for an agent tool selection. The key points are:

1. Configuration file: .bw/config.yaml
2. Resolution order for model selection:
   - Exact match: models.<tool>.<agent>
   - Then: models.<tool>.default
   - Then: tool natural default
3. Used by bw step spawn command
4. Example: Claude-code tool uses sonnet by default, but conductor agent overrides to opus
5. Supported agents: conductor, discovery, analysis, plan-writer, splitter, reviewer, worker

I need to summarize this in ONE LINE (max 80 tokens) as a complete sentence capturing the core topic and key insight.

The core topic is the model