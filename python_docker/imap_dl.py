from imap_tools import MailBox

with MailBox('outlook.office365.com').login('fraser.clark@itoworld.com', 'test') as mailbox:
    mailbox.folder.set('dmarc/reports')
    for msg in mailbox.fetch():
        for att in msg.attachments:
            print(att.filename, att.content_type)
            with open(f'./input/{att.filename}', 'wb') as f:
                f.write(att.payload)
        
    mailbox.move(mailbox.uids(), 'dmarc/archive/Aggregate')
