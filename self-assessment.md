# Self-Assessment

ประเมินตัวเองตรงๆ ในทุกหัวข้อของ roadmap

- **รอบแรก**: 27 ส.ค. 2026 (Phase 0 baseline)
- **ทบทวน**: ทุกไตรมาส — ใช้ปากกาคนละสี/emoji ต่างกัน จะได้เห็นว่าอะไรขยับ

---

## 🎯 วิธีใช้และเกณฑ์

| สัญลักษณ์ | ความหมาย      | เกณฑ์ตัดสิน                                                          |
| :-------: | :------------ | :------------------------------------------------------------------- |
|    🟢     | **รู้ลึก**    | เคยใช้จริงในงาน **และ** อธิบายให้คนอื่นเข้าใจได้โดยไม่ต้องเปิดเอกสาร |
|    🟡     | **รู้ผิวๆ**   | พอเข้าใจตอนอ่าน แต่ให้ลงมือทำเองตอนนี้ยังไม่ได้                      |
|    🔴     | **ไม่รู้เลย** | ไม่เคยได้ยิน หรือได้ยินแต่ไม่รู้ว่าคืออะไร                           |

> **จุดประสงค์ที่แท้จริงคือหาว่าอะไร "ข้ามได้"** ไม่ใช่แค่หาว่าไม่รู้อะไร
> ถ้าหัวข้อไหนเป็น 🟢 จริงๆ ตอนถึง Phase นั้นให้อ่านผ่านๆ แล้วเอาเวลาไปลงกับ 🔴 แทน — นี่คือสิ่งที่ทำให้ 12 เดือนพอ
>
> ⚠️ **เกณฑ์ 🟢 เข้มมากโดยตั้งใจ** ถ้าลังเลระหว่าง 🟢 กับ 🟡 ให้เลือก 🟡 เสมอ การประเมินตัวเองสูงเกินจริงคือวิธีที่แน่นอนที่สุดที่จะทำให้ roadmap นี้ล้มเหลว

---

## 🏛️ Phase 1 — Architecture

| หัวข้อ                                                  | ระดับ | หมายเหตุ                                                  |
| :------------------------------------------------------ | :---: | :-------------------------------------------------------- |
| Clean Architecture / Hexagonal (Ports & Adapters)       |  🟡   | เคยใช้งานใน Project Paystation แต่ยังไม่ได้ full ขนาดนั้น |
| Dependency Inversion Principle                          |  🟡   | ้เคยใช้งารใน Paystation แต่ไม่ได้เข้าใจลึก                |
| Bounded Context & Ubiquitous Language                   |  🔴   |                                                           |
| Aggregate Root, Entity, Value Object                    |  🔴   |                                                           |
| Domain Events                                           |  🔴   |                                                           |
| Repository Pattern                                      |  🔴   |                                                           |
| Factory / Builder / DI Container                        |  🟡   |                                                           |
| Adapter / Facade / Decorator                            |  🔴   |                                                           |
| Strategy / Observer / Command / Chain of Responsibility |  🔴   |                                                           |
| Python: `asyncio` & Event Loop                          |  🟡   |                                                           |
| Python: ASGI vs WSGI                                    |  🟡   |                                                           |
| Python: ORM internals & N+1                             |  🟢   |                                                           |
| Python: GIL, multiprocessing vs threading               |  🟡   |                                                           |
| Go: พื้นฐานภาษา                                         |  🔴   |                                                           |

## 💾 Phase 2 — Data Layer

| หัวข้อ                                          | ระดับ | หมายเหตุ |
| :---------------------------------------------- | :---: | :------- |
| Index: B-Tree / Hash / GIN / GiST               |  🔴   |          |
| Composite / Covering / Partial Index            |  🔴   |          |
| อ่าน `EXPLAIN (ANALYZE, BUFFERS)`               |  🔴   |          |
| Join algorithms (Nested Loop / Hash / Merge)    |  🔴   |          |
| Transaction Isolation Levels                    |  🔴   |          |
| MVCC                                            |  🔴   |          |
| Optimistic vs Pessimistic Locking               |  🔴   |          |
| Deadlock detection & แก้                        |  🟡   |          |
| Connection Pooling & pool sizing                |  🟡   |          |
| VACUUM & table bloat                            |  🔴   |          |
| Expand/Contract migration (zero-downtime)       |  🔴   |          |
| `ALTER TABLE` lock บนตารางใหญ่                  |  🟡   |          |
| Backfill ข้อมูลจำนวนมาก                         |  🟡   |          |
| Backup / Restore / PITR                         |  🟡   |          |
| Cache patterns (Aside / Through / Behind)       |  🟡   |          |
| Cache Stampede / Penetration / Hotkey           |  🔴   |          |
| Redis: Sorted Set, Bitmap, HyperLogLog, Streams |  🔴   |          |
| Redis: Distributed Lock & Lua                   |  🔴   |          |
| Normalization vs Denormalization                |  🟡   |          |
| Partitioning                                    |  🔴   |          |
| Replication Lag                                 |  🔴   |          |
| Sharding                                        |  🔴   |          |

## 🌐 Phase 3 — Distributed Systems

| หัวข้อ                                          | ระดับ  | หมายเหตุ |
| :---------------------------------------------- | :----: | :------- |
| CAP & PACELC                                    |   🔴   |          |
| Consistency models (Strong / Eventual / Causal) |   🔴   |          |
| Raft / Consensus                                |   🔴   |          |
| Quorum & Leader Election                        | 🔴<br> |          |
| Clock skew, Lamport / Vector clock              | 🔴<br> |          |
| REST: Idempotent API design                     | 🔴<br> |          |
| gRPC & Protobuf                                 |   🔴   |          |
| GraphQL vs REST vs gRPC                         |   🔴   |          |
| RabbitMQ: Exchange, DLQ                         |   🔴   |          |
| Kafka: Partition, Consumer Group, Offset        |   🔴   |          |
| Kafka: Rebalancing & Exactly-Once               |   🔴   |          |
| Schema evolution & registry                     |   🔴   |          |
| Saga Pattern                                    |   🔴   |          |
| Transactional Outbox & CDC                      |   🔴   |          |
| Idempotency Key                                 |   🔴   |          |
| Circuit Breaker                                 |   🔴   |          |
| Retry + Exponential Backoff + Jitter            |   🔴   |          |
| Bulkhead / Timeout / Fallback                   |   🔴   |          |

## 🔐 Phase 4 — Security

| หัวข้อ                               | ระดับ | หมายเหตุ |
| :----------------------------------- | :---: | :------- |
| OAuth 2.0 / OIDC / PKCE              |  🟢   |          |
| JWT pitfalls (alg confusion, revoke) |  🟢   |          |
| RBAC vs ABAC                         |  🟡   |          |
| Object-level permission / IDOR       |  🟡   |          |
| OWASP Top 10                         |  🔴   |          |
| Secrets management & rotation        |  🔴   |          |
| Encryption at rest vs in transit     |  🔴   |          |
| Password hashing (Argon2 / bcrypt)   |  🟢   |          |
| PII masking ใน log                   |  🔴   |          |
| Threat modeling (STRIDE)             |  🔴   |          |
| Dependency scanning / SBOM           |  🔴   |          |
| Container image scanning             |  🔴   |          |
| PCI-DSS / PDPA                       |  🔴   |          |

## ☁️ Phase 5 — Cloud & Ops

| หัวข้อ                                                  | ระดับ | หมายเหตุ |
| :------------------------------------------------------ | :---: | :------- |
| Docker multi-stage / distroless / non-root              |  🔴   |          |
| K8s architecture (Control Plane, Kubelet)               |  🔴   |          |
| Deployment / StatefulSet / DaemonSet                    |  🔴   |          |
| HPA & autoscaling                                       |  🔴   |          |
| Resource requests/limits & CPU throttling               |  🔴   |          |
| ConfigMap / Secret / PersistentVolume                   |  🔴   |          |
| Ingress                                                 |  🔴   |          |
| Probes (liveness/readiness/startup) & graceful shutdown |  🔴   |          |
| CI/CD pipeline design                                   |  🔴   |          |
| Blue-Green / Canary / Feature Flags                     |  🔴   |          |
| DB migration ใน CD pipeline                             |  🔴   |          |
| Structured logging & Trace ID propagation               |  🔴   |          |
| Prometheus, RED & USE method                            |  🔴   |          |
| OpenTelemetry & Jaeger                                  |  🔴   |          |
| SLI / SLO / SLA                                         |  🔴   |          |
| Error Budget                                            |  🔴   |          |

## ♾️ Continuous Tracks

| หัวข้อ                               | ระดับ | หมายเหตุ |
| :----------------------------------- | :---: | :------- |
| **L** — เขียน ADR                    |  🔴   |          |
| **L** — เขียน RFC / Design Doc       |  🔴   |          |
| **L** — นำ design review             |  🔴   |          |
| **L** — Mentoring & feedback         |  🔴   |          |
| **L** — Incident command             |  🔴   |          |
| **L** — Blameless post-mortem        |  🔴   |          |
| **D** — Capacity estimation          |  🔴   |          |
| **D** — ออกแบบระบบทั้งก้อนใน 45 นาที |  🔴   |          |
| **Q** — Test pyramid & test doubles  |  🔴   |          |
| **Q** — Testcontainers               |  🔴   |          |
| **Q** — Contract testing (Pact)      |  🔴   |          |
| **Q** — Property-based testing       |  🔴   |          |
| **Q** — Load testing (k6 / Locust)   |  🔴   |          |
| **Q** — อ่าน p50/p95/p99             |  🔴   |          |
| **Q** — Profiling & flame graph      |  🔴   |          |

---

## 📊 สรุปรอบที่ 1 (กรอกหลังประเมินครบ)

| Phase | 🟢 | 🟡 | 🔴 | ข้อสังเกต |
| :--- | :---: | :---: | :---: | :--- |
| P1 Architecture |  |  |  |  |
| P2 Data Layer |  |  |  |  |
| P3 Distributed |  |  |  |  |
| P4 Security |  |  |  |  |
| P5 Cloud & Ops |  |  |  |  |
| Tracks |  |  |  |  |

**หัวข้อ 🔴 ที่น่ากลัวที่สุด 3 อันดับแรก**
- ไม่มันใจ

**หัวข้อ 🟢 ที่มั่นใจว่าข้ามได้จริง**
- No

**Phase ที่คิดว่าจะใช้เวลานานกว่าแผน**
- ไม่มันใจ
ข้อมูลเพิมเติม 
- ผมทำงานมา 2 ปีกว่า และเป็น Backend เต็มตัว ระบบที่ได้รับทำส่วนใหญ่คือระบบ workflow แบบ Paystation การต่อ intigrate กับคนอืน และการออกแบบระบบ ออกแบบ database แต่ keyword ที่ได้มาข้างต้นผมไม่เคยได้ศึกษาจริงๆเลย หรือบางเรื่องอาจรู้ว่ามันทำอะไรยังไง แต่ไม่รู้ชื่อเรียก ผมเลยรู้สึกว่าต้องมานั้งเรียนอะไรพวกนี้แล้ว เพราะถึงเวลาที่ควรรู้แล้วสำหรับ 2 เกลือบ 3 ปี 
