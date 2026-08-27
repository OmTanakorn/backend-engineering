# Backend Engineering — Senior / Lead Track

บันทึกการเรียนรู้และผลงานจริงตาม [`roadmap.md`](./roadmap.md)
ระยะเวลา ส.ค. 2026 – ส.ค. 2027

---

## 📊 ความคืบหน้า

| Phase | ช่วงเวลา | สถานะ | Exit Criteria |
| :--- | :--- | :---: | :---: |
| **P0** Baseline & Setup | ส.ค. 2026 | 🔄 กำลังทำ | 0 / 5 |
| **P1** [Architecture](./phase-1-architecture/) | ก.ย. – พ.ย. 2026 | ⬜ ยังไม่เริ่ม | 0 / 3 |
| **P2** [Data Layer](./phase-2-data/) | พ.ย. 2026 – ม.ค. 2027 | ⬜ ยังไม่เริ่ม | 0 / 4 |
| **P3** [Distributed](./phase-3-distributed/) | ม.ค. – เม.ย. 2027 | ⬜ ยังไม่เริ่ม | 0 / 4 |
| **P4** [Security](./phase-4-security/) | เม.ย. – พ.ค. 2027 | ⬜ ยังไม่เริ่ม | 0 / 3 |
| **P5** [Cloud & Ops](./phase-5-cloud/) | พ.ค. – ส.ค. 2027 | ⬜ ยังไม่เริ่ม | 0 / 4 |

**Continuous Tracks** (เดินตลอด 12 เดือน — ดูรายละเอียดใน roadmap)

| Track | เป้าหมาย | สะสมแล้ว |
| :--- | :--- | :---: |
| **L** — Leadership | ADR 1 ฉบับ + นำ review 1 ครั้ง + post-mortem 1 ครั้ง ต่อไตรมาส | 0 |
| **D** — System Design | สัปดาห์ละ 1 โจทย์ | 0 |
| **Q** — Quality | benchmark ทุก capstone + หา bottleneck จริง 1 ครั้ง | 0 |

---

## 📂 โครงสร้าง

```text
backend-engineering/
├── roadmap.md                    # แผนหลัก — เริ่มอ่านที่นี่
│
├── phase-1-architecture/         # โน้ต + โค้ดตัวอย่างของแต่ละ Phase
│   ├── 01-clean-architecture.md
│   └── demo-clean-arch/          # โปรเจกต์ตัวอย่างที่รันได้
├── phase-2-data/
├── phase-3-distributed/
├── phase-4-security/
├── phase-5-cloud/
│
└── journal/                      # ผลผลิตจาก Continuous Tracks
    ├── adr/                      # Track L — Architecture Decision Records
    ├── system-design/            # Track D — โจทย์ที่ทำแล้ว (ลงวันที่ไว้ทุกครั้ง)
    ├── benchmarks/               # Track Q — ตัวเลขก่อน/หลัง optimization
    └── post-mortems/             # Track L — บันทึกจาก incident จริง
```

### หลักการตั้งชื่อไฟล์

| ที่ | รูปแบบ | ตัวอย่าง |
| :--- | :--- | :--- |
| โน้ตใน phase | `NN-หัวข้อ.md` (เรียงเลขใหม่ในแต่ละ phase) | `02-ddd-tactical.md` |
| ADR | `NNNN-หัวข้อ.md` | `0001-split-order-domain.md` |
| System design | `YYYY-MM-DD-หัวข้อ.md` | `2026-08-27-url-shortener.md` |
| Benchmark | `หัวข้อ-YYYY-MM-DD.md` | `rate-limiter-2027-02-15.md` |

---

## 🎯 กติกาที่ทำให้ repo นี้มีค่า

1. **ทุก Phase จบด้วย Exit Criteria ไม่ใช่ด้วยวันที่** — ทำไม่ได้ = ยังไม่ขึ้น Phase ถัดไป
2. **ทุกคำกล่าวอ้างเรื่อง performance ต้องมีตัวเลข** — ไม่มี benchmark ห้ามเขียนว่า "เร็วขึ้น"
3. **ทำโจทย์ System Design เดิมซ้ำทุกจบ Phase** — เก็บทั้งคำตอบเก่าและใหม่ไว้เทียบกัน

> สิ่งที่วัดความสำเร็จของ 12 เดือนนี้ ไม่ใช่ "เรียนจบตามกำหนด"
> แต่คือ **repo นี้มี ADR, system design writeup, ตัวเลข benchmark และ post-mortem สะสมอยู่จริง** — หลอกตัวเองไม่ได้ และเป็นหลักฐานที่ใช้สัมภาษณ์ได้
