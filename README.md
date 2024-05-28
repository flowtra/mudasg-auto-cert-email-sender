## MudaSG Automated Telegram Invites
# PROBLEM
When MudaSG, a youth-led volunteer group, started our outreach to gain more members, we needed a solution to invite approved volunteers to our Telegram Group without having the link be made public for security & privacy reasons. Initially, the HR team would manually reach out to each person to send them a one-time invite link.

# SOLUTION
To reduce HR’s workload, I created a program that would continuously monitor our Registration Google Form, and upon a new row being added, my telegram bot would create a one-time invite link, which would then be embedded in an automatic email sent to the new member via the php_mailer module.
