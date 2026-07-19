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

### Done, July 18, 2026

| Item | Value |
|---|---|
| Cloud project ID | `brightbox-digita-1743176991871` |
| Service account email | `content-os-reader@brightbox-digita-1743176991871.iam.gserviceaccount.com` |
| Key path | `~/.config/brightbox/service-account.json`, mode 600 |
| Search Console API | Enabled |
| Google Analytics Data API | Enabled |

The service account email is not a secret. It is an identifier and it needs to be pasted into
Search Console and GA4. The **key file** is the secret.

Still outstanding: granting that service account access inside Search Console and GA4, and the
GA4 numeric property ID.

---

## 1. Google Business Profile API. Start this first, it is the slowest.

**Why first:** this is the only item that requires Google to approve an application, and approval
takes weeks. Everything else here you control. Start the clock now even though the value is moderate.

**Value:** removes the manual step from GBP launch and follow up posts. Right now every GBP post is
copy and paste.

### Eligibility, confirm before applying

Google requires all of these. Verified against the Business Profile API prerequisites, July 18, 2026.

- A verified, active Google Business Profile for **60 or more days**. Brightbox is well past this.
- A website listed on the profile. Brightbox has one.
- The request submitted from an email that is an **owner or manager** on the profile. Use that
  account, not a different Google login.

### APIs to enable

Of the seven that surface when searching the API Library, enable **three**:

| API | Why |
|---|---|
| My Business Account Management API | Lists accounts. Needed to find the profile |
| My Business Business Information API | Lists locations. Needed to target the right listing |
| Business Profile Performance API | Post views and CTA interactions for the 28 day check |

Skip My Business Q&A, Lodging (hotels only), Notifications and Place Actions. None are in scope.

**The Google My Business API (v4.9) does not appear in that search result list.** That is the one
holding the `localPosts` endpoint, which is what actually creates a GBP post. The three APIs above
give read access to accounts, locations and performance data. They do not give posting. Posting is
what the approval process gates.

### Confirming approval status

Do not guess. Google gives a concrete test:

> Open the API quotas page in the Cloud console. **0 QPM means the project is not approved.
> 300 QPM means it is approved.**

Check this after submitting, and check it again before assuming any posting workflow can run.

### Steps

1. Enable the three APIs above.
2. Submit the Business Profile API access request form from the owner or manager account.
   Justification text is drafted in `clients/brightbox/gbp-api-request-draft.md`.
3. Wait. Genuinely weeks. Google does reject applications.
4. Check quota. 0 QPM means still waiting.
5. Once approved, grant the service account access to the Brightbox location, or use OAuth against
   the owner account.

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

## 4. WordPress. Declined.

**Archie declined July 18, 2026.** Not connecting. Articles stay as WordPress ready HTML that Archie
pastes in himself. Do not re-propose this.

The detail below is kept only in case that decision changes later.

<details>
<summary>Original WordPress notes</summary>

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

</details>

---

## 5. Social scheduling. Declined.

**Archie declined July 18, 2026.** Not connecting any social platform or scheduler. All social
distribution stays manual through the queue in `clients/brightbox/distribution/`. Do not re-propose.

The reasoning below still holds and is why this was the right call.

<details>
<summary>Original social notes</summary>

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

</details>

---

## 6. Keyword volume data via the Google Ads API

**Semrush ruled out.** The Semrush MCP server exists at `https://mcp.semrush.com/v2/mcp` and would be
the cleanest option, but Standard API access requires a qualifying plan plus API units. Archie is not
on one (confirmed July 19, 2026) and upgrading is not justified for this alone.

### Status July 19, 2026

| Piece | State |
|---|---|
| Google Ads MCC account | Exists, **on a different Google account than the Cloud project** |
| Developer token | Obtained, currently **Explorer** access |
| Basic access | **Not yet applied for. This is the blocker.** |
| Google Ads API on Cloud project | Not yet enabled |
| Service account granted in Google Ads | Not yet done |

### The different email does not matter

Verified against Google's documentation. The three components are independent acquisitions:

- The **Cloud project** hosts credentials and enables the API.
- The **developer token** comes from the Ads manager account's API Center and is just a string.
- The **Ads account** is the target of calls, identified by customer ID.

Nothing requires them to share an owner. What links them is granting the service account access
inside the Google Ads UI, which works across accounts.

### The actual blocker

**Explorer access cannot call `KeywordPlanIdeaService`.** Google lists planning tools among the
features Explorer restricts, alongside account creation, user management and billing. Basic access
is required and is reviewed in roughly five business days.

Explorer also caps production calls at 2,880 operations per day. Basic raises that to 15,000, which
is far beyond what this needs.

### Steps

1. **Apply for Basic access.** Sign into the MCC, `ads.google.com/aw/apicenter`, confirm the API
   Contact Email, then choose Apply for Basic Access from the access level dropdown. Brand
   verification of the Cloud project may expedite review.
2. **Enable the Google Ads API** on the Cloud project. This is separate from the Search Console and
   Analytics APIs already enabled:
   `https://console.cloud.google.com/apis/library/googleads.googleapis.com?project=brightbox-digita-1743176991871`
3. **Grant the service account access in Google Ads.** Signed in as MCC admin: Admin, Access and
   security, Users, +, then add
   `content-os-reader@brightbox-digita-1743176991871.iam.gserviceaccount.com`.
   Read-only is sufficient. Google does not permit granting admin to a service account by default
   and this workload does not need it. One service account email can be associated with up to 20
   Google Ads accounts.
4. **Store the developer token as a secret.** `~/.config/brightbox/google-ads.json`, mode 600:

   ```json
   {"developer_token": "...", "login_customer_id": "1234567890"}
   ```

   `login_customer_id` is the MCC's 10-digit customer ID without hyphens. It is **required** when
   access to a client account runs through a manager account, which is the case here.

**The developer token is a secret. It never goes in this repository and never into chat.**

### Not a blocker for content work

The system is designed to work without volume data. NeuronWriter supplies competitor and term
analysis where it matters, and topic scoring never uses invented numbers. Discovery ran successfully
on July 19, 2026 with no keyword tool at all.

## 7. Verify NeuronWriter from a cloud Routine

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
