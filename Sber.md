# Sber (Cloud.ru Evolution)

[Платформа Cloud.ru Evolution](https://console.cloud.ru/projects/52f63d48-0a1c-4082-8bd2-8b4832cc3979/spa/svp?customerId=18b32453-c607-4c69-af12-70ed3fe53a80)

Virtual machine: vm-fair-wolf
ID: 250b4bc9-ff97-4e22-97ef-4ba5b707050c
Зона доступности: ru.AZ-2
Публичный IP: 45.155.205.35

host: vm-fair-wolf
user: vm
Path to private-key: /home/vlad/.ssh/fair-minded.pub

fair-wolf.vladtacit.online 

Connecting using SSH keys:

```bash
ssh vm@45.155.205.35
```

Если есть несколько приватных ключей, дополнительно укажите, какой из них использовать для подключения:

```bash
ssh -i /path/private-key user@host-public-ip
```

[FairWolf Dashboard](https://console.cloud.ru/projects/52f63d48-0a1c-4082-8bd2-8b4832cc3979/spa/dashboards/product/eiv?start=7200&end=latest&customerId=18b32453-c607-4c69-af12-70ed3fe53a80&vm_id=250b4bc9-ff97-4e22-97ef-4ba5b707050c)

---

После апгрейда Линукс перестали работать сетевые доступы.

Чтобы исправить надо выполнить команды от пользователя с root-правами:

```bash
sudo cloud-init clean
sudo cloud-init init
```

После этого могут измениться отпечатки ssh-сервера, это нормально.

Надо удалить запись из known_hosts:

```bash
ssh-keygen -f "/home/vlad/.ssh/known_hosts" -R "45.155.205.35"
```

---

&#9635;
