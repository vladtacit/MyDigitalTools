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

[Про SSH Agent](https://habr.com/ru/companies/skillfactory/articles/503466/)

## SSH config file

[SSH config file for OpenSSH client](https://www.ssh.com/academy/ssh/config) **VPN!**

[Advanced SSH usage](https://johannes.truschnigg.info/writing/2022-07_advanced_ssh_usage/)

```bash
touch ~/.ssh/config
chmod 0700 ~/.ssh/config
```

**0700 ???** execute ???

Parameters:

* **HostName** — определяет имя реального хоста для входа в систему, альтернативно, вы можете использовать числовые IP-адреса, это также разрешено (как в командной строке, так и в спецификациях HostName).
* **User** — указывает, что пользователь должен войти в систему.
* **Port** — устанавливает номер порта для подключения на удаленном хосте, по умолчанию — 22. Используйте номер порта, настроенный в файле конфигурации sshd удаленного хоста.
* **Protocol** — этот параметр определяет версии протокола, которые ssh должен поддерживать в порядке предпочтения. Обычными значениями являются «1» и «2», несколько версий должны быть разделены запятыми.
* **IdentityFile** — определяет файл, с которого считывается идентификатор аутентификации пользователя DSA, Ed25519, RSA или ECDSA.
* **ForwardX11** — определяет, будут ли соединения X11 автоматически перенаправляться по защищенному каналу и устанавливать DISPLAY. Он имеет два возможных значения «да» или «нет».
* **Compression** — оно используется для установки сжатия во время удаленного соединения со значением «да». По умолчанию «нет».
* **ServerAliveInterval** — устанавливает интервал таймаута в секундах, после которого, если никакой ответ (или данные) не был получен с сервера, ssh отправит сообщение через зашифрованный канал, чтобы запросить ответ от сервера. Значение по умолчанию равно 0, то есть сообщения не будут отправляться на сервер, если была определена опция BatchMode.
* **ServerAliveCountMax** — устанавливает количество живых сообщений сервера, которые могут быть отправлены без получения ответа ssh с сервера.
* **LogLevel** — определяет уровень детализации, который используется при регистрации сообщений из ssh. Допустимые значения включают: QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG, DEBUG1, DEBUG2 и DEBUG3. И значение по умолчанию — INFO.

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

[Как SSH появился на 22 порту](https://habr.com/ru/articles/418533/)

[Маленькие хитрости SSH](https://habr.com/ru/companies/itsumma/articles/499920/)

&#9635;
