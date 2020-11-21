# wordG

A powerful word generator for hackers. Generates passwords with personal information.

## Usage

input.txt: includes person's personal information

output.txt: output of wordlist

wordlist.txt: if any password in your head, write to this (optional)

### Executing

#### Without Optional Wordlist

```shell
python3 wordG/src/app.py "input.txt" "output.txt" ""
```

#### With Optional Wordlist

```shell
python3 wordG/src/app.py "input.txt" "output.txt" "wordlist.txt"
```

*wordG uses words inside wordlist.txt like as a personal information for generating passwords.*
