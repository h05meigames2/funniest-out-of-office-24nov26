[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/h05meigames2/funniest-out-of-office-24nov26/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/h05meigames2/funniest-out-of-office-24nov26/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

# The Funniest Out-of-Office

An original one-line out-of-office auto-reply for the [make.fun bounty "The Funniest Out-of-Office"](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf) — a single 109-character line in which an unsupervised inbox takes initiative it absolutely should not have taken.

## The program

`main.py` (Python 3.13, standard library only, no network) validates the line — non-empty, at most 140 characters, exactly one line — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) and exits 0.

> "I'm out of office until Monday. My inbox is unsupervised and has already replied 'sounds good!' to a lawsuit."

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/ooo-out python3 main.py
cat /tmp/ooo-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
