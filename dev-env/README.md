# Dev Environment

Postgres + Redis + Kafka สำหรับใช้ตลอด roadmap — ตั้งครั้งเดียวใช้ยาว 12 เดือน

> ✅ ทดสอบแล้ว 27 ส.ค. 2026: ทั้งสามบริการขึ้น healthy, extension โหลดครบ, produce/consume Kafka ผ่าน

---

## ⚠️ พอร์ตไม่ใช่ค่ามาตรฐาน โดยตั้งใจ

เครื่องนี้รัน stack ของงาน (`paystation_postgres`, `paystation_redis`) บนพอร์ตมาตรฐานอยู่แล้ว
learning stack เลยย้ายไปพอร์ตอื่น **เพื่อให้รันคู่กันได้โดยไม่ต้องปิดอะไร**

| บริการ | พอร์ต learning | พอร์ตมาตรฐาน (งานใช้อยู่) |
| :--- | :---: | :---: |
| Postgres | **5433** | 5432 |
| Redis | **6380** | 6379 |
| Kafka | **9094** | 9092 |
| Kafka UI *(opt-in)* | **8081** | 8080 |

เปลี่ยนได้ด้วยการสร้างไฟล์ `.env` ในโฟลเดอร์นี้ (ถูก gitignore ไว้แล้ว):

```bash
LEARN_PG_PORT=15432
LEARN_REDIS_PORT=16379
```

---

## 🚀 คำสั่ง

```bash
cd dev-env

docker compose up -d --wait      # เปิด (รอจน healthy จริง)
docker compose ps                # ดูสถานะ
docker compose logs -f postgres  # ดู log
docker compose stop              # ปิดชั่วคราว ข้อมูลยังอยู่
docker compose down              # ลบ container ข้อมูลยังอยู่ใน volume
docker compose down -v           # ⚠️ ลบข้อมูลทั้งหมดด้วย

docker compose --profile tools up -d   # เปิด Kafka UI เพิ่มที่ localhost:8081
```

## 🔌 Connection strings

```bash
postgresql://dev:dev@localhost:5433/playground
redis://localhost:6380
kafka: localhost:9094
```

## 🔍 คำสั่งที่ใช้บ่อย

```bash
# Postgres shell
docker exec -it learn-postgres psql -U dev -d playground

# Redis shell
docker exec -it learn-redis redis-cli

# Kafka: สร้าง/ดู topic  (auto-create ปิดไว้ ต้องสร้างเองเสมอ)
docker exec learn-kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9094 --list
docker exec learn-kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9094 \
  --create --topic <ชื่อ> --partitions 3 --replication-factor 1
```

---

## 🎛️ สิ่งที่ตั้งค่าไว้ให้ล่วงหน้า (และเหตุผล)

| การตั้งค่า | ใช้ตอนไหน |
| :--- | :--- |
| `pg_stat_statements` | **Phase 2** — หา query ที่ช้าที่สุดในระบบ ซึ่งเป็น Exit Criteria ข้อแรกของ Phase นั้นเลย |
| `auto_explain` (>500ms) | Postgres จะ log execution plan ให้เองเมื่อ query ช้า ไม่ต้องนั่งเดาว่าอันไหนช้า |
| `pgstattuple` | ตรวจ table bloat ตอนเรียน VACUUM |
| `pg_trgm` | ไว้ฝึก GIN/GiST index |
| `auto.create.topics=false` | บังคับให้สร้าง topic เองทุกครั้ง — จะได้เห็นเรื่อง partition count ตั้งแต่แรก ไม่ใช่ปล่อยให้ Kafka เดาให้ |
| Kafka 2 listeners | `localhost:9094` สำหรับแอปที่รันบนเครื่อง, `kafka:29092` สำหรับ container ที่จะเพิ่มเข้ามาทีหลัง |

### ตัวอย่างที่จะได้ใช้จริงใน Phase 2

```sql
-- query ที่ช้าที่สุด 10 อันดับ
SELECT query, calls, round(mean_exec_time::numeric, 2) AS avg_ms, rows
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- ล้างสถิติก่อนเริ่มวัดรอบใหม่
SELECT pg_stat_statements_reset();
```
