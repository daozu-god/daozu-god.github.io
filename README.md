# Yaohui — Independent Researcher

Bilingual academic homepage built with Hugo and deployed to GitHub Pages.

- Website: https://daozu-god.github.io/
- English: https://daozu-god.github.io/en/
- 中文: https://daozu-god.github.io/zh/

## Edit the site

Edit the Markdown files under `content/en/` and `content/zh/`. Update site identity and research-area settings in `hugo.toml`.

The public profile uses the name Yaohui and the neutral title Independent Researcher. No degree, institutional appointment, publication, award, or other credential is asserted. Add only accurate, verifiable information.

## Local preview

Install Hugo 0.167.0 or later, then run `hugo server -D`. Build locally with `hugo --gc --minify`.

## Deployment

The workflow in `.github/workflows/hugo.yaml` builds the site and deploys it to GitHub Pages whenever a commit is pushed to `main`. In the repository, open **Settings → Pages** and choose **GitHub Actions** as the build and deployment source if it is not already selected.

See [README.zh-CN.md](README.zh-CN.md) for the Chinese guide.