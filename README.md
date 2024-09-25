# Backend Builderplate

Tired of generating a new backend constinously for your projects? This repo provides a backend builderplate, the skeleton, for deploying your database and basic API routes locally. For the database, we are using *MariaDB*, but feel free to implement your favorite one. 

The API is created using Flask and the entire project is locally deployed using Docker. For the database, it would be locally deployed using MariaDB and Dockerfile. 

# The docker-compose.yml file

For the moment, it just deploys a local MariaDB database and the backend API in charge of interacting with the database.

# The init.sql file

It generates a new database with the `users` table that the frontend will use to obtain all the information needed. If you want to create more tables when generating the database, just add the necessary code in this file.

# How to deploy the project locally.

As all the backend would be on a docker container, it is not necessary to install anything more than Docker. Execute the following commands in the correspondant order.

```bash
docker-compose build && docker-compose up
```

If you want to interact with the database using a terminal, just execute:

```bash
sudo docker exec -it backend_builderplate bash
```

A new docker terminal will be open for you to interact with the container. Execute:

```bash
mariadb -u admin@localhost.com -p
```

where the password is: `1234`

Voilà. You are inside the database. Use the command:

```bash
use backend_db;
```

for start using the database you have just deployed. If you want to check that everything is working correctly, you can execute:

```bash
curl http://localhost:5000/get-users
```

where you should get the following output:


```bash
{"response":[["admin","admin@localhost.com","1234"]]}
```
 Enjoy when using this builderplate and feel free to contribute to this opensource project

# Contribution Guidelines

Thank you for your interest in contributing to backend-builderplate! We value feedback and suggestions from the open-source community. Please take a moment to review our contribution guidelines before contributing.

## Opening an Issue

If you encounter a bug in the code or have an idea for an enhancement, we encourage you to open an issue. There are two issue templates to guide your contribution. Please select the one that best fits your suggestion:

### 1. Bug Fix
**Before submitting:** Check the issues tab to ensure a similar issue isn’t already open or hasn’t been recently closed. Duplicate issues may be deleted.

**What to Include:**
- Detailed steps to reproduce the bug
- Actual behavior vs expected
- System information (OS, version, etc.)
- Any error logs or screenshots

*To raise the priority of an existing issue, please react or comment on the post.*

**Bug Report Template:**

*(Please copy and paste the following into your issue)*

```markdown
---
Name: Bug report
---
**DESCRIPTION**
[Insert a clear and concise description of the issue.]

**STEPS TO REPRODUCE**
1. [Insert steps here]

**EXPECTED BEHAVIOR**
[Insert what you expected to happen.]

**SYSTEM INFORMATION:**
[Insert OS: e.g. Windows, MacOS]

**ADDITIONAL CONTEXT**
[Insert any other context about the problem here.]
```

### 2. Feature Request
**Before starting:** open a new issue to inform other developers about your proposed feature.

**What to include:**
- Brief description of the feature and its purpose
- Link to the branch you’re developing the feature on
- *(Optional)* Areas where you might encounter challenges or would feedback would be helpful

**Feature Request Template:**

*(Please copy and paste the following into your issue)*

```markdown
—
Name: Feature request 
—
 **Is your feature request related to a problem? Please describe, if applicable.**
[Insert concise description of the problem.]

**Describe the solution you'd like**
[Insert concise description of what you want to happen.] 

**Additional context (optional)** 
[Insert other context or screenshots about the feature request.]
```

## Committing Changes

Follow these steps when committing:
- **Opening an Issue:** Before working on a non-trivial issue, open an issue to describe the bug or proposed feature.
- **Branching:** Always fork the repository and check out a new branch using git checkout -b <my_feature>
- **Descriptive Branch Names:** Name your branch descriptively to indicate what issue is being worked on
- **Commit Often:** Commit frequently with meaningful descriptions, especially if the feature could break the code or cause conflicts
- **Merge Conflicts:** Ensure there are no merge conflicts before submitting a pull request

### Commit Message Guidelines
To maintain consistency, follow these guidelines when writing commit messages.

**Format the First Line:**
- Keep it short (under 50 characters)
- Begin with one of the following prefixes:
  - BUG: for fixing bugs
  -  FEAT: for adding a new feature
  -  DOC: for adding to the documentation
  -  TEST: for modifying or adding new tests

**Examples of Good Commit Messages (First Lines):**
- `BUG: fix null pointer exception when adding user`
- `FEAT: implement search functionality for users`

All commit messages should follow the following format:
```markdown
[First line - <51 characters, starts w/prefix]
[Second line - blank]
[Third line (optional) - explain commit, reference issue #, etc.]
```

**Example of What Not to Do:**
- `Fixed null pointer exception when creating a new user profile`
  - **Why:** The message is too long and does not begin with the required prefix.

## Pull Requests
To ensure smooth collaboration, follow these PR procedures:

- **Branching:** Ensure you’ve forked the repository and created a new branch with a descriptive name for each issue.
- **Focus on a Single Issue:** Each pull request should address only 1 issue at a time. Large pull requests targeting multiple issues will take longer to review and may cause conflicts for other contributors.
- **Target Branch:** All pull requests should go into the `main` branch.
- **Clear Description:** Include a concise description of your changes, referencing the issue number that you worked on.

**Pull Request Template:**

*(Please copy and paste the following into your issue)*

```markdown
**What does this PR do?**
- [ ] Fixes Issue # 
- [ ] Implements new feature 

**Summary of changes**
[Insert brief description of what your PR does.]

**Additional Notes (Optional)**
[Insert additional context]
```
