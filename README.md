# Atcoder

用 Python 练习 AtCoder。解法按比赛目录归档，每道题都是可单独提交的标准输入／输出脚本。

| 题目 | 解法 | 练习重点 |
| --- | --- | --- |
| [PracticeA. Welcome to AtCoder](https://atcoder.jp/contests/abs/tasks/practice_1) | [practice_1.py](contests/abs/practice_1.py) | 多行输入与格式化输出 |
| [ABC086A. Product](https://atcoder.jp/contests/abs/tasks/abc086_a) | [abc086_a.py](contests/abs/abc086_a.py) | 整数运算与分支 |

## 本地运行

需要 Python 3.12，无第三方依赖。在仓库根目录运行：

```sh
python contests/abs/abc086_a.py
```

输入 `3 4` 并回车，程序输出 `Even`。运行全部测试：

```sh
python -m unittest discover -s tests -v
```

## 添加新题

在 `contests/<比赛 ID>/<题目 ID>.py` 添加脚本，在 `tests/` 添加对应的 `test_*.py`，并更新上方索引。测试用真实的脚本入口传入标准输入，逐字比较标准输出。GitHub Actions 在推送和拉取请求时运行同一条命令。
