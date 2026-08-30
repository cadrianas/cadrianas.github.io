#!/usr/bin/env bash
set -euo pipefail

tmp_dir="$(mktemp -d)"
tmp_override="${tmp_dir}/comments-test-override.yml"
tmp_site="${tmp_dir}/site"
giscus_post="_posts/2022-12-10-giscus-comments.md"
disqus_post="_posts/2015-10-20-disqus-comments.md"
created_giscus_post=false
created_disqus_post=false

cleanup() {
  if [[ "${created_giscus_post}" == true ]]; then
    rm -f "${giscus_post}"
  fi
  if [[ "${created_disqus_post}" == true ]]; then
    rm -f "${disqus_post}"
  fi
  rm -rf "${tmp_dir}"
}
trap cleanup EXIT

mkdir -p _posts
if [[ ! -f "${giscus_post}" ]]; then
  cp test/fixtures/comments/giscus.md "${giscus_post}"
  created_giscus_post=true
fi
if [[ ! -f "${disqus_post}" ]]; then
  cp test/fixtures/comments/disqus.md "${disqus_post}"
  created_disqus_post=true
fi

cat >"${tmp_override}" <<'YAML'
giscus:
  repo: alshedivat/al-folio
  repo_id: R_kgDOExample
  category: Comments
  category_id: DIC_kwDOExample
disqus_shortname: al-folio
YAML

ruby -EUTF-8:UTF-8 "$(command -v bundle)" exec jekyll build --config "_config.yml,${tmp_override}" -d "${tmp_site}" >/dev/null

giscus_page="${tmp_site}/blog/2022/giscus-comments/index.html"
disqus_page="${tmp_site}/blog/2015/disqus-comments/index.html"

grep -q 'https://giscus.app/client.js' "${giscus_page}"
if grep -q 'giscus comments misconfigured' "${giscus_page}"; then
  echo "unexpected giscus misconfiguration warning in ${giscus_page}" >&2
  exit 1
fi

grep -q 'id="disqus_thread"' "${disqus_page}"
grep -q '.disqus.com/embed.js' "${disqus_page}"

echo "comments integration checks passed"
