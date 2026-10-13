"""Build the public resume snapshot. Requires Python 3.10+ and ReportLab.
Keep career facts synchronized with resume/index.html and review both PDF pages.
This script generates a local artifact; it does not upload or deploy anything.
"""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
import hashlib
ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'assets' / 'Josh_Escobar_Resume.pdf'
out.parent.mkdir(parents=True, exist_ok=True)
styles={
 'name':ParagraphStyle('name',fontName='Helvetica-Bold',fontSize=26,leading=29,textColor=HexColor('#17212b'),spaceAfter=4),
 'role':ParagraphStyle('role',fontName='Helvetica',fontSize=12,leading=16,textColor=HexColor('#334d60'),spaceAfter=7),
 'meta':ParagraphStyle('meta',fontName='Helvetica',fontSize=9.4,leading=14,textColor=HexColor('#3c4853'),spaceAfter=9),
 'section':ParagraphStyle('section',fontName='Helvetica-Bold',fontSize=11,leading=14,spaceBefore=12,spaceAfter=7,textColor=HexColor('#244a63'),keepWithNext=True),
 'job':ParagraphStyle('job',fontName='Helvetica-Bold',fontSize=11,leading=15,spaceBefore=5,spaceAfter=3,keepWithNext=True),
 'dates':ParagraphStyle('dates',fontName='Helvetica',fontSize=9.4,leading=13,textColor=HexColor('#4a5662'),spaceAfter=5,keepWithNext=True),
 'body':ParagraphStyle('body',fontName='Helvetica',fontSize=10,leading=14.1,spaceAfter=6),
 'bullet':ParagraphStyle('bullet',fontName='Helvetica',fontSize=9.8,leading=13.6,spaceAfter=5,leftIndent=10,firstLineIndent=-10),
}
story=[]
def p(t,typ='body'):return Paragraph(t,styles[typ])
def add(t,typ='body'):story.append(p(t,typ))
def job(title,place,dates,bullets):
 story.extend([p(title,'job'),p(place+' | '+dates,'dates')]);story.extend(p('&#8226; '+x,'bullet') for x in bullets)
add('Josh Escobar','name');add('Linux Infrastructure &amp; Network Engineering','role')
add('Austin, Texas | U.S. Coast Guard veteran<br/><link href="https://greycarpet.github.io/" color="#244a63">greycarpet.github.io</link> | <link href="https://github.com/greycarpet" color="#244a63">github.com/greycarpet</link>','meta')
add('Hands-on IT leader and infrastructure engineer focused on Linux systems, secure network operations, telephony, and practical automation. Experience spans end-user support, production administration, business-rule discovery, and controlled technical change.','body')
add('PROFESSIONAL EXPERIENCE','section')
job('Director of Information Technology','ECA Direct - Austin, TX','Nov 2025 - Present',[
'Administer Linux production services, Asterisk/VICIdial telephony, networking, remote access, file services, and operational systems supporting customer-facing campaigns.',
'Designed and rolled out a production Twilio connection using TLS signaling and SRTP media after a controlled Linux/PJSIP verification pilot.',
'Developed and validated Python/SQL reporting automation; estimated about 20 staff hours saved weekly and approximately 90% fewer reporting errors in recurring client deliverables.',
'Directed the transition to remote operations using Linux-hosted services, WireGuard connectivity, controlled file access, and remote-support workflows.',
'Corrected an after-hours IVR/queue behavior; affected toll-free charges declined 74% in the next full billing cycle.'
])
job('Lead IT Support Specialist','ECA Direct - Austin, TX','Oct 2023 - Nov 2025',[
'Supported workstation provisioning, employee onboarding/offboarding, access controls, and production troubleshooting across Linux and Windows systems.',
'Migrated 50 aging workstations to a standardized Lubuntu configuration and built Ansible playbooks and checks to reduce repeated setup work.',
'Helped restore centralized identity and file access with Ubuntu/Samba Active Directory and separate network storage following a server failure.'
])
job('Information Systems Technician','United States Coast Guard','Dec 2019 - Dec 2021',[
'Supported 60+ personnel using Windows workstations, Active Directory, devices, printers, and secure information systems.',
'Managed account onboarding, access validation, equipment preparation, and incident support; contributed to an operational Minotaur HUB node and emergency IT readiness.'
])
job('Fireman','United States Coast Guard','Nov 2017 - Dec 2019',[
'Served in maritime operations and maintenance, developing safety discipline, procedural rigor, and operational accountability before moving into information systems.'
])
story.append(PageBreak())
add('TECHNICAL SKILLS','section')
for head,body in [
('Linux & systems','Ubuntu, openSUSE, Lubuntu, systemd, SSH, package management, Samba, Linux permissions, storage and services.'),
('Networking & telephony','TCP/IP, DNS, routing, WireGuard VPN, firewalls, Asterisk, VICIdial, SIP, TLS, SRTP and Twilio.'),
('Automation & data','Ansible, Python, SQL, Git, YAML, reporting workflows, configuration validation and operational scripts.'),
('Infrastructure operations','Docker Compose, PostgreSQL, Redis, Nginx, SFTPGo, monitoring, incident investigation, documentation and change control.')]:
 add('<b>'+head.replace('&','&amp;')+'</b><br/>'+body)
add('SELECTED ENGINEERING WORK','section')
for title,body,url in [
('Production voice trunk encryption','Validated certificate trust, resolved PJSIP/VICIdial transport behavior, verified negotiated encrypted audio on an answered call, and rolled the secure Twilio trunk into production.','secure-voice-trunk'),
('Linux endpoint configuration','Standardized 50 Lubuntu workstations using documented installation and Ansible-based provisioning. Validated a clean-install rebuild before fleet application.','ansible-linux-deployment'),
('Reporting workflow automation','Translated manual reporting rules into reusable Python/SQL processes for cleaning, validation, calculations and deliverables; evolved the tooling into a Linux-hosted reporting application.','reporting-hub')]:
 add(title,'job');add(body);add(f'<link href="https://greycarpet.github.io/projects/{url}/" color="#244a63">greycarpet.github.io/projects/{url}/</link>','meta')
add('EDUCATION & CERTIFICATIONS','section')
add('<b>CompTIA A+ | Network+ | Linux+</b><br/>Professional certifications')
add('<b>Network Engineering Program</b><br/>CyberTex Institute of Technology | In progress, expected February 2027')
add('<b>Bachelor of Science, User Experience</b><br/>Full Sail University | Completed November 2024')
add('PUBLIC PORTFOLIO','section')
add('Read the project narratives for engineering decisions, validation evidence and the scope of reported outcomes. Weekly time savings and error reduction are estimates; the 74% reduction applies to the affected toll-free expense.','body')
def frame(c,doc):
 c.setTitle('Josh Escobar - Linux Infrastructure and Network Engineering Resume');c.setAuthor('Josh Escobar');c.setSubject('Public professional resume - greycarpet');c.setCreator('greycarpet public resume generator')
 w,h=letter;c.setStrokeColor(HexColor('#cbd2d8'));c.line(42,34,w-42,34);c.setFont('Helvetica',8);c.setFillColor(HexColor('#45545f'));c.drawString(42,22,'Josh Escobar  /  greycarpet  /  October 2026');c.drawRightString(w-42,22,str(doc.page))
doc=SimpleDocTemplate(str(out),pagesize=letter,rightMargin=42,leftMargin=42,topMargin=35,bottomMargin=44,title='Josh Escobar - Resume',author='Josh Escobar',pageCompression=1)
doc.build(story,onFirstPage=frame,onLaterPages=frame)
b=out.read_bytes();print('PDF bytes',len(b),'git hash',hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest())
