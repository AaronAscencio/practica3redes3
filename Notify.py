import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

COMMASPACE = ', '
# Define params
rrdpath = '/home/tani/PycharmProjects/Introduccion_SNMP/5-AdministraciónDeRendimiento/RRD/'
imgpath = '/home/tani/PycharmProjects/Introduccion_SNMP/5-AdministraciónDeRendimiento/IMG/'
fname = 'trend.rrd'

mailsender = "spotify2327@gmail.com"
mailreceip = "spotify2327@gmail.com"
mailserver = 'smtp.gmail.com: 587'
password = 'mqknntdplzulmcsl'

def send_alert_attached(subject,estado,img):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip
    fp = open(f'RRD/{img}.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    msg.attach(img)
    msg.attach(img)
    msg.attach(MIMEText(estado))
    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()