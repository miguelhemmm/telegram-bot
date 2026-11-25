# aws-projects

Practice repo for AWS. Each project lives in its own folder with its own SAM template
and deploys automatically from GitHub Actions.

| Project                                             | What it does                                                                            | Deploy trigger                      |
| --------------------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------- |
| [`telegram-gta6-reminder/`](telegram-gta6-reminder) | Lambda that sends a daily GTA 6 countdown to Telegram, fired by an EventBridge schedule | push to `main` touching that folder |

## Architecture

```
GitHub push (main)
   └─► GitHub Actions
         ├─ pytest
         └─ sam build + sam deploy ──► CloudFormation stack "telegram-gta6-reminder"
                                         ├─ Lambda  telegram-gta6-reminder (Python 3.12, arm64)
                                         ├─ EventBridge rule  telegram-gta6-daily  cron(0 3 * * ? *)  [21:00 MX]
                                         └─ CloudWatch log group (14-day retention)

GitHub Actions ──OIDC──► IAM role "github-actions-deploy"   (created once by infra/github-oidc.yaml)
```

No AWS access keys are stored in GitHub. The workflow exchanges a short-lived GitHub
OIDC token for AWS credentials by assuming the deploy role.

## One-time setup

All commands use the personal account profile:

```bash
export AWS_PROFILE=<AWS-PROFILE>
```

### 1. Bootstrap the OIDC provider + deploy role

```bash
aws cloudformation deploy \
  --template-file infra/github-oidc.yaml \
  --stack-name github-oidc \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides GitHubOrg=<OWNER> RepoName=<REPO>

aws cloudformation describe-stacks --stack-name github-oidc \
  --query 'Stacks[0].Outputs[?OutputKey==`RoleArn`].OutputValue' --output text
```

### 2. GitHub secrets

| Secret                | Value                        |
| --------------------- | ---------------------------- |
| `AWS_DEPLOY_ROLE_ARN` | `RoleArn` output from step 1 |
| `TELEGRAM_TOKEN`      | bot token from @BotFather    |
| `CHAT_ID`             | Telegram chat / group id     |

```bash
gh secret set AWS_DEPLOY_ROLE_ARN --body "arn:aws:iam::<ACCOUNT>:role/github-actions-deploy"
gh secret set TELEGRAM_TOKEN   # paste at prompt
gh secret set CHAT_ID --body "<chat id>"
```

### 3. Push

```bash
git push origin main
gh run watch
```

## Day-to-day

Each daily message = countdown headline + a random quote (`src/quotes.py`) + a random
spoiler-free GTA 6 tip (`src/gta_tips.py`). Edit either list freely; no trailing period on tips.

### Test

```bash
cd telegram-gta6-reminder

# this Mac has no system python3.12 -> use uv for tests and Docker for the build
uv run --python 3.12 --with pytest --no-project pytest -q   # unit tests, no network
sam validate --lint                                        # template check

# preview today's message in the terminal (nothing is sent)
uv run --python 3.12 --no-project python -c \
  "import sys, datetime; sys.path.insert(0, 'src'); import app; print(app.build_message(datetime.date.today()))"
```

### Send a real message from the terminal (instead of the Lambda console "Test" button)

```bash
# A) run the handler locally in the Lambda image (needs Docker). Sends to Telegram.
#    env.json is gitignored.
cat > env.json <<'JSON'
{ "ReminderFunction": { "TELEGRAM_TOKEN": "...", "CHAT_ID": "..." } }
JSON
sam build --use-container                                  # builds inside python3.12 arm64 image
sam local invoke ReminderFunction --env-vars env.json -e events/schedule.json

# B) invoke the DEPLOYED function right now (same as the console "Test" button)
sam remote invoke ReminderFunction --stack-name telegram-gta6-reminder
# or
aws lambda invoke --function-name telegram-gta6-reminder out.json && cat out.json
```

`events/schedule.json` is a sample EventBridge scheduled event (from
`sam local generate-event cloudwatch scheduled-event`). The handler ignores the event, so
`--no-event` works too. Rebuild (`sam build`) after code changes before `sam local invoke`;
option B runs whatever was last deployed.

### Deploy

Normal path: push to `main` touching `telegram-gta6-reminder/**`. GitHub Actions runs pytest,
then `sam build` + `sam deploy`. Watch it with `gh run watch`. Then check it with option B above.

### Change the schedule

Edit the `ScheduleExpression` default in `telegram-gta6-reminder/template.yaml`
(cron is **UTC**; Mexico City = UTC-6) and push. To pause without deleting,
set `ScheduleEnabled` to `"false"`.

### Deploy from your laptop instead of CI

```bash
sam deploy --parameter-overrides TelegramToken="$TELEGRAM_TOKEN" ChatId="$CHAT_ID"
```
