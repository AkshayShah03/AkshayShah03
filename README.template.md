# Hi, I'm Akshay Shah

I work on AI and data infrastructure, and I spend a lot of my time fixing bugs in the open-source tools I build on: agent frameworks, on-device ML runtimes, model servers and cloud SDKs. Every fix starts with a reproduction and ships with a regression test.

📍 Bryan, Texas · ✉️ akshayhiteshshah@gmail.com

## Open-source contributions

{{STATS}}

### Merged

{{MERGED}}

Google ADK merges through Copybara, so those PRs show as "Closed" on GitHub. The commit links point to the merged change.

### Under review

{{OPEN}}

### Issues and triage

{{ISSUES}}
- Reproduced and triaged auth bugs in the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk), and reviewed a maintainer PR there.

## Projects

| Project | What it is |
|---|---|
| [**leash**](https://github.com/AkshayShah03/leash) · [live demo](https://leash-y39h.onrender.com) · [video](https://youtu.be/QmP6ZTWWyb8) | A trust layer between AI shopping agents and PayPal: rules the agent can't override, an AI check that can only tighten, owner approvals and an audit ledger (TypeScript) |
| [**local-llm-eval**](https://github.com/AkshayShah03/local-llm-eval) | An evaluation harness and fallback gateway for choosing locally hosted LLMs (Qwen, Llama, Mistral on Ollama) for RAG and tool calling |
| [**meridian**](https://github.com/AkshayShah03/meridian) | A real-time AI backend on Kafka, FastAPI and pgvector, with a ReAct agent loop, multi-layer memory and multi-model routing |
| [**sentinel**](https://github.com/AkshayShah03/sentinel) | FastAPI services that sit in front of any LLM: PII detection, prompt-injection blocking, async evals and CUSUM drift detection |
| [**forge**](https://github.com/AkshayShah03/forge) | A multi-agent incident responder that turns a production alert into a structured postmortem |
| [**realtime-feature-platform**](https://github.com/AkshayShah03/realtime-feature-platform) | A feature platform that prevents training-serving skew: a shared compute path, point-in-time joins and PSI skew detection |
| [**streaming-lakehouse-optimizer**](https://github.com/AkshayShah03/streaming-lakehouse-optimizer) | Postgres → Debezium → Kafka → Flink → Iceberg, with a learned layout optimizer |
| [**incremental-vector-pipeline**](https://github.com/AkshayShah03/incremental-vector-pipeline) | CDC-driven re-embedding of only the chunks that changed, with a versioned store and instant model rollback |

<sub>Updated automatically from GitHub on {{DATE}}.</sub>
