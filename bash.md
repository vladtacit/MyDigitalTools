# bash tips

## Read file (stdin)

The following solution reads from a file if the script is called with a file name as the first parameter $1 and otherwise from standard input.

```bash
while read line
do
  echo "$line"
done < "${1:-/dev/stdin}"
```

Read file into VAR

```bash
#!/bin/bash

VAR=$(<$1)
echo $VAR
```

## Examples

[Мои личные скрипты для повседневной работы](https://habr.com/ru/companies/ruvds/articles/961514/)

## [~]
