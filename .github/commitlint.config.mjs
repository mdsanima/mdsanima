// Defined rules on commit messages; see the docs: https://commitlint.js.org/#/reference-rules

/** The array of rule types that are allowed in commit messages. */
const typesRule = ["build", "chore", "ci", "docs", "feat", "fix", "perf", "refactor", "revert", "style", "test"];

/** The array of rule subjects that are allowed in commit messages. */
const subjectsRule = ["upper-case", "pascal-case", "sentence-case", "start-case"];

/** The rules configuration for commitlint thats is used in GitHub Workflow Actions. */
const commitlintConfig = {
  rules: {
    "type-enum": [2, "always", typesRule],
    "type-case": [2, "always", "lower-case"],
    "type-empty": [2, "never"],
    "scope-case": [2, "always", "kebab-case"],
    "subject-case": [2, "never", subjectsRule],
    "subject-empty": [2, "never"],
    "subject-full-stop": [2, "never", "."],
    "header-max-length": [2, "always", 80],
    "body-case": [2, "always", "sentence-case"],
    "body-leading-blank": [2, "always"],
    "body-max-line-length": [1, "always", 100],
    "footer-leading-blank": [2, "always"],
    "footer-max-line-length": [1, "always", 100],
  },
};

export default commitlintConfig;
