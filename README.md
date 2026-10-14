# SDE Interview and Prep Roadmap

## Overview

A comprehensive, checklist-driven roadmap for preparing for **Software Development Engineer (SDE), backend engineering, system design, and Agentic AI interviews**. It brings together core computer science fundamentals and modern AI engineering topics in one place, with a focus on understanding concepts, practicing implementation, and explaining technical trade-offs clearly in interviews.

The roadmap covers **Agentic AI, LLM Engineering, and AI System Design, Algorithms, Cloud, DevOps & Infrastructure, Data Structures, Databases, Low-Level Design & Object-Oriented Design, Networking, Operating Systems, Problem-solving and Coding, Programming Languages and Concepts, Security Engineering & Authentication, System Architecture, System Design, Testing, Reliability & Observability, Version control System**. Alongside the topic checklists, it includes an **interview-readiness assessment** to help turn preparation into measurable progress.

Use the expandable checklists to track what you've studied, revisit weak areas, and prepare at your own pace. This repository is also a shared learning resource: contributions, corrections, and useful learning materials are welcome.

## Domains and Topics

**Overall progress: 1 / 829 topics completed (0.1%)**

![Overall progress](assets/progress/overall.svg)

Progress bars and counts are generated from checklist states when you commit changes to GitHub. The interview-readiness self-assessment is excluded.

**Priority key:**  
**`P0`** = essential / most frequently useful · **`P1`** = important · **`P2`** = advanced or lower-frequency. These priorities are interview-prep recommendations, not difficulty ratings.

### 1. Agentic AI, LLM Engineering, and AI System Design

![Agentic AI, LLM Engineering, and AI System Design progress](assets/progress/domain-1.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **Agent Fundamentals and Decision-Making** **`P1`**
  - [ ] Agent autonomy levels and choosing the minimum sufficient autonomy **`P1`**
  - [ ] Core agent loop: observe, decide, act, inspect results, and stop **`P0`**
  - [ ] Deterministic workflow nodes vs. model-selected actions **`P1`**
  - [ ] Human-in-the-loop reviews, approvals, and escalation **`P0`**
  - [ ] LLM workflows vs. autonomous agents: when each is appropriate **`P0`**
  - [ ] Planning: task breakdown, dependency graphs, and replanning **`P0`**
  - [ ] Reasoning-and-acting patterns (e.g., ReAct) and tool-use loops **`P0`**
  - [ ] Reflection, critique, self-correction, and their limitations **`P1`**
  - [ ] Short-term context vs. persistent long-term memory **`P1`**
  - [ ] Stop conditions, turn budgets, iteration limits, and fallback paths **`P1`**
- [ ] **Agentic Frameworks and Orchestration** **`P1`**
  - [ ] Compare LangGraph, AutoGen, CrewAI, and SDK-native agent approaches **`P2`**
  - [ ] Conditional branching, map-reduce, parallel fan-out, and fan-in **`P1`**
  - [ ] Durable execution and recovering from mid-workflow failures **`P0`**
  - [ ] LangChain: models, tools, retrievers, and integrations **`P0`**
  - [ ] LangGraph: checkpointing, persistence, interrupts, and resumability **`P0`**
  - [ ] LangGraph: retries, error recovery, and human approval flows **`P0`**
  - [ ] LangGraph: state graphs, nodes, edges, routing, and reducers **`P0`**
  - [ ] LangSmith: traces, datasets, evaluations, and debugging **`P0`**
  - [ ] Stateless service architecture vs. stateful agent execution **`P1`**
  - [ ] Workflow orchestration vs. agent orchestration **`P1`**
- [ ] **Agentic System Design Interview Practice** **`P0`**
  - [ ] Calculate throughput, per-request token cost, and p95 latency **`P0`**
  - [ ] Compare a deterministic pipeline with an autonomous agent for the same task **`P1`**
  - [ ] Design a code-review / bug-triage agent with repository tools **`P1`**
  - [ ] Design a CSV/Excel validation agent with rules and external data checks **`P1`**
  - [ ] Design a customer-support agent with search and human handoff **`P1`**
  - [ ] Design a document research agent that produces cited answers **`P1`**
  - [ ] Design a job-search agent that finds, evaluates, and ranks openings **`P0`**
  - [ ] Design a multi-agent research workflow with parallel specialists **`P1`**
  - [ ] Design an incident-response assistant with read-only diagnostics **`P1`**
  - [ ] Explain failure modes, state recovery, evaluation, and monitoring **`P0`**
  - [ ] Explain how you would enforce approvals on write/side-effect tools **`P1`**
- [ ] **Evaluation and Testing** **`P0`**
  - [ ] Agent trajectory tests: tool selection, ordering, and stop behavior **`P1`**
  - [ ] Defining success criteria before building an agent **`P1`**
  - [ ] End-to-end tests for complete multi-step agent workflows **`P1`**
  - [ ] Golden datasets and representative real-world test cases **`P1`**
  - [ ] Human review, pairwise comparisons, and error taxonomy **`P1`**
  - [ ] Integration tests with mocked external tools and APIs **`P0`**
  - [ ] LLM-as-judge: rubrics, calibration, bias, and limitations **`P0`**
  - [ ] Measures: task success, groundedness, tool correctness, cost, and latency **`P0`**
  - [ ] Offline evaluation vs. online experiments and A/B testing **`P0`**
  - [ ] Regression tests after prompt, tool, model, or retrieval changes **`P0`**
  - [ ] Robustness testing: invalid inputs, ambiguous tasks, and tool outages **`P1`**
  - [ ] Unit testing tools, nodes, validators, and deterministic logic **`P0`**
- [ ] **Hands-On Interview Readiness** **`P1`**
  - [ ] Add persistent state and resume execution after process restart **`P0`**
  - [ ] Add retries, timeouts, human approval, and safe fallback behavior **`P0`**
  - [ ] Build a RAG pipeline with citations and retrieval evaluation **`P0`**
  - [ ] Build an agent with at least two tools and schema-validated outputs **`P1`**
  - [ ] Create a small evaluation dataset and measure task success **`P0`**
  - [ ] Demonstrate a cost/latency optimization with before-and-after metrics **`P0`**
  - [ ] Explain one end-to-end project: architecture, trade-offs, impact, and lessons **`P1`**
  - [ ] Practice whiteboarding an agentic architecture in 30–45 minutes **`P1`**
  - [ ] Prepare answers for: "Why agents instead of workflows?" and "When should an agent stop?" **`P1`**
  - [ ] Trace and debug an incorrect tool-selection decision **`P0`**
- [ ] **LLM and Generative AI Fundamentals** **`P0`**
  - [ ] Closed-weight vs. open-weight models; hosted APIs vs. self-hosting **`P0`**
  - [ ] Hallucinations, uncertainty, grounding, and model limitations **`P1`**
  - [ ] Inference parameters: temperature, top-p, seed, and stop sequences **`P1`**
  - [ ] Model selection: capability, latency, context, cost, privacy, and deployment **`P0`**
  - [ ] Pretraining vs. instruction tuning vs. fine-tuning vs. alignment **`P2`**
  - [ ] Prompting vs. RAG vs. fine-tuning: decision criteria and trade-offs **`P0`**
  - [ ] Tokens, tokenization, context windows, and output limits **`P1`**
  - [ ] Transformers, attention, embeddings, and autoregressive generation **`P0`**
- [ ] **Memory, State, and Context Management** **`P1`**
  - [ ] Context compaction, summaries, and memory retrieval **`P0`**
  - [ ] Conversation state and checkpointing **`P1`**
  - [ ] Memory persistence: in-memory, databases, and durable checkpoint stores **`P1`**
  - [ ] Memory relevance, aging, deletion, and conflict resolution **`P1`**
  - [ ] Multi-replica deployments and shared state consistency **`P1`**
  - [ ] Privacy-aware memory retention and data minimization **`P1`**
  - [ ] Session isolation and user/tenant scoping **`P1`**
  - [ ] Working memory, episodic memory, semantic memory, and user preferences **`P1`**
- [ ] **Multi-Agent Systems** **`P1`**
  - [ ] Agent-to-agent communication and typed message contracts **`P0`**
  - [ ] Avoiding unnecessary agent proliferation and coordination overhead **`P1`**
  - [ ] Conflicting answers, arbitration, and consensus limits **`P1`**
  - [ ] Handoffs, delegation, and task ownership **`P1`**
  - [ ] Parallel agents, race conditions, and result aggregation **`P0`**
  - [ ] Shared state vs. agent-specific state **`P1`**
  - [ ] Single-agent vs. multi-agent trade-offs **`P1`**
  - [ ] Supervisor/worker and coordinator/specialist patterns **`P1`**
- [ ] **Production Reliability and Observability** **`P1`**
  - [ ] Cache strategies: prompt, response, embedding, and retrieval caching **`P0`**
  - [ ] Circuit breakers, dead-letter queues, and recovery workflows **`P0`**
  - [ ] Cost optimization: smaller models, batching, caching, and routing **`P1`**
  - [ ] End-to-end distributed traces for prompts, model calls, and tools **`P0`**
  - [ ] Logs, metrics, dashboards, and actionable alerting **`P0`**
  - [ ] Model and prompt versioning, release controls, and rollback **`P1`**
  - [ ] Provider outages, failover models, and graceful degradation **`P1`**
  - [ ] Request queuing, concurrency limits, and backpressure **`P0`**
  - [ ] Retry storms, duplicate side effects, and idempotency keys **`P0`**
  - [ ] SLA/SLO design and incident investigation **`P0`**
  - [ ] Streaming responses, cancellation, and timeout handling **`P1`**
  - [ ] Token usage, per-step cost, and latency budgets **`P0`**
- [ ] **Prompt Engineering and Structured Outputs** **`P1`**
  - [ ] Function/tool calling: schema design, argument validation, and error handling **`P0`**
  - [ ] Handling malformed outputs, refusals, and partial completions **`P1`**
  - [ ] Injection-resistant prompt design and explicit trust boundaries **`P1`**
  - [ ] Managing long context, truncation, summarization, and irrelevant context **`P1`**
  - [ ] Prompt templates, versioning, regression testing, and reproducibility **`P1`**
  - [ ] Structured output with JSON Schema and type validation **`P1`**
  - [ ] System, developer, user, and tool messages; instruction priority **`P1`**
  - [ ] Zero-shot, few-shot, role prompting, and task decomposition **`P1`**
- [ ] **Retrieval-Augmented Generation (RAG)** **`P0`**
  - [ ] Answer evaluation: faithfulness, factual correctness, and relevance **`P0`**
  - [ ] Chunking approaches: fixed-size, semantic, hierarchical, and overlap **`P1`**
  - [ ] Dense vs. sparse retrieval (BM25) and hybrid search **`P0`**
  - [ ] Embeddings: similarity metrics, dimension, and model selection **`P0`**
  - [ ] Grounded responses, source citations, and abstention when evidence is missing **`P1`**
  - [ ] Ingestion pipelines: parsing, cleaning, deduplication, and metadata **`P1`**
  - [ ] Multi-tenant retrieval, ACL-aware filtering, and data freshness **`P0`**
  - [ ] Query rewriting, expansion, routing, and decomposition **`P1`**
  - [ ] RAG vs. long-context prompting vs. fine-tuning: when to use which **`P0`**
  - [ ] Reranking, contextual compression, and top-k selection **`P1`**
  - [ ] Retrieval evaluation: recall\@k, precision\@k, MRR, and nDCG **`P0`**
  - [ ] Vector databases and indexing / update / deletion strategies **`P0`**
  - [ ] Vector indexes: approximate nearest neighbors, HNSW, and IVF **`P0`**
- [ ] **Security, Privacy, and Safety** **`P1`**
  - [ ] Data exfiltration threats and unsafe tool execution **`P1`**
  - [ ] Defense in depth; why instructions alone are not security boundaries **`P1`**
  - [ ] Least-privilege agent identities and scoped credentials **`P1`**
  - [ ] Output validation and policy enforcement before external actions **`P1`**
  - [ ] PII detection, redaction, encryption, and retention policies **`P0`**
  - [ ] Prompt injection: direct and indirect attacks via retrieved content/tools **`P0`**
  - [ ] Responsible AI: bias, misuse, human oversight, and transparency **`P1`**
  - [ ] Sandboxing code execution and restricting network/file access **`P0`**
  - [ ] Tenant isolation and permission-aware retrieval **`P0`**
  - [ ] Tool allowlists, confirmation for destructive actions, and audit trails **`P1`**
- [ ] **Tool Use, Integrations, and Protocols** **`P1`**
  - [ ] API authentication, authorization, least privilege, and secret handling **`P0`**
  - [ ] Approval gates for irreversible or high-impact actions **`P1`**
  - [ ] External search, database queries, code execution, and file tools **`P1`**
  - [ ] Idempotent operations, retries, backoff, timeouts, and rate limits **`P0`**
  - [ ] Model Context Protocol (MCP): clients, servers, tools, and resources **`P1`**
  - [ ] Parallel tool execution vs. sequential dependencies **`P1`**
  - [ ] Tool argument schemas and input/output contracts **`P0`**
  - [ ] Tool call audit logs and replay/debugging **`P0`**
  - [ ] Tool registry/discovery and selecting the right tool for a task **`P1`**
  - [ ] Tool result validation, sanitization, and handling untrusted content **`P1`**

</details>


### 2. Algorithms

![Algorithms progress](assets/progress/domain-2.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **Divide and Conquer** **`P1`**

  - [ ] Binary Search **`P0`**

  - [ ] Closest Pair of Points Problem **`P1`**

  - [ ] Cooley–Tukey Fast Fourier Transform (FFT) **`P2`**

  - [ ] Finding Maximum Subarray Sum (Kadane's Algorithm) **`P0`**

  - [ ] Finding Peak Element in 1D/2D Array **`P0`**

  - [ ] Karatsuba Algorithm (for Fast Multiplication) **`P2`**

  - [ ] Merge Sort **`P0`**

  - [ ] Quick Sort **`P0`**

  - [ ] Strassen's Matrix Multiplication **`P2`**

- [ ] **Dynamic Programming** **`P0`**

  - [ ] 0/1 Knapsack Problem **`P0`**

  - [ ] Coin Change Problem **`P0`**

  - [ ] Edit Distance **`P1`**

  - [ ] Fibonacci Series **`P1`**

  - [ ] Longest Common Subsequence (LCS) **`P1`**

  - [ ] Longest Increasing Subsequence (LIS) **`P1`**

  - [ ] Matrix Chain Multiplication **`P1`**

  - [ ] Memoization **`P0`**

  - [ ] Rod Cutting Problem **`P1`**

  - [ ] Shortest Path Problems (e.g., Dijkstra's Algorithm using DP) **`P1`**

  - [ ] Subset Sum Problem **`P1`**

  - [ ] Tabulation **`P0`**

- [ ] **Greedy Algorithms** **`P0`**

  - [ ] Activity Selection Problem **`P1`**

  - [ ] Dijkstra's Algorithm (for Single Source Shortest Path) **`P1`**

  - [ ] Fractional Knapsack Problem **`P0`**

  - [ ] Greedy Coloring of Graphs **`P0`**

  - [ ] Greedy Set Cover **`P0`**

  - [ ] Huffman Coding **`P1`**

  - [ ] Job Sequencing with Deadlines **`P1`**

  - [ ] Kruskal's Algorithm (for Minimum Spanning Tree) **`P0`**

  - [ ] Prim's Algorithm (for Minimum Spanning Tree) **`P0`**

- [ ] **Searching Algorithms**: **`P0`**

  - [ ] Binary Search **`P0`**

  - [ ] Breadth-First Search (BFS) **`P0`**

  - [ ] Depth-First Search (DFS) **`P0`**

  - [ ] Exponential Search **`P1`**

  - [ ] Fibonacci Search **`P2`**

  - [ ] Hashing (Hash Table) **`P0`**

  - [ ] Interpolation Search **`P2`**

  - [ ] Jump Search **`P2`**

  - [ ] Linear Search **`P1`**

  - [ ] Ternary Search **`P1`**

- [ ] **Sorting Algorithms**: **`P0`**

  - [ ] Bitonic Sort **`P2`**

  - [ ] Bubble Sort **`P1`**

  - [ ] Bucket Sort **`P1`**

  - [ ] Cocktail Shaker Sort **`P2`**

  - [ ] Comb Sort **`P2`**

  - [ ] Counting Sort **`P1`**

  - [ ] Cycle Sort **`P2`**

  - [ ] Gnome Sort **`P2`**

  - [ ] Heap Sort **`P0`**

  - [ ] Insertion Sort **`P1`**

  - [ ] Merge Sort **`P0`**

  - [ ] Pancake Sort **`P2`**

  - [ ] Quick Sort **`P0`**

  - [ ] Radix Sort **`P1`**

  - [ ] Selection Sort **`P1`**

  - [ ] Shell Sort **`P2`**

  - [ ] Strand Sort **`P2`**

  - [ ] Tim Sort **`P1`**

- [ ] **String Algorithms**: **`P1`**

  - [ ] Aho-Corasick Algorithm **`P1`**

  - [ ] Baker-Bird Algorithm **`P2`**

  - [ ] Boyer-Moore Algorithm **`P1`**

  - [ ] Breadth-First Search (BFS) in a Trie **`P0`**

  - [ ] Burrows-Wheeler Transform (BWT) **`P2`**

  - [ ] Count and Say Sequence **`P2`**

  - [ ] Depth-First Search (DFS) in a Trie **`P0`**

  - [ ] Edit Distance (Levenshtein Distance) **`P1`**

  - [ ] Hamming Distance **`P2`**

  - [ ] Knuth-Morris-Pratt (KMP) Algorithm **`P1`**

  - [ ] Longest Common Prefix (LCP) Array **`P0`**

  - [ ] Longest Common Subsequence **`P1`**

  - [ ] Longest Common Substring **`P1`**

  - [ ] Longest Palindromic Substring **`P1`**

  - [ ] Longest Repeated Substring **`P1`**

  - [ ] Manacher's Algorithm **`P2`**

  - [ ] Palindrome Check **`P1`**

  - [ ] Rabin-Karp Algorithm **`P1`**

  - [ ] Shortest Common Supersequence **`P1`**

  - [ ] String Hashing **`P0`**

  - [ ] Suffix Array Construction **`P0`**

  - [ ] Suffix Automaton **`P2`**

  - [ ] Suffix Tree Construction **`P2`**

  - [ ] Trie (Prefix Tree) Insertion and Search **`P0`**

  - [ ] Z-Algorithm **`P1`**

</details>


### 3. Cloud, DevOps & Infrastructure

![Cloud, DevOps & Infrastructure progress](assets/progress/domain-3.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **AWS Compute and Application Hosting** **`P1`**

  - [ ] API Gateway and service integration patterns **`P0`**

  - [ ] AWS Lambda: triggers, cold starts, concurrency, and idempotency **`P0`**

  - [ ] EC2: instance families, AMIs, security groups, and auto scaling groups **`P1`**

  - [ ] ECS/Fargate vs. EKS vs. EC2 vs. Lambda deployment decisions **`P0`**

  - [ ] Elastic Load Balancing (ALB/NLB) and health checks **`P0`**

- [ ] **AWS Storage and Databases** **`P0`**

  - [ ] DynamoDB: partition/sort keys, GSIs, hot partitions, capacity modes **`P0`**

  - [ ] EBS vs. EFS vs. S3; durability and consistency trade-offs **`P0`**

  - [ ] ElastiCache/Redis: cache invalidation, eviction, and replication **`P0`**

  - [ ] RDS/Aurora: backups, replicas, failover, and connection pooling **`P1`**

  - [ ] S3: object versioning, encryption, lifecycle policies, and presigned URLs **`P0`**

- [ ] **CI/CD and Release Engineering** **`P1`**

  - [ ] Artifact provenance, dependency scanning, and supply-chain security **`P2`**

  - [ ] Blue-green, canary, rolling, and feature-flag releases **`P1`**

  - [ ] Build/test/package/deploy pipelines and quality gates **`P1`**

  - [ ] GitHub Actions workflow syntax, runners, permissions, and artifacts **`P1`**

  - [ ] Rollbacks, database migrations, and backward compatibility **`P1`**

- [ ] **Cloud Computing Fundamentals** **`P1`**

  - [ ] High availability vs. disaster recovery; RTO and RPO **`P1`**

  - [ ] Horizontal vs. vertical scaling; stateless vs. stateful services **`P1`**

  - [ ] IaaS vs. PaaS vs. SaaS; shared responsibility model **`P1`**

  - [ ] Public, private, hybrid, and multi-cloud trade-offs **`P2`**

  - [ ] Regions, availability zones, fault domains, and global services **`P1`**

- [ ] **Cloud Cost, Capacity, and Operations** **`P1`**

  - [ ] Capacity planning using throughput, utilization, and p95 latency **`P0`**

  - [ ] Cost allocation, tagging, budgets, and cost observability **`P1`**

  - [ ] Multi-region architecture, backup/restore drills, and runbooks **`P0`**

  - [ ] Operational trade-offs: managed services vs. self-hosting **`P1`**

  - [ ] Reserved capacity vs. on-demand vs. spot instances **`P1`**

- [ ] **Cloud Messaging and Eventing** **`P1`**

  - [ ] EventBridge event buses, rules, and event routing **`P1`**

  - [ ] Kinesis/Kafka trade-offs for streaming workloads **`P1`**

  - [ ] Retries, poison messages, deduplication, and backpressure **`P0`**

  - [ ] SNS pub/sub, subscription filters, and fan-out **`P1`**

  - [ ] SQS standard vs. FIFO; visibility timeout; dead-letter queues **`P0`**

- [ ] **Cloud Networking and Identity** **`P1`**

  - [ ] Cloud DNS, TLS termination, CDN, and WAF integration **`P0`**

  - [ ] IAM roles/policies, least privilege, and temporary credentials **`P0`**

  - [ ] Private endpoints, peering, transit gateways, and hybrid connectivity **`P1`**

  - [ ] Security groups vs. network ACLs **`P1`**

  - [ ] VPC, public/private subnets, route tables, NAT and internet gateways **`P1`**

- [ ] **Containers and Docker** **`P0`**

  - [ ] Build reproducibility, caching, and image size optimization **`P1`**

  - [ ] Container networking, volumes, resource limits, and isolation **`P1`**

  - [ ] Image scanning, non-root containers, pinned dependencies **`P1`**

  - [ ] Images, layers, registries, Dockerfiles, and multi-stage builds **`P0`**

- [ ] **Infrastructure as Code (IaC)** **`P1`**

  - [ ] CloudFormation/CDK vs. Terraform: trade-offs **`P0`**

  - [ ] Environment parity and reproducible provisioning **`P1`**

  - [ ] Managing secrets and sensitive outputs in IaC **`P1`**

  - [ ] Remote state, locking, drift detection, and lifecycle management **`P1`**

  - [ ] Terraform providers, resources, modules, plans, and state **`P2`**

- [ ] **Kubernetes Fundamentals and Operations** **`P0`**

  - [ ] ConfigMaps, Secrets, namespaces, RBAC, and service accounts **`P1`**

  - [ ] Persistent volumes, statefulsets, and disruption budgets **`P1`**

  - [ ] Pods, deployments, replicasets, services, and ingress **`P1`**

  - [ ] Readiness/liveness/startup probes and rolling deployments **`P1`**

  - [ ] Requests/limits, HPA, cluster autoscaler, and scheduling **`P1`**

  - [ ] Troubleshooting CrashLoopBackOff, pending pods, and service discovery **`P0`**

</details>


### 4. Data Structures

![Data Structures progress](assets/progress/domain-4.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] [**Arrays**](./Data%20Structures/Arrays.md) **`P0`**

- [ ] **Graphs** **`P0`**

  - [ ] Acyclic graphs **`P0`**

  - [ ] Bipartite graphs **`P0`**

  - [ ] Directed graphs **`P0`**

  - [ ] Graphs with special properties (e.g., planar graphs, Eulerian graphs) **`P0`**

  - [ ] Representations (adjacency matrix, adjacency list) **`P1`**

    - [ ] Edge list **`P1`**

    - [ ] Incidence matrix **`P2`**

  - [ ] Spanning trees (Minimum Spanning Tree, Maximum Spanning Tree) **`P0`**

  - [ ] Traversal algorithms (DFS, BFS) **`P0`**

  - [ ] Weighted graphs **`P0`**

- [ ] **Hash Tables** **`P0`**

  - [ ] Bloom Filters **`P2`**

  - [ ] Collision resolution techniques (chaining, open addressing) **`P1`**

  - [ ] Count-Min Sketch **`P2`**

  - [ ] Cuckoo Hashing **`P0`**

  - [ ] Hash functions **`P0`**

  - [ ] Perfect Hashing **`P2`**

  - [ ] Robin Hood Hashing **`P0`**

- [ ] [**Linked Lists**](./Data%20Structures/LinkedList.md) **`P0`**

  - [ ] Circular linked lists **`P0`**

  - [ ] Doubly linked lists **`P0`**

    - [ ] Circular doubly linked lists **`P0`**

  - [ ] Singly linked lists **`P0`**

    - [ ] Circularly linked lists **`P0`**

    - [ ] Lock-free linked lists **`P0`**

  - [ ] Skip lists **`P1`**

  - [ ] Unrolled linked lists **`P2`**

- [ ] **Queues** **`P0`**

  - [ ] Applications (e.g., BFS, job scheduling) **`P0`**

  - [ ] Implementations (e.g., array-based, linked list-based, priority queues) **`P0`**

    - [ ] Circular queue **`P0`**

    - [ ] Double-ended queue (Deque) **`P1`**

- [ ] **Stacks** **`P0`**

  - [ ] Applications (e.g., expression evaluation, backtracking) **`P0`**

  - [ ] Implementations using arrays and linked lists **`P0`**

    - [ ] Array-based stack **`P0`**

    - [ ] Linked list-based stack **`P0`**

  - [ ] Priority stacks **`P2`**

- [ ] **Trees** **`P0`**

  - [ ] AVL Trees **`P0`**

  - [ ] B-Trees **`P0`**

  - [ ] Binary Search Trees (BST) **`P0`**

    - [ ] Self-balancing BST **`P1`**

      - [ ] Scapegoat tree **`P2`**

      - [ ] Tango tree **`P2`**

  - [ ] Binary Trees **`P0`**

    - [ ] Complete binary tree **`P0`**

    - [ ] Full binary tree **`P0`**

    - [ ] Perfect binary tree **`P2`**

  - [ ] Heap Trees (min-heap, max-heap) **`P0`**

  - [ ] Radix Trees **`P2`**

  - [ ] Red-Black Trees **`P0`**

  - [ ] Splay Trees **`P2`**

  - [ ] Trie **`P0`**

</details>


### 5. Databases

![Databases progress](assets/progress/domain-5.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **ACID properties** **`P0`**

  - [ ] Atomicity **`P1`**

  - [ ] Consistency **`P1`**

  - [ ] Durability **`P1`**

  - [ ] Isolation **`P1`**

- [ ] **Database design and optimization** **`P1`**

  - [ ] Materialized views **`P1`**

  - [ ] Partitioning **`P0`**

- [ ] **Indexing** **`P0`**

  - [ ] B-tree **`P0`**

  - [ ] B+ tree **`P0`**

  - [ ] Bitmap Indexing **`P0`**

- [ ] **NoSQL databases** **`P0`**

  - [ ] Examples **`P1`**

    - [ ] MongoDB Interview Questions **`P1`**

    - [ ] Redis Interview Questions **`P1`**

  - [ ] Types **`P1`**

    - [ ] Column-family **`P1`**

    - [ ] Document-based **`P1`**

    - [ ] Graph **`P0`**

    - [ ] Key-value **`P1`**

- [ ] **Relational databases (SQL)** **`P0`**

  - [ ] Database Constraints **`P1`**

    - [ ] Check constraint **`P1`**

    - [ ] Default constraint **`P1`**

    - [ ] Foreign key **`P1`**

    - [ ] Primary key **`P1`**

    - [ ] Unique constraint **`P1`**

  - [ ] Joins **`P0`**

    - [ ] Cross joins **`P0`**

    - [ ] Inner joins **`P0`**

    - [ ] Outer joins (left, right, full) **`P0`**

  - [ ] Normalization forms **`P0`**

    - [ ] Boyce-Codd Normal Form (BCNF) **`P1`**

    - [ ] First Normal Form (1NF) **`P1`**

    - [ ] Second Normal Form (2NF) **`P1`**

    - [ ] Third Normal Form (3NF) **`P1`**

  - [ ] SQL Data Control Language (DCL) **`P0`**

    - [ ] GRANT statement **`P1`**

    - [ ] REVOKE statement **`P1`**

  - [ ] SQL Data Definition Language (DDL) **`P0`**

    - [ ] ALTER statement **`P1`**

    - [ ] CREATE statement **`P1`**

    - [ ] DROP statement **`P1`**

  - [ ] SQL Data Manipulation Language (DML) **`P0`**

    - [ ] Control-of-flow language (e.g., CASE, IF-ELSE) **`P1`**

    - [ ] DELETE statement **`P1`**

    - [ ] Explicit vs. Implicit transactions **`P0`**

    - [ ] INSERT statement **`P1`**

    - [ ] MERGE statement **`P1`**

    - [ ] SELECT statement **`P1`**

    - [ ] TRUNCATE statement **`P1`**

    - [ ] UPDATE statement **`P1`**

    - [ ] UPSERT operations **`P1`**

  - [ ] SQL Data Query Language (DQL) **`P0`**

    - [ ] Aggregate functions (e.g., SUM, AVG, COUNT) **`P1`**

    - [ ] GROUP BY and HAVING clauses **`P1`**

    - [ ] Subqueries **`P1`**

    - [ ] Window functions **`P1`**

  - [ ] Stored Procedures and Functions **`P1`**

    - [ ] Creation **`P1`**

    - [ ] Execution **`P1`**

    - [ ] Parameters **`P1`**

  - [ ] Transaction Control **`P0`**

    - [ ] COMMIT statement **`P1`**

    - [ ] ROLLBACK statement **`P1`**

  - [ ] Triggers **`P1`**

    - [ ] Trigger execution order **`P1`**

    - [ ] Types of triggers (BEFORE, AFTER) **`P1`**

  - [ ] Views **`P1`**

    - [ ] Advantages and use cases **`P1`**

    - [ ] Materialized views vs. regular views **`P1`**

- [ ] **Transactions** **`P0`**

  - [ ] ACID properties in transactions **`P0`**

  - [ ] Isolation levels **`P1`**

    - [ ] Read Committed **`P1`**

    - [ ] Read Uncommitted **`P1`**

    - [ ] Repeatable Read **`P1`**

    - [ ] Serializable **`P1`**

</details>


### 6. Low-Level Design & Object-Oriented Design

![Low-Level Design & Object-Oriented Design progress](assets/progress/domain-6.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **API, Persistence, and Concurrency Design** **`P0`**

  - [ ] Data access layering, repositories, and transaction boundaries **`P0`**

  - [ ] Idempotent operations and safe retries in low-level APIs **`P0`**

  - [ ] Interface-first design and stable public contracts **`P0`**

  - [ ] Testability: dependency injection, mocks, and interface contracts **`P0`**

  - [ ] Thread safety, synchronization, immutability, and race prevention **`P0`**

  - [ ] Validation, domain errors, exceptions, and failure handling **`P0`**

- [ ] **Classic Low-Level Design Interview Problems** **`P1`**

  - [ ] Design a cache with LRU/LFU eviction **`P0`**

  - [ ] Design a chess or tic-tac-toe engine (rules, turns, extensibility) **`P1`**

  - [ ] Design a file system / in-memory directory tree **`P0`**

  - [ ] Design a library management system (loans, reservations, fines) **`P1`**

  - [ ] Design a logging framework (appenders, levels, concurrency) **`P0`**

  - [ ] Design a movie ticket booking system (seat locking, expiry) **`P1`**

  - [ ] Design a notification framework with channels and retries **`P0`**

  - [ ] Design a parking lot (spots, pricing, tickets, concurrency) **`P0`**

  - [ ] Design a rate limiter (strategy interfaces, pluggable algorithms) **`P0`**

  - [ ] Design a splitwise-style expense sharing system **`P1`**

  - [ ] Design a vending machine (inventory, payment, state transitions) **`P1`**

  - [ ] Design an elevator system (scheduling, requests, states) **`P1`**

- [ ] **Design Patterns in Practice** **`P0`**

  - [ ] Adapter / Facade for external integration **`P1`**

  - [ ] Builder for complex object construction **`P1`**

  - [ ] Command pattern for undo, queues, and operations **`P1`**

  - [ ] Decorator / Proxy for behavior interception **`P1`**

  - [ ] Dependency injection and inversion of control **`P1`**

  - [ ] Factory / Abstract Factory for object creation and extensibility **`P0`**

  - [ ] Observer / Pub-Sub for state-change notifications **`P0`**

  - [ ] Recognize when **not** to introduce a design pattern **`P0`**

  - [ ] Repository / Unit of Work for persistence boundaries **`P1`**

  - [ ] State pattern for workflow transitions **`P1`**

  - [ ] Strategy for configurable behavior **`P0`**

- [ ] **Implementation and Review** **`P1`**

  - [ ] Demonstrate a requirements change without rewriting the design **`P0`**

  - [ ] Discuss complexity, extensibility, and maintainability trade-offs **`P0`**

  - [ ] Review edge cases, invariants, and failure behavior **`P0`**

  - [ ] Write compilable, testable code for a scoped LLD problem **`P1`**

- [ ] **Object-Oriented Design Fundamentals** **`P0`**

  - [ ] Classes, objects, interfaces, abstract classes, and composition **`P0`**

  - [ ] Cohesion, coupling, separation of concerns, and modularity **`P1`**

  - [ ] DRY, KISS, YAGNI, and premature abstraction trade-offs **`P0`**

  - [ ] Encapsulation, abstraction, inheritance, and polymorphism in design **`P0`**

  - [ ] Favor composition over inheritance; identify misuse of hierarchies **`P0`**

  - [ ] SOLID principles applied to practical classes and services **`P0`**

- [ ] **Requirements and Domain Modeling** **`P0`**

  - [ ] Clarify functional/non-functional requirements and scope **`P0`**

  - [ ] Define extension points without overengineering **`P1`**

  - [ ] Identify entities, value objects, aggregates, and invariants **`P1`**

  - [ ] Model relationships, ownership, object lifecycles, and state transitions **`P1`**

  - [ ] Translate use cases into classes, interfaces, and interactions **`P0`**

- [ ] **UML and Communication** **`P1`**

  - [ ] Class diagrams: associations, aggregation, composition, inheritance **`P0`**

  - [ ] Explain trade-offs while iterating the model with an interviewer **`P1`**

  - [ ] Sequence diagrams: method calls, boundaries, and async events **`P0`**

  - [ ] State machine diagrams: transitions, guards, and terminal states **`P1`**

</details>


### 7. Networking

![Networking progress](assets/progress/domain-7.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **DNS (Domain Name System)** **`P0`**

  - [ ] Resolution process **`P0`**

- [ ] **HTTP protocol** **`P0`**

  - [ ] Request methods (GET, POST, etc.) **`P1`**

  - [ ] Status codes **`P1`**

- [ ] **Routing algorithms** **`P1`**

  - [ ] Shortest Path algorithms (Dijkstra's, Bellman-Ford) **`P2`**

- [ ] **TCP/IP stack** **`P0`**

  - [ ] OSI model layers **`P1`**

  - [ ] TCP vs. UDP **`P0`**

</details>


### 8. Operating Systems

![Operating Systems progress](assets/progress/domain-8.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **Deadlock detection and prevention** **`P0`**

- [ ] **File systems** **`P1`**

  - [ ] Distributed file systems (HDFS, Ceph) **`P0`**

  - [ ] File system encryption **`P0`**

  - [ ] Journaling file systems (ext3, ext4) **`P1`**

  - [ ] Network file systems (NFS, SMB) **`P1`**

- [ ] **Memory management** **`P1`**

  - [ ] Buddy memory allocation **`P1`**

  - [ ] Memory-mapped files **`P1`**

  - [ ] Page replacement algorithms (LRU, FIFO, Clock) **`P1`**

- [ ] **Processes** **`P0`**

- [ ] **Scheduling algorithms** **`P1`**

  - [ ] Earliest Deadline First (EDF) **`P1`**

  - [ ] Fair share scheduling **`P1`**

  - [ ] Weighted Fair Queuing (WFQ) **`P1`**

- [ ] **Thread synchronization mechanisms**: **`P0`**

  - [ ] Monitors **`P1`**

  - [ ] Mutexes **`P1`**

  - [ ] Semaphores **`P1`**

- [ ] **Threads** **`P0`**

</details>


### 9. Problem-solving and Coding

![Problem-solving and Coding progress](assets/progress/domain-9.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **Coding best practices** **`P1`**

  - [ ] Code readability **`P1`**

  - [ ] Code reusability **`P1`**

  - [ ] Code reviews **`P1`**

  - [ ] Error handling **`P1`**

  - [ ] Naming conventions **`P1`**

  - [ ] Testing **`P1`**

  - [ ] Version control (e.g., Git) **`P1`**

- [ ] **Coding techniques** **`P1`**

  - [ ] Backtracking **`P0`**

  - [ ] Binary search **`P0`**

  - [ ] Bit manipulation **`P1`**

  - [ ] Divide and conquer **`P1`**

  - [ ] Dynamic programming **`P0`**

  - [ ] Fast and slow pointers **`P0`**

  - [ ] Greedy algorithms **`P0`**

  - [ ] Hashing **`P0`**

  - [ ] Modular programming **`P1`**

  - [ ] Recursion **`P0`**

  - [ ] Sliding window **`P0`**

  - [ ] Two pointers **`P0`**

- [ ] **Debugging** **`P1`**

  - [ ] Debugger tools **`P1`**

  - [ ] Print debugging **`P1`**

  - [ ] Rubber duck debugging **`P1`**

- [ ] **Optimization** **`P1`**

  - [ ] Algorithmic optimization **`P1`**

  - [ ] Profiling tools **`P1`**

  - [ ] Space-time trade-offs **`P1`**

- [ ] **Problem-solving strategies** **`P1`**

  - [ ] Break it down **`P1`**

  - [ ] Implement the plan **`P1`**

  - [ ] Look for patterns **`P1`**

  - [ ] Make a plan **`P1`**

  - [ ] Solve a simpler problem **`P1`**

  - [ ] Test your solution **`P1`**

  - [ ] Understand the problem **`P1`**

- [ ] **Time and space complexity analysis** **`P0`**

  - [ ] Big O notation **`P0`**

  - [ ] Big Omega notation **`P0`**

  - [ ] Big Theta notation **`P1`**

  - [ ] Space complexity analysis **`P0`**

</details>


### 10. Programming Languages and Concepts

![Programming Languages and Concepts progress](assets/progress/domain-10.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **Asynchronous programming** **`P0`**

  - [ ] Callbacks **`P1`**

  - [ ] Coroutines **`P1`**

  - [ ] Futures **`P1`**

  - [ ] Promises **`P0`**

- [ ] **Concurrency** **`P0`**

  - [ ] Asynchronous programming **`P0`**

  - [ ] Deadlocks **`P0`**

  - [ ] Parallelism vs. Concurrency **`P0`**

  - [ ] Race conditions **`P0`**

  - [ ] Synchronization primitives (locks, mutexes, semaphores) **`P1`**

  - [ ] Thread safety **`P0`**

  - [ ] Threads vs. Processes **`P0`**

- [ ] **Design patterns** **`P0`**

  - [ ] Behavioral patterns **`P1`**

  - [ ] Creational patterns **`P1`**

  - [ ] Structural patterns **`P1`**

- [ ] **Error handling** **`P1`**

  - [ ] Error propagation **`P1`**

  - [ ] Error recovery **`P1`**

  - [ ] Exception handling mechanisms **`P1`**

  - [ ] Exception safety **`P1`**

  - [ ] Exceptions vs. Error codes **`P1`**

- [ ] **Functional programming** **`P1`**

  - [ ] Closures **`P1`**

  - [ ] Higher-order functions **`P1`**

  - [ ] Lambda expressions **`P0`**

  - [ ] Pure functions **`P1`**

  - [ ] Referential transparency **`P1`**

- [ ] **Functional vs. Imperative vs. Declarative programming** **`P1`**

- [ ] **Garbage collection** **`P0`**

  - [ ] Generational GC **`P1`**

  - [ ] Tracing vs. Reference counting **`P0`**

- [ ] **Lambda calculus** **`P2`**

- [ ] **Memory layout** **`P1`**

  - [ ] Data segment vs. Code segment **`P1`**

  - [ ] Stack vs. Heap memory allocation **`P0`**

- [ ] **Memory management** **`P1`**

  - [ ] Garbage collection algorithms (e.g., Mark and Sweep, Generational GC) **`P0`**

  - [ ] Manual vs. Automatic memory management **`P1`**

  - [ ] Stack vs. Heap **`P0`**

- [ ] **Networking** **`P1`**

  - [ ] Client-server architecture **`P1`**

  - [ ] Protocols (TCP, UDP) **`P0`**

  - [ ] Remote Procedure Call (RPC) **`P1`**

  - [ ] Sockets **`P1`**

- [ ] **Object-oriented programming (OOP)** **`P0`**

  - [ ] Abstraction **`P0`**

  - [ ] Composition vs. Inheritance **`P0`**

  - [ ] Encapsulation **`P0`**

  - [ ] Inheritance **`P0`**

  - [ ] Method overriding vs. Method overloading **`P1`**

  - [ ] Polymorphism **`P0`**

- [ ] **Programming paradigms** **`P1`**

  - [ ] Aspect-oriented programming **`P2`**

  - [ ] Declarative programming **`P1`**

  - [ ] Event-driven programming **`P0`**

  - [ ] Functional programming **`P1`**

  - [ ] Imperative programming **`P1`**

  - [ ] Object-oriented programming **`P0`**

  - [ ] Procedural programming **`P1`**

- [ ] **Recursion** **`P0`**

  - [ ] Anonymous recursion **`P2`**

  - [ ] Mutual recursion **`P2`**

  - [ ] Tail recursion **`P0`**

- [ ] **Regular expressions** **`P1`**

- [ ] **Type systems** **`P1`**

  - [ ] Nominal vs. Structural typing **`P1`**

  - [ ] Static vs. Dynamic typing **`P1`**

  - [ ] Strong vs. Weak typing **`P1`**

- [ ] **Virtual Memory** **`P1`**

  - [ ] Demand Paging **`P1`**

  - [ ] Page replacement algorithms (FIFO, LRU, Optimal) **`P1`**

</details>


### 11. Security Engineering & Authentication

![Security Engineering & Authentication progress](assets/progress/domain-11.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **Application and API Security** **`P0`**

  - [ ] API rate limiting, quotas, abuse prevention, and audit logs **`P0`**

  - [ ] Broken object-level authorization (BOLA/IDOR) **`P0`**

  - [ ] CORS behavior and common misconfigurations **`P1`**

  - [ ] Cross-site scripting (XSS), output encoding, and CSP **`P1`**

  - [ ] CSRF, SSRF, open redirects, and request smuggling basics **`P1`**

  - [ ] File upload validation and malware scanning **`P1`**

  - [ ] Input validation, schema validation, and safe deserialization **`P1`**

  - [ ] OWASP Top 10 and common exploitation paths **`P0`**

  - [ ] SQL/NoSQL injection and parameterized queries **`P0`**

- [ ] **Authentication and Authorization** **`P0`**

  - [ ] Authentication vs. authorization; identity vs. session management **`P0`**

  - [ ] JWT structure, claims, signature validation, and key rotation **`P0`**

  - [ ] OAuth 2.0 roles, authorization code + PKCE, scopes, and refresh tokens **`P0`**

  - [ ] OpenID Connect (OIDC) vs. OAuth 2.0 **`P0`**

  - [ ] RBAC vs. ABAC vs. policy-based access control **`P1`**

  - [ ] Service-to-service authentication and workload identities **`P0`**

  - [ ] Sessions, cookies, SameSite, HttpOnly, Secure, and CSRF protection **`P0`**

  - [ ] SSO, SAML basics, MFA, and passkeys/WebAuthn **`P1`**

- [ ] **Core Security Principles** **`P1`**

  - [ ] CIA triad, defense in depth, least privilege, and secure defaults **`P1`**

  - [ ] Secure SDLC, security reviews, and responsible vulnerability disclosure **`P1`**

  - [ ] Security requirements vs. security controls vs. residual risk **`P0`**

  - [ ] Threat modeling (STRIDE), trust boundaries, and attack surfaces **`P1`**

- [ ] **Cryptography and Data Protection** **`P0`**

  - [ ] Data classification, minimization, retention, and deletion **`P1`**

  - [ ] Encryption at rest vs. in transit and envelope encryption **`P0`**

  - [ ] Hashing, password hashing (Argon2/bcrypt), salts, and pepper **`P0`**

  - [ ] HMAC, digital signatures, and authenticated encryption **`P0`**

  - [ ] KMS, secrets managers, certificate rotation, and key lifecycles **`P1`**

  - [ ] Symmetric vs. asymmetric encryption; key-exchange basics **`P0`**

  - [ ] TLS handshake, certificates, certificate authorities, and mTLS **`P1`**

- [ ] **Infrastructure, Cloud, and Supply-Chain Security** **`P1`**

  - [ ] Container/Kubernetes security contexts, RBAC, and network policies **`P0`**

  - [ ] Dependency vulnerabilities, SBOMs, and software supply-chain attacks **`P1`**

  - [ ] IAM least privilege and privilege escalation risks **`P0`**

  - [ ] Network segmentation, zero-trust architecture, and private access **`P1`**

  - [ ] SAST vs. DAST vs. SCA; CI security gates **`P1`**

  - [ ] Secrets leakage prevention and incident credential rotation **`P1`**

- [ ] **LLM and Agent Security** **`P0`**

  - [ ] Auditability and rollback of agent-triggered side effects **`P1`**

  - [ ] Output validation, sandboxing, and safe execution environments **`P1`**

  - [ ] Prompt injection vs. instruction-following; untrusted retrieved content **`P0`**

  - [ ] RAG authorization filtering, document-level access controls **`P0`**

  - [ ] Secrets/PII exfiltration threats through tools and model responses **`P1`**

  - [ ] Tool permission boundaries, allowlists, and human approval for writes **`P1`**

- [ ] **Security Operations and Design Interviews** **`P1`**

  - [ ] Centralized security logging and tamper-evident audit trails **`P0`**

  - [ ] Design secure multi-tenant data access and tenant isolation **`P1`**

  - [ ] Explain trade-offs between usability, latency, and security **`P0`**

  - [ ] Incident lifecycle: detection, containment, eradication, recovery **`P1`**

  - [ ] Model replay attacks, confused deputy issues, and privilege boundaries **`P1`**

</details>


### 12. System Architecture

![System Architecture progress](assets/progress/domain-12.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **Caching strategies** **`P1`**

  - [ ] Cache aside **`P0`**

  - [ ] Cache stampede prevention **`P0`**

  - [ ] Write-behind caching **`P1`**

  - [ ] Write-through caching **`P1`**

- [ ] **Client-server architecture** **`P1`**

  - [ ] Basics **`P1`**

  - [ ] Communication protocols **`P1`**

- [ ] **Event-Driven Architecture (EDA)** **`P0`**

  - [ ] Advantages **`P1`**

  - [ ] Basics **`P1`**

  - [ ] Components **`P1`**

  - [ ] Implementations (e.g., Apache Kafka) **`P1`**

- [ ] **Layered Architecture** **`P1`**

  - [ ] Business logic layer **`P1`**

  - [ ] Cross-cutting concerns layer **`P1`**

  - [ ] Data access layer **`P1`**

  - [ ] Presentation layer **`P1`**

- [ ] **Message Queuing** **`P0`**

  - [ ] Basics **`P1`**

  - [ ] Implementations (e.g., RabbitMQ, Kafka) **`P1`**

  - [ ] Use cases **`P1`**

- [ ] [**Microservices**](./System%20Design/Microservices.md) **`P0`**

- [ ] [**RESTful architecture**](./System%20Design/RESTfulArchitecture.md) **`P0`**

- [ ] **Service-Oriented Architecture (SOA)** **`P1`**

  - [ ] Advantages **`P1`**

  - [ ] Challenges **`P1`**

  - [ ] Principles **`P1`**

</details>


### 13. System Design

![System Design progress](assets/progress/domain-13.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- Resources:

  - [System Design Interview by Alex Xu](./System%20Design/Resources/System%20Design%20Interview%20by%20Alex%20Xu.pdf)

  - [Designing Data Intensive Applications by Martin Kleppmann](./System%20Design/Resources/Designing%20Data%20Intensive%20Applications%20by%20Martin%20Kleppmann.pdf)

- [ ] **Database design and optimization** **`P1`**

  - [ ] Database normalization forms (1NF, 2NF, 3NF, BCNF) **`P0`**

  - [ ] Materialized views **`P1`**

  - [ ] NoSQL databases (document, key-value, column-family, graph) **`P0`**

  - [ ] Partitioning **`P0`**

- [ ] **Design patterns** **`P0`**

  - [ ] **Behavioral patterns** **`P1`**

    - [ ] Chain of Responsibility **`P1`**

    - [ ] Command **`P1`**

    - [ ] Iterator **`P1`**

    - [ ] Mediator **`P1`**

    - [ ] Memento **`P1`**

    - [ ] Observer **`P0`**

    - [ ] State **`P1`**

    - [ ] Strategy **`P0`**

    - [ ] Template Method **`P1`**

    - [ ] Visitor **`P1`**

  - [ ] **Creational patterns** **`P1`**

    - [ ] Abstract Factory **`P0`**

    - [ ] Builder **`P1`**

    - [ ] Factory Method **`P0`**

    - [ ] Prototype **`P1`**

    - [ ] Singleton **`P1`**

  - [ ] **Structural patterns** **`P1`**

    - [ ] Adapter **`P1`**

    - [ ] Bridge **`P1`**

    - [ ] Composite **`P1`**

    - [ ] Decorator **`P1`**

    - [ ] Facade **`P1`**

    - [ ] Flyweight **`P1`**

    - [ ] Proxy **`P1`**

- [ ] **Distributed systems** **`P1`**

  - [ ] ACID vs. BASE **`P0`**

  - [ ] Distributed tracing **`P0`**

  - [ ] Eventual consistency **`P1`**

  - [ ] Fault tolerance and resilience **`P0`**

  - [ ] Leader election algorithms (Paxos, Raft) **`P1`**

- [ ] **Microservices architecture** **`P0`**

  - [ ] API gateway **`P0`**

  - [ ] Caching strategies **`P1`**

    - [ ] Cache aside **`P0`**

    - [ ] Cache stampede prevention **`P0`**

    - [ ] Write-behind caching **`P1`**

    - [ ] Write-through caching **`P1`**

  - [ ] Choreography vs. Orchestration **`P0`**

  - [ ] Circuit Breaker pattern **`P0`**

  - [ ] Load balancing **`P0`**

    - [ ] Adaptive load balancing algorithms **`P0`**

    - [ ] Anycast routing **`P1`**

    - [ ] Content Delivery Networks (CDNs) **`P0`**

    - [ ] DNS load balancing **`P0`**

  - [ ] Saga pattern **`P1`**

- [ ] **Object-oriented design principles** **`P0`**

  - [ ] DRY (Don't Repeat Yourself) **`P1`**

  - [ ] KISS (Keep It Simple, Stupid) **`P1`**

  - [ ] Law of Demeter (Principle of Least Knowledge) **`P1`**

  - [ ] Open/Closed Principle **`P1`**

  - [ ] SOLID principles **`P0`**

    - [ ] Dependency Inversion Principle (DIP) **`P1`**

    - [ ] Interface Segregation Principle (ISP) **`P0`**

    - [ ] Liskov Substitution Principle (LSP) **`P1`**

    - [ ] Open/Closed Principle (OCP) **`P1`**

    - [ ] Single Responsibility Principle (SRP) **`P1`**

  - [ ] YAGNI (You Aren't Gonna Need It) **`P1`**

- [ ] **Scalability** **`P0`**

  - [ ] Auto-scaling **`P1`**

  - [ ] Consistent Hashing **`P0`**

  - [ ] Replication vs. Partitioning **`P0`**

</details>


### 14. Testing, Reliability & Observability

![Testing, Reliability & Observability progress](assets/progress/domain-14.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **Backend and Distributed-System Testing** **`P1`**

  - [ ] API contract tests, schema compatibility, and consumer-driven contracts **`P0`**

  - [ ] Concurrency tests, race conditions, and fault injection **`P0`**

  - [ ] Database integration tests, transactions, and migration tests **`P0`**

  - [ ] Idempotency tests and at-least-once delivery failure cases **`P0`**

  - [ ] Message queue/event handler tests: ordering, duplication, retry, DLQ **`P0`**

  - [ ] Property-based tests, fuzz testing, and boundary-value analysis **`P1`**

  - [ ] Testcontainers, ephemeral environments, and service virtualization **`P1`**

- [ ] **LLM and Agent Evaluation & Reliability** **`P0`**

  - [ ] Agent failure recovery, human handoff, and safety regression tests **`P0`**

  - [ ] Cost, token usage, latency, and failure-budget dashboards **`P0`**

  - [ ] Golden datasets, regression suites, and offline/online evaluation **`P0`**

  - [ ] Hallucination, grounding, task-success, and retrieval metrics **`P0`**

  - [ ] Judge-model calibration, human review, and inter-rater agreement **`P1`**

  - [ ] Tool-call tracing, execution-step replay, and state checkpoint tests **`P0`**

- [ ] **Logging, Metrics, and Tracing** **`P0`**

  - [ ] Alert quality: actionable alerts, thresholds, burn-rate alerts **`P1`**

  - [ ] Distributed tracing, spans, context propagation, and sampling **`P0`**

  - [ ] Logs/metrics/traces correlation for root-cause analysis **`P0`**

  - [ ] Metrics cardinality, aggregation, dashboards, and retention **`P0`**

  - [ ] OpenTelemetry instrumentation and collectors **`P1`**

  - [ ] RED (rate, errors, duration) and USE (utilization, saturation, errors) **`P1`**

  - [ ] Structured logging, severity levels, and correlation IDs **`P0`**

- [ ] **Performance and Scalability Testing** **`P0`**

  - [ ] Capacity baselines and regression performance testing **`P1`**

  - [ ] Load vs. stress vs. spike vs. soak testing **`P1`**

  - [ ] Profiling CPU, memory, I/O, and database queries **`P1`**

  - [ ] Throughput, latency distributions (p50/p95/p99), and error rates **`P0`**

  - [ ] Workload modeling, realistic traffic, and bottleneck diagnosis **`P1`**

- [ ] **Production Incidents and Operational Excellence** **`P1`**

  - [ ] Blameless postmortems with contributing factors and follow-ups **`P1`**

  - [ ] Change management, feature flags, safe rollouts, and rollback **`P1`**

  - [ ] Incident severity, triage, mitigation, and communication **`P1`**

  - [ ] On-call handoffs, runbooks, escalation, and ownership **`P1`**

  - [ ] Reliability-related architectural trade-offs **`P1`**

  - [ ] Root-cause analysis: timelines, hypotheses, and evidence **`P1`**

- [ ] **Reliability Engineering (SRE)** **`P1`**

  - [ ] Availability math and the implications of dependency chains **`P1`**

  - [ ] Capacity and saturation monitoring **`P1`**

  - [ ] Chaos engineering and game-day exercises **`P1`**

  - [ ] Disaster recovery drills, backups, and restore verification **`P0`**

  - [ ] Fault tolerance, redundancy, graceful degradation, and bulkheads **`P0`**

  - [ ] Retry policies, exponential backoff, jitter, and circuit breakers **`P0`**

  - [ ] SLIs, SLOs, SLAs, and error budgets **`P0`**

  - [ ] Timeouts, cancellation, rate limiting, and backpressure **`P1`**

- [ ] **Software Testing Foundations** **`P1`**

  - [ ] Functional vs. non-functional testing **`P1`**

  - [ ] Mocks, stubs, fakes, spies, and contract boundaries **`P0`**

  - [ ] Test coverage metrics and their limitations **`P0`**

  - [ ] Test isolation, deterministic fixtures, and repeatable environments **`P1`**

  - [ ] Testing pyramid vs. testing trophy; risk-based test selection **`P1`**

  - [ ] Unit, integration, end-to-end (E2E), and acceptance tests **`P1`**

</details>


### 15. Version control System

![Version control System progress](assets/progress/domain-15.svg)

<details>
<summary><strong>View topics and checklist</strong></summary>

- [ ] **Bitbucket** **`P2`**

- [ ] [**Git**](./Version%20Control%20Systems/Git.md) **`P1`**

</details>

## Interview Readiness Assessment

Before calling a topic “done,” check whether you can explain and apply it under interview conditions.

- [ ] I can explain the core idea without notes in 1–2 minutes.

- [ ] I can name a realistic use case and when **not** to use it.

- [ ] I can compare alternatives and explain time, memory, cost, or operational trade-offs.

- [ ] I can describe edge cases, failure modes, and mitigations.

- [ ] I can implement it, solve a related problem, or diagram it where applicable.

- [ ] I can handle follow-up questions and communicate uncertainty clearly.

**Simple self-rating:** **0** = unfamiliar · **1** = recognize it · **2** = explain with notes · **3** = explain and apply unaided · **4** = defend the design and trade-offs. Aim for **3+ on P0 topics** rather than superficial coverage of everything.

## Features

- **Structured Learning Path**: Follow a well-organized roadmap covering key domains such as **Data Structures**, **Algorithms**, **System Design**, **Operating Systems**, **Networking**, **Databases**, and more.

- **Checklist-based Approach**: Track your progress systematically with checklist-style items for each topic, ensuring thorough coverage of concepts and practical skills.

- **Recommended Resources**: Access curated lists of recommended resources, including books, online courses, coding platforms, articles, and practice problems to enhance your understanding and skills.

- **Tailored Preparation**: Customize your preparation based on the specific requirements and focus areas of the companies you're interviewing with, maximizing your chances of success.

- **Tips and Recommendations**: Benefit from valuable tips and recommendations for problem-solving, coding practice, behavioral and soft skills development, and adapting to different interview formats.

## How to Use

1\\. **Clone the Repository**: Clone this repository to your local machine using Git.

2\\. **Navigate to Domains**: Explore the `Domains` directory to find checklists for different domains/topics.

3\\. **Check Off Items**: As you study and practice, mark off checklist items to track your progress.

4\\. **Explore Resources**: Browse through the `Resources` directory for recommended resources corresponding to each domain/topic.

5\\. **Customize Your Plan**: Tailor your preparation plan based on your strengths, weaknesses, and the requirements of the companies you're targeting.

6\\. **Community Learning**: Engage with fellow learners, share insights, ask questions, and collaborate on improving the roadmap together.

7\\. **Stay Updated**: Periodically update your progress and revisit topics to reinforce your understanding and skills.

## Contributions

Contributions are welcome! If you have suggestions for improving the roadmap, additional resources to recommend, or want to fix any errors, feel free to open an issue or submit a pull request.

## Disclaimer

This roadmap is intended as a general guideline and may not cover every aspect of SDE interviews. It's essential to supplement my preparation with additional resources and adapt based on individual needs and experiences.

## Credits

This project is inspired by various interview preparation resources and the collective wisdom of the developer community.
