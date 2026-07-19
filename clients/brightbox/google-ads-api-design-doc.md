# Google Ads API: Design Documentation

**Draft for Archie's review. Do not submit until the TODO items are resolved.**

Structured to match Google's "Sample Design Documentation" template: Company Name, Business Model,
Tool Access/Use, Tool Design, API Services Called, Tool Mockups.

Two notes on why this is written the way it is:

- **Brightbox manages ads for clients, unlike the sample company.** The sample, Will's Widgets, only
  advertises for websites it owns. Brightbox is an agency. That difference is stated plainly below
  rather than glossed, because misrepresenting the business model is the fastest way to get rejected
  and the slowest way to find out.
- **The narrowness is the strongest argument.** This tool reads keyword ideas and nothing else. It
  cannot create, modify or pause anything. Saying so explicitly removes the reviewer's main concern.

---

## Company Name

Brightbox Digital

---

## Business Model

Brightbox Digital is a one person web design and digital marketing business based in Fort Wayne,
Indiana, owned and operated by Archie Brady. We serve local small businesses, contractors, home
service companies and professional service providers, primarily in Northeast Indiana.

Our services include website design and development, search engine optimization, local SEO, Google
Business Profile optimization, and Google Ads and Facebook advertising management.

**We manage Google Ads accounts both for our own business and on behalf of client businesses,**
through a Google Ads manager account. Client accounts are linked to that manager account with the
client's authorization.

Our website is https://brightboxdigital.io/

> **TODO for Archie:** confirm this describes the business accurately, and confirm that client
> accounts are linked under the MCC. If you do not currently manage any client accounts through the
> MCC, say so instead, because a simpler answer is a better one.

---

## Tool Access/Use

The tool is an **internal command line script used by one person, Archie Brady, the sole owner and
operator of Brightbox Digital.**

- It is **not externally accessible.** There is no web interface, no login, no hosted service and no
  public endpoint.
- It runs locally on Archie's computer and is executed manually from a terminal.
- **No other person has access to it.** No employees, no clients, no third parties.
- Output is never shared with clients or published. It is read on screen and written to a private
  file on the same machine.
- It does not resell, redistribute or expose Google Ads data to anyone.

**Purpose:** keyword research to inform which articles Brightbox publishes on its own website blog.

Brightbox runs an editorial process for planning blog content. Before committing to an article
topic, we want to know whether people actually search for the terms involved, and roughly how often.
This tool retrieves keyword ideas and their historical search volume so that topic selection is
based on real demand data rather than guesswork.

**This is a content planning tool, not an ad management tool.** It does not create campaigns, modify
bids, change budgets, pause ads, or alter any account in any way.

---

## Tool Design

A Python script executed manually from the command line. It performs a single operation.

**Flow:**

1. Archie runs the script with a seed keyword, for example
   `./scripts/keyword-volume "google ads small budget"`.
2. The script authenticates to the Google Ads API using a **Google Cloud service account**, with the
   service account granted read access to the Google Ads manager account. No user OAuth flow and no
   stored user password.
3. It calls `KeywordPlanIdeaService.GenerateKeywordIdeas` once, passing the seed keyword, language
   and geographic targeting.
4. It reads the returned keyword ideas and their historical metrics, specifically average monthly
   searches and competition level.
5. It prints the results to the terminal and appends them to a local CSV file inside a **private
   git repository** that only Archie can access.
6. The script exits. It maintains no database, no server, no scheduled job and no persistent process.

**Frequency of use:** roughly two to four times per month, matching our publishing cadence of two
articles per month. Each run makes a small number of API calls. Expected usage is far below the
Basic access limit of 15,000 operations per day.

**Data handling:** returned keyword data is stored only in a local CSV file on Archie's machine in a
private repository. It is not published, shared, resold or exposed through any interface. No
credentials are stored in the repository; the service account key is held outside it with restricted
file permissions.

**Write operations: none.** The script has no code path that creates, updates or deletes anything in
any Google Ads account. It is read only by design, not by convention.

---

## API Services Called

- **`KeywordPlanIdeaService.GenerateKeywordIdeas`** — retrieve keyword ideas and historical search
  volume metrics for a seed keyword, to evaluate whether a proposed blog topic has real search
  demand.

That is the complete list. No other service is called.

If historical trend detail is later required, we would additionally call
**`KeywordPlanIdeaService.GenerateKeywordHistoricalMetrics`**, which is also read only. No mutate
service of any kind is used.

---

## Tool Mockups

The tool is a command line script and is **not externally accessible**, so there is no user
interface to screenshot. Google's template notes that screenshots or mock-ups are required *if the
tool is externally accessible*. This one is not.

For clarity, here is representative terminal output showing exactly what the tool does:

```
$ ./scripts/keyword-volume "google ads small budget" --location "Fort Wayne, Indiana"

Seed keyword: google ads small budget
Location:     Fort Wayne, Indiana    Language: English
Service:      KeywordPlanIdeaService.GenerateKeywordIdeas

KEYWORD IDEA                              AVG MONTHLY SEARCHES   COMPETITION
--------------------------------------------------------------------------
google ads small budget                                    xxx           LOW
small business google ads cost                             xxx        MEDIUM
how much to spend on google ads                            xxx           LOW
google ads budget wasted                                   xxx           LOW

4 keyword ideas returned. 1 API operation used.
Appended to clients/brightbox/research/keyword-volume.csv
No write operations performed.
```

The tool produces terminal text and a local CSV file. There is no dashboard, no report distribution
and no interface any other person can reach.

---

## Checklist before submitting

- [ ] Confirm the business model paragraph is accurate, especially whether client accounts are
      linked under the MCC
- [ ] Confirm the tool description matches what you actually want built. If you also want this to
      pull performance data from client accounts later, **say so now.** Applying for a narrow use
      case and then broadening it is worse than describing the full scope up front
- [ ] Confirm the manager account email used to apply is the one that holds the developer token
- [ ] Confirm API Contact Email in the API Center is current, since that is where Google replies

## Notes

Google reviews Basic access applications in roughly five business days. Completing **brand
verification** of the Google Cloud project may expedite it.

Cloud project: `brightbox-digita-1743176991871`, project number `824815042391`.

The strongest thing about this application is that the use case is genuinely small and genuinely
read only. Do not embellish it to sound more substantial. A narrow, accurate description of a
read-only tool is the easiest kind of application for a reviewer to approve.
