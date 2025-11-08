# Git

[Book](https://git-scm.com/book)

[Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world)

[Pro Git](../_Store/progit-ru.1027.pdf)

[15 команд Git, которые покрывают 90% повседневной работы разработчика](https://habr.com/ru/articles/905658/)

[Как я использую git](https://habr.com/ru/companies/beget/articles/852626/)

[Шпаргалка для новичков — от GIT до Деплоя](https://habr.com/ru/articles/928532/) **GitOps**

[Think Like (a) Git](https://think-like-a-git.net/)

[GitHub Flavored Markdown Spec](https://github.github.com/gfm/)

[emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet)

## Create repository

[ConvenientHome](https://github.com/vladtacit/ConvenientHome)

See shell scripts in _Store!

Показать подписи всех коммитов в логе, начиная с последнего коммита:

```bash
git log --show-signature
```

Подпись конкретного коммита:

```bash
git cat-file -p <commit_hash>
```

[Клонирование и создание репозиториев](https://git-scm.com/book/ru/v2/%D0%9F%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-C%3A-%D0%9A%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B-Git-%D0%9A%D0%BB%D0%BE%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B8-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B5%D0%B2) **git init/clone**

## Work with multiple remotes

[Git and multiple remotes](https://blog.tinned-software.net/git-and-multiple-remotes/)

[Pushing to Multiple Git Repos](https://gist.github.com/rvl/c3f156e117e22a25f242)

[Git - Pushing code to two remotes](https://stackoverflow.com/questions/14290113/git-pushing-code-to-two-remotes) **!!!**

## Read it!

[GitHub Flow](https://docs.github.com/ru/get-started/using-github/github-flow)

[Мегагайд: культура работы с Git](https://habr.com/ru/companies/yandex_praktikum/articles/812139/) **Git Flow**

[Ежедневная работа с Git](https://habr.com/ru/articles/174467/)

[19 советов по повседневной работе с Git](https://habr.com/ru/companies/vk/articles/267595/)

[Достаточно Git-а, чтобы быть (менее) опасным](https://habr.com/ru/articles/268951/)

[Git: Больше чем commit и push. 5 команд, которые спасут вашу репутацию (и нервные клетки)](https://habr.com/ru/companies/timeweb/articles/927102/)
>revert, stash, cherry-pick, reset --soft и bisect

[Git снизу вверх](https://habr.com/ru/companies/intel/articles/344962/)

[Документация по GitHub Pages](https://docs.github.com/ru/pages)

[Линус Торвальдс, Бьёрн Страуструп и Брендан Грегг контрибьютят в мой хобби-проект. Зачем?](https://habr.com/ru/post/515550/)

[Генеалогическое древо внутри Git](https://habr.com/ru/post/351158/)

[23 команды Git, которые должен знать каждый разработчик](https://www.cloud4y.ru/blog/23-git-command/)

[30 команд Git, необходимых для освоения интерфейса командной строки Git](https://habr.com/ru/companies/ruvds/articles/599929/)

[Ежедневная работа с Git](https://habr.com/ru/articles/174467/)

[Git за полчаса: руководство для начинающих](https://proglib.io/p/git-for-half-an-hour)

[Git для новичков (часть 1)](https://habr.com/ru/articles/541258/)  
[Git для новичков (часть 2)](https://habr.com/ru/articles/542616/)

[Описание внутреннего git протокола](https://habr.com/ru/articles/823642/)

[Делаем резервное копирование сайта с помощью git и Makefile](https://habr.com/ru/articles/425259/)

[Знания как код: архитектурный репозиторий в git на базе PlantUML](https://habr.com/ru/companies/rshb/articles/816199/)

[Как информативно оформить профиль на GitHub?](https://habr.com/ru/articles/813399/)

[About passkeys](https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys)

---

## GitHub Actions

[Документация по GitHub Actions](https://docs.github.com/ru/actions)

[Github Actions. Простой пример для уверенного знакомства](https://habr.com/ru/articles/711278/)

[Run your GitHub Actions locally!](https://github.com/nektos/act)

---
[Как работать с Git и Gitflow: разбираемся на примерах](https://habr.com/ru/companies/beeline_cloud/articles/829142/)

---
[CI/CD на GitHub Actions и GitLab CI для самых маленьких. Часть 1](https://habr.com/ru/articles/914560/)

[CI/CD на GitHub Actions и GitLab CI для самых маленьких. Часть 2](https://habr.com/ru/articles/914614/)

## GitVerse

On [GitVerse](https://gitverse.ru/new) create a new repository @{USER}/@{REPO}

@{USER} - user name
@{REPO} - repository name

### New repository (SSH)

[How to configure command line git to use ssh key](https://stackoverflow.com/questions/23546865/how-to-configure-command-line-git-to-use-ssh-key)

On the localhost create a directory for the repository and go to it.

```bash
touch README.md
git init
git add .
git commit -m "Initial commit"
git branch -M master
git remote add origin ssh://git@gitverse.ru:2222/${USER}/${REPO}.git
git push -u origin master
```

### Existing repository (SSH)

On the localhost go to the repository directory

```bash
git remote add origin ssh://git@gitverse.ru:2222/${USER}/${REPO}.git
git branch -M master
git push -u origin master
```

---

[10 полезных команд Git](https://habr.com/ru/companies/otus/articles/795525/)

## GitHub CLI

[GitHub CLI](https://cli.github.com/)

[GitHub’s official command line tool](https://github.com/cli/cli)

[Как улучшить свои навыки работы с Git с помощью GitHub CLI](https://habr.com/ru/companies/otus/articles/867782/)

## Git tags

[Git - Работа с тегами](https://git-scm.com/book/ru/v2/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Git-%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-%D1%82%D0%B5%D0%B3%D0%B0%D0%BC%D0%B8)

[8 правил, которые пригодятся при описании Git-коммитов](https://habr.com/ru/companies/sberbank/articles/662744/)

[Отрабатываем Git hooks на автоматизации commit message](https://habr.com/ru/companies/dins/articles/584562/)

## [~]

