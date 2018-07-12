#!/usr/bin/env python3

#
# Quick Reply Messages
#
import sys
import datetime
import os

THANKS = "\n\nThanks,\nP\n"
reply = sys.argv[1]

if reply == "like":
  body = "👍🏻"
  close = THANKS
elif reply == "thanks":
  body = "✅ Thanks"
  close = ""
elif reply == "agreed":
  body = "🤝 Agreed"
  close = THANKS
else:
  raise ValueError("Invalid reply type " + reply)

out = '''
{ actions = (
  {
    type = "replyMessage";
    body = "%s %s"; 
    resultActions = ( { type = "sendMessage"; } );	
  },
  {
    type = "notify";
    formatString = "Replied %s";
  },
  {
    type = "moveMessage";
    mailbox = "archive";
  },
  {
    type    = "changeFlags";
    enable  = ( "\\Seen", "\\$NotJunk" );
    disable = ( "\\$Junk", "\\Junk" );
  },
); }
''' % (body, close, body)
print (out)

