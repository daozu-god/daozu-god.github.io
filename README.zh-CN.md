# Yaohui 学术个人主页

这是一个基于 Hugo 的中英双语独立学术研究主页，使用 GitHub Pages 免费托管。

- 网站首页：https://daozu-god.github.io/
- 英文主页：https://daozu-god.github.io/en/
- 中文主页：https://daozu-god.github.io/zh/

## 网站栏目

- 关于我 / About
- 研究方向 / Research
- 学术论文 / Publications
- 预印本 / Preprints
- 研究项目 / Projects
- 技术笔记 / Technical Notes
- 学术简历 / Academic CV
- 联系方式 / Contact

## 本地预览

安装 Hugo 0.167.0，然后在仓库根目录运行：

```bash
hugo server -D
```

正式构建：

```bash
hugo --gc --minify
```

## 自动部署

仓库已配置 GitHub Actions 工作流：每次向 main 分支推送时自动构建并部署。

首次发布前，请进入 GitHub 仓库 **Settings → Pages**，将 **Build and deployment → Source** 设置为 **GitHub Actions**。随后在 **Actions** 页面查看构建和部署结果。

## 修改个人资料

- 站点姓名、身份、语言设置及研究方向：`hugo.toml`
- 英文页面：`content/en/`
- 中文页面：`content/zh/`
- 页面模板：`layouts/`
- 样式：`static/css/site.css`

当前公开资料采用 Yaohui 与 Independent Researcher 的中性表述。请仅添加真实、可核验的学历、任职、论文、奖项和研究成果；不要公开密码、私人数据、未获授权的论文材料或仍处于协调披露期的漏洞细节。
