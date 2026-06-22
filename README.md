# retrospective-skill

`retrospective-coach` 是一个用于个人复盘的 Codex skill。它会根据你提供的“今天状态”和“今天做了什么”，生成中文复盘文档，并给出理性、具体、带一点活气的改进建议。

它的重点不是替你写一段漂亮总结，而是把事实留下来：你原本说了什么、你实际做了什么、状态如何、哪里值得表扬、哪里应该批评、明天应该用 KISS 怎么改善。

## 它适合做什么

- 每日复盘：记录当天状态、行动、产出、问题和 KISS 明日行动。
- 每周总结：从一周的日复盘中提取进展、阻力、模式和下周实验。
- 每月总结：整理本月证据、能力增长、代价、系统修正和下月重点。
- 每年总结：回看年度项目、习惯变化、反复课题和下一年战略重点。

## 核心原则

- 默认使用简体中文生成复盘内容。
- 保留 `原始记录`，不把用户输入吞掉或改写没了。
- 保留 `我做了什么`，让复盘建立在事实上。
- AI 建议必须包含表扬、批评和 KISS 明日行动。
- 表扬要有证据，批评要直接，但不能羞辱。
- 不拍马屁，不阿谀奉承，不写空泛鸡汤。
- 语气可以开朗、有陪伴感，但判断要理性。

## KISS 复盘法

这个 skill 使用 KISS 作为“明天怎么改”的行动框架：

- `Keep｜继续保持`：明天继续保留今天有效的行为、判断或环境条件。
- `Improve｜需要改进`：指出今天最该修的弱点，并给出具体修法。
- `Start｜开始做`：明天新增一个小动作。
- `Stop｜停止做`：明天停止一个拖慢状态、产出或判断的行为。

KISS 不替代 `原始记录`、`我做了什么` 和 `今日状态`。它只负责把 AI 的建议压成明天能执行的动作，避免复盘写得热闹但第二天用不上。

## 安装到本机 Codex

把仓库克隆到 Codex skills 目录下：

```powershell
git clone https://github.com/xxy-0502/retrospective-skill.git C:\Users\<你的用户名>\.codex\skills\retrospective-coach
```

如果你已经在本机维护这个仓库，也可以把整个仓库目录复制到：

```text
C:\Users\<你的用户名>\.codex\skills\retrospective-coach
```

安装后，新开一个 Codex 线程或重启 Codex，让 skill 列表刷新。

## 使用方式

在 Codex 中可以这样说：

```text
使用 $retrospective-coach 做今天复盘。
状态：昨晚睡得晚，上午启动慢，晚上专注度还不错。
今天做了：整理了项目结构，写了 README，推送到 GitHub。
做得好的地方：发现问题后能及时修正。
做得不好的地方：一开始没有把输出语言说清楚。
明天想改善：早点进入工作状态，减少来回补需求。
```

也可以直接说：

```text
今天复盘：状态一般，下午拖了一会儿，但晚上完成了 skill 的部署和 README。帮我总结，并给我明天怎么改。
```

## 生成的目录结构

默认会使用 `reviews/` 作为复盘根目录，并按照年、月、周组织文件：

```text
reviews/
└── 2026/
    ├── year-summary.md
    └── 2026-06/
        ├── month-summary.md
        └── 2026-W25/
            ├── 2026-06-21.md
            └── week-summary.md
```

每日复盘会放进对应的周文件夹。周总结、月总结、年总结会作为独立 Markdown 文件保留。

## 每日复盘内容

每日复盘默认包含：

- `原始记录`
- `我做了什么`
- `今日状态`
- `AI复盘`
- `总结`
- `信号`
- `做得好的地方`
- `做得不好的地方`
- `KISS 明日行动`
- `下一步行动`

## 辅助脚本

仓库内置脚本用于稳定创建目录和占位文件：

```powershell
python scripts\retrospective_journal.py --root reviews --date 2026-06-21 --create
```

脚本会输出对应日期的路径信息，并创建日复盘、周总结、月总结和年总结文件。文件内容由 Codex 根据你的记录继续填写。

## 仓库结构

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── review-framework.md
├── scripts/
│   └── retrospective_journal.py
├── README.md
└── LICENSE
```

## 维护

修改 skill 后，建议运行校验：

```powershell
python C:\Users\<你的用户名>\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
python -m py_compile scripts\retrospective_journal.py
```

然后提交并推送：

```powershell
git status
git add .
git commit -m "Update retrospective skill"
git push
```

## 许可证

MIT License
