# Connection Guide

What needs connecting, in the order worth doing it, and what Archie has to do personally.

Checked July 18, 2026: the Claude connector registry has **no** ready made connector for Search
Console, GA4, Google Business Profile or WordPress. None of these are a click-to-connect. Each needs
credentials plus a script or a self hosted MCP server.

---

## The single biggest efficiency win

**Search Console, GA4 and Google Business Profile all run off one Google Cloud project.** Set up one
project with one service account, then enable three APIs on it and grant that service account access
in three places. Do not create three separate projects.

Do this once and items 1, 2 and 3 below all get much shorter.

### One time Google Cloud setup

1. Go to <https://console.cloud.google.com/>, signed in as the Google account that owns the
   Brightbox properties.
2. Create a project. Name it something like `brightbox-content-os`.
3. Create a service account under IAM and Admin, Service Accounts. Name it `content-os-reader`.
4. Create a JSON key for it and download it.
5. **Note the service account email.** It looks like
   `content-os-reader@brightbox-content-os.iam.gserviceaccount.com`. You will paste this into three
   different products.

**Where the key file goes.** Not in this repo. Put it at `~/.config/brightbox/service-account.json`
and `chmod 600` it. The repo `.gitignore` already blocks `credentials.json` and `token.json`, but
the safest thing is for the file to never live in the repo directory at all.

**Never paste the contents of that file into chat.** I do not need to see it. I only need to know
the path.

---

## 1. Google Business Profile API. Start this first, it is the slowest.

**Why first:** this is the only item that requires Google to approve an application, and approval
takes weeks. Everything else here you control. Start the clock now even though the value is moderate.

**Value:** removes the manual step from GBP launch and follow up posts. Right now every GBP post is
copy and paste.

**Steps:**

1. In the Cloud project, enable these APIs:
   - Google My Business API (v4.9)
   - My Business Business Information API
   - My Business Account Management API
2. Submit the Business Profile API access request form. Google requires a written justification
   describing what you will build and why.
3. Wait. This is genuinely weeks, sometimes longer, and Google does reject applications.
4. Once approved, grant the service account access to the Brightbox location, or use OAuth against
   your own account.

**What you need before starting:** the Google account that manages the Brightbox GBP listing, and a
short written description of the use case. I can draft that justification if you want. Keep it
honest and narrow: publishing posts linking to published articles, and reading post insights.

**What I will build once approved:** a `scripts/gbp-post` limited to list accounts, list locations,
create post, get post, list posts, and read insights. Nothing that can touch business name,
categories, address, phone, hours or ownership.

**If it gets rejected:** GBP stays manual permanently and that is survivable. The distribution
workflow already produces complete ready to post packages.

---

## 2. Google Search Console. Highest value for effort.

**Why:** the monitoring workflow is currently half blind. The 7 day indexing check and the entire
28 and 90 day analysis depend on this. Without it, `monitor-blog` can only hand you a list of
reports to pull by hand.

**Steps:**

1. Enable the **Google Search Console API** in the Cloud project.
2. Open Search Console, select the brightboxdigital.io property.
3. Settings, Users and permissions, Add user.
4. Paste the service account email. Grant **Full** if you want URL inspection and indexing requests,
   or **Restricted** for read only performance data.

**Decision you need to make:** Restricted is read only and safe. Full allows requesting indexing,
which the workflow uses once per article. I would grant Full, since requesting indexing once on a
new article is the whole point and the workflow already limits it to a single request.

**What you need:** ownership of the Search Console property. You already have this.

**Time:** about ten minutes once the Cloud project exists.

---

## 3. GA4. Do it at the same time as Search Console.

**Why:** sessions, engaged sessions and conversions for the 28 and 90 day checks. Search Console
tells you whether people found the article. GA4 tells you what they did next.

**Steps:**

1. Enable the **Google Analytics Data API** in the Cloud project.
2. Open GA4, Admin, Property Access Management.
3. Add the service account email with the **Viewer** role. Viewer is enough, do not grant more.
4. Note the numeric **Property ID** from Admin, Property Settings. It looks like `123456789`. This
   is not the same as the G- measurement ID.

**What you need:** admin on the GA4 property, and the property ID.

**Time:** about ten minutes.

---

## 4. WordPress. Easy, but genuinely optional.

**Why it is optional:** you chose HTML output. The system already produces WordPress ready HTML that
you paste in. Connecting WordPress saves you a paste, and adds a credential to protect. That is a
real tradeoff, not a formality.

**Connect it if** you get tired of manual pasting, or you want media uploaded and metadata populated
automatically.

**Steps:**

1. Log into WordPress admin.
2. Users, Profile, scroll to Application Passwords.
3. Create one named `Content OS`. Copy the generated password immediately, it is shown once.
4. Store it in `~/.config/brightbox/` alongside the Google key. **Not in the repo. Not in chat.**

**Requirements:** the REST API must be reachable at `https://brightboxdigital.io/wp-json/wp/v2/`.
Some security plugins block it. Worth checking before you generate the password.

**Hard limit that does not change:** drafts only. Publishing stays a separate explicit approval,
connected or not.

**Time:** about five minutes.

---

## 5. Social scheduling. Lowest priority, and I would skip it.

You post to Instagram, Facebook, TikTok, LinkedIn and YouTube. Automating all five means either a
paid scheduler with an API, or five separate platform apps each with its own review process. TikTok
and Instagram in particular are slow to approve API access.

**The reason I would skip it:** the workflow requires your approval on social content anyway, and
Reels need you to actually record them. Automating the final publish step saves very little when the
recording and approval are manual regardless.

**If you want it anyway,** the realistic path is a scheduler with an API, such as Buffer, Metricool
or Publer, rather than five direct integrations. The system would push approved content into the
scheduler queue and you would still confirm.

**Recommendation:** leave this manual. The distribution queue in `clients/brightbox/distribution/`
is sufficient.

---

## 6. Verify NeuronWriter from a cloud Routine

Not a new connection. NeuronWriter works in local Claude Code, but that does not prove it works from
a scheduled cloud Routine, which is a different environment.

**This must pass before the Routine is created.** Test it by running a Routine once manually and
confirming it can call `list-projects`.

---

## Priority order

| # | System | Effort | Lead time | Value | Do it? |
|---|---|---|---|---|---|
| 1 | GBP API | Medium | **Weeks** | Medium | Start now, purely because of the wait |
| 2 | Search Console | Low | Same day | **High** | Yes |
| 3 | GA4 | Low | Same day | High | Yes |
| 4 | WordPress | Low | Same day | Low | Optional |
| 5 | Social | High | Weeks | Low | Skip |
| 6 | NeuronWriter in Routine | Low | Same day | Blocking | Required before scheduling |

**Suggested sequence for one sitting:** create the Cloud project, submit the GBP application to start
the clock, then connect Search Console and GA4 while you are already in the console. That is roughly
an hour and unblocks the monitoring workflow entirely.

---

## Security rules for all of this

- No credential, key, token or application password goes in this repository. Ever.
- Do not paste any secret into chat. I need file paths and property IDs, never the values.
- Service account gets the minimum role that works. Viewer on GA4. Nothing beyond posts on GBP.
- Cloud Routines get only the connectors discovery needs. Not GBP, not WordPress, not GA4.
  An unattended run should never hold write access to anything published.
- If a key is ever exposed, revoke it in the Cloud console first and regenerate. Do not try to
  clean it out of git history and assume that was enough.

---

## What I can and cannot do

**I can:** write every script, wire up credential loading from a path you give me, build the
monitoring and GBP posting workflows, and draft the GBP API justification text.

**I cannot, and you have to do personally:** anything in the Google Cloud console, any OAuth consent
screen, the GBP API application, generating the WordPress application password, and granting the
service account access inside Search Console and GA4. These all require you to be signed in as the
account owner.
