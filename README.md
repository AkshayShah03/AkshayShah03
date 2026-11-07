# Hi, I'm Akshay Shah

I work on AI and data infrastructure, and I spend a lot of my time fixing bugs in the open-source tools I build on: agent frameworks, on-device ML runtimes, model servers and cloud SDKs. Every fix starts with a reproduction and ships with a regression test.

📍 Bryan, Texas · ✉️ akshayhiteshshah@gmail.com

## Open-source contributions

**16 merged PRs** · **74 under review** · **35 bug reports filed**, across Google, Apple MLX, AWS, NVIDIA, Tesla, Ollama and Anthropic projects.

### Merged

| Project | PR | What it fixed |
|---|---|---|
| **Google ADK** | [#7663](https://github.com/google/adk-python/pull/7663) ([b981250](https://github.com/google/adk-python/commit/b981250)) | `FirestoreSessionService` returned every user's sessions for an empty user id |
| | [#7729](https://github.com/google/adk-python/pull/7729) ([cbe786b](https://github.com/google/adk-python/commit/cbe786b)) | An expired OAuth2 token with no refresh token crashed the tool |
| | [#7665](https://github.com/google/adk-python/pull/7665) ([37b1ab3](https://github.com/google/adk-python/commit/37b1ab3)) | Failed MCP tool results reached Claude marked as successes |
| | [#7476](https://github.com/google/adk-python/pull/7476) ([f5db310](https://github.com/google/adk-python/commit/f5db310)) | `ApigeeLlm` dropped text sent alongside a function response |
| | [#7479](https://github.com/google/adk-python/pull/7479) ([019387c](https://github.com/google/adk-python/commit/019387c)) | Artifacts saved in agent callbacks were never recorded |
| | [#7499](https://github.com/google/adk-python/pull/7499) ([a6ed859](https://github.com/google/adk-python/commit/a6ed859)) | A workflow `JoinNode` inside a loop fired with the previous iteration's outputs |
| | [#7991](https://github.com/google/adk-python/pull/7991) ([ba142cf](https://github.com/google/adk-python/commit/ba142cf)) | Resuming a workflow re-ran a node that was still waiting for output |
| **Apple MLX** | [#4663](https://github.com/ml-explore/mlx/pull/4663) | `layer_norm` and SDPA fallbacks ignored the caller's stream (C++ core) |
| **MLX-VLM** | [#2484](https://github.com/Neywa-Labs/mlx-vlm/pull/2484) | The OpenAI-compatible server ignored `max_completion_tokens` |
| | [#2486](https://github.com/Neywa-Labs/mlx-vlm/pull/2486) | The Anthropic-compatible stream sent text past `stop_sequences` |
| | [#2492](https://github.com/Neywa-Labs/mlx-vlm/pull/2492) | Multi-turn Phi-3-vision / Phi-4-MM chats with images crashed |
| | [#2473](https://github.com/Neywa-Labs/mlx-vlm/pull/2473) | The Eagle3 speculative-decoding drafter failed without its own embeddings |
| | [#2476](https://github.com/Neywa-Labs/mlx-vlm/pull/2476) | PaddleOCR-VL LoRA training didn't freeze the vision encoder and rejected packed patches |
| | [#2479](https://github.com/Neywa-Labs/mlx-vlm/pull/2479) | Documented video input for `apply_chat_template` |
| **NVIDIA NeMo Agent Toolkit** | [#2476](https://github.com/NVIDIA/NeMo-Agent-Toolkit/pull/2476) | MCP service-account tokens had a timezone-naive expiry, so no credentials were sent |
| **AWS Strands Agents** | [#5016](https://github.com/strands-agents/harness-sdk/pull/5016) | Warnings were logged for every earlier message on every request (N² log lines) |

Google ADK merges through Copybara, so those PRs show as "Closed" on GitHub. The commit links point to the merged change.

### Under review

| Project | PRs | Highlights |
|---|---|---|
| **AWS SageMaker Python SDK** | [45](https://github.com/aws/sagemaker-python-sdk/pulls?q=is%3Apr+author%3AAkshayShah03) | Bugs in the v3 SDK across training, serving, pipelines and core, such as a KMS key sent as a customer encryption key, `mpirun -np` given the wrong rank count, and `AsyncPredictor` hanging instead of timing out |
| **Ollama** | [10](https://github.com/ollama/ollama/pulls?q=is%3Apr+author%3AAkshayShah03) | Responses API text dropped next to tool calls, blobs not pruned after pull or copy, a race in blob-download cancellation |
| **Tesla** | [7](https://github.com/search?q=is%3Apr+author%3AAkshayShah03+org%3Ateslamotors&type=pullrequests) | [vehicle-command #528](https://github.com/teslamotors/vehicle-command/pull/528) wake-up polling, [#537](https://github.com/teslamotors/vehicle-command/pull/537) cabin overheat level; [fleet-telemetry #581](https://github.com/teslamotors/fleet-telemetry/pull/581) Kafka client errors, [#585](https://github.com/teslamotors/fleet-telemetry/pull/585) statsd tags; [fixed-containers #246](https://github.com/teslamotors/fixed-containers/pull/246) |
| **MLX-VLM** | [4](https://github.com/Neywa-Labs/mlx-vlm/pulls?q=is%3Apr+author%3AAkshayShah03+is%3Aopen) | Qwen3-VL embedding position IDs, GLM-OCR image input, pooling options |
| **Google ADK** | [2](https://github.com/google/adk-python/pulls?q=is%3Apr+author%3AAkshayShah03+is%3Aopen) | Workflow resume replay, keeping finished parallel tool results on abort |
| **Anthropic Claude Agent SDK** | [2](https://github.com/anthropics/claude-agent-sdk-python/pulls?q=is%3Apr+author%3AAkshayShah03) | A client disconnect race, recursive TypedDict schemas for MCP tools |
| **NVIDIA** | 2 | [garak #2355](https://github.com/NVIDIA/garak/pull/2355) reproducible seeded prompts, [warp #2147](https://github.com/NVIDIA/warp/pull/2147) empty trailing slices |
| **AWS Strands Agents** | [2](https://github.com/strands-agents/harness-sdk/pulls?q=is%3Apr+author%3AAkshayShah03+is%3Aopen) | Contributor setup docs |

### Issues and triage

- Filed 35 bug reports with reproductions: [Google ADK](https://github.com/google/adk-python/issues?q=author%3AAkshayShah03) (14), [MLX-VLM](https://github.com/Neywa-Labs/mlx-vlm/issues?q=author%3AAkshayShah03) (4), [NVIDIA](https://github.com/search?q=is%3Aissue+author%3AAkshayShah03+org%3ANVIDIA&type=issues) (4), [Ollama](https://github.com/ollama/ollama/issues?q=author%3AAkshayShah03) (3), [Tesla](https://github.com/teslamotors/fleet-telemetry/issues?q=author%3AAkshayShah03) (3), [Strands](https://github.com/strands-agents/harness-sdk/issues?q=author%3AAkshayShah03) (3), and others.
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

<sub>Counts as of November 2026.</sub>
