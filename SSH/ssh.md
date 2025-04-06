# SSH

## Authentication

[Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Generating a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com" -f /path/to/key-file -N passphrase
```

Check the key-file with passphrase:

```bash
ssh-keygen -y -f /path/to/key-file_with_passphrase
echo $?
```
The exit status ($?) will be 1 to indicate an error.

## Local TCP forwarding

Zabbix:

```bash
$ ssh -L 8484:localhost:8484 vm@45.155.205.35
Last login: Sun Feb  2 09:41:14 2025 from 188.168.123.198
```

PostgreSQL:

## Read it!

[Знакомство с SSH](https://habr.com/ru/articles/802179/)

[Памятка пользователям ssh](https://habr.com/ru/articles/122445/)

[Как настроить прокси в Google Chrome](https://proxy-top.info/articles/nastroyka-proxy-chrome/)

[Configuring a SOCKS proxy server in Chrome](https://www.chromium.org/developers/design-documents/network-stack/socks-proxy/)

[SSH-туннели: настройка и примеры использования](https://firstvds.ru/technology/ssh-tunnels)

&#9635;
