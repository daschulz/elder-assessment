"""Build the Eldership Candidate Assessment (test format) as branded Sun City HTML."""
import os
import sys

# Paths were left pointing at ~/Desktop/Sun City AI Team, which stopped existing when the
# AI OS moved off iCloud-synced Desktop on 2026-09-07. Repaired 2026-09-25.
ROOT = os.environ.get("AIOS_ROOT", "/Users/dannyschulz/AI OS")
LIBRARY = os.path.join(ROOT, "Team Library")
sys.path.insert(0, os.path.join(LIBRARY, "Team", "Brand Assets"))
from sun_city_html import page, lockup_b64, ORANGE, CHARCOAL, LGRAY

FILLABLE = "--fillable" in sys.argv
REPO = os.path.dirname(os.path.abspath(__file__))
INBOX = os.path.join(LIBRARY, "Owner's Inbox", "Eldership")

# The fillable build IS the published page: it is what GitHub Pages serves at
# https://daschulz.github.io/elder-assessment/ , so it is written straight into the repo.
OUT = (os.path.join(REPO, "index.html")
       if FILLABLE else
       os.path.join(INBOX, "Eldership Candidate Assessment.html"))

# ---------- extra CSS for test formatting ----------
EXTRA_CSS = f"""
<style>
.qblock{{margin:0 0 26px;page-break-inside:avoid;}}
.qnum{{color:{ORANGE};font-weight:700;font-size:14px;letter-spacing:.04em;}}
.qtext{{font-weight:500;font-size:15.5px;margin:2px 0 10px;}}
.lines{{height:var(--h,130px);background:repeating-linear-gradient(
  to bottom,transparent,transparent 25px,{LGRAY} 25px,{LGRAY} 26px);
  margin-top:6px;}}
.shortline{{border-bottom:1px solid {CHARCOAL};display:inline-block;
  min-width:280px;height:20px;}}
.mc{{list-style:none;padding-left:6px;margin:8px 0 0;}}
.mc li{{position:relative;padding-left:58px;margin:9px 0;font-size:14.5px;
  page-break-inside:avoid;}}
.mc li .opt{{position:absolute;left:0;top:0;color:{ORANGE};font-weight:700;}}
.mc li::before{{content:"\\2610";position:absolute;left:28px;top:-1px;
  color:{CHARCOAL};font-size:16px;}}
table.triage{{width:100%;border-collapse:collapse;margin:14px 0;font-size:13.5px;}}
table.triage th{{background:{ORANGE};color:#fff;font-weight:500;text-align:center;
  padding:8px 6px;font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;}}
table.triage th:first-child{{text-align:left;padding-left:10px;}}
table.triage td{{border:1px solid {LGRAY};padding:8px 10px;}}
table.triage td.c{{text-align:center;font-size:18px;color:{CHARCOAL};width:88px;}}
table.info{{width:100%;border-collapse:collapse;margin:14px 0;font-size:14px;}}
table.info td{{border-bottom:1px solid {LGRAY};padding:14px 8px 6px 0;}}
table.info td .fl{{color:{LGRAY};font-size:10.5px;letter-spacing:.08em;
  text-transform:uppercase;display:block;margin-bottom:14px;}}
.secdesc{{font-style:italic;color:#55555a;font-size:14px;margin:8px 0 18px;}}
.instr{{border:1px solid {LGRAY};border-radius:4px;padding:18px 22px;margin:20px 0;}}
.instr h3{{margin:0 0 10px;font-size:13px;letter-spacing:.1em;text-transform:uppercase;
  color:{ORANGE};}}
.instr ul{{margin:0;padding-left:18px;}}
.instr li{{margin:6px 0;font-size:14px;}}
table.rubric{{width:100%;border-collapse:collapse;margin:12px 0;font-size:12.5px;}}
table.rubric th{{background:{CHARCOAL};color:#fff;font-weight:500;text-align:left;
  padding:7px 9px;font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;}}
table.rubric td{{border:1px solid {LGRAY};padding:7px 9px;vertical-align:top;}}
table.rubric td.score{{text-align:center;width:150px;letter-spacing:.35em;
  font-size:14px;white-space:nowrap;}}
.detach{{border-top:2px dashed {LGRAY};margin-top:40px;padding-top:8px;
  color:{LGRAY};font-size:11px;letter-spacing:.1em;text-transform:uppercase;
  text-align:center;}}
@media print{{ .qblock{{page-break-inside:avoid;}} .evalpage{{page-break-before:always;}}
  .cover{{height:auto !important;min-height:82vh !important;page-break-after:always;}} }}
</style>
"""

FILL_CSS = f"""
<style>
.ans{{background:#fbfaf9;border:1px solid {LGRAY};border-radius:4px;
  min-height:var(--h,130px);height:auto;padding:10px 12px;font-size:14.5px;
  line-height:1.55;outline:none;}}
.ans:focus{{border-color:{ORANGE};box-shadow:0 0 0 2px rgba(242,88,50,.15);}}
.ans:empty::before{{content:"Type your answer here\\2026";color:{LGRAY};}}
.fill{{display:block;min-height:24px;font-size:15px;outline:none;padding:2px 4px;}}
.fill:focus{{background:#fff7f4;}}
.fill:empty::before{{content:"\\00a0";}}
input[type=radio],input[type=checkbox]{{accent-color:{ORANGE};width:17px;height:17px;
  vertical-align:-3px;margin-right:4px;cursor:pointer;}}
.mc li{{padding-left:58px;}}
.mc li input{{position:absolute;left:24px;top:1px;}}
.toolbar{{position:fixed;bottom:0;left:0;width:100%;background:{CHARCOAL};
  color:#fff;padding:12px 24px;display:flex;align-items:center;gap:18px;
  font-size:13px;z-index:50;}}
.toolbar .spacer{{flex:1;}}
.toolbar button{{font-family:'Gotham',Arial,sans-serif;font-weight:700;font-size:13px;
  letter-spacing:.06em;text-transform:uppercase;background:{ORANGE};color:#fff;
  border:none;border-radius:4px;padding:11px 22px;cursor:pointer;}}
.toolbar button:hover{{filter:brightness(1.08);}}
.toolbar button.ghost{{background:transparent;border:1.5px solid rgba(255,255,255,.55);}}
.toolbar button.ghost:hover{{background:rgba(255,255,255,.12);filter:none;}}
.toolbar a{{color:#fff;}}
@media(max-width:640px){{.toolbar{{gap:10px;padding:10px 12px;flex-wrap:wrap;}}
  .toolbar button{{padding:10px 14px;font-size:12px;}}
  .toolbar .spacer{{display:none;}}
  #savestate{{flex-basis:100%;font-size:12px;}}}}
body{{padding-bottom:70px;}}
@media print{{
  .toolbar{{display:none !important;}}
  body{{padding-bottom:0;}}
  .ans{{background:#fff;border-color:{CHARCOAL};}}
  .ans:empty::before{{content:"";}}
}}
</style>
"""

qn = 0
def q(text, lines_px=130):
    global qn; qn += 1
    if FILLABLE:
        box = f"<div class='ans' contenteditable='true' data-k='q{qn}' style='--h:{lines_px}px'></div>"
    else:
        box = f"<div class='lines' style='--h:{lines_px}px'></div>"
    return (f"<div class='qblock'><span class='qnum'>QUESTION {qn:02d}</span>"
            f"<p class='qtext'>{text}</p>{box}</div>")

def q_mc(text, options):
    global qn; qn += 1
    letters = "ABCDEFG"
    if FILLABLE:
        lis = "".join(
            f"<li><span class='opt'>{letters[i]}.</span>"
            f"<input type='radio' name='q{qn}' value='{letters[i]}' data-k='q{qn}'><label>{o}</label></li>"
            for i, o in enumerate(options))
        return (f"<div class='qblock'><span class='qnum'>QUESTION {qn:02d}</span>"
                f"<p class='qtext'>{text}</p><ul class='mc' style='list-style:none'>{lis}</ul></div>")
    lis = "".join(f"<li><span class='opt'>{letters[i]}.</span>{o}</li>" for i, o in enumerate(options))
    return (f"<div class='qblock'><span class='qnum'>QUESTION {qn:02d}</span>"
            f"<p class='qtext'>{text}</p><ul class='mc'>{lis}</ul></div>")

def q_checks(text, options):
    global qn; qn += 1
    if FILLABLE:
        def li(i, o):
            return f"<li style='padding-left:0;list-style:none'><label><input type='checkbox' data-k='q{qn}_{i}'> {o}</label></li>"
        half = (len(options) + 1) // 2
        col1 = "".join(li(i, o) for i, o in enumerate(options[:half]))
        col2 = "".join(li(i + half, o) for i, o in enumerate(options[half:]))
        return (f"<div class='qblock'><span class='qnum'>QUESTION {qn:02d}</span>"
                f"<p class='qtext'>{text}</p>"
                f"<div style='display:flex;gap:30px'>"
                f"<ul style='flex:1;padding:0;margin:8px 0'>{col1}</ul>"
                f"<ul style='flex:1;padding:0;margin:8px 0'>{col2}</ul></div></div>")
    half = (len(options) + 1) // 2
    col1 = "".join(f"<li>{o}</li>" for o in options[:half])
    col2 = "".join(f"<li>{o}</li>" for o in options[half:])
    return (f"<div class='qblock'><span class='qnum'>QUESTION {qn:02d}</span>"
            f"<p class='qtext'>{text}</p>"
            f"<div style='display:flex;gap:30px'>"
            f"<ul class='checks' style='flex:1'>{col1}</ul>"
            f"<ul class='checks' style='flex:1'>{col2}</ul></div></div>")

def fill(key):
    """A typeable single-line field (fillable mode) or blank space (print mode)."""
    return f"<div class='fill' contenteditable='true' data-k='{key}'></div>" if FILLABLE else ""

def sec(num, title, desc=None):
    d = f"<p class='secdesc'>{desc}</p>" if desc else ""
    return f"<h1 class='section'><span class='num'>PART {num}</span> — {title}</h1>{d}"

# ---------- cover ----------
body = f"""
<div class='cover'>
  <p class='eyebrow'>Sun City Church &bull; Eldership</p>
  <p class='t2'>Eldership Candidate</p>
  <p class='t3'>Assessment</p>
  <div class='rule'></div>
  <p class='tag'>A written examination for candidates to the eldership of Sun City Church</p>
  <table class='info' style='max-width:420px;margin:36px auto 0;text-align:left;'>
    <tr><td><span class='fl'>Candidate Name</span>{fill('cover_name')}</td></tr>
    <tr><td><span class='fl'>Date Issued</span>{fill('cover_issued')}</td></tr>
    <tr><td><span class='fl'>Date Due</span>{fill('cover_due')}</td></tr>
  </table>
  <img class='lockup' src='data:image/png;base64,{lockup_b64()}'>
</div>

<div class='instr'>
<h3>Instructions to the Candidate</h3>
<ul>
<li>This assessment has <b>eight parts</b>. Answer every question. If a question does not apply to you, write <b>N/A</b>.</li>
<li>There is no time limit. Take the time to answer thoughtfully and in your own words — depth matters more than length.</li>
<li>Part III (Bible &amp; Doctrine) is not pass/fail. Even among our elders there are healthy shades of divergence. We are looking for <b>how you think</b>, not merely what you conclude. If your view on a matter is not fully formed, say so and explain your leanings.</li>
{'<li>Type your answers directly into this page. <b>Your progress saves automatically</b> in this browser — you can close it and come back anytime on the same device.</li><li>When finished, complete the affirmation on the final page, then click <b>Submit Assessment</b> in the bar at the bottom. Your answers are sent to Sun City Church, a copy downloads to your computer, and you&rsquo;ll be prompted to save a PDF as well. <b>Please email the downloaded copy to danny@suncitychurch.com too</b>, so there is no chance your work is lost in transit. You can download a copy at any time with the <b>Download my answers</b> button, finished or not.</li>' if FILLABLE else '<li>Written answers may be completed on these pages or typed and attached, numbered to match.</li><li>Sign the affirmation on the final page before returning the assessment.</li>'}
<li>Your answers will be reviewed by the Lead Pastor and current elders and will form the basis of your candidacy interview.</li>
</ul>
</div>
"""

# ---------- Part I: Candidate Information ----------
body += sec("I", "Candidate Information")
body += f"""
<table class='info'>
<tr><td colspan='2'><span class='fl'>Full Name</span>{fill('info_name')}</td></tr>
<tr><td><span class='fl'>Phone Number</span>{fill('info_phone')}</td><td><span class='fl'>Email Address</span>{fill('info_email')}</td></tr>
<tr><td colspan='2'><span class='fl'>Home Address</span>{fill('info_address')}</td></tr>
<tr><td><span class='fl'>Date of Birth</span>{fill('info_dob')}</td><td><span class='fl'>Name of Spouse (if applicable)</span>{fill('info_spouse')}</td></tr>
<tr><td><span class='fl'>Spouse's Birthday</span>{fill('info_spouse_bday')}</td><td><span class='fl'>Wedding Anniversary</span>{fill('info_anniv')}</td></tr>
<tr><td colspan='2'><span class='fl'>Children's Names &amp; Ages</span>{fill('info_children')}</td></tr>
</table>
"""

# ---------- Part II: Personal ----------
body += sec("II", "Personal")
body += q("Briefly describe your personal spiritual journey (salvation, water baptism, Holy Spirit baptism, etc.).", 156)
body += q("What are your motivations for ministry and for becoming an Elder?", 130)
body += q("Read the qualifications of 1 Timothy 3:1&ndash;7, Titus 1:5&ndash;9, Acts 20:28&ndash;35 and 1 Peter 5:1&ndash;4. Summarize how you feel your life compares to these qualifications.", 156)
body += q("We believe stewardship should be modeled by those in leadership. What is your view on tithes and offerings, and do you tithe consistently? Do you give regularly beyond the tithe to other important church opportunities?", 130)
body += q("What major successes have you experienced, and how do these benefit you as a ministry leader?", 130)
body += q("What setbacks or failures have you experienced, and how will these work for your good as an Elder?", 130)
body += q("Describe any past involvement in other churches, including their affiliation with denominations or movements, your level of involvement, and your reason for leaving. Are you in good standing with previous pastors and leaders? Are there any unresolved issues?", 156)
body += q("Do you have any criminal record or child molestation charges? If so, explain.", 104)
body += q("Have you submitted a background check with Sun City Church? If not, would you be willing to fill one out immediately?", 78)
body += q("Can you make a commitment of a minimum of 3&ndash;5 years as an Elder?", 78)

# ---------- Part III: Bible & Doctrine ----------
body += sec("III", "Bible &amp; Doctrine",
    "Please do not view this section as pass/fail. Even among the elders, where there is general agreement on these subjects, there would still be shades of divergence &mdash; and that is healthy. These questions help us get to know a candidate&rsquo;s perspective. Some questions ask about concepts articulated in our Statement of Faith; we are not only looking for whether you agree, but how you would explain it in your own words. If you need more detail before you can answer, say so or reach out for clarification. It&rsquo;s alright if your opinions are not fully formed on a matter; simply state this and explain your leanings.")
body += q("Do you fully agree with all of the official doctrinal statements of Sun City Church as defined in our Statement of Faith? If there are any points of uncertainty, please mention them and explain your beliefs or assumptions on those points.", 130)
body += q("What is your view of Scripture? What is it? What is its origin? How do we relate to it? Please speak to the subject of authority, infallibility, and its place in forming church policy.", 156)
body += q("In your opinion, what are some of the most important principles for interpreting Scripture accurately?", 130)
body += q("How would you articulate the gospel to an unbeliever? What are the primary components of the gospel?", 130)
body += q("While the church may have many roles and ministries, what would you say is its primary purpose according to Scripture? How should that purpose affect things like service planning, administration, staffing, and the church&rsquo;s relationship to society?", 156)
body += q("What is your view on church discipline (i.e., addressing sin in a church member)? Should it ever lead to a member being removed from church fellowship? If so, under what circumstances? What Scripture premise validates your stance?", 156)
body += q("What is your current view on racism? What role should the church play (if any) in addressing this issue?", 130)
body += q("Is a homosexual relationship sinful if it is loving, consensual, and monogamous (in legal marriage)? Explain.", 130)
body += q("Do you think Christians can always find complete freedom from same-sex attraction (SSA) if they struggle with it? If yes, explain. If no, how would you advise them in their journey of sanctification in this area?", 130)
body += q("Do you think Christians are free to discover or decide their own gender identity regardless of their biological sex?", 104)
body += q("How would you explain Scripture&rsquo;s teaching on hell as you understand it? Speak to the following: What is it? Who goes there? For how long? Who sends them?", 130)

# --- theological triage grid ---
qn += 1
triage_topics = [
    "The deity of Jesus",
    "The bodily resurrection of Jesus",
    "The infallibility of Scripture",
    "Water baptism",
    "Tithing",
    "Sign gifts (speaking in tongues, prophecy, etc.)",
    "Women in ministry leadership",
    "The model of church government",
    "The place of Israel in God's program",
    "Social consumption of alcohol (not drunkenness)",
]
if FILLABLE:
    rows = "".join(
        f"<tr><td>{t}</td>"
        + "".join(f"<td class='c'><input type='radio' name='triage{i}' value='{v}' data-k='triage{i}'></td>"
                  for v in ("die", "divide", "discuss"))
        + "</tr>"
        for i, t in enumerate(triage_topics))
else:
    rows = "".join(f"<tr><td>{t}</td><td class='c'>&#9744;</td><td class='c'>&#9744;</td><td class='c'>&#9744;</td></tr>" for t in triage_topics)
body += f"""
<div class='qblock'><span class='qnum'>QUESTION {qn:02d}</span>
<p class='qtext'>For each doctrine or practice below, mark the level of importance you would assign it:</p>
<ul class='lead' style='font-size:13.5px;'>
<li><b>Die for it</b> &mdash; all Christians must agree on this</li>
<li><b>Divide over it</b> &mdash; we must agree in order to go to church together, especially in leadership</li>
<li><b>Discuss it</b> &mdash; we can agree to disagree and continue debate and discussion in fellowship</li>
</ul>
<table class='triage'>
<tr><th>Doctrine / Practice</th><th>Die for it</th><th>Divide over it</th><th>Discuss it</th></tr>
{rows}
</table></div>
"""

body += "<p class='eyebrow'>Views on Debated Doctrines</p><p class='secdesc'>There are some doctrines on which Christians tend to have a greater diversity of views. Usually they &ldquo;agree to disagree&rdquo; on these matters, but a general awareness of your leanings is helpful. Select the option that best represents your view.</p>"

body += q_mc("What best represents your view on <b>election</b>?", [
    "God predestined us to be saved and our decision to accept him was therefore inevitable.",
    "God predestined us to be saved based on his foreknowledge of our decision or faith.",
    "God predestined Christ and his church as a corporate reality, not specific individuals.",
    "I am not sure; or I do not have a strong opinion."])
body += q_mc("What best represents your view on <b>Holy Spirit baptism</b>?", [
    "The baptism in the Holy Spirit is what all believers experience at the moment of salvation and there is not necessarily an immediate outward evidence.",
    "The baptism in the Holy Spirit is distinct from salvation and is accompanied by some form of outward evidence &mdash; often/usually speaking in tongues.",
    "The baptism in the Holy Spirit is distinct from salvation and is always accompanied by the outward evidence of speaking in tongues.",
    "I am not sure; or I do not have a strong opinion."])
body += q_mc("What best represents your view on <b>women in eldership</b>?", [
    "The Bible teaches that only men should be elders in the local church.",
    "The Bible does not limit women from being elders in the local church.",
    "A woman can be an elder, but only alongside her husband.",
    "I am not sure; or I do not have a strong opinion."])
body += q_mc("What best represents your view on <b>end times</b>?", [
    "The Biblical promises to restore Israel will occur at the end of history in a straightforward way that pertains to national/ethnic Israel.",
    "The Biblical promises to restore Israel find fulfillment in Christ and his church.",
    "The Biblical promises to restore Israel find ultimate fulfillment in Christ and his church, yet some promises may find a unique fulfillment in national or ethnic Israel.",
    "I am not sure; or I do not have a strong opinion."])

# ---------- Part IV: Family ----------
body += sec("IV", "Family")
body += q("If married, describe the strengths and weaknesses of your marriage. If not married, write N/A.", 130)
body += q("Describe the current state of your marriage.", 104)
body += q("Have either you or your spouse been married previously? If so, briefly describe the circumstances.", 104)
body += q("How is your relationship with your children? Are there any concerns we should know about?", 104)
body += q("Are there any financial circumstances that would hinder your ability to lead?", 104)

# ---------- Part V: Vocation ----------
body += sec("V", "Vocation")
body += q("What is your vocation, and how do those skills help you in serving as an Elder?", 130)
body += q("Do you see any conflict of interest between what you do for work and your potential role as an Elder?", 104)
body += q("How are you able to balance the pressure between family, work, and ministry?", 130)
body += q("How would your boss, co-workers, or customers (if applicable) define your character in the workplace?", 104)

# ---------- Part VI: People Skills ----------
body += sec("VI", "People Skills")
body += q("How often do you extend hospitality to others, and in what manner (in or out of the church)?", 130)
body += q("How would you deal with someone who needed adjustment or correction?", 130)

# ---------- Part VII: Spiritual Gifts / Church / Ministry ----------
body += sec("VII", "Spiritual Gifts, Church &amp; Ministry")
body += q("What are your spiritual gifts?", 104)
body += q("In what settings do you use your spiritual gifts?", 104)
body += q("Summarize your church attendance habits.", 78)
body += q("What ministries are you currently involved in? In what way?", 104)
body += q("Do you have a burden to be involved in full-time ministry, plant a church, or be sent to the mission field? If so, explain.", 104)
body += q("Describe previous ministry experiences (staff or Dream Team).", 130)
body += q("In what leadership roles have you had experience?", 104)
body += q("What do you believe about the concept of church membership?", 104)
body += q("Do you understand and support Sun City Church&rsquo;s form of church government? Please explain briefly.", 104)

# ---------- Part VIII: Counseling ----------
body += sec("VIII", "Counseling")
body += q("Describe any previous counseling training, education, or experience.", 104)
body += q_checks("Which of the following areas would you feel comfortable counseling? (Check all that apply.)", [
    "Marriage", "Sexual issues (abuse, adultery, pornography)", "Child raising",
    "Addictions / substance abuse", "Teen problems", "Business issues",
    "Relational offenses", "Finances", "Legal issues", "Personal life direction"])
body += q("What guidelines do you think are appropriate for counseling members of the opposite sex?", 104)

for topic in ["bankruptcy", "abortion", "suicide", "suing another Christian"]:
    body += q(f"How might you counsel someone who is considering {topic}?", 104)
body += q("How might you counsel someone who is having pre-marital sex?", 104)
body += q("How might you counsel someone who is considering divorce?", 104)
body += q("How might you counsel someone who is considering remarriage?", 104)
body += q("Do you have any questions or concerns in regard to becoming an active Elder?", 104)

# ---------- affirmation & signature ----------
sig_label = "Candidate Signature (type your full legal name)" if FILLABLE else "Candidate Signature"
body += f"""
<h1 class='section'>Candidate Affirmation</h1>
<p>I affirm that the answers given in this assessment are true and complete to the best of
my knowledge. I understand that this assessment will be reviewed by the Lead Pastor and
current elders of Sun City Church as part of my candidacy, and I welcome their questions
and follow-up on anything I have written.</p>
<table class='info' style='max-width:520px;'>
<tr><td><span class='fl'>{sig_label}</span>{fill('sig_name')}</td><td style='width:180px;'><span class='fl'>Date</span>{fill('sig_date')}</td></tr>
</table>
"""

# ---------- evaluator page ----------
rubric_rows = "".join(
    f"<tr><td><b>{part}</b> — {focus}</td><td class='score'>1&nbsp;&nbsp;2&nbsp;&nbsp;3&nbsp;&nbsp;4&nbsp;&nbsp;5</td></tr>"
    for part, focus in [
        ("Part II · Personal", "Testimony, motives, 1 Tim 3 / Titus 1 self-awareness, stewardship, church history clean"),
        ("Part III · Doctrine", "Alignment with Statement of Faith; clarity of gospel; sound handling of Scripture"),
        ("Part III · Triage grid", "Weights essentials as essentials; charitable on debatables"),
        ("Part IV · Family", "Household in order; marriage healthy; finances stable"),
        ("Part V · Vocation", "No conflicts of interest; healthy work/family/ministry balance; reputation with outsiders"),
        ("Part VI · People Skills", "Hospitable; corrects others with grace and courage"),
        ("Part VII · Ministry", "Gifts identified and in use; supports membership and church government"),
        ("Part VIII · Counseling", "Biblically grounded, wise, knows limits and when to refer"),
    ])
EVAL_PAGE = f"""
<div class='evalpage'>
<div class='detach'>For the review team only &mdash; detach before giving the assessment to the candidate</div>
<h1 class='section' style='page-break-before:avoid;'>Evaluator&rsquo;s Scoring Guide</h1>
<p class='secdesc'>Score each area 1&ndash;5 (1 = significant concern &middot; 3 = adequate, follow up in interview &middot; 5 = exemplary). Written answers are weighed on biblical grounding, self-awareness, and humility of tone &mdash; not eloquence.</p>
<table class='rubric'>
<tr><th>Area</th><th>Score</th></tr>
{rubric_rows}
</table>
<p class='label'>Automatic follow-up flags</p>
<ul class='checks'>
<li>Disagreement or hesitation on the Statement of Faith (Q11)</li>
<li>Unresolved issues with a previous church or pastor (Q7)</li>
<li>Criminal record disclosure or unwillingness to complete a background check (Q8&ndash;9)</li>
<li>Unable to commit 3&ndash;5 years (Q10)</li>
<li>Marriage or family concerns (Part IV)</li>
<li>&ldquo;Die for it&rdquo; marked on clearly debatable matters, or essentials marked &ldquo;Discuss it&rdquo; (Q22)</li>
</ul>
<p class='label'>Recommendation</p>
<ul class='checks'>
<li><b>Advance</b> — proceed to candidacy interview</li>
<li><b>Advance with questions</b> — interview must address flagged items</li>
<li><b>Delay</b> — revisit in ______ months</li>
<li><b>Decline</b> — with pastoral follow-up</li>
</ul>
<table class='info' style='max-width:520px;'>
<tr><td><span class='fl'>Reviewed By</span></td><td style='width:180px;'><span class='fl'>Date</span></td></tr>
</table>
</div>
"""

FOOT = "<div class='foot'><b>Sun City Church</b> &nbsp;&middot;&nbsp; Eldership Candidate Assessment &nbsp;&middot;&nbsp; Confidential</div>"

if not FILLABLE:
    body += EVAL_PAGE
body += FOOT

FILL_JS = """
<div class='toolbar'>
  <span id='savestate'>&#10003; Progress saves automatically in this browser</span>
  <span class='spacer'></span>
  <button class='ghost' onclick='downloadAnswers()'>Download my answers</button>
  <button onclick='finishAssessment()'>Submit Assessment</button>
</div>
<script>
const KEY='suncity-elder-assessment';
function collect(){
  const d={};
  document.querySelectorAll('[contenteditable][data-k]').forEach(el=>{d[el.dataset.k]=el.innerHTML;});
  document.querySelectorAll('input[type=radio]').forEach(el=>{if(el.checked)d['r:'+el.name]=el.value;});
  document.querySelectorAll('input[type=checkbox][data-k]').forEach(el=>{d['c:'+el.dataset.k]=el.checked;});
  return d;
}
function restore(){
  let d; try{d=JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){d={};}
  document.querySelectorAll('[contenteditable][data-k]').forEach(el=>{
    if(d[el.dataset.k]!==undefined)el.innerHTML=d[el.dataset.k];});
  document.querySelectorAll('input[type=radio]').forEach(el=>{
    if(d['r:'+el.name]===el.value)el.checked=true;});
  document.querySelectorAll('input[type=checkbox][data-k]').forEach(el=>{
    if(d['c:'+el.dataset.k])el.checked=true;});
}
let t;
function save(){
  clearTimeout(t);
  t=setTimeout(()=>{
    localStorage.setItem(KEY,JSON.stringify(collect()));
    const s=document.getElementById('savestate');
    s.textContent='\\u2713 Saved '+new Date().toLocaleTimeString();
  },400);
}
document.addEventListener('input',save);
document.addEventListener('change',save);
// ---- Google Form submission bridge ----
const FORM_ACTION='https://docs.google.com/forms/d/e/1FAIpQLSe0M__wM5Xu-xnq1bw_CXRFpt1zP4X5WX3-xLJjsOfNvymYVw/formResponse';
const TEXT_MAP={info_name:375159091,info_phone:1657113946,info_address:210702194,
info_email:883268367,info_spouse:1200257753,info_children:1547925286,
q1:2006808268,q2:1661290097,q3:734884496,q4:436550171,q5:123480212,q6:1777255882,
q7:1464713940,q8:1823776532,q9:1239172496,q10:1279237220,q11:537402127,q12:613320180,
q13:2057259273,q14:1657644089,q15:357982325,q16:1937524205,q17:1612866431,
q18:1296970216,q19:423914883,q20:988580778,q21:2018265459,q27:1212275925,
q28:1666133068,q29:1298695742,q30:1816154962,q31:1004549281,q32:2096341018,
q33:1869401306,q34:1501450890,q35:2042235635,q36:919663293,q37:1454613827,
q38:1421683929,q39:291641587,q40:1968599967,q41:1314032524,q42:1143915222,
q43:1237247020,q44:694785179,q45:557298937,q46:1457505193,q47:909415527,
q49:2076106728,q51:1780383950,q52:1356547141,q53:144499840,q54:685874624,
q55:1410681374,q56:1749234340,q57:808568836};
const BANKRUPTCY=[251111383,257577889]; // duplicate question in the form
const DATE_MAP={info_dob:1872147540,info_spouse_bday:1399645082,info_anniv:1558097236};
const TRIAGE_ENTRIES=[1618685955,1754658151,1992096791,1502551351,775578946,
1249690591,238573329,1924857347,518300512,1485678859];
const TRIAGE_VALUES={die:"I'd die for it (All Christians must agree on this)",
divide:"I'd divide over it (We must agree in order to go to church together, especially in leadership)",
discuss:"I'd discuss it (We can agree to disagree and continue debates and discussions in fellowship)"};
const MC_MAP={
q23:[238460750,["God predestined us to be saved and our decision to accept him was therefore inevitable.","God predestined us to be saved based on his foreknowledge of our decision or faith.","God predestined Christ and his church as a corporate reality, not specific individuals.","I am not sure; or I do not have a strong opinion."]],
q24:[1584999111,["The baptism in the Holy Spirit is what all believers experience at the moment of salvation and there is not necessarily an immediate outward evidence.","The baptism in the Holy Spirit is distinct from salvation and is accompanied by some form of outward evidence\\u2014often/usually speaking in tongues.","The baptism in the Holy Spirit is distinct from salvation and is always accompanied by the outward evidence of speaking in tongues.","I am not sure; or I do not have a strong opinion."]],
q25:[2460096,["The Bible teaches that only men should be elders in the local church.","The Bible does not limit women from being elders in the local church.","A woman can be an elder, but only alongside her husband.","I am not sure; or I do not have a strong opinion."]],
q26:[1475889401,["The Biblical promises to restore Israel will occur at the end of history in a straightforward way that pertains to national/ethnic Israel.","The Biblical promises to restore Israel find fulfilment in Christ and his church.","The Biblical promises to restore Israel find ultimate fulfillment in Christ and his church, yet some promises may find a unique fulfillment in national or ethnic Israel.","I am not sure; or I do not have a strong opinion."]]};
const CHECK_ENTRY=2122477547;
const CHECK_CHOICES=["Marriage","Sexual issues (abuse, adultery, pornography)","Child raising","Addictions / substance abuse","Teen problems","Business issues","Relational offenses","Finances","Legal issues","Personal life direction"];
function txt(k){const el=document.querySelector("[contenteditable][data-k='"+k+"']");return el?el.innerText.trim():'';}
function buildSubmission(){
  const p=new URLSearchParams();
  for(const[k,id]of Object.entries(TEXT_MAP)){const v=txt(k);if(v)p.append('entry.'+id,v);}
  const bank=txt('q50');if(bank)BANKRUPTCY.forEach(id=>p.append('entry.'+id,bank));
  const nm=txt('info_name')||txt('cover_name');if(nm&&!txt('info_name'))p.append('entry.375159091',nm);
  for(const[k,id]of Object.entries(DATE_MAP)){
    const v=txt(k);if(!v)continue;const d=new Date(v);
    if(!isNaN(d)){p.append('entry.'+id+'_year',d.getFullYear());
      p.append('entry.'+id+'_month',d.getMonth()+1);p.append('entry.'+id+'_day',d.getDate());}}
  TRIAGE_ENTRIES.forEach((id,i)=>{
    const c=document.querySelector("input[name='triage"+i+"']:checked");
    if(c)p.append('entry.'+id,TRIAGE_VALUES[c.value]);});
  for(const[k,[id,choices]]of Object.entries(MC_MAP)){
    const c=document.querySelector("input[name='"+k+"']:checked");
    if(c)p.append('entry.'+id,choices['ABCD'.indexOf(c.value)]);}
  document.querySelectorAll("input[type=checkbox][data-k]").forEach(el=>{
    if(!el.checked)return;const i=parseInt(el.dataset.k.split('_')[1],10);
    if(CHECK_CHOICES[i]!==undefined)p.append('entry.'+CHECK_ENTRY,CHECK_CHOICES[i]);});
  p.append('pageHistory','0,1,2,3,4,5,6,7');
  p.append('fvv','1');
  return p;
}
function candidateName(){
  const el=document.querySelector("[contenteditable][data-k='info_name']");
  const n=(el?el.textContent:'').trim().replace(/[\\/:*?"<>|]/g,'').slice(0,60);
  return n||'Candidate';
}
function downloadAnswers(){
  // A self-contained copy of this page with every answer in place. Works whether or
  // not the submission reached the church, and whether or not you are online.
  try{
    const clone=document.documentElement.cloneNode(true);
    clone.querySelectorAll('.toolbar,#gform-sink,script').forEach(el=>el.remove());
    clone.querySelectorAll('[contenteditable]').forEach(el=>el.removeAttribute('contenteditable'));
    const banner=clone.querySelector('body');
    if(banner){
      const note=document.createElement('div');
      note.style.cssText='padding:14px 18px;margin:0 0 12px;border:2px solid #8a7a56;background:#f4f2ed;font:14px Arial,sans-serif';
      note.innerHTML='<b>Saved copy of the Eldership Candidate Assessment.</b> Downloaded '
        +new Date().toLocaleString()+'. Email this file to danny@suncitychurch.com.';
      banner.insertBefore(note,banner.firstChild);
    }
    const blob=new Blob(['<!doctype html>'+clone.outerHTML],{type:'text/html'});
    const a=document.createElement('a');
    a.href=URL.createObjectURL(blob);
    a.download='Eldership Assessment - '+candidateName()+' - '
      +new Date().toISOString().slice(0,10)+'.html';
    document.body.appendChild(a);a.click();
    setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove();},2000);
    return true;
  }catch(e){
    alert('The copy could not be downloaded automatically. Please use your browser\\'s Print option and save as PDF, then email it to danny@suncitychurch.com.');
    return false;
  }
}
function submitToChurch(){
  return new Promise(resolve=>{
    let fr=document.getElementById('gform-sink');
    if(!fr){fr=document.createElement('iframe');fr.id='gform-sink';fr.name='gform-sink';
      fr.style.display='none';document.body.appendChild(fr);}
    const f=document.createElement('form');
    f.action=FORM_ACTION;f.method='POST';f.target='gform-sink';f.style.display='none';
    for(const[k,v]of buildSubmission().entries()){
      const inp=document.createElement('input');inp.type='hidden';inp.name=k;inp.value=v;
      f.appendChild(inp);}
    document.body.appendChild(f);
    const done=()=>{f.remove();resolve(true);};
    fr.addEventListener('load',done,{once:true});
    setTimeout(done,6000);
    f.submit();
  });
}
function countingChecks(){
  return [...document.querySelectorAll("input[type=checkbox][data-k]")].filter(el=>el.checked).length;
}
async function finishAssessment(){
  const empty=[...document.querySelectorAll('.ans')].filter(el=>!el.textContent.trim()).length;
  if(empty>0 && !confirm(empty+' written answer(s) are still blank. Submit anyway?'))return;
  // That counseling-areas question was marked required on the church's form, which silently
  // rejected the whole submission when it was blank. It was made optional on 2026-09-25, so
  // this is now only a nudge and never a wall.
  if(countingChecks()===0 &&
     !confirm('You have not ticked any areas in "Which of the following areas would you feel '
       +'comfortable counseling". Submit anyway?'))return;
  const btn=document.querySelector('.toolbar button:not(.ghost)');
  if(localStorage.getItem(KEY+'-submitted')==='1' &&
     !confirm('You already sent this assessment. Send it again?')){downloadAnswers();window.print();return;}
  btn.disabled=true;btn.textContent='Sending\\u2026';
  await submitToChurch();
  localStorage.setItem(KEY+'-submitted','1');
  btn.disabled=false;btn.textContent='Send again';
  // The church form is on another domain, so the browser is not allowed to tell us
  // whether it accepted the answers. Never claim a delivery we cannot verify: leave
  // the candidate holding a copy and one clear instruction.
  document.getElementById('savestate').innerHTML=
    '<b>Sent, and a copy has downloaded.</b> Please email that copy to '
    +'<a href="mailto:danny@suncitychurch.com" style="color:#fff">danny@suncitychurch.com</a> '
    +'so we know for certain it arrived.';
  downloadAnswers();
  window.print();
}
restore();
if(localStorage.getItem(KEY+'-submitted')==='1'){
  const b=document.querySelector('.toolbar button:not(.ghost)');
  if(b)b.textContent='Send again';
  const s=document.getElementById('savestate');
  if(s)s.innerHTML='Your answers are restored. If you were told this was submitted before '
    +'2026-09-25, it may not have reached us \\u2014 press <b>Download my answers</b> and email '
    +'the file to <a href="mailto:danny@suncitychurch.com" style="color:#fff">danny@suncitychurch.com</a>.';}
</script>
"""
if FILLABLE:
    body += FILL_JS

html = page("Eldership Candidate Assessment — Sun City Church",
            (EXTRA_CSS + FILL_CSS if FILLABLE else EXTRA_CSS) + body)
with open(OUT, "w") as f:
    f.write(html)
print(f"Wrote {OUT} ({len(html)//1024} KB, {qn} questions)")
