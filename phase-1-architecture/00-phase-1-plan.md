# Phase 1 · แผนปฏิบัติการ 8 สัปดาห์ 🗺️

> แตกมาจาก [`roadmap.md` § Phase 1](../roadmap.md) — ไฟล์นี้คือ checklist ที่ติ๊กระหว่างทาง
> **เริ่มจริง**: 27 ส.ค. 2026 *(เริ่มก่อนกำหนดในปฏิทิน 14 ก.ย. ประมาณ 2.5 สัปดาห์)*
> **สนามทดลอง**: Paystation — Workflow Engine · **ขอบเขต: แกน step transition เท่านั้น**

---

## 🎯 ของที่ต้องส่งจริงๆ มี 4 ชิ้น

ทุกอย่างในไฟล์นี้คือทางไปสู่ 4 ชิ้นนี้ ไม่ใช่การไล่อ่านหัวข้อให้ครบ

| # | ของที่ต้องได้ | ไฟล์ปลายทาง |
| :-: | :--- | :--- |
| 1 | **ตัวเลข before/after** ของ "ทางเขียนคำตอบ step ลง DB" เทียบกับ "ทางที่บังคับกฎ" | [`02-paystation-write-path-survey.md`](./02-paystation-write-path-survey.md) |
| 2 | **ADR ฉบับแรก** — เลือกแนวทาง A หรือ B + ผ่านรีวิวจากเพื่อนร่วมทีม | [`../journal/adr/`](../journal/adr/) `0001-workflow-domain-approach.md` |
| 3 | **โค้ด Paystation** ที่ย้ายกฎทั้ง 4 ข้อออกจาก view/serializer ได้ครบ | repo งาน |
| 4 | **คำอธิบายด้วยปาก** ว่า abstraction ไหนใน codebase ผิด · ผิดยังไง · แก้ยังไง | ซ้อมกับเพื่อนร่วมทีม |

---

## 📋 Checklist ตามลำดับ

### 🔹 สัปดาห์ที่ 0 — ยังไม่แตะโค้ด Paystation

- [ ] รัน demo ให้ผ่าน — `cd demo-clean-arch && uv run pytest` → **10 passed**
- [ ] เปิด [`demo-clean-arch/domain/order.py`](./demo-clean-arch/domain/order.py) ดูว่า import อะไรบ้าง
      — import list นั้นคือ **Dependency Rule ทั้งหมด** ไม่มีอะไรมากกว่านั้น
- [ ] เริ่ม **Track D** สัปดาห์ละ 1 โจทย์ *(สะสมอยู่ 0 — ปล่อยไว้จะไม่มีวันตามทัน)*

### 🔹 สัปดาห์ที่ 1–2 — สำรวจ *(งานแรกจริงของ Phase 1)*

- [ ] นับให้ครบว่ามี **กี่ทางที่เขียนคำตอบของ step ลง DB ได้**
      `API` · `Django admin` · `management command` · `celery task` · `bulk import` · `signal` · `data migration / script`
- [ ] นับว่า **กี่ทางที่บังคับกฎ** "แก้ step ก่อนหน้า → ต้องล้างคำตอบของ step หลังจากนั้น"
- [ ] เขียนส่วนต่างออกมาเป็นตัวเลข → นี่คือค่า **before** ที่ใช้วัดตอนจบ Phase
- [ ] ไล่กฎทั้ง 4 ข้อในตาราง Phase 0 ว่าตอนนี้อยู่บรรทัดไหนของโค้ด (`file:line`)

> 🚫 **ห้ามข้ามไปแก้โค้ดก่อน** — ไม่มีตัวเลข before แปลว่า Phase 1 พิสูจน์ไม่ได้ว่าสำเร็จ

### 🔹 สัปดาห์ที่ 2–3 — ADR + ออกแบบ Aggregate

- [ ] เขียน `journal/adr/0001-workflow-domain-approach.md` — เลือก **A (แยกจริง)** หรือ **B (ผสม)**
      *แนะนำตาม roadmap: เริ่มที่ B แล้วค่อยยก A เฉพาะ Workflow Aggregate แกนกลาง*
- [ ] นิยาม Aggregate ให้ชัด: **หนึ่งเคสที่กำลังวิ่ง + เส้นทางที่เดินมา + คำตอบทั้งหมด** = เปลี่ยนพร้อมกันเป็นก้อนเดียว
- [ ] ตอบคำถามที่ยังค้างจาก Phase 0: workflow แตกกิ่งได้
      ⇒ การล้างคำตอบต้องอิง **เส้นทางที่เคสนี้เดินมาจริง** ไม่ใช่เลข step ตายตัว
- [ ] ส่ง ADR ให้เพื่อนร่วมทีมรีวิว — *ข้อนี้เป็น Exit Criteria รีวิวไม่ผ่าน = ยังไม่จบ*

📚 อ่านคู่กัน: **Learning DDD (Khononov)** ส่วน Tactical
— [`self-assessment.md`](../self-assessment.md) ให้ Aggregate / Entity / VO / Domain Event / Repository เป็น 🔴 ทั้งแถว นี่คือช่องว่างใหญ่ที่สุดของ Phase นี้

### 🔹 สัปดาห์ที่ 4–6 — ลงมือ *(แนวทาง B)*

- [ ] ย้าย business logic จาก view → `application/use_cases/`
- [ ] ย้ายกฎทั้ง 4 ข้อเข้า domain
  - [ ] เคสที่สร้างแล้วยึด workflow definition เดิม แม้ template ถูกแก้
  - [ ] แก้คำตอบ step ก่อนหน้า → step หลังจากนั้นต้องตอบใหม่
  - [ ] ใครมีสิทธิ์ตอบ step ไหน
  - [ ] คำตอบของ step ถูกต้องไหม *(schema อยู่ domain · validate ที่ boundary)*
- [ ] Serializer เหลือแค่ validate **รูปร่าง** — validate **กฎ** ต้องอยู่ใน domain
- [ ] บีบทุก write path ให้ผ่านทางเดียวกัน ← **นี่คือหัวใจ ไม่ใช่ความสวยของ layer**
- [ ] ใช้ **Strategy pattern** กับกฎ transition ที่ผันแปร *(ได้หัวข้อ 1.3 ไปในตัว ไม่ต้องแยก block นั่งอ่าน)*

> 🚩 **กับดัก**: อย่าเผลอเก็บคำตอบเป็น JSON ก้อนเดียวเพราะ "แต่ละ step ไม่เหมือนกัน"
> กฎจะหลุดจาก domain ไปอยู่ที่ผู้เรียกใช้ทั้งหมด — โจทย์แท้จริงคือ *เก็บความยืดหยุ่นไว้โดยไม่ทิ้งกฎ*

### 🔹 สัปดาห์ที่ 7 — ยกเป็นแนวทาง A เฉพาะแกนกลาง *(ถ้าไหว)*

- [ ] Workflow Aggregate เป็น dataclass ล้วน + repository แปลง Django Model ↔ domain object
- [ ] พิสูจน์: `grep -r "django" domain/` → **ต้องไม่เจอสักบรรทัด**
- [ ] เทส domain ทั้งหมดรันผ่าน **โดยไม่ต้องมี database**

### 🔹 สัปดาห์ที่ 8 — ปิด Phase

- [ ] นับ write path ใหม่ → เทียบกับตัวเลข **before**
- [ ] ทำโจทย์ **URL Shortener ซ้ำ** แบบไม่เปิดของเก่า แล้วเทียบกับ [รอบ 27 ส.ค. 2026](../journal/system-design/2026-08-27-url-shortener.md)
      *(เกณฑ์วัดอยู่ท้าย [ไฟล์รีวิว](../journal/system-design/2026-08-27-url-shortener-review.md))*
- [ ] อัปเดต [`self-assessment.md`](../self-assessment.md) รอบที่ 2 + ตารางความคืบหน้าใน [`README.md`](../README.md)

---

## ✅ Exit Criteria — ติ๊กตอนจบ

**ตัวชี้วัดหลัก (ใช้ได้ทั้ง A และ B)**
- [ ] ทุกทางที่เขียนคำตอบของ step ลง DB **บังคับกฎเดียวกันหมด** — เทียบกับตัวเลข before
- [ ] ย้ายกฎทั้ง 4 ข้อออกจาก view/serializer ได้ครบ

**ถ้าเลือกแนวทาง A กับ Workflow Aggregate**
- [ ] domain layer ไม่มี `import django` เลยแม้แต่บรรทัดเดียว
- [ ] เทส domain ทั้งหมดรันผ่านโดยไม่ต้องมี database

**ทุกกรณี**
- [ ] ADR 1 ฉบับ อธิบายการตัดสินใจ A vs B และผ่านการรีวิวจากเพื่อนร่วมทีม
- [ ] อธิบายให้คนอื่นฟังได้ว่า abstraction ไหนใน codebase ปัจจุบันผิด ผิดยังไง แก้ยังไง

---

## ♾️ Continuous Tracks ที่ต้องเดินคู่กันตลอด Phase นี้

| Track | ต้องทำระหว่าง Phase 1 |
| :--- | :--- |
| **L** — Leadership | ADR-0001 + นำ review 1 ครั้ง *(ใช้ session รีวิว ADR นี่แหละ)* |
| **D** — System Design | สัปดาห์ละ 1 โจทย์ → จบ Phase ควรมี ~8 ไฟล์ใน `journal/system-design/` |
| **Q** — Quality | วาง testing strategy ของชั้น domain/use case ให้ทีมใช้ต่อได้ |
