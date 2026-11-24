# weirdest-job-title-20261124

[![make.fun · Weirdest Job Title: Blind Judge Showdown](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)
[![rank](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/sopiahusen42/weirdest-job-title-20261124/rank.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/leaderboard)
[![reward](https://make.fun/badge/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922/sopiahusen42/weirdest-job-title-20261124/reward.svg)](https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922)

A job title for a position that cannot exist: the landlocked division still needs its lighthouse keeper. This is the entry for make.fun's "Weirdest Job Title: Blind Judge Showdown" bounty.

## The line

```
Lighthouse Keeper, Landlocked Division
```

## Run it

```
python3 main.py
cat /output/entry.txt
```

## How it works

main.py holds the line in the constant `ENTRY` and validates it before writing: it must be a string, non-blank, between 1 and 60 Unicode code points, free of `\n` and `\r`, and equal to its own stripped form. Any failure prints one line to stderr and exits 1. On success it creates the output directory, writes `ENTRY` plus a newline as UTF-8 with newline translation disabled, reads the bytes back to confirm they match, prints nothing and exits 0. The output directory is `MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`. The program is deterministic and takes no input.

Entered on make.fun with referral code 7mrxg5tp - https://make.fun/?ref=7mrxg5tp
