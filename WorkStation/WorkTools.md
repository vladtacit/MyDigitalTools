# Work tools

[Простые лайфхаки для автоматизации работы с помощью Python](https://habr.com/ru/companies/netologyru/articles/881796/)

[Закадровый перевод видео](https://github.com/ilyhalight/voice-over-translation)
>Небольшое расширение, которое добавляет закадровый перевод видео из YaBrowser в другие браузеры

[19 команд ffmpeg для любых нужд](https://habr.com/ru/articles/171213/)

[Microsoft Edit](https://github.com/microsoft/edit)
>A simple editor for simple needs.

## find command

[find(1) — Linux manual page](https://man7.org/linux/man-pages/man1/find.1.html)

[10 ways to use the Linux find command](https://www.redhat.com/en/blog/linux-find-command)

[find (Unix)](https://en.wikipedia.org/wiki/Find_(Unix))

[find](https://ru.wikipedia.org/wiki/Find)
>утилита поиска файлов по имени и другим свойствам, используемая в UNIX‐подобных операционных системах.

Hide "Permission denied" error:

```bash
find . > search_result 2> >(grep -v 'Permission denied$' >&2)
```

## Compress and uncompress

[GNU zip. WiKi](https://en.wikipedia.org/wiki/Gzip)

[GNU zip. WiKi Rus](https://ru.wikipedia.org/wiki/Gzip)

**gzip** выполняет только две функции: сжатие и распаковку одного файла; упаковка нескольких файлов в один архив невозможна. При сжатии к оригинальному расширению файла добавляется суффикс .gz. Для упаковки нескольких файлов обычно их сначала архивируют (объединяют) в один файл утилитой tar, а потом этот файл сжимают с помощью gzip. Таким образом, сжатые архивы обычно имеют двойное расширение .tar.gz, либо сокращённое .tgz.

To unzip a gzipped file you use the gunzip command:

```bash
gunzip filename.gz
```

## [~]
