"""Build the public, one-page resume. Requires ReportLab and Python 3.10+.
Career content matches the November 2026 resume and career evidence profile.
Public contact uses LinkedIn; phone and email remain in the application copy.
Run from any directory; inspect the generated PDF before publishing.
"""
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
ROOT = Path(__file__).resolve().parents[1]
out = ROOT / 'assets' / 'Josh_Escobar_Resume.pdf'
styles = {
 'Title': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=26, leading=29, spaceAfter=1),
 'Subtitle': ParagraphStyle('target', fontName='Helvetica-Bold', fontSize=15, leading=18, spaceAfter=9),
 'Contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=9, leading=11, spaceAfter=8),
 'Heading 1': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=10, leading=12, spaceBefore=7, spaceAfter=3, keepWithNext=True),
 'Normal': ParagraphStyle('body', fontName='Helvetica', fontSize=9.5, leading=11.1, spaceAfter=2),
 'List Bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=9.5, leading=11.1, leftIndent=16, firstLineIndent=-10, spaceAfter=3),
 'Date': ParagraphStyle('date', fontName='Helvetica', fontSize=9, leading=11.1, alignment=2),
}

CONTENT = [('Title', 'JOSH ESCOBAR', 'JOSH ESCOBAR'),
 ('Subtitle',
  'LINUX SYSTEMS AND INFRASTRUCTURE ENGINEER',
  'LINUX SYSTEMS AND INFRASTRUCTURE ENGINEER'),
 ('Contact',
  'Austin, TX | <link '
  'href="https://www.linkedin.com/in/joshescobarx/">linkedin.com/in/joshescobarx</link> | <link '
  'href="https://greycarpet.github.io/">greycarpet.github.io</link>',
  ''),
 ('Heading 1', 'PROFESSIONAL SUMMARY', 'PROFESSIONAL SUMMARY'),
 ('Normal',
  'Hands-on infrastructure professional and U.S. Coast Guard veteran focused on Linux '
  'administration, networking, automation, and production support. Delivered Linux migrations, '
  'improved VoIP reliability, and automated business reporting. Seeking individual contributor '
  'opportunities in Linux systems administration and infrastructure engineering.',
  'Hands-on infrastructure professional and U.S. Coast Guard veteran focused on Linux '
  'administration, networking, automation, and production support. Delivered Linux migrations, '
  'improved VoIP reliability, and automated business reporting. Seeking individual contributor '
  'opportunities in Linux systems administration and infrastructure engineering.'),
 ('Heading 1', 'TECHNICAL SKILLS', 'TECHNICAL SKILLS'),
 ('Normal',
  '<b>Systems: </b>Ubuntu, Lubuntu, openSUSE/ViciBox, systemd, SSH, Samba, LUKS, ext4, Linux '
  'permissions',
  'Systems: Ubuntu, Lubuntu, openSUSE/ViciBox, systemd, SSH, Samba, LUKS, ext4, Linux permissions'),
 ('Normal',
  '<b>Networking and security: </b>TCP/IP, DNS, WireGuard, firewalls, Fail2ban, packet capture, '
  'TLS/SRTP',
  'Networking and security: TCP/IP, DNS, WireGuard, firewalls, Fail2ban, packet capture, TLS/SRTP'),
 ('Normal',
  '<b>Operations: </b>Grafana, Prometheus, Uptime Kuma, Asterisk, VICIdial, Windows endpoints, '
  'Active Directory fundamentals',
  'Operations: Grafana, Prometheus, Uptime Kuma, Asterisk, VICIdial, Windows endpoints, Active '
  'Directory fundamentals'),
 ('Normal',
  '<b>Automation: </b>Basic Bash and SQL; AI-assisted Ansible, Python automation, PowerShell, and '
  'Docker Compose configuration',
  'Automation: Basic Bash and SQL; AI-assisted Ansible, Python automation, PowerShell, and Docker '
  'Compose configuration'),
 ('Normal',
  '<b>Certifications: </b>CompTIA A+, Network+, Linux+',
  'Certifications: CompTIA A+, Network+, Linux+'),
 ('Heading 1', 'PROFESSIONAL EXPERIENCE', 'PROFESSIONAL EXPERIENCE'),
 ('Normal',
  '<b>ECA Direct, Inc. | Austin, TX</b>\tOctober 2023–Present',
  'ECA Direct, Inc. | Austin, TX\tOctober 2023–Present'),
 ('Normal',
  '<b>Director of Information Technology</b>\tNovember 2025–Present',
  'Director of Information Technology\tNovember 2025–Present'),
 ('Normal',
  'Technical owner for approximately 50 employees, 200,000–250,000 monthly call minutes, and '
  'approximately 25 agents at peak production concurrency.',
  'Technical owner for approximately 50 employees, 200,000–250,000 monthly call minutes, and '
  'approximately 25 agents at peak production concurrency.'),
 ('List Bullet',
  'Migrated approximately 300 GB of sensitive client data to Ubuntu/Samba with LUKS encryption and '
  'rebuilt access controls, with no operating-hours disruption for six users.',
  'Migrated approximately 300 GB of sensitive client data to Ubuntu/Samba with LUKS encryption and '
  'rebuilt access controls, with no operating-hours disruption for six users.'),
 ('List Bullet',
  'Automated reporting across 32 campaigns and delivered a self-service platform using AI-assisted '
  'development, reducing estimated weekly effort from eight staff hours to 30 minutes.',
  'Automated reporting across 32 campaigns and delivered a self-service platform using AI-assisted '
  'development, reducing estimated weekly effort from eight staff hours to 30 minutes.'),
 ('List Bullet',
  'Migrated telephony from VPS to VDS without agent disruption; reported voice-quality complaints '
  'fell from 3–5 per week to zero following the March 2026 cutover.',
  'Migrated telephony from VPS to VDS without agent disruption; reported voice-quality complaints '
  'fell from 3–5 per week to zero following the March 2026 cutover.'),
 ('List Bullet',
  'Used Grafana/Prometheus alerts to identify and contain unauthorized cryptomining; preserved '
  'evidence, revoked compromised access, and hardened SSH with no production downtime.',
  'Used Grafana/Prometheus alerts to identify and contain unauthorized cryptomining; preserved '
  'evidence, revoked compromised access, and hardened SSH with no production downtime.'),
 ('List Bullet',
  'Corrected IVR routing and queue timeouts, reducing affected toll-free inbound charges by 74% '
  'and saving $923.56 in the following billing cycle.',
  'Corrected IVR routing and queue timeouts, reducing affected toll-free inbound charges by 74% '
  'and saving $923.56 in the following billing cycle.'),
 ('Normal',
  '<b>Information Technology Support Specialist</b>\tOctober 2023–November 2025',
  'Information Technology Support Specialist\tOctober 2023–November 2025'),
 ('List Bullet',
  'Migrated approximately 50 aging Windows workstations to Lubuntu over a weekend, returning the '
  'fleet to service by the next business day with limited hardware upgrades.',
  'Migrated approximately 50 aging Windows workstations to Lubuntu over a weekend, returning the '
  'fleet to service by the next business day with limited hardware upgrades.'),
 ('List Bullet',
  'Standardized applications and endpoint security through AI-assisted Ansible development; '
  'estimated provisioning time fell from 1–2 hours to about 10 minutes per workstation.',
  'Standardized applications and endpoint security through AI-assisted Ansible development; '
  'estimated provisioning time fell from 1–2 hours to about 10 minutes per workstation.'),
 ('List Bullet',
  'Contained an unauthorized-calling incident using Firewalld, Fail2ban, SSH restrictions, and '
  'credential rotation; authored the root-cause analysis.',
  'Contained an unauthorized-calling incident using Firewalld, Fail2ban, SSH restrictions, and '
  'credential rotation; authored the root-cause analysis.'),
 ('Normal',
  '<b>Information Systems Technician | United States Coast Guard</b>\tDecember 2019–December 2021',
  'Information Systems Technician | United States Coast Guard\tDecember 2019–December 2021'),
 ('List Bullet',
  'Supported approximately 60+ users across Windows, Active Directory, classified and unclassified '
  'accounts, endpoint support, and authentication devices.',
  'Supported approximately 60+ users across Windows, Active Directory, classified and unclassified '
  'accounts, endpoint support, and authentication devices.'),
 ('List Bullet',
  'Assisted a senior administrator with a Windows Server 2012-to-2016 domain controller upgrade, '
  'completing installation and validation within a one-hour maintenance window.',
  'Assisted a senior administrator with a Windows Server 2012-to-2016 domain controller upgrade, '
  'completing installation and validation within a one-hour maintenance window.'),
 ('List Bullet',
  'Installed and configured a Red Hat-based Minotaur HUB, including operating system, networking, '
  'and application configuration.',
  'Installed and configured a Red Hat-based Minotaur HUB, including operating system, networking, '
  'and application configuration.'),
 ('Heading 1', 'EDUCATION', 'EDUCATION'),
 ('Normal',
  'Network Engineer Program | CyberTex Institute of Technology\tExpected February 2027',
  'Network Engineer Program | CyberTex Institute of Technology\tExpected February 2027'),
 ('Normal',
  'B.S., User Experience | Full Sail University\t2024',
  'B.S., User Experience | Full Sail University\t2024')]
story=[]
for kind,html,plain in CONTENT:
    if '\t' in plain:
        # Right-aligned dates retain a predictable, selectable reading order.
        left,right=html.split('\t',1)
        row=Table([[Paragraph(left,styles['Normal']),Paragraph(right,styles['Date'])]],colWidths=[342,146.4], hAlign='LEFT')
        row.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
        row.keepWithNext=True
        story.append(row)
    else:
        if kind=='List Bullet':html='&#8226; '+html
        story.append(Paragraph(html,styles[kind]))
def frame(canvas,doc):
    canvas.saveState()
    canvas.setFillColor(HexColor('#94B6CF'))
    canvas.rect(0,0,42,792,fill=1,stroke=0)
    canvas.restoreState()
    canvas.setTitle('Josh Escobar - Linux Systems and Infrastructure Engineer')
    canvas.setAuthor('Josh Escobar')
    canvas.setSubject('Hands-on individual contributor resume')
doc=SimpleDocTemplate(str(out),pagesize=letter,leftMargin=72,rightMargin=39.6,topMargin=50,bottomMargin=39.6,pageCompression=1)
doc.build(story,onFirstPage=frame,onLaterPages=frame)
print(out)
