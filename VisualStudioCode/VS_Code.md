# VS Code

[Пишем простые расширения VS Code для автоматизации задач командной строки](https://habr.com/ru/companies/ncloudtech/articles/822475/)

[Всё, что необходимо (и достаточно) знать о создании пользовательских интерфейсов в расширениях VS Code](https://habr.com/ru/companies/ncloudtech/articles/881890/)

[Agent mode: available to all users and supports MCP](https://code.visualstudio.com/blogs/2025/04/07/agentMode)

[Самое заметное обновление VS Code в 2025 году. Агенты теперь доступны всем, бесплатно и с поддержкой MCP](https://habr.com/ru/companies/bar/news/898538/) **Agent mode**

Как подключить прокси в VS Code?

```
{
    "http.proxy": "http://user:pass@my.proxy.address:8080",
    "http.proxyStrictSSL": false,
}
```

[Частые полезные настройки VS Code](https://gist.github.com/muks999/50caf7ba36c4899233d25cd620ed4b79)

## Workspaces

[What is a VS Code "workspace"?](https://code.visualstudio.com/docs/editor/workspaces)

[User and Workspace Settings](https://code.visualstudio.com/docs/getstarted/settings)

[Multi-root Workspaces](https://code.visualstudio.com/docs/editor/multi-root-workspaces)

## Language Server Protocol - LSP

[Langserver.org](https://langserver.org/)

[Влияние протокола языкового сервера (LSP) на будущее IDE](https://habr.com/ru/articles/555502/)

[Обзор LSP: что это такое, зачем нужно, как работает](https://habr.com/ru/companies/sberbank/articles/838786/)

[Зачем нужен протокол языкового сервера (LSP)?](https://habr.com/ru/companies/piter/articles/667882/)

[Comment] На середине плюнул и пошёл читать оригинал, очень уж перевод кривой

[Original: Why LSP?](https://matklad.github.io/2022/04/25/why-lsp.html)


## VS Code Extensions

[Your First Extension](https://code.visualstudio.com/api/get-started/your-first-extension)

[Extension API](https://code.visualstudio.com/api)

[Пишем простые расширения VS Code для автоматизации задач командной строки](https://habr.com/ru/companies/ncloudtech/articles/822475/)

[Всё, что необходимо (и достаточно) знать о создании пользовательских интерфейсов в расширениях VS Code](https://habr.com/ru/companies/ncloudtech/articles/881890/)

## VS Code. Python virtual environment

[Python environments in VS Code](https://code.visualstudio.com/docs/python/environments) **Read it!**

```bash
# 1. Install package 
sudo apt install -y python3-venv

# 2. Create virtual virtual environment
python3 -m venv ~/python-bot-venv

# 3. Activate virtual environment
source ~/python-bot-venv/bin/activate

# 4. Install needed packages
(python-bot-venv) pip install python-telegram-bot sqlalchemy python-dotenv

```

~/python-bot-venv/bin/python **??? Как правильно настроить VS Code?**

[VS Code, python, контейнеры — как обуздать эту триаду и разрабатывать внутри контейнера](https://habr.com/ru/companies/amvera/articles/836604/)

[Переменные окружения .env в приложениях Python](https://ramziv.com/article/40) About python-dotenv

----

[Настройка подключения через SSH в VSCode](https://timeweb.cloud/docs/unix-guides/configuring-ssh-connection-in-vscode)

[Remote SSH: Tips and Tricks](https://code.visualstudio.com/blogs/2019/10/03/remote-ssh-tips-and-tricks)

## Read it

[Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)

[Полезные расширения VScode для работы с документацией](https://habr.com/ru/companies/agima/articles/798523/)

[Работа с Git в Visual Studio Code](https://htmlacademy.ru/blog/git/git-in-vscode)

[Плагины для VS Code, которые стоит использовать в 2024 году](https://habr.com/ru/companies/ru_mts/articles/825234/)

[VSCode, SourceCraft Code Assistant и микроконтроллеры](https://habr.com/ru/companies/yandex/articles/892502/)

---

[SourceCraft Code Assistant](https://yandex.cloud/ru/docs/code-assistant/)

[Как мы учили Yandex Code Assistant помогать разработчикам с написанием кода и делать их счастливыми](https://habr.com/ru/companies/yandex/articles/841436/)

[VSCode, SourceCraft Code Assistant и микроконтроллеры](https://habr.com/ru/companies/yandex/articles/892502/)

---

[Data Wrangler Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.datawrangler)

[Data Wrangler Extension for Visual Studio Code](https://github.com/microsoft/vscode-data-wrangler)

[Getting Started with Data Wrangler in VS Code](https://code.visualstudio.com/docs/datascience/data-wrangler)

[Data Science in VS Code tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial)

[Как я использую плагины VSCode для обработки Json-файлов в работе системным аналитиком](https://habr.com/ru/companies/ru_mts/articles/829134/)

[Remote Development using SSH](https://code.visualstudio.com/docs/remote/ssh)

## Markdown preview

[Github markdown rendering](https://github.com/mjbvz/vscode-github-markdown-preview)

ToDo: See [Features](https://github.com/mjbvz/vscode-github-markdown-preview#features)

[Markdown preview](https://code.visualstudio.com/Docs/languages/markdown#_markdown-preview)

## Forks

[Build and Run Code-OSS](https://github.com/Microsoft/vscode/wiki/How-to-Contribute#build-and-run) - How make fork the VS Code repository

[VSCodium](https://vscodium.com/) from [Codeium](https://habr.com/ru/companies/otus/articles/894448/)

[VSCodium GitHub](https://github.com/VSCodium/vscodium) - binary releases of VS Code without MS branding/telemetry/licensing

[Cursor](https://www.cursor.com/) - The AI Code Editor from [Anysphere](https://anysphere.inc/)

[Обзор AI-ассистента Cursor для разработчиков](https://habr.com/ru/companies/otus/articles/844866/)

[Cursor vs Windsurf vs GitHub Copilot](https://habr.com/ru/companies/otus/articles/894448/)

Virtual assistants:

* GitHub - Copilot
* Codeium - Windsurf
* Anysphere - Cursor

## ToDo

[Проверка русской и английской орфографии в VSCode](https://qna.habr.com/q/630783)

[Google опубликовала расширение Colab для Visual Studio Code](https://habr.com/ru/news/967144/)

## [~]
