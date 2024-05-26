
import pymupdf
import subprocess
import glob, os, shutil


def getFilenameList(emailList):
    with open(emailList, 'r') as inFile:
        emails = inFile.read().splitlines()

    p = []
    for email in emails:
        p.append(email.split('@')[0])

    return p

def splitPDF(directory, toSplit, filenameList):
    src = pymupdf.open(f"{directory}/{toSplit}")
    for i, page in enumerate(src):
        tar = pymupdf.open()
        tar.insert_pdf(src, from_page=page.number, to_page=page.number)
        tar.save(f"{directory}/{filenameList[i]}.pdf")
        tar.close()

    return True

def sendEmail(email, name, attachmentFilename):

    result = subprocess.run(
        ['php', 'php_files/1mailer.php', email, name, attachmentFilename],  # program and arguments
        stdout=subprocess.PIPE,  # capture stdout
        check=True,
        shell=False# raise exception if program fails
    )
    if 'Email sent to' in str(result.stdout):
        return True

def createFoldersFromCoaFiles():

    folder = '/Users/putra/Desktop/Python Projects/MudaSG Automated Certificate Emails/MudaSG COAs'

    for file_path in glob.glob(os.path.join(folder, '*.*')):
        new_dir = file_path.rsplit('.', 1)[0]
        os.mkdir(os.path.join(folder, new_dir))
        shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))

COAsubfolders = [ f.name for f in os.scandir('/Users/putra/Desktop/Python Projects/MudaSG Automated Certificate Emails/MudaSG COAs') if f.is_dir() ]
for subf in COAsubfolders:
    print(f'[+] Processing {subf}')
    with open(f'MudaSG COAs/{subf}/emails.txt', 'r') as inFile:
        emails = inFile.read().splitlines()

    parsedEms = [em.split('@')[0] for em in emails]

    if splitPDF(f'MudaSG COAs/{subf}', f'{subf}.pdf', parsedEms):
        print(f'[+] PDFs split into individuals')

    for email in emails:
        emP = email.split('@')[0]
        if sendEmail(email, 'unusedParam', f'MudaSG COAs/{subf}/{emP}.pdf'):
            print(f'[+] Sent cert email to {email}')
