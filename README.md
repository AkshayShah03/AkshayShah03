# Hi, I'm Akshay Shah

I work on AI and data infrastructure, and I spend a lot of my time fixing bugs in the open-source tools I build on: agent frameworks, on-device ML runtimes, model servers and cloud SDKs. Every fix starts with a reproduction and ships with a regression test.

📍 Bryan, Texas · ✉️ akshayhiteshshah@gmail.com

## Open-source contributions

**16 merged PRs** · **71 under review** · **36 issues filed**, across 9 open-source projects from Google, Apple MLX, AWS, NVIDIA, Tesla, Ollama and Anthropic.

### Merged

| Project | PR | What it fixed |
|---|---|---|
| **Google ADK** | [#7991](https://github.com/google/adk-python/pull/7991) ([ba142cf](https://github.com/google/adk-python/commit/ba142cf)) | Resuming a workflow re-ran a node that was still waiting for output |
|  | [#7729](https://github.com/google/adk-python/pull/7729) ([cbe786b](https://github.com/google/adk-python/commit/cbe786b)) | An expired OAuth2 token with no refresh token crashed the tool |
|  | [#7663](https://github.com/google/adk-python/pull/7663) ([b981250](https://github.com/google/adk-python/commit/b981250)) | `FirestoreSessionService` returned every user's sessions for an empty user id |
|  | [#7665](https://github.com/google/adk-python/pull/7665) ([37b1ab3](https://github.com/google/adk-python/commit/37b1ab3)) | Failed MCP tool results reached Claude marked as successes |
|  | [#7499](https://github.com/google/adk-python/pull/7499) ([a6ed859](https://github.com/google/adk-python/commit/a6ed859)) | A workflow `JoinNode` inside a loop fired with the previous iteration's outputs |
|  | [#7479](https://github.com/google/adk-python/pull/7479) ([019387c](https://github.com/google/adk-python/commit/019387c)) | Artifacts saved in agent callbacks were never recorded |
|  | [#7476](https://github.com/google/adk-python/pull/7476) ([f5db310](https://github.com/google/adk-python/commit/f5db310)) | `ApigeeLlm` dropped text sent alongside a function response |
| **Apple MLX** | [#4663](https://github.com/ml-explore/mlx/pull/4663) | `layer_norm` and SDPA fallbacks ignored the caller's stream (C++ core) |
| **MLX-VLM** | [#2473](https://github.com/Neywa-Labs/mlx-vlm/pull/2473) | The Eagle3 speculative-decoding drafter failed without its own embeddings |
|  | [#2486](https://github.com/Neywa-Labs/mlx-vlm/pull/2486) | The Anthropic-compatible stream sent text past `stop_sequences` |
|  | [#2476](https://github.com/Neywa-Labs/mlx-vlm/pull/2476) | PaddleOCR-VL LoRA training didn't freeze the vision encoder and rejected packed patches |
|  | [#2492](https://github.com/Neywa-Labs/mlx-vlm/pull/2492) | Multi-turn Phi-3-vision / Phi-4-MM chats with images crashed |
|  | [#2484](https://github.com/Neywa-Labs/mlx-vlm/pull/2484) | The OpenAI-compatible server ignored `max_completion_tokens` |
|  | [#2479](https://github.com/Neywa-Labs/mlx-vlm/pull/2479) | Documented video input for `apply_chat_template` |
| **AWS Strands Agents** | [#5016](https://github.com/strands-agents/harness-sdk/pull/5016) | Warnings were logged for every earlier message on every request (N² log lines) |
| **NVIDIA** | [#2476](https://github.com/NVIDIA/NeMo-Agent-Toolkit/pull/2476) | MCP service-account tokens had a timezone-naive expiry, so no credentials were sent |

Google ADK merges through Copybara, so those PRs show as "Closed" on GitHub. The commit links point to the merged change.

### Under review

| Project | PRs | Highlights |
|---|---|---|
| **AWS SageMaker Python SDK** | [42](https://github.com/search?q=is%3Apr+is%3Aopen+repo%3Aaws%2Fsagemaker-python-sdk+author%3AAkshayShah03&type=pullrequests) | Bugs in the v3 SDK across training, serving, pipelines and core, such as a KMS key sent as a customer encryption key, `mpirun -np` given the wrong rank count, and `AsyncPredictor` hanging instead of timing out |
| **Ollama** | [10](https://github.com/search?q=is%3Apr+is%3Aopen+repo%3Aollama%2Follama+author%3AAkshayShah03&type=pullrequests) | Responses API text dropped next to tool calls, blobs not pruned after pull or copy, a race in blob-download cancellation |
| **Tesla** | [7](https://github.com/search?q=is%3Apr+is%3Aopen+org%3Ateslamotors+author%3AAkshayShah03&type=pullrequests) | Vehicle wake-up polling, cabin overheat protection level, Kafka client errors, statsd tags, `FixedBitset` construction |
| **MLX-VLM** | [4](https://github.com/search?q=is%3Apr+is%3Aopen+repo%3ANeywa-Labs%2Fmlx-vlm+author%3AAkshayShah03&type=pullrequests) | Qwen3-VL embedding position IDs, GLM-OCR image input, pooling options |
| **Google ADK** | [2](https://github.com/search?q=is%3Apr+is%3Aopen+repo%3Agoogle%2Fadk-python+author%3AAkshayShah03&type=pullrequests) | Workflow resume replay, keeping finished parallel tool results on abort |
| **AWS Strands Agents** | [2](https://github.com/search?q=is%3Apr+is%3Aopen+repo%3Astrands-agents%2Fharness-sdk+author%3AAkshayShah03&type=pullrequests) | Contributor setup docs |
| **NVIDIA** | [2](https://github.com/search?q=is%3Apr+is%3Aopen+org%3ANVIDIA+author%3AAkshayShah03&type=pullrequests) | Reproducible seeded prompts in garak, empty trailing slices in Warp |
| **Anthropic Claude Agent SDK** | [2](https://github.com/search?q=is%3Apr+is%3Aopen+repo%3Aanthropics%2Fclaude-agent-sdk-python+author%3AAkshayShah03&type=pullrequests) | A client disconnect race, recursive TypedDict schemas for MCP tools |

### Issues and triage

- Filed 36 issues (bug reports with reproductions, and proposals): [Google ADK](https://github.com/search?q=is%3Aissue+repo%3Agoogle%2Fadk-docs+repo%3Agoogle%2Fadk-python+author%3AAkshayShah03&type=issues) (16), [MLX-VLM](https://github.com/search?q=is%3Aissue+repo%3ANeywa-Labs%2Fmlx-vlm+author%3AAkshayShah03&type=issues) (4), [NVIDIA](https://github.com/search?q=is%3Aissue+org%3ANVIDIA+author%3AAkshayShah03&type=issues) (4), [AWS Strands Agents](https://github.com/search?q=is%3Aissue+repo%3Astrands-agents%2Fharness-sdk+author%3AAkshayShah03&type=issues) (3), [Tesla](https://github.com/search?q=is%3Aissue+org%3Ateslamotors+author%3AAkshayShah03&type=issues) (3), [Ollama](https://github.com/search?q=is%3Aissue+repo%3Aollama%2Follama+author%3AAkshayShah03&type=issues) (3), [Anthropic Claude Agent SDK](https://github.com/search?q=is%3Aissue+repo%3Aanthropics%2Fclaude-agent-sdk-python+author%3AAkshayShah03&type=issues) (2), [MCP Python SDK](https://github.com/search?q=is%3Aissue+repo%3Amodelcontextprotocol%2Fpython-sdk+author%3AAkshayShah03&type=issues) (1).
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

<sub>Updated automatically from GitHub on November 9, 2026.</sub>
