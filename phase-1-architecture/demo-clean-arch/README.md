# 🧪 Clean Architecture & DDD Sandbox (Python)

โปรเจกต์ตัวอย่างสำหรับการฝึกปฏิบัติการออกแบบสถาปัตยกรรมซอฟต์แวร์ระดับ Senior โดยใช้หลักการ **Clean Architecture (Hexagonal / Ports & Adapters)** และ **Domain-Driven Design (DDD)**

---

## 📂 โครงสร้างโปรเจกต์ (Project Structure)

```text
clean_arch_demo/
├── domain/                      # 1. Core Business Rules (Pure Python)
│   ├── order.py                 # Domain Entity (Order, calculate_total, mark_as_paid)
│   └── exceptions.py            # Domain Exceptions
│
├── application/                 # 2. Use Cases & Interfaces
│   ├── ports/                   # Contracts / Interfaces (Protocols)
│   │   ├── order_repository.py  # Contract for persistence
│   │   ├── stock_service.py     # Contract for stock management
│   │   └── payment_gateway.py   # Contract for payment processing
│   └── use_cases/               # Application Business Workflows
│       ├── create_order.py      # CreateOrderUseCase
│       └── cancel_order.py      # CancelOrderUseCase
│
├── infrastructure/              # 3. Adapters / External Implementations
│   └── adapters/
│       ├── in_memory_order_repo.py
│       ├── mock_stock_service.py
│       └── mock_payment_gateway.py
│
├── presentation/                # 4. Entrypoint / UI
│   └── cli.py                   # Demo CLI runner with Dependency Injection
│
└── tests/                       # Unit Test Suite (< 50ms)
    ├── test_domain_order.py
    ├── test_create_order_use_case.py
    └── test_cancel_order_use_case.py
```

---

## ⚡ คำสั่งรันโปรเจกต์ (Commands)

```bash
# 1. รัน Unit Tests ทั้งหมด (รวดเร็วมาก ไม่ต้องใช้ DB จริง)
uv run pytest

# 2. รันโปรแกรมสาธิตการทำงานผ่าน CLI
uv run python presentation/cli.py
```

---

## 🎯 Hands-on Challenge: แบบฝึกหัดสำหรับคุณ

เพื่อฝึกทักษะ Clean Architecture ให้คล่องแคล่ว แนะนำให้ลองทำโจทย์ต่อไปนี้:

### 🏆 โจทย์: เพิ่มระบบแจ้งเตือนอีเมลเมื่อชำระเงินสำเร็จ (Notification Port)
1. **สร้าง Port ใหม่** ใน `application/ports/notification_service.py`:
   - กำหนด `NotificationService` Protocol ที่มี method `send_order_confirmation(order_id: str, email: str, amount: Decimal) -> bool`
2. **ปรับปรุง Use Case** ใน `application/use_cases/create_order.py`:
   - รับ `notification_service: NotificationService` ใน `__init__`
   - เพิ่ม field `customer_email: str` ใน `CreateOrderCommand`
   - เรียกส่ง Notification เมื่อ `order.mark_as_paid()` สำเร็จ
3. **สร้าง Adapter** ใน `infrastructure/adapters/mock_notification_service.py`:
   - บันทึก log การส่งอีเมล
4. **เขียน Unit Test เพิ่ม** ใน `tests/test_create_order_use_case.py`:
   - ยืนยันว่า Notification ถูกเรียกส่งจริงเมื่อสร้าง Order สำเร็จ
